tinymce.init({
    selector: "textarea",
    theme: "modern",
    width: 760,
    height: 300,
    //spell checker plugin not working. So, removed from plugins and toolbars.
    plugins: [
         "advlist autolink autoresize autosave link image lists charmap print preview hr anchor pagebreak",
         "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
         "save table contextmenu directionality emoticons template paste textcolor"
   ],
   content_css: "css/content.css",
   //Multi_Row Toolbar
   toolbar: [
            "insertfile undo redo | formatselect | bold italic forecolor backcolor | fontselect fontsizeselect",
            "bullist numlist outdent indent |  alignleft aligncenter alignright alignjustify | link image |  hr charmap emoticons insertdatetime | preview"
   ],
   browser_spellcheck : true,
   style_formats: [
        {title: 'Bold text', inline: 'b'},
        {title: 'Red text', inline: 'span', styles: {color: '#ff0000'}},
        {title: 'Red header', block: 'h1', styles: {color: '#ff0000'}},
        {title: 'Example 1', inline: 'span', classes: 'example1'},
        {title: 'Example 2', inline: 'span', classes: 'example2'},
        {title: 'Table styles'},
        {title: 'Table row 1', selector: 'tr', classes: 'tablerow1'}
    ]
 });