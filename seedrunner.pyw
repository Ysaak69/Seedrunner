import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import random

# ── BIP39 WORDLIST ────────────────────────────────────────────────────
bip39_words = [
    "abandon","ability","able","about","above","absent","absorb","abstract","absurd","abuse",
    "access","accident","account","accuse","achieve","acid","acoustic","acquire","across","act",
    "action","actor","actress","actual","adapt","add","addict","address","adjust","admit",
    "adult","advance","advice","aerobic","affair","afford","afraid","again","age","agent",
    "agree","ahead","aim","air","airport","aisle","alarm","album","alcohol","alert",
    "alien","all","alley","allow","almost","alone","alpha","already","also","alter",
    "always","amateur","amazing","among","amount","amused","analyst","anchor","ancient","anger",
    "angle","angry","animal","ankle","announce","annual","another","answer","antenna","antique",
    "anxiety","any","apart","apology","appear","apple","approve","april","arch","arctic",
    "area","arena","argue","arm","armed","armor","army","around","arrange","arrest",
    "arrive","arrow","art","artefact","artist","artwork","ask","aspect","assault","asset",
    "assist","assume","asthma","athlete","atom","attack","attend","attitude","attract","auction",
    "audit","august","aunt","author","auto","autumn","average","avocado","avoid","awake",
    "aware","away","awesome","awful","awkward","axis","baby","bachelor","bacon","badge",
    "bag","balance","balcony","ball","bamboo","banana","banner","bar","barely","bargain",
    "barrel","base","basic","basket","battle","beach","bean","beauty","because","become",
    "beef","before","begin","behave","behind","believe","below","belt","bench","benefit",
    "best","betray","better","between","beyond","bicycle","bid","bike","bind","biology",
    "bird","birth","bitter","black","blade","blame","blanket","blast","bleak","bless",
    "blind","blood","blossom","blouse","blue","blur","blush","board","boat","body",
    "boil","bomb","bone","bonus","book","boost","border","boring","borrow","boss",
    "bottom","bounce","box","boy","bracket","brain","brand","brass","brave","bread",
    "breeze","brick","bridge","brief","bright","bring","brisk","broccoli","broken","bronze",
    "broom","brother","brown","brush","bubble","buddy","budget","buffalo","build","bulb",
    "bulk","bullet","bundle","bunker","burden","burger","burst","bus","business","busy",
    "butter","buyer","buzz","cabbage","cabin","cable","cactus","cage","cake","call",
    "calm","camera","camp","can","canal","cancel","candy","cannon","canoe","canvas",
    "canyon","capable","capital","captain","car","carbon","card","cargo","carpet","carry",
    "cart","case","cash","casino","castle","casual","cat","catalog","catch","category",
    "cattle","caught","cause","caution","cave","ceiling","celery","cement","census","century",
    "cereal","certain","chair","chalk","champion","change","chaos","chapter","charge","chase",
    "chat","cheap","check","cheese","chef","cherry","chest","chicken","chief","child",
    "chimney","choice","choose","chronic","chuckle","chunk","churn","cigar","cinnamon","circle",
    "citizen","city","civil","claim","clap","clarify","claw","clay","clean","clerk",
    "clever","click","client","cliff","climb","clinic","clip","clock","clog","close",
    "cloth","cloud","clown","club","clump","cluster","clutch","coach","coast","coconut",
    "code","coffee","coil","coin","collect","color","column","combine","come","comfort",
    "comic","common","company","concert","conduct","confirm","congress","connect","consider","control",
    "convince","cook","cool","copper","copy","coral","core","corn","correct","cost",
    "cotton","couch","country","couple","course","cousin","cover","coyote","crack","cradle",
    "craft","cram","crane","crash","crater","crawl","crazy","cream","credit","creek",
    "crew","cricket","crime","crisp","critic","crop","cross","crouch","crowd","crucial",
    "cruel","cruise","crumble","crunch","crush","cry","crystal","cube","culture","cup",
    "cupboard","curious","current","curtain","curve","cushion","custom","cute","cycle","dad",
    "damage","damp","dance","danger","daring","dash","daughter","dawn","day","deal",
    "debate","debris","decade","december","decide","decline","decorate","decrease","deer","defense",
    "define","defy","degree","delay","deliver","demand","demise","denial","dentist","deny",
    "depart","depend","deposit","depth","deputy","derive","describe","desert","design","desk",
    "despair","destroy","detail","detect","develop","device","devote","diagram","dial","diamond",
    "diary","dice","diesel","diet","differ","digital","dignity","dilemma","dinner","dinosaur",
    "direct","dirt","disagree","discover","disease","dish","dismiss","disorder","display","distance",
    "divert","divide","divorce","dizzy","doctor","document","dog","doll","dolphin","domain",
    "donate","donkey","donor","door","dose","double","dove","draft","dragon","drama",
    "drastic","draw","dream","dress","drift","drill","drink","drip","drive","drop",
    "drum","dry","duck","dumb","dune","during","dust","dutch","duty","dwarf",
    "dynamic","eager","eagle","early","earn","earth","easily","east","easy","echo",
    "ecology","economy","edge","edit","educate","effort","egg","eight","either","elbow",
    "elder","electric","elegant","element","elephant","elevator","elite","else","embark","embody",
    "embrace","emerge","emotion","employ","empower","empty","enable","enact","end","endless",
    "endorse","enemy","energy","enforce","engage","engine","enhance","enjoy","enlist","enough",
    "enrich","enroll","ensure","enter","entire","entry","envelope","episode","equal","equip",
    "era","erase","erode","erosion","error","erupt","escape","essay","essence","estate",
    "eternal","ethics","evidence","evil","evoke","evolve","exact","example","excess","exchange",
    "excite","exclude","excuse","execute","exercise","exhaust","exhibit","exile","exist","exit",
    "exotic","expand","expect","expire","explain","expose","express","extend","extra","eye",
    "eyebrow","fabric","face","faculty","fade","faint","faith","fall","false","fame",
    "family","famous","fan","fancy","fantasy","farm","fashion","fat","fatal","father",
    "fatigue","fault","favorite","feature","february","federal","fee","feed","feel","female",
    "fence","festival","fetch","fever","few","fiber","fiction","field","figure","file",
    "film","filter","final","find","fine","finger","finish","fire","firm","first",
    "fiscal","fish","fit","fitness","fix","flag","flame","flash","flat","flavor",
    "flee","flight","flip","float","flock","floor","flower","fluid","flush","fly",
    "foam","focus","fog","foil","fold","follow","food","foot","force","forest",
    "forget","fork","fortune","forum","forward","fossil","foster","found","fox","fragile",
    "frame","frequent","fresh","friend","fringe","frog","front","frost","frown","frozen",
    "fruit","fuel","fun","funny","furnace","fury","future","gadget","gain","galaxy",
    "gallery","game","gap","garage","garbage","garden","garlic","garment","gas","gasp",
    "gate","gather","gauge","gaze","general","genius","genre","gentle","genuine","gesture",
    "ghost","giant","gift","giggle","ginger","giraffe","girl","give","glad","glance",
    "glare","glass","glide","glimpse","globe","gloom","glory","glove","glow","glue",
    "goat","goddess","gold","good","goose","gorilla","gospel","gossip","govern","gown",
    "grab","grace","grain","grant","grape","grass","gravity","great","green","grid",
    "grief","grit","grocery","group","grow","grunt","guard","guess","guide","guilt",
    "guitar","gun","gym","habit","hair","half","hammer","hamster","hand","happy",
    "harbor","hard","harsh","harvest","hat","have","hawk","hazard","head","health",
    "heart","heavy","hedgehog","height","hello","helmet","help","hen","hero","hidden",
    "high","hill","hint","hip","hire","history","hobby","hockey","hold","hole",
    "holiday","hollow","home","honey","hood","hope","horn","horror","horse","hospital",
    "host","hotel","hour","hover","hub","huge","human","humble","humor","hundred",
    "hungry","hunt","hurdle","hurry","hurt","husband","hybrid","ice","icon","idea",
    "identify","idle","ignore","ill","illegal","illness","image","imitate","immense","immune",
    "impact","impose","improve","impulse","inch","include","income","increase","index","indicate",
    "indoor","industry","infant","inflict","inform","inhale","inherit","initial","inject","injury",
    "inmate","inner","innocent","input","inquiry","insane","insect","inside","inspire","install",
    "intact","interest","into","invest","invite","involve","iron","island","isolate","issue",
    "item","ivory","jacket","jaguar","jar","jazz","jealous","jeans","jelly","jewel",
    "job","join","joke","journey","joy","judge","juice","jump","jungle","junior",
    "junk","just","kangaroo","keen","keep","ketchup","key","kick","kid","kidney",
    "kind","kingdom","kiss","kit","kitchen","kite","kitten","kiwi","knee","knife",
    "knock","know","lab","label","labor","ladder","lady","lake","lamp","language",
    "laptop","large","later","latin","laugh","laundry","lava","law","lawn","lawsuit",
    "layer","lazy","leader","leaf","learn","leave","lecture","left","leg","legal",
    "legend","leisure","lemon","lend","length","lens","leopard","lesson","letter","level",
    "liar","liberty","library","license","life","lift","light","like","limb","limit",
    "link","lion","liquid","list","little","live","lizard","load","loan","lobster",
    "local","lock","logic","lonely","long","loop","lottery","loud","lounge","love",
    "loyal","lucky","luggage","lumber","lunar","lunch","luxury","lyrics","machine","mad",
    "magic","magnet","maid","mail","main","major","make","mammal","man","manage",
    "mandate","mango","mansion","manual","maple","marble","march","margin","marine","market",
    "marriage","mask","mass","master","match","material","math","matrix","matter","maximum",
    "maze","meadow","mean","measure","meat","mechanic","medal","media","melody","melt",
    "member","memory","mention","menu","mercy","merge","merit","merry","mesh","message",
    "metal","method","middle","midnight","milk","million","mimic","mind","minimum","minor",
    "minute","miracle","mirror","misery","miss","mistake","mix","mixed","mixture","mobile",
    "model","modify","mom","moment","monitor","monkey","monster","month","moon","moral",
    "more","morning","mosquito","mother","motion","motor","mountain","mouse","move","movie",
    "much","muffin","mule","multiply","muscle","museum","mushroom","music","must","mutual",
    "myself","mystery","myth","naive","name","napkin","narrow","nasty","nation","nature",
    "near","neck","need","negative","neglect","neither","nephew","nerve","nest","net",
    "network","neutral","never","news","next","nice","night","noble","noise","nominee",
    "noodle","normal","north","nose","notable","note","nothing","notice","novel","now",
    "nuclear","number","nurse","nut","oak","obey","object","oblige","obscure","observe",
    "obtain","obvious","occur","ocean","october","odor","off","offer","office","often",
    "oil","okay","old","olive","olympic","omit","once","one","onion","online",
    "only","open","opera","opinion","oppose","option","orange","orbit","orchard","order",
    "ordinary","organ","orient","original","orphan","ostrich","other","outdoor","outer","output",
    "outside","oval","oven","over","own","owner","oxygen","oyster","ozone","pact",
    "paddle","page","pair","palace","palm","panda","panel","panic","panther","paper",
    "parade","parent","park","parrot","party","pass","patch","path","patient","patrol",
    "pattern","pause","pave","payment","peace","peanut","pear","peasant","pelican","pen",
    "penalty","pencil","people","pepper","perfect","permit","person","pet","phone","photo",
    "phrase","physical","piano","picnic","picture","piece","pig","pigeon","pill","pilot",
    "pink","pioneer","pipe","pistol","pitch","pizza","place","planet","plastic","plate",
    "play","please","pledge","pluck","plug","plunge","poem","poet","point","polar",
    "pole","police","pond","pony","pool","popular","portion","position","possible","post",
    "potato","pottery","poverty","powder","power","practice","praise","predict","prefer","prepare",
    "present","pretty","prevent","price","pride","primary","print","priority","prison","private",
    "prize","problem","process","produce","profit","program","project","promote","proof","property",
    "prosper","protect","proud","provide","public","pudding","pull","pulp","pulse","pumpkin",
    "punch","pupil","puppy","purchase","purity","purpose","purse","push","put","puzzle",
    "pyramid","quality","quantum","quarter","question","quick","quit","quiz","quote","rabbit",
    "raccoon","race","rack","radar","radio","rail","rain","raise","rally","ramp",
    "ranch","random","range","rapid","rare","rate","rather","raven","raw","razor",
    "ready","real","reason","rebel","rebuild","recall","receive","recipe","record","recycle",
    "reduce","reflect","reform","refuse","region","regret","regular","reject","relax","release",
    "relief","rely","remain","remember","remind","remove","render","renew","rent","reopen",
    "repair","repeat","replace","report","require","rescue","resemble","resist","resource","response",
    "result","retire","retreat","return","reunion","reveal","review","reward","rhythm","rib",
    "ribbon","rice","rich","ride","ridge","rifle","right","rigid","ring","riot",
    "ripple","risk","ritual","rival","river","road","roast","robot","robust","rocket",
    "romance","roof","rookie","room","rose","rotate","rough","round","route","royal",
    "rubber","rude","rug","rule","run","runway","rural","sad","saddle","sadness",
    "safe","sail","salad","salmon","salon","salt","salute","same","sample","sand",
    "satisfy","satoshi","sauce","sausage","save","say","scale","scan","scare","scatter",
    "scene","scheme","school","science","scissors","scorpion","scout","scrap","screen","script",
    "scrub","sea","search","season","seat","second","secret","section","security","seed",
    "seek","segment","select","sell","seminar","senior","sense","sentence","series","service",
    "session","settle","setup","seven","shadow","shaft","shallow","share","shed","shell",
    "sheriff","shield","shift","shine","ship","shiver","shock","shoe","shoot","shop",
    "short","shoulder","shove","shrimp","shrug","shuffle","shy","sibling","sick","side",
    "siege","sight","sign","silent","silk","silly","silver","similar","simple","since",
    "sing","siren","sister","situate","six","size","skate","sketch","ski","skill",
    "skin","skirt","skull","slab","slam","sleep","slender","slice","slide","slight",
    "slim","slogan","slot","slow","slush","small","smart","smile","smoke","smooth",
    "snack","snake","snap","sniff","snow","soap","soccer","social","sock","soda",
    "soft","solar","soldier","solid","solution","solve","someone","song","soon","sorry",
    "sort","soul","sound","soup","source","south","space","spare","spatial","spawn",
    "speak","special","speed","spell","spend","sphere","spice","spider","spike","spin",
    "spirit","split","spoil","sponsor","spoon","sport","spot","spray","spread","spring",
    "spy","square","squeeze","squirrel","stable","stadium","staff","stage","stairs","stamp",
    "stand","start","state","stay","steak","steel","stem","step","stereo","stick",
    "still","sting","stock","stomach","stone","stool","story","stove","strategy","street",
    "strike","strong","struggle","student","stuff","stumble","style","subject","submit","subway",
    "success","such","sudden","suffer","sugar","suggest","suit","summer","sun","sunny",
    "sunset","super","supply","supreme","sure","surface","surge","surprise","surround","survey",
    "suspect","sustain","swallow","swamp","swap","swarm","swear","sweet","swift","swim",
    "swing","switch","sword","symbol","symptom","syrup","system","table","tackle","tag",
    "tail","talent","talk","tank","tape","target","task","taste","tattoo","taxi",
    "teach","team","tell","ten","tenant","tennis","tent","term","test","text",
    "thank","that","theme","then","theory","there","they","thing","this","thought",
    "three","thrive","throw","thumb","thunder","ticket","tide","tiger","tilt","timber",
    "time","tiny","tip","tired","tissue","title","toast","tobacco","today","toddler",
    "toe","together","toilet","token","tomato","tomorrow","tone","tongue","tonight","tool",
    "tooth","top","topic","topple","torch","tornado","tortoise","toss","total","tourist",
    "toward","tower","town","toy","track","trade","traffic","tragic","train","transfer",
    "trap","trash","travel","tray","treat","tree","trend","trial","tribe","trick",
    "trigger","trim","trip","trophy","trouble","truck","true","truly","trumpet","trust",
    "truth","try","tube","tuition","tumble","tuna","tunnel","turkey","turn","turtle",
    "twelve","twenty","twice","twin","twist","two","type","typical","ugly","umbrella",
    "unable","unaware","uncle","uncover","under","undo","unfair","unfold","unhappy","uniform",
    "unique","unit","universe","unknown","unlock","until","unusual","unveil","update","upgrade",
    "uphold","upon","upper","upset","urban","urge","usage","use","used","useful",
    "useless","usual","utility","vacant","vacuum","vague","valid","valley","valve","van",
    "vanish","vapor","various","vast","vault","vehicle","velvet","vendor","venture","venue",
    "verb","verify","version","very","vessel","veteran","viable","vibrant","vicious","victory",
    "video","view","village","vintage","violin","virtual","virus","visa","visit","visual",
    "vital","vivid","vocal","voice","void","volcano","volume","vote","voyage","wage",
    "wagon","wait","walk","wall","walnut","want","warfare","warm","warrior","wash",
    "wasp","waste","water","wave","way","wealth","weapon","wear","weasel","weather",
    "web","wedding","weekend","weird","welcome","west","wet","whale","what","wheat",
    "wheel","when","where","whip","whisper","wide","width","wife","wild","will",
    "win","window","wine","wing","wink","winner","winter","wire","wisdom","wise",
    "wish","witness","wolf","woman","wonder","wood","wool","word","work","world",
    "worry","worth","wrap","wreck","wrestle","wrist","write","wrong","yard","year",
    "yellow","you","young","youth","zebra","zero","zone","zoo",
]

