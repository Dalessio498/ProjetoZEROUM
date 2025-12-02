package teste.teste.controller;


import teste.teste.model.Produto;
import teste.teste.repository.ProdutoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/produtos")
public class HomeController {

    @Autowired
    private ProdutoRepository produtoRepository;


    @GetMapping
    public String paginaProdutos(Model model) {
        model.addAttribute("produto", new Produto()); // formulário vazio
        model.addAttribute("produtos", produtoRepository.findAll()); // lista de produtos
        return "produtos";
    }

    // Criar produto
    @PostMapping("/criar")
    public String criarProduto(@ModelAttribute Produto produto) {
        produtoRepository.save(produto);
        return "redirect:/produtos"; // volta pra mesma página
    }

    // Excluir produto
    @GetMapping("/excluir/{id}")
    public String excluirProduto(@PathVariable int id) {
        produtoRepository.deleteById(id);
        return "redirect:/produtos";
    }
}

