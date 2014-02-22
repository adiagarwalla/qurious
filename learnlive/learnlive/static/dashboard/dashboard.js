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

function get_profile() {
    // gets the profile of the person and autopopulates the values
    // of the input fields
    $.get('/dashboard/profile/', function(data) {
        for (i = 0; i < data.length; i++) {
            $("#profile_name").val(data[i].fields.profile_name);
            $("#phone_number").val(data[i].fields.phone_number);
            $("#Desc").val(data[i].fields.bio);
        }
    });
}

function get_notifications() {
    // gets the dashboard data
    $.get('/dashboard/notifications/', function(data) {
        $("#notification").empty();
        for (i = 0; i < data.length; i++) {
            $("#notification").prepend("<div class=\"alert alert-info\">" + data[i].fields.message + " - " + data[i].fields.prof_from_username + "<button link_name=\"" + data[i].fields.url_inclass + "\" class=\"notif_button btn btn-primary active\" style=\" float: right; margin-top: -7px;\">Enter into session</button></div>");
        }
        $("#notification").prepend("<h2 class=\"tabheading\">Notification</h2>");
    });
}