# ── COLORS ────────────────────────────────────────────────────────────
BG       = "#0d0d0d"
BG2      = "#161616"
BG3      = "#1e1e1e"
CARD     = "#1a1a1a"
BORDER   = "#2a2a2a"
ORANGE   = "#ff4500"
ORANGE2  = "#ff6534"
ORANGE_DIM = "#7a2000"
TEXT     = "#e8e6e3"
TEXT_DIM = "#818384"
TEXT_MED = "#b0adaa"
GREEN    = "#46d160"
WHITE    = "#ffffff"

FONT_TITLE  = ("Segoe UI", 22, "bold")
FONT_HEAD   = ("Segoe UI", 13, "bold")
FONT_BODY   = ("Segoe UI", 10)
FONT_SMALL  = ("Segoe UI", 9)
FONT_MONO   = ("Consolas", 10, "bold")
FONT_MONO_S = ("Consolas", 9)

# ── HELPERS ───────────────────────────────────────────────────────────
def assign_numbers(seed, words):
    h = hashlib.sha256(seed.encode("utf-8")).digest()
    rng = random.Random(int.from_bytes(h, "big"))
    nums = list(range(1, len(words) + 1))
    rng.shuffle(nums)
    return list(zip(words, nums))

def make_separator(parent, color=BORDER):
    f = tk.Frame(parent, bg=color, height=1)
    f.pack(fill="x", padx=20, pady=6)
    return f

