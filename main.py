from flask import Flask, url_for, render_template, request, redirect, send_from_directory, jsonify
import json
from twilio.rest import Client
from bs4 import BeautifulSoup
import requests
import random
from datetime import date
today=str(date.today())

img_names=[]
for i in range(1,26):
    img_names.append(str(i))
video_frames=['https://www.youtube.com/embed/PsYhx7UVjAI',"https://www.youtube.com/embed/UykTYYgArbc","https://www.youtube.com/embed/VzqbCpadANs","https://www.youtube.com/embed/z4OV0N6A0fQ","https://www.youtube.com/embed/gQsRSfGFx5s",]

account_sid='AC7f538cde22899d3e4520523ed21164aa'
auth_token="443e389f144466d402445f2cdef7c2d6"

# website_data=requests.get("https://parade.com/1034896/marynliles/nature-quotes/").text
# soup=BeautifulSoup(website_data,"html.parser")
# quotes=soup.find_all("p")
#
# quotes=quotes[4:len(quotes)-1]
# quotes_list=[]
# for quote in quotes:
#     temp_list=quote.text.split('.')
#     try:
#         quotes_list.append(temp_list[1])
#     except:
#         quotes_list.append("This is the most beautiful place in the world")


quotes_list=[' In nature, nothing is perfect and everything is perfect', ' Forget not that the earth delights to feel your bare feet and the winds long to play with your hair', ' Look deep into nature, and then you will understand everything better', ' Heaven is under our feet as well as over our heads', ' To me a lush carpet of pine needles or spongy grass is more welcome than the most luxurious Persian rug', ' We don’t inherit the earth from our ancestors, we borrow it from our children', 'This is the most beautiful place in the world', ' I believe in God, only I spell it Nature', ' Choose only one master—nature', ' Nature does not hurry, yet everything is accomplished', ' If you truly love nature, you will find beauty everywhere', '\xa0There is something infinitely healing in the repeated refrains of nature—the assurance that dawn comes after night, and spring after winter', ' Leave the road, take the trails', ' Live in each season as it passes; breathe the air, drink the drink, taste the fruit, and resign yourself to the influence of the earth', ' I go to nature to be soothed and healed, and to have my senses put in order', " It is not so much for its beauty that the forest makes a claim upon men's hearts, as for that subtle something, that quality of air that emanation from old trees, that so wonderfully changes and renews a weary spirit", 'This is the most beautiful place in the world', ' For most of history, man has had to fight nature to survive; in this century he is beginning to realize that, in order to survive, he must protect it', ' There’s a whole world out there, right outside your window', ' To forget how to dig the earth and to tend the soil is to forget ourselves', " Preserve and cherish the pale blue dot, the only home we've ever known", ' Study nature, love nature, stay close to nature', ' The sun, with all those planets revolving around it and dependent on it, can still ripen a bunch of grapes as if it had nothing else in the universe to do', ' To make a prairie it takes a clover and one bee, One clover, and a bee, And revery', ' Men argue', ' All my life through, the new sights of Nature made me rejoice like a child', ' Colors are the smiles of nature', ' Land really is the best art', 'This is the most beautiful place in the world', ' Everything in nature invites us constantly to be what we are', " The best thing one can do when it's raining is to let it rain", ' Many eyes go through the meadow, but few see the flowers in it', " Spring is nature's way of saying, 'Let's party!’ —Robin Williams", ' The earth has music for those who listen', ' There are always flowers for those who want to see them', ' The goal of life is to make your heartbeat match the beat of the universe, to match your nature with Nature', ' The Amen of nature is always a flower', ' Nature teaches more than she preaches', 'This is the most beautiful place in the world', ' Adopt the pace of nature', ' A weed is no more than a flower in disguise', ' The earth is what we all have in common', ' Although we say mountains belong to the country, actually, they belong to those that love them', ' The least movement is of importance to all nature', ' The goal of life is living in agreement with nature', ' Use what talents you possess: the woods would be very silent if no birds sang there except those that sang best', ' Let the rain kiss you', ' Nature is loved by what is best in us', ' Solitary trees, if they grow at all, grow strong', 'This is the most beautiful place in the world', ' A morning-glory at my window satisfies me more than the metaphysics of books', ' The world is not to be put in order', ' One touch of nature makes the whole world kin', ' By discovering nature, you discover yourself', ' Time spent amongst trees is never wasted time', 'This is the most beautiful place in the world', ' Sunshine is delicious, rain is refreshing, wind braces us up, snow is exhilarating; there is really no such thing as bad weather, only different kinds of good weather', ' Never, no, never did nature say one thing and wisdom another', ' If we surrendered to earth’s intelligence we could rise up rooted, like trees', ' The fairest thing in nature, a flower, still has its roots in earth and manure', ' Those who contemplate the beauty of the earth find reserves of strength that will endure as long as life lasts', ' The poetry of the earth is never dead', ' I just wish the world was twice as big and half of it was still unexplored', ' In all things of nature there is something of the marvelous', ' The richness I achieve comes from Nature, the source of my inspiration', ' The ocean is a mighty harmonist', ' Nature always wears the colors of the spirit', ' Nature is just enough; but men and women must comprehend and accept her suggestions', ' I think nature’s imagination is so much greater than man’s, she’s never going to let us relax', ' Deep in their roots, all flowers keep the light', ' Plant seeds of happiness, hope, success, and love; it will all come back to you in abundance', 'This is the most beautiful place in the world', ' Between every two pines there is a doorway to a new world', ' Life sucks a lot less when you add mountain air, a campfire and some peace and quiet', ' Don’t judge each day by the harvest you reap but by the seeds you plant', ' Let us permit nature to have her way', ' Nature is not a place to visit', ' I felt my lungs inflate with the onrush of scenery—air, mountains, trees, people', ' To sit in the shade on a fine day and look upon verdure is the most perfect refreshment', ' I believe a leaf of grass is no less than the journey-work of the stars', ' Nature’s beauty is a gift that cultivates appreciation and gratitude', ' The earth laughs in flowers', 'This is the most beautiful place in the world', ' I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived', ' Looking at beauty in the world, is the first step of purifying the mind', ' Nature is pleased with simplicity', ' Nature is an infinite sphere of which the center is everywhere and the circumference nowhere', ' Yosemite Valley, to me, is always a sunrise, a glitter of green and golden wonder in a vast edifice of stone and space', ' Love the world as your own self; then you can truly care for all things', ' Should you shield the canyons from the windstorms you would never see the true beauty of their carvings', ' We still do not know one thousandth of one percent of what nature has revealed to us', ' It is said that the forest has a certain limit if you look straight ahead, but the sides are boundless', " If you can't be in awe of Mother Nature, there's something wrong with you", ' Like music and art, love of nature is a common language that can transcend political or social boundaries', " If one way be better than another, that you may be sure is nature's way", ' Going to the mountains is like going home', ' Those who find beauty in all of nature will find themselves at one with the secrets of life itself', ' The world is mud-luscious and puddle-wonderful', ' Some of nature’s most exquisite handiwork is on a miniature scale, as anyone knows who has applied a magnifying glass to a snowflake', ' Just living is not enough', ' The beauty of the natural world lies in the details', ' My father considered a walk among the mountains as the equivalent of churchgoing', ' Every flower is a soul blossoming in nature', 'This is the most beautiful place in the world', ' Man’s heart away from nature becomes hard', ' I took a walk in the woods and came out taller than the trees', ' If you wish to know the divine, feel the wind on your face and the warm sun on your hand', ' Nature is the art of God', ' Everything in nature is lyrical in its ideal essence, tragic in its fate, and comic in its existence', ' Rest is not idleness, and to lie sometimes on the grass under trees on a summer’s day, listening to the murmur of the water, or watching the clouds float across the sky, is by no means a waste of time']



