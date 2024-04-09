select * from tb_locacao tl

create table Cliente(
idCliente INT PRIMARY KEY,
nome VARCHAR(100),
cidade VARCHAR(40),
estado VARCHAR(40),
pais VARCHAR(40)
)

insert into Cliente (idCliente, nome, cidade, estado, pais)
select idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente from tb_locacao tl
group by tl.idCliente

create table Carro(
idCarro INT PRIMARY KEY,
kilometragem INT,
classificacao VARCHAR(50),
marca VARCHAR(80),
modelo VARCHAR(80),
ano INT,
idCombustivel INT,
foreign key (idCombustivel) references Combustivel(idCombustivel)
)

insert into Carro (idCarro, kilometragem, classificacao, marca, modelo, ano, idCombustivel)
select idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel from tb_locacao tl
group by tl.idCarro

create table Combustivel(
idCombustivel INT PRIMARY KEY,
tipoCombustivel VARCHAR(20)
)

insert into Combustivel (idCombustivel, tipoCombustivel)
select idcombustivel, tipoCombustivel from tb_locacao tl
group by tl.idcombustivel

create table Locacao(
idLocacao INT PRIMARY KEY,
dataLocacao DATETIME,
horaLocacao TIME,
qtdDiaria INT,
vlrDiaria DECIMAL(18,2),
dataEntrega DATETIME,
horaEntrega TIME,
idCliente INT,
idCarro INT,
idVendedor INT,
foreign key (idCliente) references Cliente(idCliente),
foreign key (idCarro) references Carro(idCarro),
foreign key (idVendedor) references Vendedor(idVendedor)
)

insert into Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idCarro, idVendedor)
select idLocacao, substr(dataLocacao, 1, 4) || '-' || SUBSTR(dataLocacao, 5, 2) || '-' || SUBSTR(dataLocacao, 7, 2), horaLocacao, qtdDiaria, vlrDiaria, substr(dataEntrega, 1, 4) || '-' || SUBSTR(dataEntrega, 5, 2) || '-' || SUBSTR(dataEntrega, 7, 2), horaEntrega, idCliente, idCarro, idVendedor from tb_locacao tl
group by tl.idLocacao

create table Vendedor(
idVendedor INT PRIMARY KEY,
nome VARCHAR(15),
sexo SMALLINT,
estado VARCHAR(40)
)

insert into Vendedor (idVendedor, nome, sexo, estado)
select idVendedor, nomeVendedor, sexoVendedor, estadoVendedor from tb_locacao tl
group by tl.idVendedor

select * from Cliente

select * from Carro

select * from Combustivel

select * from Locacao

select * from Vendedor