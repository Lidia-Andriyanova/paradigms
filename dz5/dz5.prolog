// Логическая парадигма

sum_list([], 0):-!.
sum_list([Head|Tail], Sum):- sum_list(Tail, TailSum), Sum is TailSum + Head


sum_list([1, 2, 3, 4], Sum).