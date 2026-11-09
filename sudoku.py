
# python sudoku.py input_file output_file

import sys
import re
 
def number_finder(input_file, output_file):
    file = input_file.read()
    row_list = re.split("\n", file)
    row_list = [list(strnumbers.replace(" ", "")) for strnumbers in row_list]
    row_list = [[int(number) for number in row] for row in row_list]
    column_list = [[row[n] for row in row_list] for n in range(0,9)]
    three_x_threes = []
    for m in range(0, 7, 3):
        temporary_list = []
        for n in range(0,9):
            temporary_list.append(row_list[n][m:m+3])
        for n in range(0, 7, 3):
            three_x_threes.append(temporary_list[n] + temporary_list[n+1] + temporary_list[n+2])
    
    step = 0
    while step != len(re.findall("0", file)):
        for n in range(0,9):
            for i, number in enumerate(row_list[n]):
                if number == 0:
                    row_p_list = [numb for numb in row_list[n] if numb != 0]
                    column_p_list = [numb for numb in column_list[i] if numb != 0]
                    m = (i // 3) * 3 + (n // 3) #i ve n cinsinden kacinci blokta oldugunu bulmak icin formul
                    mth_number = (n % 3) * 3 + (i % 3)#ayni yontem ancak konum bulmak uzerine
                    # bu formulun kaynagi su: bizden once kac tane 3 erli sira doldu? (012 rowlar bir sira 345 rowlar bir sira 678 bir sira)
                    # mesela 8. blocktaysak 8"i 3 e bolebiliriz (cunku boylelikle tam olarak kac siranin dolu oldugunu anliyoruz 
                    # kalan ise sonraki 3 lude bizim kacinci olacagimiz yani en son 3 lude 2. yiz. 
                    three_p_list = [numb for numb in three_x_threes[m] if numb != 0]
                    potential_numbers = [numb for numb in range(1,10) if numb not in list(set(row_p_list).union(set(three_p_list), set(column_p_list)))]
                    
                    if len(potential_numbers) == 1:
                        row_list[n][i] = potential_numbers[0]
                        column_list[i][n] = potential_numbers[0]
                        three_x_threes[m][mth_number] = potential_numbers[0]
                        step += 1
                        output_file.write("-" * 18 + "\n")
                        output_file.write(f"Step {step} - {potential_numbers[0]} @ R{n+1}C{i + 1}" + "\n")
                        output_file.write("-" * 18 + "\n")
                        for row in row_list:
                            output_file.write(" ".join([str(numb) for numb in row]) + "\n")
                    

def main():
    with open(sys.argv[1],"r") as input_file:
        with open(sys.argv[2], "w") as output_file:
            number_finder(input_file,output_file) 


if __name__ == "__main__":
    main()