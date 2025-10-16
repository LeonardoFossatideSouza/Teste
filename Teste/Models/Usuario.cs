using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Teste.Models
{
    [Table("Usuarios")]
    public class Usuario
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public string Nome { get; set; }
        [Required]
        [DataType(DataType.Password)]
        public string Senha { get; set; }

        [Required]
        public Perfil Perfil { get; set; }
    }

    public enum Perfil
    {
        Admin,
        Usuario
    }
}
