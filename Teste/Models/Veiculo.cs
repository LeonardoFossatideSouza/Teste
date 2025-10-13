using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Teste.Models
{
    [Table("Veiculos")]
    public class Veiculo
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar nome")]
        public string Nome { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar Placa")]
        public string Placa { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar Ano de Fabricação")]
        public int AnoFabricacao { get; set; }

        [Required(ErrorMessage = "Obrigatorio informar Ano do Modelo")]
        public int AnoModelo { get; set; }
    }
}
