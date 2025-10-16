using Microsoft.EntityFrameworkCore;
namespace Teste.Models
{
    public class AppDbConetext : DbContext
    {
        public AppDbConetext(DbContextOptions<AppDbConetext> options) : base(options)
        {
        }
        public DbSet<Veiculo> Veiculos { get; set; }

        public DbSet<Consumo> Consumos { get; set; }

        public DbSet<Usuario> Usuarios { get; set; }
    }
    
}
