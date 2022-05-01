from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

posts = [
        {
            "source": {
                "id": "cnn",
                "name": "CNN"
            },
            "author": "Nectar Gan and CNN's Beijing Bureau",
            "title": "Beijing shuts Universal Studios, bans restaurant dining in major escalation of Covid restrictions - CNN",
            "description": "Beijing has banned all restaurant dining, shut down Universal Studios and ordered residents to provide proof of a negative Covid test to enter public venues in a major escalation of restrictions as a five-day holiday gets underway.",
            "url": "https://www.cnn.com/2022/05/01/china/beijing-covid-labor-day-holiday-intl-hnk/index.html",
            "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/220430214012-beijing-covid-050122-restricted-super-tease.jpg",
            "publishedAt": "2022-05-01T05:24:00Z",
            "content": None
        },
        {
            "source": {
                "id": None,
                "name": "WAPT Jackson"
            },
            "author": "Gracyn Gordon",
            "title": "One dead, multiple shot at Mudbugs Festival at state fairgrounds - WAPT Jackson",
            "description": "One dead, multiple injured, according to police",
            "url": "https://www.wapt.com/article/one-dead-multiple-shot-at-mudbugs-festival-at-state-fairgrounds/39869754",
            "urlToImage": "https://kubrick.htvapps.com/htv-prod/ibmig/cms/image/wapt/13381576-generic-red-blue-police-lights-nighttime-jpg.jpg?crop=1.00xw:0.752xh;0,0&resize=1200:*",
            "publishedAt": "2022-05-01T04:47:00Z",
            "content": "JACKSON, Miss. —Hinds County Sheriff Tyree Jones says multiple people were shot at the state fairgrounds Saturday night during the Mudbugs Festival.\r\nOne person is dead and several injured. Police be… [+313 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "ESPN"
            },
            "author": "Mel Kiper Jr.",
            "title": "NFL draft grades - Mel Kiper Jr. picks steals, sleepers and favorite 2022 classes from all 32 teams - ESPN",
            "description": "The Texans got a few foundational prospects. The Lions got an in-state star. And the Titans might have gotten the steal of the draft.",
            "url": "https://www.espn.com/nfl/insider/draft2022/insider/story/_/id/33827196/nfl-draft-grades-mel-kiper-jr-picks-steals-sleepers-favorite-2022-classes-all-32-teams",
            "urlToImage": "https://a.espncdn.com/combiner/i?img=%2Fphoto%2F2022%2F0429%2Fnfl_mel%2Dkipers%2Ddraft%2Dgrades_16x9.jpg",
            "publishedAt": "2022-05-01T04:34:07Z",
            "content": "This was my 39th year doing the NFL draft for ESPN, and I can't remember a trading frenzy quite like the one we saw in the middle of Round 1 on Thursday. There were picks and players flying off the b… [+73408 chars]"
        },
        {
            "source": {
                "id": "politico",
                "name": "Politico"
            },
            "author": None,
            "title": "Trevor Noah's top White House Correspondents Dinner moments - POLITICO - POLITICO",
            "description": "The headliner quipped that it was his “great honor” to speak at the “nation’s most distinguished super-spreader event.”",
            "url": "https://www.politico.com/news/2022/05/01/trevor-noah-white-house-correspondents-highlights-best-moments-00029073",
            "urlToImage": "https://static.politico.com/6e/24/de8fe01a4c6a997c06607cc564cd/biden-correspondents-dinner-02722.jpg",
            "publishedAt": "2022-05-01T04:25:02Z",
            "content": "Trevor Noah, host of Comedy Central's \"The Daily Show,\" speaks at the annual White House Correspondents' Association dinner, Saturday, April 30, 2022, in Washington. | Patrick Semansky/AP Photo\r\nDail… [+510 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "New York Times"
            },
            "author": "Anupreeta Das, Lauren Hirsch",
            "title": "Can Elon Musk Make Twitter’s Numbers Work? - The New York Times",
            "description": "Financially speaking, the billionaire’s buyout of the social media network breaks all the usual rules.",
            "url": "https://www.nytimes.com/2022/04/30/business/elon-musk-twitter.html",
            "urlToImage": "https://static01.nyt.com/images/2022/04/29/business/00musk-financial-1/00musk-financial-1-facebookJumbo.jpg",
            "publishedAt": "2022-05-01T04:18:00Z",
            "content": "Still, the interest rates on the loans reflect the risk that they might not get paid back. The banks dont hold on to the loans but sell them to other investors in the market, so if Twitter cant pay i… [+1928 chars]"
        },
        {
            "source": {
                "id": "ign",
                "name": "IGN"
            },
            "author": "Adam Bankhurst",
            "title": "NASA's Ingenuity Helicopter Beams Back Eerie Spacecraft Wreckage From Mars - IGN - IGN",
            "description": "NASA's Ingenuity helicopter has beamed back to Earth eerie yet incredible images of the NASA Perseverance rover wreckage that helped bring it to the Red Planet last year.",
            "url": "https://www.ign.com/articles/nasa-ingenuity-helicopter-beams-back-eerie-spacecraft-wreckage-from-mars-perseverance",
            "urlToImage": "https://assets-prd.ignimgs.com/2022/05/01/maes1-1651375208712.png?width=1280",
            "publishedAt": "2022-05-01T03:30:16Z",
            "content": "NASA's Ingenuity helicopter has beamed back to Earth eerie yet incredible images of the NASA Perseverance rover wreckage that helped bring it to the Red Planet last year.\r\nAs reported by CBS News, In… [+1655 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "MMA Fighting"
            },
            "author": "Jose Youngs",
            "title": "Katie Taylor vs Amanda Serrano in Tweets: Pros react to Katie Taylor’s split decision over Amanda Serrano - MMA Fighting",
            "description": "Twitter had a lot to say following Katie Taylor’s historic victory over Amanda Serrano.",
            "url": "https://www.mmafighting.com/2022/4/30/23050950/katie-taylor-vs-amanda-serrano-in-tweets-pros-react-katie-taylors-split-decision-over-amanda-serrano",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/9McOw0-Frg1rPDsKh0Tj3jIDHkk=/0x0:4904x2568/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23430008/1240362659.jpg",
            "publishedAt": "2022-05-01T03:28:48Z",
            "content": "When Katie Taylor and Amanda Serrano finally entered the squared circle inside Madison Square Garden, the hype surrounding their boxing match was palpable.\r\nWith Taylor, the reigning WBA, WBC, IBF, W… [+1829 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "YouTube"
            },
            "author": None,
            "title": "Marlon Vera Octagon Interview | UFC Vegas 53 - UFC - Ultimate Fighting Championship",
            "description": None,
            "url": "https://www.youtube.com/supported_browsers?next_url=https:%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D__jGW4rCe1I",
            "urlToImage": None,
            "publishedAt": "2022-05-01T02:42:48Z",
            "content": "Your browser isnt supported anymore. Update it to get the best YouTube experience and our latest features. Learn more\r\nRemind me later"
        },
        {
            "source": {
                "id": None,
                "name": "Deadline"
            },
            "author": "Brandon Choe",
            "title": "Country Music Hall Of Fame Ceremony To Proceed Following Naomi Judd’s Death; Wynonna Expected To Attend The Judds’ Induction - Deadline",
            "description": "The Country Music Hall of Fame and Museum will continue with its medallion ceremony on Sunday, May 1st in Nashville following news of the death of country music icon Naomi Judd, who, along with her daughter Wynonna, was set to be inducted as The Judds. Accord…",
            "url": "https://deadline.com/2022/04/country-music-hall-of-fame-ceremony-to-proceed-following-naomi-judds-death-wynonna-expected-attend-the-judds-induction-1235013809/",
            "urlToImage": "https://deadline.com/wp-content/uploads/2022/04/MEGA852812_063-e1651372001868.jpg?w=1024",
            "publishedAt": "2022-05-01T02:30:00Z",
            "content": "The Country Music Hall of Fame and Museum will continue with its medallion ceremony on Sunday, May 1st in Nashville following news of the death of country music icon Naomi Judd, who, along with her d… [+1486 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "New York Post"
            },
            "author": "Kathianne Boniello",
            "title": "15 hurt in Atlanta 'pedal pub' accident - New York Post ",
            "description": "Two people were critically hurt and another 13 injured when a pub on wheels overturned in midtown Atlanta, according to reports.",
            "url": "https://nypost.com/2022/04/30/15-hurt-in-atlanta-pedal-pub-accident/",
            "urlToImage": "https://nypost.com/wp-content/uploads/sites/2/2022/04/pedal-1.jpg?quality=75&strip=all&w=1024",
            "publishedAt": "2022-05-01T02:29:30Z",
            "content": "Two people were critically hurt and another 13 injured when a pub on wheels overturned in midtown Atlanta, according to reports.\r\nThe Saturday evening incident unfolded when the “pedal pub” — a large… [+560 chars]"
        },
        {
            "source": {
                "id": "cnn",
                "name": "CNN"
            },
            "author": "Andy Rose, CNN",
            "title": "3 University of Oklahoma students were killed in a traffic accident while returning from a storm-chasing trip - CNN",
            "description": "Three University of Oklahoma meteorology students were killed late Friday night when their vehicle hydroplaned and was struck by a tractor-trailer, according to the Oklahoma Highway Patrol.",
            "url": "https://www.cnn.com/2022/04/30/us/oklahoma-college-students-die-storm-chasing-trip/index.html",
            "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/220430205333-oklahoma-college-students-die-storm-chasing-trip-map-card-only-super-tease.jpg",
            "publishedAt": "2022-05-01T02:23:00Z",
            "content": "(CNN)Three University of Oklahoma meteorology students were killed late Friday night when their vehicle hydroplaned and was struck by a tractor-trailer, according to the Oklahoma Highway Patrol. \r\nTh… [+2652 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "CBS Sports"
            },
            "author": "",
            "title": "2022 NFL undrafted free agent tracker: Falcons sign Titans coach Mike Vrabel's son, Eagles sign Carson Strong - CBS Sports",
            "description": "Here's a rundown of every undrafted rookie signing",
            "url": "https://www.cbssports.com/nfl/draft/news/2022-nfl-undrafted-free-agent-tracker-falcons-sign-titans-coach-mike-vrabels-son-eagles-sign-carson-strong/",
            "urlToImage": "https://sportshub.cbsistatic.com/i/r/2022/05/01/767bbbd8-a23e-4f70-913f-5e1c032e7088/thumbnail/1200x675/684dc1d2fe69099a99cfa00a43f23de8/tyler-vrabel.png",
            "publishedAt": "2022-05-01T02:15:00Z",
            "content": "The 2022 NFL Draft has ended, with 262 players hearing their names called over the past three days. But for those players who didn't hear their names called, hope is not lost. Shortly after the draft… [+8773 chars]"
        },
        {
            "source": {
                "id": None,
                "name": "WKRC TV Cincinnati"
            },
            "author": "CATHY BUSSEWITZ AP Business Writer",
            "title": "Exxon Mobil doubled its profit from last year to nearly $5.5 billion - WKRC TV Cincinnati",
            "description": "NEW YORK (AP) - Exxon Mobil reported $5. 48 billion in profits during the first quarter as oil and gas prices rose steadily, more than doubling its profits compared with the same quarter last year. But the oil giant took a huge hit as it abandoned its Russian…",
            "url": "https://local12.com/news/nation-world/exxon-mobil-doubled-its-profit-from-last-year-to-nearly-55-billion-oil-and-gas-prices-rose-steadily-russian-operations-gasoline-energy",
            "urlToImage": "https://local12.com/resources/media/8978050a-93ac-4f06-82fb-c7f7da100875-large16x9_AP22119403725612.jpg?1651366415000",
            "publishedAt": "2022-05-01T00:55:16Z",
            "content": None
        },
]

@app.route("/")
def index():
 return render_template('index.html', datas=posts)


if __name__ == "__main__":
 app.run(debug=True)