ar CategoriesListPage = {
	init: function() {
		this.$container = $('.categories-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},
};

var ProductsListPage = {
	init: function() {
		this.$container = $('.products-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

};

$(document).ready(function() {
	CategoriesListPage.init();
	ProductsListPage.init();
});

$(document).ready(function(){
    $('#comprar').click(function(){
         $('events').submit();
    });
});