$(document).ready(function(){

    $('input').on('itemAdded', function(event) {
            var tag = event.item;
            var takeawayId = event.currentTarget.id;

        $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/tags/",
                    data: {takeaway_id:takeawayId,tag_value:tag, operation:'add' },
                    success: function(data){
                     //console.log(button_id   );
                     //alert(button_id);
                     if (data=='True') {

                     }else {
                         event.cancel =true
                     }

                       }
                });
    });

     $('input').on('itemRemoved', function(event) {
            var tag = event.item;
            var takeawayId = event.currentTarget.id;

        $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/tags/",
                    data: {takeaway_id:takeawayId,tag_value:tag, operation:'delete' },
                    success: function(data){
                     //console.log(button_id   );
                     //alert(button_id);
                     if (data=='True') {

                     }else {
                         event.cancel =true
                     }

                       }
                });
    });



});
