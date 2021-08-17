$(document).ready(function(event){
                      $(document).on('click', '#like', function(event){
                          event.preventDefault();
                          var pk = $(this).attr('value');
                            console.log(pk);
//                           $.ajax({
//                               type: 'POST',
//                               url: '{% url "blog1:like_post" %}',
//                               data: {
//                                   'id': pk,
//                                   'csrfmiddlewaretoken': '{{ csrf_token }}'
//                               },
//                               datatype: 'json',
//                               success: function(response){
//                                   $('#like-section').html(response['form'])
//       
//                               },
//                               error: function(rs, e){
//                                   console.log(rs.responseText);
//                               },
//                           });
                      });
                  });