# ── ONBOARDING ────────────────────────────────────────────────────────
class OnboardingWindow(tk.Toplevel):

    def __init__(self, master, on_done):
        super().__init__(master)
        self.on_done = on_done
        self.step    = 0
        self.title("SeedRunner")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.geometry("600x460")
        self._center()
        self.grab_set()
        self._build()

    def _center(self):
        self.update_idletasks()
        sw = self.winfo_screenwidth(); sh = self.winfo_screenheight()
        self.geometry(f"600x460+{(sw-600)//2}+{(sh-460)//2}")


    def _build(self):
        for w in self.winfo_children(): w.destroy()
        if self.step == 0: self._page_text()
        else:              self._page_visual()

    # ── PAGE 1: plain language ─────────────────────────────────────────
    def _page_text(self):
        # top bar
        top = tk.Frame(self, bg=BG2, height=52)
        top.pack(fill="x"); top.pack_propagate(False)
        tk.Label(top, text="SeedRunner", bg=BG2, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(side="left", padx=20, pady=14)
        tk.Label(top, text="1 / 2", bg=BG2, fg=TEXT_DIM,
                 font=FONT_SMALL).pack(side="right", padx=20)

        # progress
        pf = tk.Frame(self, bg=BG); pf.pack(pady=(12,0))
        tk.Frame(pf, bg=ORANGE,  width=32, height=4).pack(side="left", padx=3)
        tk.Frame(pf, bg=BORDER,  width=8,  height=4).pack(side="left", padx=3)

        # content
        body = tk.Frame(self, bg=BG)
        body.pack(expand=True, fill="both", padx=32, pady=(18, 8))

        # headline
        tk.Label(body,
                 text="Your crypto wallet has a seed phrase.\nSeedRunner hides it — without storing anything.",
                 bg=BG, fg=TEXT, font=("Segoe UI", 12, "bold"),
                 wraplength=520, justify="left").pack(anchor="w", pady=(0, 16))

        # three bullet blocks
        bullets = [
            ("1", "You pick a password — any phrase you'll remember."),
            ("2", "SeedRunner uses that password to give every word in the BIP-39 list "
                  "a unique number. Same password = same numbers, always."),
            ("3", "Write the number for each word of your seed on paper.\n"
                  "Anyone who finds it just sees a list of numbers — useless without your password."),
        ]
        for num, text in bullets:
            row = tk.Frame(body, bg=BG)
            row.pack(fill="x", pady=5)

            badge = tk.Frame(row, bg=ORANGE, width=24, height=24)
            badge.pack(side="left", padx=(0,12))
            badge.pack_propagate(False)
            tk.Label(badge, text=num, bg=ORANGE, fg=WHITE,
                     font=("Segoe UI", 9, "bold")).pack(expand=True)

            tk.Label(row, text=text, bg=BG, fg=TEXT_MED, font=FONT_BODY,
                     wraplength=460, justify="left", anchor="nw").pack(side="left", fill="x", expand=True)

        # divider + note
        tk.Frame(body, bg=BORDER, height=1).pack(fill="x", pady=(14, 10))
        tk.Label(body,
                 text="To recover your seed: re-enter the same password → same numbers appear → look up your words.",
                 bg=BG, fg=TEXT_DIM, font=("Segoe UI", 9),
                 wraplength=520, justify="left").pack(anchor="w")

        # button
        btn_row = tk.Frame(self, bg=BG)
        btn_row.pack(fill="x", padx=24, pady=(0,18))
        tk.Button(btn_row, text="See how it works  →", bg=ORANGE, fg=WHITE,
                  font=("Segoe UI", 10, "bold"), relief="flat", bd=0,
                  padx=18, pady=10, activebackground=ORANGE2, activeforeground=WHITE,
                  command=self._next).pack(side="right")

    # ── PAGE 2: visual flow ────────────────────────────────────────────
    def _page_visual(self):
        # top bar
        top = tk.Frame(self, bg=BG2, height=52)
        top.pack(fill="x"); top.pack_propagate(False)
        tk.Label(top, text="How it works", bg=BG2, fg=TEXT,
                 font=("Segoe UI", 13, "bold")).pack(side="left", padx=20, pady=14)
        tk.Label(top, text="2 / 2", bg=BG2, fg=TEXT_DIM,
                 font=FONT_SMALL).pack(side="right", padx=20)

        # progress
        pf = tk.Frame(self, bg=BG); pf.pack(pady=(12,0))
        tk.Frame(pf, bg=BORDER, width=8,  height=4).pack(side="left", padx=3)
        tk.Frame(pf, bg=ORANGE, width=32, height=4).pack(side="left", padx=3)

        # visual flow canvas
        canvas = tk.Canvas(self, bg=BG, highlightthickness=0, height=300)
        canvas.pack(fill="x", padx=24, pady=(14,0))

        # We draw after idle so geometry is ready
        self.after(50, lambda: self._draw_flow(canvas))

        # buttons
        btn_row = tk.Frame(self, bg=BG)
        btn_row.pack(fill="x", padx=24, pady=(8,18))
        tk.Button(btn_row, text="← Back", bg=BG3, fg=TEXT_DIM,
                  font=FONT_SMALL, relief="flat", bd=0, padx=14, pady=8,
                  activebackground=BORDER, activeforeground=TEXT,
                  command=self._prev).pack(side="left")
        tk.Button(btn_row, text="Get Started  →", bg=ORANGE, fg=WHITE,
                  font=("Segoe UI", 10, "bold"), relief="flat", bd=0,
                  padx=18, pady=10, activebackground=ORANGE2, activeforeground=WHITE,
                  command=self._next).pack(side="right")

    def _draw_flow(self, canvas):
        canvas.update_idletasks()
        W = canvas.winfo_width()
        if W < 10: W = 552

        # helpers
        def box(cx, cy, w, h, col, label, sublabel=""):
            x1,y1,x2,y2 = cx-w//2, cy-h//2, cx+w//2, cy+h//2
            canvas.create_rectangle(x1,y1,x2,y2, fill=col, outline="", width=0)
            canvas.create_text(cx, cy-(10 if sublabel else 0),
                               text=label, fill=TEXT, font=("Segoe UI",9,"bold"), anchor="center")
            if sublabel:
                canvas.create_text(cx, cy+12, text=sublabel,
                                   fill=TEXT_DIM, font=("Segoe UI",8), anchor="center")

        def arrow(x1,y1,x2,y2):
            canvas.create_line(x1,y1,x2,y2, fill=BORDER, width=2, arrow="last",
                               arrowshape=(8,10,4))

        def label(cx,cy,txt,col=TEXT_DIM):
            canvas.create_text(cx,cy,text=txt,fill=col,
                               font=("Segoe UI",8),anchor="center")

        # ── SETUP flow (top half) ──────────────────────────────────────
        y1 = 50
        # nodes
        xs = [W*0.12, W*0.32, W*0.52, W*0.72, W*0.92]

        box(xs[0], y1, 90, 36, BG3,    "Your seed",      "e.g. apple moon...")
        arrow(xs[0]+46, y1, xs[1]-46, y1)
        box(xs[1], y1, 90, 36, BG3,    "Your password",  "e.g. myDog42!")
        arrow(xs[1]+46, y1, xs[2]-30, y1)
        box(xs[2], y1, 60, 36, "#2a1400", "SHA-256",     "hash")
        arrow(xs[2]+31, y1, xs[3]-46, y1)
        box(xs[3], y1, 90, 36, BG3,    "Word → Number",  "apple = 1847")
        arrow(xs[3]+46, y1, xs[4]-40, y1)
        box(xs[4], y1, 78, 36, "#0d200d", "Write on",    "paper")

        # section label
        canvas.create_text(W*0.5, y1-34, text="SETUP  —  do this once",
                           fill=TEXT_DIM, font=("Segoe UI",8,"bold"), anchor="center")
        canvas.create_line(W*0.05, y1-24, W*0.95, y1-24, fill=BORDER, width=1, dash=(4,4))

        # ── divider ───────────────────────────────────────────────────
        ymid = 120
        canvas.create_line(W*0.05, ymid, W*0.95, ymid, fill=BORDER, width=1, dash=(4,4))
        canvas.create_text(W*0.5, ymid+14, text="RECOVERY  —  whenever you need your seed back",
                           fill=TEXT_DIM, font=("Segoe UI",8,"bold"), anchor="center")

        # ── RECOVERY flow (bottom half) ───────────────────────────────
        y2 = 185
        box(xs[4], y2, 78, 36, "#0d200d", "Your numbers", "from paper")
        arrow(xs[4]-40, y2, xs[3]+46, y2)
        box(xs[3], y2, 90, 36, BG3,    "Your password",  "same as before")
        arrow(xs[3]-46, y2, xs[2]+31, y2)
        box(xs[2], y2, 60, 36, "#2a1400", "SHA-256",     "same hash")
        arrow(xs[2]-31, y2, xs[1]+46, y2)
        box(xs[1], y2, 90, 36, BG3,    "Number → Word",  "1847 = apple")
        arrow(xs[1]-46, y2, xs[0]+46, y2)
        box(xs[0], y2, 90, 36, BG3,    "Seed restored",  "apple moon...")

        # ── key insight box ───────────────────────────────────────────
        yi = 255
        canvas.create_rectangle(W*0.1, yi, W*0.9, yi+36,
                                 fill="#1a0900", outline=ORANGE_DIM, width=1)
        canvas.create_text(W*0.5, yi+18,
                           text="Without your password the numbers are random noise.  No password = no seed.",
                           fill=ORANGE2, font=("Segoe UI",9), anchor="center")

    def _next(self):
        if self.step == 0:
            self.step = 1; self._build()
        else:
            self.destroy(); self.on_done()

    def _prev(self):
        if self.step == 1:
            self.step = 0; self._build()

# ── RAM VIEW ──────────────────────────────────────────────────────────
class RamViewWindow(tk.Toplevel):
    PAGE_DURATION = 15

    def __init__(self, master, pairs, sort_mode, pages_count):
        super().__init__(master)
        self.title("SeedRunner — RAM View")
        self.configure(bg=BG)
        self.state("zoomed")
        self.config(cursor="none")

        if sort_mode == "alpha":
            pairs = sorted(pairs, key=lambda x: x[0])
        else:
            pairs = sorted(pairs, key=lambda x: x[1])

        # split into pages
        n = len(pairs)
        size = n // pages_count
        self.pages = []
        start = 0
        for i in range(pages_count):
            end = start + size if i < pages_count - 1 else n
            self.pages.append(pairs[start:end])
            start = end

        self.current = 0
        self.timer   = self.PAGE_DURATION

        self._build_chrome()
        self.after(100, self._display_page)
        self._tick()
        self.protocol("WM_DELETE_WINDOW", self._close)

    def _build_chrome(self):
        # top bar
        self.top_bar = tk.Frame(self, bg=BG2, height=48)
        self.top_bar.pack(fill="x")
        self.top_bar.pack_propagate(False)

        tk.Label(self.top_bar, text="🔒  SeedRunner RAM View",
                 bg=BG2, fg=TEXT, font=FONT_HEAD).pack(side="left", padx=20, pady=12)

        tk.Button(self.top_bar, text="Quit", bg="#2a0000", fg="#f88",
                  font=FONT_SMALL, relief="flat", bd=0, padx=12, pady=6,
                  activebackground="#400", activeforeground=WHITE,
                  cursor="hand2", command=self.master.quit).pack(side="right", padx=8, pady=8)

        tk.Button(self.top_bar, text="← Back", bg=BG3, fg=TEXT_DIM,
                  font=FONT_SMALL, relief="flat", bd=0, padx=12, pady=6,
                  activebackground=BORDER, activeforeground=TEXT,
                  cursor="hand2", command=self._close).pack(side="right", padx=(0,4), pady=8)

        self.timer_label = tk.Label(self.top_bar, text="", bg=BG2,
                                    fg=ORANGE, font=("Consolas", 11, "bold"))
        self.timer_label.pack(side="right", padx=16)

        self.page_label = tk.Label(self.top_bar, text="", bg=BG2,
                                   fg=TEXT_DIM, font=FONT_SMALL)
        self.page_label.pack(side="right", padx=4)

        # warning strip
        warn = tk.Frame(self, bg="#1a0a00", height=28)
        warn.pack(fill="x")
        warn.pack_propagate(False)
        tk.Label(warn, text="Write your numbers on paper only — no screenshots, no photos, no cloud",
                 bg="#1a0a00", fg=ORANGE_DIM, font=("Segoe UI", 9)).pack(pady=5)

        # content area
        self.content = tk.Frame(self, bg=BG)
        self.content.pack(expand=True, fill="both", padx=12, pady=8)

    def _display_page(self):
        for w in self.content.winfo_children(): w.destroy()
        pairs = self.pages[self.current]

        count = len(pairs)

        # draw on a canvas so we control exact pixel placement
        self.content.update_idletasks()
        self.update_idletasks()
        W = self.content.winfo_width()
        H = self.content.winfo_height()
        if W < 100:
            W = self.winfo_screenwidth()
        if H < 100:
            H = self.winfo_screenheight() - 120

        # find font size where all rows fit
        for fs in range(11, 5, -1):
            row_h = fs + 5
            cols = max(1, W // (fs * 10 + 30))
            rows = (count + cols - 1) // cols
            if rows * row_h <= H:
                break

        font_num  = ("Consolas", fs, "bold")
        font_word = ("Consolas", fs)
        row_h = fs + 5
        rows  = (count + cols - 1) // cols
        col_w = W // cols

        canvas = tk.Canvas(self.content, bg=BG, highlightthickness=0,
                           width=W, height=H)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)

        for idx, (word, num) in enumerate(pairs):
            c = idx // rows
            r = idx  % rows
            x = c * col_w + 4
            y = r * row_h + 4
            canvas.create_text(x + col_w//3, y, text=f"{num:4}",
                               fill=ORANGE, font=font_num, anchor="nw")
            canvas.create_text(x + col_w//3 + fs*4, y, text=" "+word,
                               fill=TEXT,   font=font_word, anchor="nw")

        self.page_label.config(
            text=f"Page {self.current+1} of {len(self.pages)}")

    def _tick(self):
        self.timer -= 1
        if self.timer <= 0:
            self.timer   = self.PAGE_DURATION
            self.current = (self.current + 1) % len(self.pages)
            self._display_page()
        secs = self.timer
        bar  = "█" * secs + "░" * (self.PAGE_DURATION - secs)
        self.timer_label.config(text=f"{bar}  {secs}s")
        self._tick_id = self.after(1000, self._tick)

    def _close(self):
        if hasattr(self, "_tick_id"): self.after_cancel(self._tick_id)
        try:
            self.unbind_all("<MouseWheel>")
        except Exception:
            pass
        for w in self.content.winfo_children(): w.destroy()
        self.master.deiconify()
        self.master.lift()
        self.destroy()

# ── MAIN WINDOW ───────────────────────────────────────────────────────
class SeedRunnerApp:
    def __init__(self, root):
        self.root = root
        root.title("SeedRunner")
        root.configure(bg=BG)
        root.geometry("680x620")
        root.minsize(600, 580)
        self._center()
        self._build()

    def _center(self):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - 680) // 2; y = (sh - 540) // 2
        self.root.geometry(f"680x620+{x}+{y}")

    def _show_donate(self):
        win = tk.Toplevel(self.root)
        win.title("Support SeedRunner")
        win.configure(bg=BG)
        win.resizable(False, False)
        win.grab_set()

        win.update_idletasks()
        sw = win.winfo_screenwidth(); sh = win.winfo_screenheight()
        win.geometry(f"480x520+{(sw-480)//2}+{(sh-520)//2}")

        # header
        top = tk.Frame(win, bg=BG2, height=52)
        top.pack(fill="x"); top.pack_propagate(False)
        tk.Label(top, text="⚡  Support SeedRunner", bg=BG2, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(side="left", padx=20, pady=14)
        tk.Button(top, text="✕", bg=BG2, fg=TEXT_DIM, relief="flat", bd=0,
                  font=("Segoe UI", 11), activebackground=BG2,
                  cursor="hand2", command=win.destroy).pack(side="right", padx=16)

        tk.Label(win, text="SeedRunner is free forever.\nIf it helped you, a sat or two is always appreciated 🙏",
                 bg=BG, fg=TEXT_MED, font=("Segoe UI", 10),
                 justify="center").pack(pady=(20, 16))

        # QR codes side by side
        qr_frame = tk.Frame(win, bg=BG)
        qr_frame.pack(expand=True)

        import base64, os
        script_dir = os.path.dirname(os.path.abspath(__file__))

        import base64 as _b64, io, tempfile, os
        QR_GIF = {
            "lightning": "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",
            "onchain":   "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",
        }
        for key, label, color in [
            ("lightning", "⚡ Lightning", ORANGE),
            ("onchain",   "₿ On-chain (Bitcoin)", "#f7931a"),
        ]:
            col = tk.Frame(qr_frame, bg=BG)
            col.pack(side="left", padx=20)
            tk.Label(col, text=label, bg=BG, fg=color,
                     font=("Segoe UI", 10, "bold")).pack(pady=(0, 8))
            tmp = tempfile.NamedTemporaryFile(suffix=".gif", delete=False)
            tmp.write(_b64.b64decode(QR_GIF[key]))
            tmp.close()
            photo = tk.PhotoImage(file=tmp.name)
            os.unlink(tmp.name)
            lbl = tk.Label(col, image=photo, bg=BG)
            lbl.image = photo
            lbl.pack()
            wallet_hint = "Scan with any\nLightning wallet" if key == "lightning" else "Scan with any\nBitcoin wallet"
            tk.Label(col, text=wallet_hint, bg=BG, fg=TEXT_DIM,
                     font=("Segoe UI", 9), justify="center").pack(pady=(8, 0))

        tk.Button(win, text="Close", bg=BG3, fg=TEXT_DIM,
                  font=FONT_SMALL, relief="flat", bd=0, padx=20, pady=8,
                  activebackground=BORDER, cursor="hand2",
                  command=win.destroy).pack(pady=20)

    def _build(self):
        # ── HEADER
        header = tk.Frame(self.root, bg=BG2, height=64)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_frame = tk.Frame(header, bg=BG2)
        logo_frame.pack(side="left", padx=24, pady=12)
        tk.Label(logo_frame, text="●", bg=BG2, fg=ORANGE,
                 font=("Segoe UI", 18, "bold")).pack(side="left", padx=(0,8))
        tk.Label(logo_frame, text="SeedRunner", bg=BG2, fg=TEXT,
                 font=("Segoe UI", 16, "bold")).pack(side="left")
        tk.Label(logo_frame, text=" v1.0", bg=BG2, fg=TEXT_DIM,
                 font=("Segoe UI", 10)).pack(side="left", pady=(6,0))

        tk.Button(header, text="Quit", bg="#2a0000", fg="#f88",
                  font=FONT_SMALL, relief="flat", bd=0, padx=12, pady=6,
                  activebackground="#400", activeforeground=WHITE,
                  cursor="hand2", command=self.root.quit).pack(side="right", padx=16, pady=10)

        tk.Button(header, text="⚡ Donate", bg=BG3, fg=ORANGE,
                  font=FONT_SMALL, relief="flat", bd=0, padx=12, pady=6,
                  activebackground=BORDER, activeforeground=ORANGE2,
                  cursor="hand2", command=self._show_donate).pack(side="right", padx=(0,4), pady=10)

        tk.Label(header, text="BIP-39 Word Shuffler", bg=BG2, fg=TEXT_DIM,
                 font=FONT_SMALL).pack(side="right", padx=8)

        # ── FOOTER (before card so always visible)
        import webbrowser
        footer = tk.Frame(self.root, bg=BG2, height=40)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)
        tk.Button(footer, text="How it works →", bg=BG2, fg=ORANGE,
                  font=("Segoe UI", 9, "bold"), relief="flat", bd=0,
                  activebackground=BG2, activeforeground=ORANGE2,
                  cursor="hand2",
                  command=lambda: webbrowser.open("https://ysaak69.github.io/Seedrunner")).pack(side="right", padx=16, pady=10)

        # ── MAIN CARD
        card = tk.Frame(self.root, bg=CARD, bd=0)
        card.pack(fill="both", expand=True, padx=24, pady=20)

        # inner padding frame
        inner = tk.Frame(card, bg=CARD)
        inner.pack(fill="both", expand=True, padx=28, pady=24)

        # section: password
        tk.Label(inner, text="Your password  (generates the SHA-256 hash)", bg=CARD, fg=TEXT_DIM,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")

        pw_frame = tk.Frame(inner, bg=BG3, highlightbackground=BORDER,
                            highlightthickness=1)
        pw_frame.pack(fill="x", pady=(4, 16))

        self.pw_var   = tk.StringVar()
        self.show_pw  = tk.BooleanVar(value=False)

        self.pw_entry = tk.Entry(
            pw_frame, textvariable=self.pw_var, show="•",
            bg=BG3, fg=TEXT, insertbackground=ORANGE,
            font=("Segoe UI", 12), relief="flat", bd=0,
            highlightthickness=0
        )
        self.pw_entry.pack(side="left", fill="x", expand=True, padx=12, pady=10)

        self.eye_btn = tk.Button(
            pw_frame, text="👁", bg=BG3, fg=TEXT_DIM, relief="flat", bd=0,
            font=("Segoe UI", 11), activebackground=BG3, activeforeground=TEXT,
            command=self._toggle_pw
        )
        self.eye_btn.pack(side="right", padx=8)

        # strength bar
        self.strength_frame = tk.Frame(inner, bg=CARD)
        self.strength_frame.pack(fill="x", pady=(0, 16))
        self.strength_bar   = tk.Frame(self.strength_frame, bg=BORDER, height=3)
        self.strength_bar.pack(fill="x")
        self.strength_fill  = tk.Frame(self.strength_bar, bg=ORANGE, height=3)
        self.strength_fill.place(x=0, y=0, relheight=1, relwidth=0)
        self.strength_lbl   = tk.Label(self.strength_frame, text="", bg=CARD,
                                       fg=TEXT_DIM, font=("Segoe UI", 8))
        self.strength_lbl.pack(anchor="e", pady=(2,0))
        self.pw_var.trace_add("write", self._update_strength)

        tk.Label(inner, text="⚠  Never enter your seed phrase here — this tool only shows the numbered list",
                 bg=CARD, fg="#ff2222", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,4))

        make_separator(inner)

        # section: sort
        tk.Label(inner, text="Sort order", bg=CARD, fg=TEXT_DIM,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(8,6))

        self.sort_var = tk.StringVar(value="alpha")
        sort_row = tk.Frame(inner, bg=CARD)
        sort_row.pack(anchor="w")

        for val, label, desc in [
            ("alpha",  "Alphabetical", "A → Z"),
            ("number", "Numerical",    "1 → 2048"),
        ]:
            self._radio_pill(sort_row, label, desc, self.sort_var, val)

        make_separator(inner)

        # section: pages
        tk.Label(inner, text="Pages", bg=CARD, fg=TEXT_DIM,
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(8,6))

        self.pages_var = tk.IntVar(value=2)
        pages_row = tk.Frame(inner, bg=CARD)
        pages_row.pack(anchor="w")

        for val, lbl in [(2,"2 pages"),(3,"3 pages"),(4,"4 pages")]:
            self._radio_pill(pages_row, lbl, "", self.pages_var, val, wide=False)

        # ── hash preview
        self.hash_lbl = tk.Label(inner, text="", bg=CARD, fg=TEXT_DIM,
                                 font=("Consolas", 8), wraplength=580, anchor="w")
        self.hash_lbl.pack(fill="x", pady=(16, 0))
        self.pw_var.trace_add("write", self._update_hash)

        # ── action button
        btn_frame = tk.Frame(inner, bg=CARD)
        btn_frame.pack(fill="x", pady=(20, 0))

        self.gen_btn = tk.Button(
            btn_frame,
            text="Show shuffled BIP-39 list  →",
            bg=ORANGE, fg=WHITE,
            font=("Segoe UI", 11, "bold"),
            relief="flat", bd=0,
            padx=24, pady=12,
            activebackground=ORANGE2, activeforeground=WHITE,
            command=self._generate,
            cursor="hand2"
        )
        self.gen_btn.pack(fill="x")



    def _radio_pill(self, parent, label, desc, var, val, wide=True):
        def select():
            var.set(val)
            for f, v in getattr(self, f"_pills_{id(var)}", []):
                active = (v == var.get())
                f.configure(bg=ORANGE if active else BG3,
                             highlightbackground=ORANGE if active else BORDER)
                for child in f.winfo_children():
                    child.configure(bg=ORANGE if active else BG3,
                                    fg=WHITE if active else TEXT_MED)

        frame = tk.Frame(parent, bg=BG3,
                         highlightbackground=BORDER, highlightthickness=1,
                         cursor="hand2")
        frame.pack(side="left", padx=(0, 8))

        lbl1 = tk.Label(frame, text=label, bg=BG3, fg=TEXT_MED,
                        font=("Segoe UI", 9, "bold"))
        lbl1.pack(padx=14, pady=(8,2) if desc else (8,8))

        if desc:
            lbl2 = tk.Label(frame, text=desc, bg=BG3, fg=TEXT_DIM,
                            font=("Segoe UI", 8))
            lbl2.pack(padx=14, pady=(0,8))

        attr = f"_pills_{id(var)}"
        if not hasattr(self, attr): setattr(self, attr, [])
        getattr(self, attr).append((frame, val))

        for child in [frame, lbl1] + (frame.winfo_children()):
            child.bind("<Button-1>", lambda e: select())
        frame.bind("<Button-1>", lambda e: select())
        lbl1.bind("<Button-1>", lambda e: select())

        if var.get() == val:
            frame.configure(bg=ORANGE, highlightbackground=ORANGE)
            for child in frame.winfo_children():
                child.configure(bg=ORANGE, fg=WHITE)

    def _toggle_pw(self):
        self.show_pw.set(not self.show_pw.get())
        self.pw_entry.configure(show="" if self.show_pw.get() else "•")

    def _update_strength(self, *_):
        pw = self.pw_var.get()
        score = 0
        if len(pw) >= 8:  score += 1
        if len(pw) >= 14: score += 1
        if any(c.isdigit() for c in pw): score += 1
        if any(not c.isalnum() for c in pw): score += 1
        if any(c.isupper() for c in pw) and any(c.islower() for c in pw): score += 1

        colors = ["#ff4500","#ff6534","#ffa500","#7fcf5a","#46d160"]
        labels = ["Very weak","Weak","Fair","Strong","Very strong"]
        if pw:
            w = (score / 5)
            self.strength_fill.place(relwidth=w)
            self.strength_fill.configure(bg=colors[score-1] if score > 0 else BORDER)
            self.strength_lbl.configure(text=labels[score-1] if score > 0 else "",
                                        fg=colors[score-1] if score > 0 else TEXT_DIM)
        else:
            self.strength_fill.place(relwidth=0)
            self.strength_lbl.configure(text="")

    def _update_hash(self, *_):
        pw = self.pw_var.get()
        if pw:
            h = hashlib.sha256(pw.encode()).hexdigest()
            self.hash_lbl.configure(text=f"SHA-256 → {h[:32]}…")
        else:
            self.hash_lbl.configure(text="")

    def _generate(self):
        pw = self.pw_var.get().strip()
        if not pw:
            messagebox.showerror("Missing password",
                                 "Please enter a password to generate the list.",
                                 parent=self.root)
            return
        pairs = assign_numbers(pw, bip39_words)
        RamViewWindow(self.root, pairs, self.sort_var.get(), self.pages_var.get())

# ── BOOT ─────────────────────────────────────────────────────────────
def boot():
    root = tk.Tk()
    root.withdraw()
    root.update()

    def launch():
        root.deiconify()
        root.lift()
        try:
            SeedRunnerApp(root)
        except Exception as e:
            import traceback
            import tkinter.messagebox as mb
            mb.showerror("Startup Error", traceback.format_exc())

    launch()
    root.mainloop()

if __name__ == "__main__":
    boot()
