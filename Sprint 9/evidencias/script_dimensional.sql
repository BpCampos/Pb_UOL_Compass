SELECT * FROM Cliente c

SELECT * FROM Carro car

SELECT * FROM Combustivel co

SELECT * FROM Locacao l 

SELECT * FROM Vendedor v

-- Dimensão Cliente
create view dim_cliente as
select idCliente as codigoCliente,
	   nome as nomeCliente,
	   cidade as cidadeCliente,
	   estado as estadoCliente,
	   pais as paisCliente
from Cliente

-- Dimensão Carro
create view dim_carro as
select idCarro as codigoCarro,
	   kilometragem as kilometragemCarro,
	   classificacao as classificacaoCarro,
	   marca as marcaCarro,
	   modelo as modeloCarro,
	   ano as anoCarro,
	   co.idCombustivel as combustivel
from Carro car
join Combustivel co on co.idCombustivel = car.idCombustivel

-- Dimensão Combustivel
create view dim_combustivel as
select idCombustivel as codigoCombustivel,
	   tipoCombustivel as tipoCombustivel
from Combustivel co

-- Dimensão Vendedor
create view dim_vendedor as
select idVendedor as codigoVendedor,
	   nome as nomeVendedor,
	   sexo as sexoVendedor,
	   estado as estadoVendedor
from Vendedor v

-- Dimensão tempo
create view dim_tempo as
select datalocacao  as dataLocacao,
	   STRFTIME('%Y', dataLocacao) as anoLocacao,
	   STRFTIME('%m', dataLocacao) as mesLocacao,
	   STRFTIME('%W', dataLocacao) as semanaLocacao,
	   STRFTIME('%d', dataLocacao) as diaLocacao,
	   horaLocacao as horaLocacao,
	   STRFTIME('%H', horaLocacao) as horaLocacao, 
	   STRFTIME('%M', horaLocacao) as minutoLocacao,
	   dataEntrega as dataEntrega,
	   STRFTIME('%Y', dataEntrega) as anoEntrega,
	   STRFTIME('%m', dataEntrega) as mesEntrega,
	   STRFTIME('%W', dataEntrega) as semanaEntrega,
	   STRFTIME('%d', dataEntrega) as diaEntrega,
	   horaEntrega as horaEntrega,
	   STRFTIME('%H', horaEntrega) as horaEntrega, 
	   STRFTIME('%M', horaEntrega) as minutoEntrega
from Locacao l

create view fato_locacao as
select idLocacao as codigoLocacao,
	   dataLocacao as dataLocacao,
	   horaLocacao as horaLocacao,
	   qtdDiaria as qtdDiara,
	   vlrDiaria as vlrDiaria,
	   dataEntrega as dataEntrega,
	   horaEntrega as horaEntrega,
	   idCliente as codigoCliente,
	   idCarro as codigoCarro,
	   idVendedor as codigoVendedor
from Locacao l

select * from dim_carros

select * from dim_cliente

select * from dim_tempo

select * from dim_combustivel 

select * from dim_vendedor

select * from fato_locacao fl

