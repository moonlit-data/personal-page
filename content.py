"""All the words on the site, English and Chinese. Facts come from his resume base, the old site and what he told us.
{{?text}} = waiting for his confirmation: shown with a small mark in a draft; build.py --final refuses while any remain.
No student information, mentor names, phone, address or portfolio findings, ever.
"""

UI = {
    "en": {"about": "About", "experience": "Experience", "projects": "Projects", "contact": "Contact", "other": "中文",
           "contact_h": "Contact", "contact_body": "Contact details coming soon.", "tbc": "to confirm",
           "title_home": "团团", "title_about": "About", "title_experience": "Experience", "title_projects": "Projects"},
    "zh": {"about": "关于", "experience": "经历", "projects": "作品", "contact": "联系", "other": "EN",
           "contact_h": "联系", "contact_body": "联系方式稍后放上。", "tbc": "待确认",
           "title_home": "团团", "title_about": "关于", "title_experience": "经历", "title_projects": "作品"},
}

HOME = {
    "en": {
        "name": "团团",
        "tagline": "I studied math, taught it for a year, and I'm moving into data work.",
        "who_h": "Who I am",
        "who": ["I graduated from the University of Florida in 2025 with a B.S. in Mathematics, cum laude, and a minor in education. From August 2025 to June 2026 I taught Algebra 1, Algebra 2 and electives at Trilogy School in Gainesville, Florida.",
                "Now I'm learning data analysis, and learning Lean 4 so I can write proofs a computer can check. Math is still the part I care about most. Away from the desk, I've cleared UCoB, UWU and TEA in Final Fantasy XIV."],
        "make_h": "What I make",
        "cards": [
            {"kind": "Teaching", "title": "Algebra 1 and 2 courses", "href": "projects.html#teaching",
             "body": "At Trilogy I developed both courses from the opening pre-assessment through the unit tests, using the textbook and AI tools. With the electives, that came to about 200 lessons, projects and tests, counting teacher and student versions.",
             "foot": "Sample lessons coming, with no student information."},
            {"kind": "Game, in progress", "title": "Dream Tamer", "href": "projects.html#games",
             "body": "An idle monster-taming game I'm making with Godot and AI coding tools. It runs on PC so far.",
             "foot": "Screenshots go up once the art is better."},
        ],
    },
    "zh": {
        "name": "团团",
        "tagline": "学数学，教过一年数学，现在转向数据工作。",
        "who_h": "我是谁",
        "who": ["2025 年毕业于佛罗里达大学，数学学士（cum laude），辅修教育。2025 年 8 月到 2026 年 6 月，在佛罗里达州盖恩斯维尔的 Trilogy School 教 Algebra 1、Algebra 2 和几门选修课。",
                "现在在学数据分析，也在学 Lean 4，用它写计算机能检查的证明。我最在意的还是数学。工作之外，我在《最终幻想 XIV》里打过 UCoB、UWU 和 TEA。"],
        "make_h": "我做的东西",
        "cards": [
            {"kind": "教学", "title": "Algebra 1 和 2 课程", "href": "projects.html#teaching",
             "body": "在 Trilogy，我用课本和 AI 工具把这两门课从开学摸底做到单元测试。算上选修课，一共约 200 份课件、项目和测试（教师版和学生版分开算）。",
             "foot": "之后放课程样例，不含任何学生信息。"},
            {"kind": "游戏，制作中", "title": "Dream Tamer", "href": "projects.html#games",
             "body": "我正在用 Godot 和 AI 编程工具做的放置类怪物养成游戏，目前能在电脑上运行。",
             "foot": "美术再好一点就放截图。"},
        ],
    },
}

