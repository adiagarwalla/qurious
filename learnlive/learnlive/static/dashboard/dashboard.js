function get_user_skills() {
    // this function gets the user skills
    $.get('/dashboard/skills/', function(data) {
        // alert the data for now
        $("#skill_set0").empty();
        $("#skill_set1").empty();
        $("#skill_set2").empty();
        for (i = 0; i < data.length; i++) {
            var mod = i % 3;
            if (!data[i].fields.is_marketable) {
                $("#skill_set" + mod).append("<li class=\"active\"><input type=\"hidden\" value=\""+ data[i].pk +"\" /><a href=\"#\" data-toggle=\"modal\" data-target=\"#myModal\" class=\"modal_link\"><span class=\"badge pull-right\">" + data[i].fields.price + "</span>" + data[i].fields.name + "</a></li>");
            } else {
                // alternative html goes here.
                $("#skill_set" + mod).append("<li class=\"active\"><input type=\"hidden\" value=\""+ data[i].pk +"\" /><a href=\"#\" data-toggle=\"modal\" data-target=\"#myModal\" style=\" background-color: rgb(201,62,59);\"><span class=\"badge pull-right\">" + data[i].fields.price + "</span>" + data[i].fields.name + "</a></li>");
            }
        }
    });
}
