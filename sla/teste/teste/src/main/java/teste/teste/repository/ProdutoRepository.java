package teste.teste.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import teste.teste.model.Produto;

public interface ProdutoRepository extends JpaRepository<Produto, Integer> {
}