ABOUT = {
    "en": {
        "h": "About",
        "lead": "I like math, and I like explaining it.",
        "sections": [
            {"h": "How I got here", "p": [
                "I studied mathematics at Palm Beach State College and then at the University of Florida, where I also went through the UFTeach program. I started thinking about teaching in college, after helping a classmate with calculus and finding how much I enjoyed it.",
                "I taught for a year after graduating. In the classroom I broke hard ideas into short steps that a student could follow alone. I'm now moving into data and IT work, and I'm building a portfolio of data projects.",
            ]},
            {"h": "Math", "p": [
                "My upper-level courses included Sets and Logic, Linear Algebra, Real Analysis I and II, Abstract Algebra, Topology and Number Theory.",
                "For my honors projects at Palm Beach State I computed graph homology with mod-2 linear algebra and applied calculus to the Ebola outbreak.",
                "I started learning Lean 4 in September 2026 so I can prove theorems with it. I'm still a beginner.",
            ]},
            {"h": "Outside of work", "p": [
                "I play Final Fantasy XIV and have cleared UCoB, UWU and TEA.",
            ]},
        ],
    },
    "zh": {
        "h": "关于",
        "lead": "我喜欢数学，也喜欢把它讲明白。",
        "sections": [
            {"h": "一路走来", "p": [
                "我先在 Palm Beach State College 学数学，后来转到佛罗里达大学，也在那里读了 UFTeach 项目。开始想教书是在大学，那时帮同学学微积分，发现自己很喜欢讲。",
                "毕业后教了一年书。教学时，我把难的概念拆成学生一个人也能跟下来的小步骤。现在我在转向数据和 IT 工作，也在做数据作品集。",
            ]},
            {"h": "数学", "p": [
                "高年级修过的课包括集合与逻辑、线性代数、实分析 I 和 II、抽象代数、拓扑，还有数论。",
                "在 Palm Beach State 的荣誉项目里，我用模 2 线性代数计算图的同调，也把微积分用在埃博拉疫情上。",
                "我 2026 年 9 月开始学 Lean 4，想用它证明定理，现在还是初学者。",
            ]},
            {"h": "工作之外", "p": [
                "我玩《最终幻想 XIV》，打过 UCoB、UWU 和 TEA。",
            ]},
        ],
    },
}

EXPERIENCE = {
    "en": {
        "h": "Experience",
        "lead": "Teaching is the largest part so far, with some IT before it.",
        "groups": [
            {"h": "Work", "items": [
                {"title": "Mathematics Teacher", "org": "Trilogy School, Gainesville, FL", "when": "Aug 2025 to Jun 2026", "points": [
                    "Developed the Algebra 1 and Algebra 2 curriculum on my own, using the textbook and AI tools, from the opening pre-assessment through the unit tests.",
                    "Produced about 200 documents across Algebra 1, Algebra 2 and electives including Coding, Unsolved Mysteries and Financial Literacy, counting teacher and student versions separately.",
                    "Checked problems and answer keys before anything reached students.",
                    "Designed, pitched and ran a 9-week Unsolved Mysteries elective. When the class fell a week behind, I rebuilt the schedule without dropping a major project.",
                ]},
                {"title": "UFTeach teaching internships", "org": "Parker Elementary, Eastside High, P.K. Yonge and Buchholz High, Gainesville, FL", "when": "Spring 2024 to Spring 2025", "points": [
                    "Taught elementary math, IB Mathematics: Applications and Interpretation, 6th-grade accelerated math and Algebra 2 Honors.",
                    "Adjusted explanations for each age and skill level, turning multi-step problems into short steps and hands-on activities.",
                    "Presented a research poster on how absences affect math learning at the UF College of Education symposium in April 2025.",
                ]},
                {"title": "IT Help Desk Assistant, Federal Work-Study", "org": "Palm Beach State College, Boca Raton, FL", "when": "Oct 2019 to Oct 2020", "points": [
                    "Supported students and staff with account, password and software issues, mostly remotely during COVID-19.",
                    "Created, categorized and assigned support tickets in Zendesk.",
                    "Updated software on the college's Surface Book and MacBook devices and helped roll out eduroam access.",
                ]},
            ]},
            {"h": "Education", "items": [
                {"title": "B.S. in Mathematics, cum laude", "org": "University of Florida, minor in education", "when": "Aug 2025", "points": []},
                {"title": "Associate of Arts, Mathematics", "org": "Palm Beach State College, Honors Gold, Koch Honors College", "when": "Aug 2021", "points": []},
            ]},
            {"h": "Student leadership", "items": [
                {"title": "Treasurer and Vice President of Service", "org": "Phi Theta Kappa", "when": "2020 to 2021", "points": ["Handled purchasing within a $20,000 annual budget."]},
                {"title": "Treasurer", "org": "Student Government Association", "when": "2020 to 2021", "points": []},
            ]},
        ],
    },
    "zh": {
        "h": "经历",
        "lead": "目前最多的是教学，更早还做过 IT。",
        "groups": [
            {"h": "工作", "items": [
                {"title": "数学老师", "org": "Trilogy School，佛罗里达州盖恩斯维尔", "when": "2025 年 8 月至 2026 年 6 月", "points": [
                    "用课本和 AI 工具独立开发 Algebra 1 和 Algebra 2 课程，从开学摸底一直到单元测试。",
                    "在 Algebra 1、Algebra 2 和 Coding、Unsolved Mysteries、Financial Literacy 等选修课上做了约 200 份文档（教师版和学生版分开算）。",
                    "所有题目和答案在发给学生之前都检查过。",
                    "设计、提案并开设了 9 周的 Unsolved Mysteries 选修课。进度落后一周时重排了课表，没有砍掉任何大项目。",
                ]},
                {"title": "UFTeach 教学实习", "org": "Parker Elementary、Eastside High、P.K. Yonge 和 Buchholz High，盖恩斯维尔", "when": "2024 年春至 2025 年春", "points": [
                    "教过小学数学、IB Mathematics: Applications and Interpretation、六年级加速数学和 Algebra 2 Honors。",
                    "按不同年龄和水平调整讲法，把多步骤的题拆成小步骤和动手活动。",
                    "2025 年 4 月在佛罗里达大学教育学院的研讨会上展示了关于缺课如何影响数学学习的研究海报。",
                ]},
                {"title": "IT 帮助台助理（联邦勤工俭学）", "org": "Palm Beach State College，佛罗里达州博卡拉顿", "when": "2019 年 10 月至 2020 年 10 月", "points": [
                    "帮学生和教职员工解决账号、密码和软件问题，新冠期间主要远程。",
                    "在 Zendesk 里创建、分类和分派工单。",
                    "给学校的 Surface Book 和 MacBook 更新软件，协助推广 eduroam。",
                ]},
            ]},
            {"h": "教育", "items": [
                {"title": "数学学士，cum laude", "org": "佛罗里达大学，辅修教育", "when": "2025 年 8 月", "points": []},
                {"title": "数学副学士", "org": "Palm Beach State College，Koch 荣誉学院 Honors Gold", "when": "2021 年 8 月", "points": []},
            ]},
            {"h": "学生组织", "items": [
                {"title": "财务主管、服务副主席", "org": "Phi Theta Kappa", "when": "2020 至 2021 年", "points": ["在每年 20,000 美元的预算内负责采购。"]},
                {"title": "财务主管", "org": "学生会", "when": "2020 至 2021 年", "points": []},
            ]},
        ],
    },
}