app = Flask(__name__)

@app.route("/")
def home():
    with open("images_data.json", "r") as fp:
        images_data = json.load(fp)
    with open("Famous-people.json", "r") as fp:
        data2 = json.load(fp)
    with open("blog_details.json",'r') as fp:
        blogs=json.load(fp)
    return render_template("index.html",i=random.choice([1,2,3,4,5,6]),data=images_data, data2=data2, quote=random.choice(quotes_list),hero_img=random.choice(img_names),video=random.choice(video_frames),home="active",read="",write="",know="",contact="",blogs=blogs)

@app.route("/about_uk")
def about():
    with open("Famous-people.json", "r") as fp:
        data2 = json.load(fp)
    return render_template("about_uk.html",i=random.choice([1,2,3,4,5,6]),data2=data2,quote=random.choice(quotes_list),hero_img=random.choice(img_names),home="",read="",write="",know="active",contact="")

@app.route("/messages",methods=["POST","GET"])
def message():
    if request.method=="POST":
        data = request.form
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{data['name']}\n{data['email']}\n{data['subject']}\n{data['message']}\n",
            from_='+12407302563',
            to='+917037632200'
        )
        print(message.sid)
        return redirect(url_for("reply",message="You will be contacted soon."))


# @app.route('/newpage')
# def newpage():
#     return render_template('portfolio-details.html')

