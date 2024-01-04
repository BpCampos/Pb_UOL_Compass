# SQL

## Seção 2 - Configuração do ambiente

- `pgAdmin` → Ferramenta para administrar e gerenciar banco de dados PostgreSQL
- Possui interfaces gráficas de administração, ferramentas de pesquisa, debugger de código procedural entre outras funcionalidades
- Podemos criar novas bases de dados ou schemas em bases já existentes no painel lateral do `pgAdmin`

## Seção 3 - Comandos básicos

### SELECT

- Serve para selecionar as colunas de tabelas

```sql

select coluna_1, coluna_2, coluna_3 from schema_1.tabela_1
```

- Para selecionar todas as informações da tabela, basta utilizar `*` junto do `select`

### DISTINCT

- Serve para remover as linhas duplicadas, mostrando apenas as linhas distintas

```sql
#Basta apenas colocar a palavra 'distinct' depois do select
select distinct coluna_1 from schema_1.tabela_1
```

- Se acrescentarmos mais de uma coluna, o comando `distinct` procurará por pares distintos ao invés de cada coluna separadamente

### WHERE

- Serve para filtrar as linhas da tabela de acordo com uma condição

```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x = true
```

- Para utilizar o `where` é preciso se atentar a letras `maiúsculas` e `minúsculas` pois trazem resultados diferentes, assim como é preciso utilizar aspas simples `‘’` quando for texto
- Podemos usar `OR` e `AND`, para adicionar mais de uma condição

```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x = true or age < 30 and car = false
```

- No `PostgreSQL` as datas são escritas como: ‘YYYY-MM-DD’ ou ‘YYYYMMDD’

### ORDER BY

- Server para ordenar a seleção de acordo com uma regra definida pelo usuário

```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x = true
order by coluna_1
```

- O `order by`, no caso de valores, sempre ordenará de forma crescente. Para alterar esse comportamento, basta adicionar `desc` ao final do valor do `order by`
- No caso de valores em texto, o `order by` apresentará eles na ordem alfabética

### LIMIT

- Limita a quantidade de linhas que serão mostradas ao executar a query

```sql
select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
limit N
```

- Podemos usar em conjunto com `order by` para pegar valores do fundo da tabela por exemplo

## Seção 4 - Operadores

### Operadores aritméticos

- São eles: `+ - * / ^ %`
- Podemos usar esse operadores para fazer o banco de dados nos mostrar dados alterados por nos através dos operadores

```sql
#Nesse caso uma coluna será criada com o resultado do manipulação de datas
select email, birth_date, (current_date - birth_date) / 365
from sales.customers
```

- O `current_date` é do próprio SQL
- Podemos usar `aspas duplas` para dar nome a colunas e.g. **“idade do cliente”**

```sql
#O operador || server para fazer junções de colunas
select first_name || ' ' || last_name as nome_completo from sales.customers
```

- O operador `||` server para fazer junções de colunas

### Operadores de comparação

- São eles: `= > < ≥ ≤ <>`
- Assim como os aritméticos, os operadores de comparação aparecem em uma nova coluna quando usados

### Operadores lógicos

- Unir expressões simples em uma expressão composta
- São eles:
  - `AND`
  - `OR`
  - `NOT`
  - `BETWEEN`
  - `IN` → Trabalha junto de uma lista para saber quais informações estão naquela tabela
  - `LIKE`
  - `ILIKE`
  - `IS NULL`

```sql
select * from sales.products where price between 100.000 and 200.000

select * from sales.products where price between not 100.000 and 200.000

select * from sales.products where brand in ('HONDA', 'TOYOTA', 'RENAULT')
```

- O operador `LIKE` tem uma função diferente usando `%` para representar um caractere coringa, ou seja é para considerar tudo que vier depois ou antes do `%` dependendo da situação

```sql
#O Like é case sensitive
select distinct first_name from sales.customers where first_name like 'ANA%'
```

- Usando `ILIKE` podemos ignorar das letras serem `maiúsculas` ou `minúsculas` na hora da busca

## Seção 5 - Funções agregadas

### Funções de agregação

- São elas: `COUNT() SUM() MIN() MAX() AVG()`

