console.log('O arquivo script.js está carregado corretamente');

function toggleMenu() {
    const navMenu = document.querySelector('.nav-menu');
    navMenu.classList.toggle('mobile');
  }

// Componente ProductCard atualizado
Vue.component('product-card', { 
    // Define uma propriedade chamada 'product', que será passada para o componente como um objeto contendo informações sobre o produto.
    props: ['product'], 
    
    // A função data retorna um objeto contendo as variáveis reativas do componente. 
    // Aqui, estamos usando a variável 'flipped' para controlar o estado de rotação do card.
    data() {
        return {
            flipped: false // Define o estado inicial do card como não girado. 'false' significa que o lado da frente está sendo exibido.
        };
    },
    template: `
        <div class="product-card" @click="toggleFlip" :class="{ 'flipped': flipped }">
            <div class="card-inner">
                <!-- Frente do card -->
                <div class="card-face card-front">
                    <!-- Exibe a imagem do produto -->
                    <img :src="product.image" :alt="product.name" />
                    <!-- Exibe o nome do produto -->
                    <p>{{ product.name }}</p>
                    <!-- Link para o WhatsApp com base no número associado ao produto -->
                    <a :href="'https://wa.me/' + product.whatsapp" class="whatsapp-button" target="_blank">
                        <img src="img/icons/whatsapp.png" alt="WhatsApp"> Fazer pedido
                    </a>
                </div>
                <!-- Verso do card -->
                <div class="card-face card-back">
                    <!-- Conteúdo do verso do card -->
                    <p>{{ product.name }}</p>
                </div>
            </div>
        </div>
    `,
    methods: {
        // Método para alternar o estado de rotação do card
        toggleFlip() {
            this.flipped = !this.flipped; // Alterna o estado do card entre frente e verso
        }
    }
});




// Instância Vue principal
new Vue({
    // Define o elemento HTML onde o Vue será montado (id #app)
    el: '#app',
    // Define os dados da instância Vue
    data: {
        searchQuery: '', // Armazena o texto de busca digitado pelo usuário
        products: [ // Lista de produtos com nome, imagem e número do WhatsApp
            { name: 'Arranhador', image: 'img/produtos/Arranhador.png', whatsapp: '5561981639946' },
            { name: 'Bandana', image: 'img/produtos/Bandana.png', whatsapp: '5561981639946' },
            { name: 'Bandeja', image: 'img/produtos/Bandeja.png', whatsapp: '5561981639946' },
            { name: 'Banho Seco', image: 'img/produtos/BanhoSeco.png', whatsapp: '5561981639946' },
            { name: 'Blusão', image: 'img/produtos/Blusao.png', whatsapp: '5561981639946' },
            { name: 'Cama', image: 'img/produtos/Cama.png', whatsapp: '5561981639946' },
            { name: 'Cama Confortável', image: 'img/produtos/Cama2.png', whatsapp: '5561981639946' },
            { name: 'Capa de Chuva', image: 'img/produtos/CapaDeChuva.png', whatsapp: '5561981639946' },
            { name: 'Casinha', image: 'img/produtos/Casinha.png', whatsapp: '5561981639946' },
            { name: 'Cobertor', image: 'img/produtos/Cobertor.png', whatsapp: '5561981639946' },
            { name: 'Comedouro', image: 'img/produtos/Comedouro.png', whatsapp: '5561981639946' },
            { name: 'Creme Dental', image: 'img/produtos/CremeDental.png', whatsapp: '5561981639946' },
            { name: 'Golden Adulto', image: 'img/produtos/GoldenAdulto.png', whatsapp: '5561981639946' },
            { name: 'Golden Gato 1', image: 'img/produtos/GoldenGato1.png', whatsapp: '5561981639946' },
            { name: 'Golden Gato 2', image: 'img/produtos/GoldenGato2.png', whatsapp: '5561981639946' },
            { name: 'Golden Gato 3', image: 'img/produtos/GoldenGato3.png', whatsapp: '5561981639946' },
            { name: 'Golden Gato 4', image: 'img/produtos/GoldenGato4.png', whatsapp: '5561981639946' },
            { name: 'Golden Light', image: 'img/produtos/GoldenLight.png', whatsapp: '5561981639946' },
            { name: 'Golden Pequeno', image: 'img/produtos/GoldenPequeno.png', whatsapp: '5561981639946' },
            { name: 'Golden Pequeno Porte', image: 'img/produtos/GoldenPequenoPorte.png', whatsapp: '5561981639946' },
            { name: 'Golden Senior', image: 'img/produtos/GoldenSenior.png', whatsapp: '5561981639946' },
            { name: 'GranPlus Gato', image: 'img/produtos/GranPlusGato.png', whatsapp: '5561981639946' },
            { name: 'Guia', image: 'img/produtos/Guia.png', whatsapp: '5561981639946' },
            { name: 'Kit Higiene', image: 'img/produtos/KitHigiene.png', whatsapp: '5561981639946' },
            { name: 'Limpeza Auricular', image: 'img/produtos/LimpezaAuricular.png', whatsapp: '5561981639946' },
            { name: 'Pedigree Adulto', image: 'img/produtos/PedigreeAdulto.png', whatsapp: '5561981639946' },
            { name: 'Pedigree Filhote', image: 'img/produtos/PedigreeFilhote.png', whatsapp: '5561981639946' },
            { name: 'Peitoral', image: 'img/produtos/Peitoral.png', whatsapp: '5561981639946' },
            { name: 'Tapete Higiênico', image: 'img/produtos/TapeteHigienico.png', whatsapp: '5561981639946' },
            { name: 'Transporte', image: 'img/produtos/Transporte.png', whatsapp: '5561981639946' },
        ]
    },
    // Computed property para filtrar produtos com base na busca
    computed: {
        // Filtra produtos de acordo com o texto digitado no campo de busca
        filteredProducts() {
            // Filtra pelo nome do produto, comparando com o texto da busca (ignora maiúsculas/minúsculas)
            return this.products.filter(product =>
                product.name.toLowerCase().includes(this.searchQuery.toLowerCase())
            );
        }
    }
});


  