@app.route("/<message>")
def reply(message):
    return render_template('reply.html',i=random.choice([1,2,3,4,5,6]),hero_img=random.choice(img_names),message=message)



@app.route('/<int:index>',methods=["POST","GET"])
def read_blog(index):
    with open("blog_details.json","r") as fp:
        data=json.load(fp)
    for blog in data:
        if data[blog]['number']==index:
            requested_post=data[blog]
    if request.method=="POST":
        comment_data=request.form
        for blog in data:
            if int(data[blog]['number'])==index:
                data[blog]['comments'][comment_data['name']]=comment_data['comment']
                requested_post=data[blog]
                with open("blog_details.json","w") as fp:
                    json.dump(data,fp,indent=4)

    return render_template('blog_details.html',hero_img=random.choice(img_names),i=random.choice([1,2,3,4,5,6]),data=requested_post,date=today,alldata=data,home="",read="active",write="",know="",contact="")

@app.route('/add_images',methods=["GET","POST"])
def add_images():
    if request.method=="POST":
        data=request.form
        with open("images_data.json",'r') as fp:
            img_data=json.load(fp)

        with open("images_data.json","w") as fp:
            img_data[data['img_name']]={
                'url':data['url'],
                'category':data['category'],
                'link':data['link']
            }
            json.dump(img_data,fp,indent=4)

        return render_template('message.html',hero_img=random.choice(img_names),message="Your image has been added.")
    else:
        return render_template('add-images.html',i=random.choice([1,2,3,4,5,6]),hero_img=random.choice(img_names))


@app.route('/add_blog',methods=["GET","POST"])
def add_blog():
    if request.method=="POST":
        blog_form=request.form
        with open("blog_details.json","r") as fp:
            data=json.load(fp)
        number=1
        for blog in data:
            number+=1
        new_blog={
            "number":number,
            "author":blog_form['name'],
            "img-url":blog_form['img'],
            "date":today,
            "blog-title":blog_form['title'],
            "blog":blog_form['blog'],
            "about-author":blog_form['about'],
            "comments":{}
        }
        data[blog_form['title']]=new_blog
        with open("blog_details.json","w") as fp:
            json.dump(data,fp,indent=4)
        return redirect(url_for('read_blog',index=number))
    return render_template('add_blog.html',i=random.choice([1,2,3,4,5,6]),hero_img=random.choice(img_names),home="",read="",write="active",know="",contact="")


@app.route('/download_map')
def download_map():
    return send_from_directory('download',path='Tourist-Map-Uttarakhand.pdf')

@app.route('/contact')
def contact():
    return render_template('contact.html',i=random.choice([1,2,3,4,5,6]),hero_img=random.choice(img_names),home="",read="",write="",know="",contact="active")

@app.route('/blog_api')
def blog_api():
    with open("blog_details.json","r") as fp:
        blog_data=json.load(fp)
    return jsonify(blog_data)

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        blog_form=request.form
        with open("user_details.json","r") as fp:
            data=json.load(fp)
        number=1
        for user in data:
            number+=1
        new_user={
            "number":number,
            "name":blog_form['name'],
            "state":blog_form['state'],
            "password":blog_form['password'],
            "email":blog_form['email'],
            "about":blog_form['about'],
            }
        data[blog_form['email']]=new_user
        with open("user_details.json","w") as fp:
            json.dump(data,fp,indent=4)
        return redirect(url_for('reply',message="You have been registered."))
    return render_template("register.html",i=random.choice([1,2,3,4,5,6]),hero_img=random.choice(img_names),home="",read="",write="",know="",contact="")



if __name__=="__main__":
    app.run(debug=True)