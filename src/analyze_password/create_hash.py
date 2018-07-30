import crypt

def check_password(user_hash, salt):

    str = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    for p0 in range(len(str)):
        for p1 in range(len(str)):
            for p2 in range(len(str)):
                for p3 in range(len(str)):

                    count += 1
                    if count % 1000 == 0:
                        print(count)

                    tmp_password = str[p0] + str[p1] + str[p2] + str[p3]
                    if user_hash == crypt.crypt(tmp_password, salt):
                        print(tmp_password) 
                        return

salt = "$6$" + "G7Zt9PQ4"
test_hash = "$6$G7Zt9PQ4$sG/7BaUABqYIrOvLs9oX7MDGuJoR98juI8zTBOvpMEzvrBrtQ/ymZn01vqFLy48dwT1E9VIf.YJ/asP971DF90"

check_password(test_hash, salt)


