from Post import Post
class User:

    posts_by_user_dict = {}

    def __init__(self, name, email, id_number, major, year_born):
        self.name = name
        self.email = email
        self.id_number = id_number
        self.major = major
        self.year_born = year_born
   
    def create_post(self, title, body, time):
        post = Post(title, body, time)

        if self.name in User.posts_by_user_dict:
            User.posts_by_user_dict[self.name].append(post)
        else:
            User.posts_by_user_dict[self.name] = [post]
        
        return post

jake = User('Jake','hilljake93@gmail.com',1234567,'biology',1993)
kate = User('Kate','katehill734@gmail.com',7654321,'education',1992)
becca = User('Becca','becmelang@gmail.com',9876543,'anthropology',1989)
frank = User('Frank','frobenalt@gmail.com',9361836,'political science',1991)
jesse = User('Jesse','jbfern@gmail.com',1902944,'criminal justice',1992)
rachel = User('Rachel','rachgrs@gmail.com',1928384,'marketing',1991)

jake.create_post("Post 1", "Im hungry", "10:15")
jake.create_post("Post 2", "sdjfnsdkfjnaef")
jake.create_post("Post 3", "kjsdnfskdajnf")
kate.create_post("Post 4", "kjsskdajnf")

posts = User.posts_by_user_dict 

for key in posts:
    print(key)
    for k in posts[key]:
        print(k)