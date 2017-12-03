$(document).ready(function() {
  $("script[src^='/scripts']").each(function() {
    $.getScript('.' + this.src);
  })
});
