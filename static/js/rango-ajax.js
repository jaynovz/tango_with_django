/**
 * Created by leia on 3/24/15.
 */

$(document).ready(function() {

    $('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });
    });

    $('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
         $('#cats').html(data);
        });
    });

    $('#adds').click(function(){
    var pageurl = $(this).attr("data-pageurl");
    var pagetitle = $(this).attr("data-pagetitle");
    var categoryid = $(this).attr("data-categoryid");
        console.log("pageurl= "+pageurl+" pagetitle= "+ pagetitle);
     $.get('/rango/auto_add_page/', {pageurl: pageurl, pagetitle: pagetitle, category_id: categoryid}, function(data){

               $(this).hide();
           });
    });
});