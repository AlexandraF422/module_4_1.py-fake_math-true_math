import fake_math as f_div
import true_math as t_div

result1 = f_div.fake_divide(69, 3)
result2 = f_div.fake_divide(3, 0)
result3 = t_div.true_divide(49, 7)
result4 = t_div.true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)