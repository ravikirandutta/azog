function make_public1(takeawayID,button_id) {

               $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/makepublic/",
                    data: "takeaway_id="+takeawayID,
                    success: function(data){
                     //console.log(button_id   );
                     //alert(button_id);
                     if (data=='True') {
                         $("#"+button_id).html('Make Private');
                     }else {
                         $("#"+button_id).html('Make Public');
                     }

                       }
                });
         }

         function vote(takeawayID,button_id,vote_value) {
            //alert(vote_value)
               $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/vote/",
                    data: {takeaway_id:takeawayID,vote_value:vote_value },
                    success: function(data){
                     //console.log(button_id   );
                     //alert(data);
                     $("#votecount"+takeawayID).html(data);


                       }
                });
         }

           function divClicked() {
            //alert(10);
               var divHtml = $(this).text();
               //var takeaway_id = $(this).id();
               var takeaway_id = this.id;
               //var component = '<textarea id="'+takeaway_id+'" />';
               var component = '<textarea class="col-xs-12" id="'+takeaway_id+'" />';
               var editableText = $(component);
               //var editableText = $("<textarea />");
               editableText.val(divHtml);
               $(this).replaceWith(editableText);
               //alert(editableText);
               editableText.focus();
               // setup the blur event for this new textarea
               editableText.blur(editableTextBlurred);

           }

      function editableTextBlurred() {
          var html = $(this).val();
          var id = this.id;
          var viewableText = $('<div class="editableNotes" id="'+id+'">');
          viewableText.html(html);
          $(this).replaceWith(viewableText);
          // setup the click event for this new div
          viewableText.click(divClicked);
          saveEditedNotes(id,html);
      }

      function saveEditedNotes(takeawayID,text) {

               $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/edit/",
                    data: {takeaway_id:takeawayID,takeaway_text:text },
                    success: function(data){
                     //console.log(button_id   );
                     //alert(data);


                       }
                });
         }

         function deleteNotes(takeawayID) {

               $.ajax({
                    type: "POST",
                    url: "/takeaway/notes/delete/",
                    data: {takeaway_id:takeawayID},
                    success: function(data){
                     //console.log(button_id   );
                     //alert(data);
                     //var div = $("span[id=data]").remove();
                     $("li[id='P_" + data + "']").remove();
                    //$(takeawayID).remove();

                       }
                });
         }
