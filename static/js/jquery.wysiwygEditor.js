(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var actions = [
  {
    title: 'undo'
  },
  {
    title: 'repeat',
    action: 'redo',
    break: true
  },
  {
    title: 'bold',
    nodeName: 'B'
  },
  {
    title: 'italic',
    nodeName: 'I'
  },
  {
    title: 'underline',
    nodeName: 'U',
    break: true
  },
  {
    title: 'align-left',
    action: 'justifyLeft',
    nodeName: 'left'
  },
  {
    title: 'align-center',
    action: 'justifyCenter',
    nodeName: 'center'
  },
  {
    title: 'align-right',
    action: 'justifyRight',
    nodeName: 'right'
  },
  {
    title: 'align-justify',
    action: 'justifyFull',
    nodeName: 'justify',
    break: true
  },
  {
    title: 'list-ol',
    action: 'insertOrderedList',
    nodeName: 'OL'
  },
  {
    title: 'list-ul',
    action: 'insertUnorderedList',
    nodeName: 'UL',
    break: true
  },
  {
    title: 'link',
    action: 'createLink',
    nodeName: 'A',
    value: true,
    desc: 'Insert link URL'
  },
  {
    title: 'image',
    action: 'insertImage',
    value: true,
    desc: 'Insert image URL',
  }
];

module.exports = actions;

},{}],2:[function(require,module,exports){
// Backlight active tools
module.exports = function(randomID, elements, actions) {

  $.each(actions, function() {
    var action = this;
    var match = false;

    $.each(elements, function() {
      var nodeName = this.nodeName;

      // Align property style name
      if(this.style.textAlign != '')
        nodeName = this.style.textAlign;

      if(typeof(action.nodeName) != 'undefined' && action.nodeName === nodeName)
        match = true;
    });

    if(match)
      $('#' + randomID).find('.wysiwygEditor-' + action.title).addClass('action-active');
    else
      $('#' + randomID).find('.wysiwygEditor-' + action.title).removeClass('action-active');
  });

};

},{}],3:[function(require,module,exports){
module.exports = function(randomID, editArea, getAction, backlightActiveTools, actions) {

  $.each(actions, function(i) {
    $('#' + randomID).find('.wysiwygEditor-' + actions[i].title).bind('click', function(e) {
      e.preventDefault();
      editArea.body.focus();

      if(typeof(actions[i].value) != 'undefined') {
        var value = prompt(actions[i].desc);
        if(value != null)
          editArea.execCommand(getAction(actions[i]), false, value);
      } else {
        editArea.execCommand(getAction(actions[i]), false, null);
      }

      $(this).toggleClass('action-active');
      backlightActiveTools(randomID, $(editArea.getSelection().anchorNode).parents(), actions);
    });
  });
  
};

},{}],4:[function(require,module,exports){
// Get action
module.exports = function(element) {

    if(typeof(element.action) != 'undefined')
      return element.action;
      
    if(typeof(element.title) != 'undefined')
      return element.title;

};

},{}],5:[function(require,module,exports){
// iframeLoaded
module.exports = function(element, callback) {

  var loop = true;

  while(loop) {
    if($(element).length) {
      $($(element)[0].contentDocument).ready(function() {
        callback();
      });
      loop = false;
    }
  }

}

},{}],6:[function(require,module,exports){
// iframeSettings
exports.setAttributes = function(editArea) {

  $(editArea).designMode = 'on';
  $(editArea.body).attr('contenteditable', true);

};

exports.setStylesheet = function(editArea) {

  $(editArea.head).append('<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,300,800" rel="stylesheet" type="text/css">');

};

exports.setCss = function(editArea) {

  $(editArea.body).css('padding', '15px');
  $(editArea.body).css('font-family', 'Open Sans, sans-serif');
  $(editArea.body).css('font-size', '13px');
  $(editArea.body).css('line-height', '1.6em');

}

exports.setWidth = function(iframe) {

  // Set iframe width
  iframe.width(iframe.parent().width());
  $(window).resize(function() {
    iframe.width(iframe.parent().width());
  });

};

},{}],7:[function(require,module,exports){
$.fn.wysiwygEditor = function() {

  'use strict'

  var textarea = this;

  var randomID = 'wysiwygEditor-' + Math.floor(Math.random() * 1000000);
  var actions = require('./actions')
  var markup = require('./markup');
  var iframeLoaded = require('./iframeLoaded');
  var iframeSettings = require('./iframeSettings');
  var getAction = require('./getAction');
  var backlightActiveTools = require('./backlightActiveTools');
  var bindClickToolbar = require('./bindClickToolbar.js');
  var triggerContentChanged = require('./triggerContentChanged.js');

  // Hide original textarea
  textarea.css('display', 'none');
  textarea.addClass(randomID);

  // Create new wysiwygEditor
  textarea.before(markup(randomID, actions));
  var iframe = $('#' + randomID).find('iframe');

  iframeLoaded(iframe, function() {
    var editArea = iframe[0].contentDocument;

    // Set iframe width
    iframeSettings.setWidth(iframe);

    // Set iframe body to editable
    iframeSettings.setAttributes(editArea);

    // Iframe body styles
    iframeSettings.setStylesheet(editArea);
    iframeSettings.setCss(editArea);

    // Copy data from textarea to iframe
    $(editArea.body).html(textarea.val());

    // Bind click events for toolbar
    bindClickToolbar(randomID, editArea, getAction, backlightActiveTools, actions);

    // Trigger contentChanged
    triggerContentChanged(randomID, editArea, textarea, backlightActiveTools, actions);

    // Textarea synchronization
    $(editArea.body).on('contentChanged', function() {
      textarea.val($(this).html());
    });
  });

  return this;
}

},{"./actions":1,"./backlightActiveTools":2,"./bindClickToolbar.js":3,"./getAction":4,"./iframeLoaded":5,"./iframeSettings":6,"./markup":8,"./triggerContentChanged.js":9}],8:[function(require,module,exports){
// Create markup
module.exports = function(randomID, actions) {

  var markup = '';

  markup += '<div id="' + randomID + '" class="wysiwygEditor-wrapper">';
  markup +=   '<div class="wysiwygEditor-toolbar">';
  markup +=     '<ul>';

  // Display all tools
  $.each(actions, function(i) {
    markup +=       '<li>';
    markup +=         '<a href class="wysiwygEditor-' + actions[i].title + '" title="' + actions[i].title.toUpperCase() + '">';
    markup +=           '<i class="fa fa-' + actions[i].title + '"></i>';
    markup +=        '</a>';
    markup +=       '</li>';

    // Break
    if(typeof(actions[i].break) != 'undefined') {
      markup +=     '<li class="break">|</li>'
    }
  });

  markup +=     '</ul>';
  markup +=   '</div>';
  markup +=   '<div class="wysiwygEditor-editArea">';
  markup +=     '<iframe src="about:blank" height="300"></iframe>';
  markup +=   '</div>';
  markup +=   '<div class="wysiwygEditor-footer">';
  markup +=   'HTML';
  markup +=   '</div>';
  markup += '</div>';

  return markup;

}

},{}],9:[function(require,module,exports){
module.exports = function(randomID, editArea, textarea, backlightActiveTools, actions) {

  $.each(['click', 'keyup'], function() {
    $(editArea.body).bind(this.toString(), function(e) {
      if($(this).html() != textarea.val())
        $(this).trigger('contentChanged');

      // Update footer element indicator
      var footerElementIndicator = '';
      var elements = $(editArea.getSelection().anchorNode).parents();

      for(var i = elements.length - 1; i >= 0; i--) {
        footerElementIndicator += elements[i].nodeName;
        if(i != 0)
          footerElementIndicator+= ' &raquo; ';
      }

      $('#' + randomID).find('.wysiwygEditor-footer').html(footerElementIndicator);

      backlightActiveTools(randomID, elements, actions);
    });
  });

};

},{}]},{},[7]);
