import hashlib

username_trial = "SCHOFIELD"
bUsername_trial = b"SCHOFIELD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"

key_part_dynamic1_solved = ""

# if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[4]

#         if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[5]

#         if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[3]

#         if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
#             return False
#         else:
#             i += 1
key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[6]

#         if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[2]
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[7]

#         if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
#             return False
#         else:
#             i += 1

key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[1]
#         if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
#             return False
key_part_dynamic1_solved += hashlib.sha256(bUsername_trial).hexdigest()[8]

print(key_part_static1_trial + key_part_dynamic1_solved + key_part_static2_trial)