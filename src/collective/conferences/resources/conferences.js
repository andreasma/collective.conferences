/*global location: false, window: false, jQuery: false */
(function ($, collective_conferences) {
    "use strict";
    collective_conferences.init_voting_viewlet = function (context) {
        var notyetvoted = context.find("#conference_notyetvoted"),
            alreadyvoted = context.find("#conference_alreadyvoted"),
            delete_votings = context.find("#conference_delete_votings"),
            delete_votings2 = context.find("#conference_delete_votings2");

        if (context.find("#conference_voted").length !== 0) {
            alreadyvoted.show();

        } else {
            notyetvoted.show();
        }

        function vote(rating) {
            return function inner_vote() {
                $.post(context.find("#context_url").attr('href') + '/vote', {
                    rating: rating
                }, function () {
                    location.reload();
                });
            };
        }

        context.find("#conference_voting_plus").click(vote(1));
        context.find("#conference_voting_neutral").click(vote(0));
        context.find("#conference_voting_negative").click(vote(-1));

        delete_votings.click(function () {
            delete_votings2.toggle();
        });
        delete_votings2.click(function () {
            $.post(context.find("#context_url").attr("href") + "/clearvotes", function () {
                location.reload();
            });
        });
    };
}(jQuery, window.collective_conferences = window.collective_conferences || {}));