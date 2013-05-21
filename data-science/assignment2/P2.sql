-- (g) multiply
select A.row_num, B.col_num, sum(A.value * B.value) from A join B on A.col_num = B.row_num group by A.row_num, B.col_num;