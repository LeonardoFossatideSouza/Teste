using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
namespace Teste.Models
{
    [Table("Consumo")]
    public class Consumo
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar a descrição")]
        [Display(Name = "Descrição")]
        public string Descricao { get; set; }

        public DateTime Data { get; set; }


        [Required(ErrorMessage = "Obrigatorio informar o Valor")]
        public decimal Valor { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar o KM do Veiculo")]
        public int km { get; set; }

        [Display(Name = "Tipo de Combustivel")]
        public TipodeCombustivel Tipo { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar o Veiculo")]
        [Display(Name = "Veiculo")]
        public int VeiculoId { get; set; }

        [ForeignKey("VeiculoId")]
        public Veiculo Veiculo { get; set; }
    }

    public enum  TipodeCombustivel
    {
        Gasolina,
        Etanol
    }
}