PROJECTS = {
    "en": {
        "h": "Projects",
        "lead": "Things I have made, and some still being made.",
        "groups": [
            {"id": "teaching", "h": "Teaching", "items": [
                {"title": "Algebra 1 and 2 courses", "body": "Both courses, planned from the opening pre-assessment through the unit tests, broken into units, daily lessons, practice, projects and tests. Key lessons have separate teacher and student versions.", "foot": "Sample lessons coming, with no student information."},
                {"title": "Unsolved Mysteries elective", "body": "A 9-week elective I designed, pitched and ran at Trilogy School."},
                {"title": "Logic lessons", "body": "Truth tables, Knights and Knaves puzzles and the game of Nim, written to build reasoning skills."},
                {"title": "{{?Harmonae City Development}}", "body": "A geometry project for an 11th and 12th grade IB class. Students design a city from geometric shapes, a cat cafe and a shopping mall for cat products among them, then work out areas, missing sides and angles with the laws of sines and cosines, and extend the design into 3D."},
                {"title": "Optimizing Our World", "body": "A two-week Calculus AB unit sketch. Students act as city planners, model a park, garden or parking lot, and use derivatives to justify their design."},
            ]},
            {"id": "games", "h": "Games", "items": [
                {"title": "Dream Tamer", "kind": "In progress", "body": "An idle monster-taming game I'm making with Godot and AI coding tools. It runs on PC so far.", "foot": "Screenshots go up once the art is better."},
            ]},
            {"id": "novels", "h": "Novels", "items": [
                {"title": "Between the Two Ends of the Copper Wire: The Fourth Beat", "kind": "Revising", "img": "cover_copper_wire.jpg",
                 "body": "Yiji runs a small vegetable shop on North Lane, with no very fixed hours. At two in the morning a mouse in a suit, carrying a briefcase, climbs the footstool and pushes one slice of cucumber across the counter. \"I want to buy this shop.\"",
                 "foot": "By 团团. Written in Chinese."},
                {"title": "Syncopation: The Inverted Rest", "kind": "Revising", "img": "cover_syncopation.jpg",
                 "body": "A grey fox in a trench coat runs acquisitions at an investment firm. Under the city lie twelve more streets, and not one deed to their land has ever been on the market.",
                 "foot": "By 团团. Written in Chinese."},
                {"title": "Polyphony: The Unfinished Cadence", "kind": "Revising", "img": "cover_polyphony.jpg",
                 "body": "After the sky turned red, the vegetable shop on North Lane stayed open. Everyone outside the ring of light has moved down to the twelve streets. Those inside it still live in their old houses.",
                 "foot": "By 团团. Written in Chinese. The cover is provisional."},
            ]},
            {"id": "data", "h": "Data", "items": [
                {"title": "Data analysis projects", "kind": "In progress", "body": "My data portfolio will go here when the projects are finished."},
            ]},
            {"id": "tools", "h": "Tools", "items": [
                {"title": "Course document workflow", "body": "An AI-assisted workflow for producing course documents, with a rules file for structure and formatting, a required check before saving, and a log of corrections so the same mistake does not come back."},
                {"title": "Personal automation", "body": "I set up my own automation system with AI tools."},
            ]},
        ],
    },
    "zh": {
        "h": "作品",
        "lead": "做过的东西，还有一些正在做。",
        "groups": [
            {"id": "teaching", "h": "教学", "items": [
                {"title": "Algebra 1 和 2 课程", "body": "两门课从开学摸底规划到单元测试，拆成单元、每日课程、练习、项目和测试。重点课有教师版和学生版。", "foot": "之后放课程样例，不含任何学生信息。"},
                {"title": "Unsolved Mysteries 选修课", "body": "我在 Trilogy School 设计、提案并开设的 9 周选修课。"},
                {"title": "逻辑课", "body": "真值表、骑士与无赖谜题和 Nim 游戏，用来练推理。"},
                {"title": "{{?Harmonae City Development}}", "body": "给 11、12 年级 IB 班做的几何项目。学生用几何图形设计一座城市，里面有猫咖和卖猫用品的商场，然后用正弦定理、余弦定理算面积、缺失的边和角，再把设计扩展到三维。"},
                {"title": "Optimizing Our World", "body": "两周的 Calculus AB 单元草案。学生扮演城市规划师，给公园、花园或停车场建模，用导数说明自己的设计。"},
            ]},
            {"id": "games", "h": "游戏", "items": [
                {"title": "Dream Tamer", "kind": "制作中", "body": "我正在用 Godot 和 AI 编程工具做的放置类怪物养成游戏，目前能在电脑上运行。", "foot": "美术再好一点就放截图。"},
            ]},
            {"id": "novels", "h": "小说", "items": [
                {"title": "《紫铜丝两端的第四拍》", "kind": "修改中", "img": "cover_copper_wire.jpg",
                 "body": "依迹在北巷开了一家蔬果便利店。店不大，营业时间也不大固定。凌晨两点，一只穿西装、打领带、提着公文包的干干鼠推门进来，爬上垫脚凳，把一片黄瓜推到柜台上。“我要买下这家店。”",
                 "foot": "署名：团团。"},
                {"title": "《逆拍：反转的休止符》", "kind": "修改中", "img": "cover_syncopation.jpg",
                 "body": "算无遗在瓜本投资管收购。他是一只灰毛狐狸，上门收房的时候也叫您。这座城底下还有十二条街。十二条街的地，市面上一张地契也没有。",
                 "foot": "署名：团团。"},
                {"title": "《复调：未完成的终止式》", "kind": "修改中", "img": "cover_polyphony.jpg",
                 "body": "天红了以后，北巷的蔬果便利店一直开着。光圈外面的人都搬走了，搬到地底下那十二条街上去了，光圈里面的人还住在原来的屋子里。",
                 "foot": "署名：团团。封面暂定。"},
            ]},
            {"id": "data", "h": "数据", "items": [
                {"title": "数据分析项目", "kind": "制作中", "body": "数据作品集做完后会放在这里。"},
            ]},
            {"id": "tools", "h": "工具", "items": [
                {"title": "课程文档流程", "body": "一套用 AI 辅助做课程文档的流程：有规定结构和格式的规则文件，保存前必须检查，改过的错误都记下来，同样的错不再犯。"},
                {"title": "个人自动化", "body": "我用 AI 工具搭了自己的自动化系统。"},
            ]},
        ],
    },
}
