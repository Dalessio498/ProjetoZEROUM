package teste.teste.model;

import jakarta.persistence.*;
import java.math.BigDecimal;

@Entity
@Table(name = "produto")
public class Produto {

    public Produto() {}

    public Produto(String nomeProduto, BigDecimal precoProduto, String marcaProduto, String categoriaProduto) {
        this.nomeProduto = nomeProduto;
        this.precoProduto = precoProduto;
        this.marcaProduto = marcaProduto;
        this.categoriaProduto = categoriaProduto;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "nome_produto")
    private String nomeProduto;

    @Column(name = "preco_produto")
    private BigDecimal precoProduto;

    @Column(name = "marca_produto")
    private String marcaProduto;

    @Column(name = "categoria_produto")
    private String categoriaProduto;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNomeProduto() {
        return nomeProduto;
    }

    public void setNomeProduto(String nomeProduto) {
        this.nomeProduto = nomeProduto;
    }

    public BigDecimal getPrecoProduto() {
        return precoProduto;
    }

    public void setPrecoProduto(BigDecimal precoProduto) {
        this.precoProduto = precoProduto;
    }

    public String getMarcaProduto() {
        return marcaProduto;
    }

    public void setMarcaProduto(String marcaProduto) {
        this.marcaProduto = marcaProduto;
    }

    public String getCategoriaProduto() {
        return categoriaProduto;
    }

    public void setCategoriaProduto(String categoriaProduto) {
        this.categoriaProduto = categoriaProduto;
    }
}
