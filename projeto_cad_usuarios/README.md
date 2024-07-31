PAREI NO MINUTO 9:06 DO CANAL DEVAPRENDER


ESTOU VENDO UM PROJETO SIMPLES DO CANAL DEVAPRENDER PRA TER UMA BASE E DEPOIS IR FAZER UM CURSO DE DJANGO NO YOUTUBE, SÓ NÃO SEI QUANDO SERÁ ESSE DEPOIS.



Cada funcionalidade é um novo app no django;;
Para começar damos um django-admin startproject nomedoprojeto;
É bom que vc coloque um nome fácil para diferenciar um app do porjeto em si;
Para criar um app precisamos entrar dentro da pasta;
cd .\projeto_cad_usuarios\ e um ls para confirmar se vc entrou na pasta desejada;
Para dar inicio a um app usamos o django-admin startapp nomedoapp (recomendado iniciar com o nome app);
Para fazer com que o django saiba qual página exibir usamos o urls.py, views.py e o templates.py;
O urls serve para criarmos uma rota/caminho;
No views é algo como "certo, estou na url, mas o que eu vou exibir aqui?";
Logo em seguida, nós fazemos o que iremos exibir com html, css e js (frontend) no arquivo templates;
No urls.py iremos criar a estrutura de rota, view responsável e nome de referência. Caso eu queira simplesmente acessar a página inicial colocamos apenas '' mas se quisermos algo específico colocamos um erickgabriel/, ou seja, o que vem depois youtube.com/erickgabriel/;
Criamos uma função no views.py que diz o que fazer quando chegarmos na url que foi criada, então importamos o views pro urls.py;
A função é criada passando um request que é um parametro imbutido do django que te permite acessar os dados dentro daquela página e usamos um return render(request, 'usuarios/home.html');