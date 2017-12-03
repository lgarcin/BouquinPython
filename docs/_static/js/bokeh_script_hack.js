$("script[src^='/scripts']").each(function() {
  $(this).append('<div>toto</div>')
});