```sql
#Ao usar o count(*), contamos todas as linhas da tabela
select count(*) from sales.funnel
select count(distinct product_id) from sales.funnel
```

- O `COUNT()` não contabiliza espaços nulos a menos que passemos `*` como argumento
- Se quisermos usar o `distinct`, juntamente do count, precisamos colocar ele dentro do parenteses de argumento

```sql
#Subquery, quando passamos uma query dentro de outra
select *
from sales.products
where price = (select max(price) from sales.products)
```

- Na `subquery` acima buscamos o produto com o maior preço

### GROUP BY

- Serve para agrupar registros semelhantes de uma coluna
- Geralmente usado com as `funções de agragação`

```sql
select state, count(*) as contagem from sales.customers group by state

#Precisamos usar o **group** **by** com todos valores do select, caso contrário a query não irá funcionar. Nesse caso são: **'state'** e **'professional_status'**
select state, professional_status, count(*) as contagem from sales.customers
group by state, professional_status order by contagem desc
```

- Podemos usar o `group by` sem nada para que ele funcione igual ao `distinct`

### HAVING

- Serve para filtrar linhas de seleção por uma coluna agrupada

```sql
select state, count(*) from sales.customers group by state having count(*) > 100
```

## Seção 6 - Joins

### Tipos de joins

- `LEFT JOIN` → Junta todos os dados da tabela a esquerda e todos os dados da tabela a direita que correspondem aos da primeira
- `INNER JOIN` → Pega apenas os dados que derem match das duas tabelas
- `RIGHT JOIN` → O inverso do `LEFT JOIN`
- `FULL JOIN` → Pega todos os dados de ambas as tabelas

```sql
select t1.cpf, t1.name, t2.state
from temp_tables.tabela_1 as t1 left join temp_tables.tabela_2 as t2
on t1.cpf = t2.cpf
```

- No `select` passamos quais informações serão buscadas de quais tabelas. No caso acima: `t1.cpf` `t1.name` e `t2.state`
- Após passar o `select` escolhemos qual tabela será a `primeira(left)`, escolhemos o `tipo de join` e passamos a `segunda tabela(right)`
- Na parte do `on` passamos quais campos das duas tabelas devem ser levados em conta para o `join`

### Exemplos para facilitar

```sql
select cus.professional_status, count(fun.paid_date) as pagamentos
from sales.funnel as fun
left join sales.customers as cus
on cus.customer_id = fun.customer_id
group by cus.professional_status
```

- As duas tabelas continham `customer_id`, o que facilitou o join pegando o status profissional e a quantidade contada de pagamentos

```sql
select reg.region, count(fun.visit_page_date) as visitas
from sales.funnel as fun
left join sales.customers as cus
	on fun.customer_id = cus.customer_id
left join temp_tables.regions as reg
	on lower(cus.city) = lower(reg.city)
	and lower(cus.state) = lower(reg.state)
group by reg.region
order by visitas desc
```

- É possível usar mais de um `join`

## Seção 7 - Unions

- Serve para que podemos colar uma tabela na outra desde que as tabelas tenham o `mesmo número de colunas` e sejam do `mesmo tipo de dado`

```sql
select * from sales.products
union all
select * from sales.funnel
```

## Seção 8 - Subqueries

### Tipos de subquery

- Servem para consultar dados de outras consultas
- Subquery no `WHERE`

```sql
select * from sales.products
where price = (select min(price) from sales.products)
```

- Essa subquery não pode retornar mais de uma coluna
- Subquery com `WITH`

```sql
with alguma_tabela as (
	select professional_status, (current_date - birth_date) / 365 as idade
	from sales.customers
)
select professional_status, avg(idade) as idade_media
from alguma_tabela
group by professional_status
```

- No caso acima estamos criando com o `with` uma query que retorna duas colunas que serão utilizadas na próxima query
- Subquery `FROM`
- Funciona da mesma forma que a com `WITH` porém é feito dentro da própria query principal
- Subquery no `SELECT`

```sql
select fun.visit_id, fun.visit_page_date, sto.store_name,(
	select count(*)
	from sales.funnel as fun2
	where fun2.visit_page_date <= fun.visit_page_date
	and fun2.store_id = fun.store_id
) as visitas_acumuladas
from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
order by fun.visit_page_date
```

