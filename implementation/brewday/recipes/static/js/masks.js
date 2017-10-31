jQuery(function($){
	$("#idatanascimento").mask("99/99/9999",{placeholder:"__/__/____"});
	$(".data_mask").mask("99/99/9999",{placeholder:"__/__/____"});
	$(".hora_mask").mask("99:99",{placeholder:"__:__"});
	$("#icpf").mask("999.999.999-99",{placeholder:"___.___.___-__"});
	$("#icnpj").mask("99.999.999/9999-99",{placeholder:"__.___.___/____-__"});
	$("#itelefone").mask(SPMaskBehavior, spOptions);
});

var SPMaskBehavior = function (val) {
  return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
  onKeyPress: function(val, e, field, options) {
      field.mask(SPMaskBehavior.apply({}, arguments), options);
    }
};
