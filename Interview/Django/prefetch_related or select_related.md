
select_related - для many to one/ one to one
prefetch_related - для связей many to many 


Поскольку select related делает join, а prefetch_related делает отдельный запрос, что позволяет избежать дублирования лишних данных при выборке из many to many и связывает данные на стороне python.