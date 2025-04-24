name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")
vcontent =f'''FN:{name}
TEL:{phone}
EMAIL:{email}'''
with open(f"{name.replace(' ','_')}.vcf", "w") as vfile:
    vfile.write(str(vcontent))
print("vCard for",name,"has been created successfully!")
