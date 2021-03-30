odoo.define('ray.school', function (require) {
    "use strict";

    var core = require('web.core');
    var tour = require('web_tour.tour');

    var _t = core._t;

    tour.register('ray_school',
        { url: "/web" },
        [
            tour.STEPS.SHOW_APPS_MENU_ITEM,
            {
                trigger: '.o_app[data-menu-xmlid="ray_school.ray_school_home_menu_top"]',
                content: _t('Open Ray School'),
                position: 'bottom',
                edition: 'enterprise'
            },
            {
                trigger: '[data-menu-xmlid="ray_school.ray_school_students"]',
                content: _t("click students")
            },
            {
                trigger: 'span:contains("partents")',
                content: _t("click students"),
            },
            {
                trigger: ".o_list_button_add",
                content: _t('create button clicked'),
            },
            {
                trigger: 'input[name="email"]',
                content: _t('write mail '),
                run :'text mail@mail.com'
            }
        ]
    );

});
