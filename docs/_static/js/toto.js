$("script[src^='/scripts']").attr('src', function(i, oldsrc) {
  return 'tata' + oldsrc;
});
