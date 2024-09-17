import random
import string

# تعريف مجموعة الأحرف المتاحة: الأحرف الكبيرة والصغيرة، والأرقام فقط
characters = string.ascii_letters + string.digits

# الطول المطلوب للنصوص
length = 22

# دالة لتوليد توليفة عشوائية
def generate_random_combination():
    return ''.join(random.choices(characters, k=length))

# توليد عدد معين من التوليفات العشوائية غير المكررة
def generate_unique_combinations(num_combinations, file_name, chunk_size=100000):
    count = 0
    unique_combinations = set()  # استخدام set لتجنب التكرار
    with open(file_name, 'w') as file:
        while count < num_combinations:
            new_combination = generate_random_combination()
            # تحقق إذا كانت التوليفة جديدة
            if new_combination not in unique_combinations:
                unique_combinations.add(new_combination)  # أضف التوليفة إلى المجموعة
                file.write(new_combination + '\n')
                count += 1
            # طباعة تقدم العملية بعد كل chunk_size
            if count % chunk_size == 0:
                print(f'{count} unique combinations generated so far...')

if __name__ == "__main__":
    output_file = 'unique_billion_combinations.txt'  # اسم الملف الناتج
    num_combinations = 1000000000  # عدد التوليفات المطلوبة (مليار)
    generate_unique_combinations(num_combinations, output_file)
