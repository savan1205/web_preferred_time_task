odoo.define('task_1912.preferred_time', function (require) {

'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;
require('website_sale.website_sale');
publicWidget.registry.WebsiteSale = publicWidget.registry.WebsiteSale.include({
    events: _.extend({}, VariantMixin.events || {}, {
      'change select#preferred_time': '_onChangePreferred',
    }),
    start: function () {

                return this._super(...arguments);
            },
    _onChangePreferred:function(ev)
    {
    var current_selected_preffered = $(ev.currentTarget.options).filter(':selected').val()
    this._rpc({
            model: 'sale.order',
            method : 'update_preffered_time',
            args: [[parseInt(current_selected_preffered),$(this.$el.find('div#cart_total table tr#order_total_untaxed td')[1]).find('span').data('oe-id')
]],
        });


    }
    })
    return publicWidget.registry.WebsiteSale;
    })
