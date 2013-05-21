-- (a) select σdocid=10398_txt_earn(frequency) 
select count(*) from (select * from frequency f where f.docid = '10398_txt_earn');

-- (b) select project πterm( σdocid=10398_txt_earn and count=1(frequency))
select count(*) from (select term from frequency f where f.docid = '10398_txt_earn' and f.count = 1);

-- (c) union πterm( σdocid=10398_txt_earn and count=1(frequency)) U πterm( σdocid=925_txt_trade and count=1(frequency))
select count(*) from (select term from frequency f1 where f1.docid='10398_txt_earn' and f1.count=1 union select term from frequency f2 where f2.docid='925_txt_trade' and f2.count=1);

-- (d) count:
select count(*) from (select * from frequency f where f.term = 'parliament');

-- (e) big documents
select count(*) from (select docid, sum(count) from frequency f group by f.docid having sum(f.count) > 300);

-- (f) two words
select count(*) from (select f1.docid from frequency f1 inner join frequency f2 on f1.docid = f2.docid where f1.term = 'transactions' and f2.term='world');