## Seção 9 - Tratamento de dados

### Conversão de unidades

- Tipos de conversão: `::` e `CAST`
- `Texto em data`

```sql
#Transformando o texto em data com ::date
select '2021-10-01'::date - '2021-02-01'::date
```

- `Texto em número`

```sql
select '100'::numeric - '10'::numeric
```

- `Número em texto`

```sql
select replace(112122::text, '1','A')
```

### Tratamento geral

- `CASE WHEN`
- Funciona de modo parecido com `if/else` ou `switch case` nas linguagens de programação

```sql
with faixa_de_renda(
	select
		income,
		case
				when income < 5000 then '0-5000'
				when income >= 5000 and income < 10000 then '5000 - 10000'
				when income >= 10000 and income < 15000 then '10000 - 15000'
				else '15000+'
				end as faixa_renda
	from sales.customers
)
```

- `COALESCE()`
- Serve para tratamento de dados nulos. Caso o valor passado seja nulo, o `coalesce` altera pelo segundo valor passado, geralmente uma subquery

```sql
select
	*,
	coalesce(population, (select avg(population) from temp_tables.regions)) as population_ajustada

from temp_tables.regions
```

### Tratamento de texto

- `LOWER()`

```sql
select upper('São Paulo') = 'SÃO PAULO'
```

- `UPPER()`

```sql
select lower('São Paulo') = 'são paulo'
```

- `TRIM()` → retira os espaços do texto

```sql
	select trim('SÃO PAULO     ') = 'SÃO PAULO'
```

- `REPLACE()` → altera os caracteres por outra sequência de caracteres

```sql
select replace('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'
```

### Tratamento de datas

- `INTERVAL` → soma de datas

```sql
#Podemos passar qual unidade de data que quisermos
select current_date + interval '10 weeks'
```

- `DATE_TRUNC` → usado para agrupar dados por mes/ano/dia e facilitar a visualização dos dados

```sql
select
	date_trunc('month', visit_page_date)::date as visit_page_month,
	count(*)
from sales.funnel
group by visit_page_month
```

- `EXTRACT` → extrai informações como `day of week(dow)` de datas. Outras informações podem ser extraídas também

```sql
select
	current_date
	extract('dow' from current_date)
```

- `DATEDIFF` → calcula diferença entre datas

```sql
select datediff('weeks', '2018-06-01', current_date)
```

### Funções

- Conteúdo avançado para criar soluções para queries `sql` usando outros operadores

## Seção 10 - Manipulação de tabelas

### Tabelas - Criação e deleção

- Criar uma tabela a partir de uma `query`

```sql
select
	customer_id,
	datediff('years', birth_date, current_date) as idade_clientes
	into temp_tables.customer_age #forma de criar uma tabela
from sales.customers
```

- Criar uma tabela a partir do zero

```sql
create table temp_tables.profissoes (
	professional_status varchar,
	status_profissional varchar
)
#Agora precisamos inserir dados na nova tabela
insert into temp_tables.profissoes
(professional_status, status profissional)

values
('freelancer', 'freelancer'),
('retired','aposentado'),
('clt','clt')
... #Todos os outros dados necessários
```

- Deletar tabelas

```sql
drop table temp_tables.profissoes
```

### Linhas - Inserção, atualização e deleção

- Para inserir dados, basta utilizar o `insert into` e os `values` como mostrado na parte de tabelas
- **Atualização:**

```sql
update temp_tables.profissoes
set professional_status = 'intern'
where status_profissional = 'estagiario(a)'
```

- Apagar linhas:

```sql
delete from temp_tables.profissoes
where status_profissional = 'desempregado(a)'
or status_profissional = 'estagiario(a)'
```

### Colunas - Inserção, atualização e deleção

- **Inserir colunas**

```sql
alter table sales.customers
add customer_age int

#Inserir dados na nova coluna
update sales.customer
set customer_age = datediff('years', birth_date, current_date)
where true
```

- **Alterar do tipo da coluna**

```sql
alter table sales.customers
alter column customer_age type varchar
```

- **Alterar o nome da coluna**

```sql
alter table sales.customers
rename column customer_age to age
```

- **Deletar coluna**

```sql
drop column age
```
