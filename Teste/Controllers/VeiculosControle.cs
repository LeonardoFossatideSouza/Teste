using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using Teste.Models;
namespace Teste.Controllers
{
    public class VeiculosControle : Controller
    {
        private readonly AppDbConetext _context;
        public VeiculosControle(AppDbConetext context)
        {
            _context = context;

        }

        public async Task<IActionResult> Index()
        {
            var dados = _context.Veiculos.ToList();
            return View(dados);
        }
        public IActionResult Create()
        {
            return View();
        }
        [HttpPost]
        public async Task<IActionResult> Create(Veiculo veiculo)
        {
            if (ModelState.IsValid)
            {
                _context.Veiculos.Add(veiculo);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }
            return View(veiculo);
        }
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
                return NotFound();

            var dados = await _context.Veiculos.FindAsync(id);

            if (dados == null)
                return NotFound();

            return View(dados);
        }
        [HttpPost]
        public async Task<IActionResult> Edit(int id, Veiculo veiculo)
        {
            if (id != veiculo.Id)
                return NotFound();

            if (ModelState.IsValid)
            {
                _context.Veiculos.Update(veiculo);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }
            return View(veiculo);
        }
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
                return NotFound();

            var dados = await _context.Veiculos.FindAsync(id);

            if (dados == null)
                return NotFound();

            return View(dados);
        }
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
                return NotFound();

            var dados = await _context.Veiculos.FindAsync(id);

            if (dados == null)
                return NotFound();

            return View(dados);
        }
        [HttpPost, ActionName("Delete")]
        public async Task<IActionResult> DeleteConfig(int? id)
        {
            if (id == null)
                return NotFound();

            var dados = await _context.Veiculos.FindAsync(id);

            if (dados == null)
                return NotFound();
            
            _context.Veiculos.Remove(dados);
            await _context.SaveChangesAsync();

            return RedirectToAction("index");
        }
     public async Task<IActionResult> Relatorio(int? id)
        {
            if (id == null)
                return NotFound();
            var Veiculos = await _context.Veiculos.FindAsync(id);
            if (Veiculos == null)
                return NotFound();
            var consumos = _context.Consumos
                .Where(c => c.VeiculoId == id)
                .OrderByDescending(c => c.Data)
                .ToList();

            decimal total = consumos.Sum(c => c.Valor); // Remover "decimal" da declaração, pois já existe como parâmetro

            ViewBag.Veiculo = Veiculos;
            ViewBag.Total = total;

            return View(consumos);

        }       
    
    
    
    }
}
