$(function(){
	var featherEditor = new Aviary.Feather({
        apiKey: '9600cddff',
        apiVersion: 2,
        onSave: function(imageID, newURL) {
			saveback.save(newURL, function(data){
				window.console.log(data);
			});
        },
        postUrl: 'http://triple-t.mit.edu/photoeditor/featherposturl/',
		appendTo: "editpane"
    });

	saveback.setKey('asdlkfjs');

	$(".openbutton").click(function(){
		saveback.getFile(saveback.MIMETYPES.IMAGES,function(url, token, data) {
			var img = $('<img id="#editimage"/>');
			img.attr("src", url);
			$(".editpane").empty().append(img);

			featherEditor.launch({
				image: img[0],
				url: url
			});
		});
	});
});
