# 语种检查使用说明 #
	1、根据excel的各列的内容填写config.ini配置,config.ini中的等号前面的表示国家代码(详解语言国家代码表),等号后面的表示Excel表格中对应的列B、C、D等 以此内推，注意:这里一定要把映射填写正确

    log日志信息说明:

    expe:cs fact:jw id------{(GMT+07:00) Bangkok, Jakarta} {(GMT + 07: 00) Bangkok, Jakarta}

    expe:cs 表示预期的国家语种为cs

    fact:jw id 表示实际使用谷歌翻译得到的国家语言代码,有多个值表示可能同一个字符在这几个国家意思一样

    ------:分隔符 没有实际意义

    {(GMT+07:00) Bangkok, Jakarta}: 第一个大括号内的表示Excel中的字符

    {(GMT + 07: 00) Bangkok, Jakarta}:第二个大括号内的内容表示使用谷歌翻译为预期国家代码(这里为cs)的字符串
    
[GetTk](https://github.com/MrS0m30n3/google-translate/tree/master/google_translate)

# Language Code #
	language	ISO-639-1 Code

	Afrikaans	af
	Albanian	sq
	Amharic	am
	Arabic	ar
	Armenian	hy
	Azeerbaijani	az
	Basque	eu
	Belarusian	be
	Bengali	bn
	Bosnian	bs
	Bulgarian	bg
	Catalan	ca
	Cebuano	ceb
	Chinese (Simplified)	zh-CN
	Chinese (Traditional)	zh-TW
	Corsican	co
	Croatian	hr
	Czech	cs
	Danish	da
	Dutch	nl
	English	en
	Esperanto	eo
	Estonian	et
	Finnish	fi
	French	fr
	Frisian	fy
	Galician	gl
	Georgian	ka
	German	de
	Greek	el
	Gujarati	gu
	Haitian Creole	ht
	Hausa	ha
	Hawaiian	haw
	Hebrew	iw
	Hindi	hi
	Hmong	hmn
	Hungarian	hu
	Icelandic	is
	Igbo	ig
	Indonesian	id
	Irish	ga
	Italian	it
	Japanese	ja
	Javanese	jw
	Kannada	kn
	Kazakh	kk
	Khmer	km
	Korean	ko
	Kurdish	ku
	Kyrgyz	ky
	Lao	lo
	Latin	la
	Latvian	lv
	Lithuanian	lt
	Luxembourgish	lb
	Macedonian	mk
	Malagasy	mg
	Malay	ms
	Malayalam	ml
	Maltese	mt
	Maori	mi
	Marathi	mr
	Mongolian	mn
	Myanmar (Burmese)	my
	Nepali	ne
	Norwegian	no
	Nyanja (Chichewa)	ny
	Pashto	ps
	Persian	fa
	Polish	pl
	Portuguese (Portugal, Brazil)	pt
	Punjabi	pa
	Romanian	ro
	Russian	ru
	Samoan	sm
	Scots Gaelic	gd
	Serbian	sr
	Sesotho	st
	Shona	sn
	Sindhi	sd
	Sinhala (Sinhalese)	si
	Slovak	sk
	Slovenian	sl
	Somali	so
	Spanish	es
	Sundanese	su
	Swahili	sw
	Swedish	sv
	Tagalog (Filipino)	tl
	Tajik	tg
	Tamil	ta
	Telugu	te
	Thai	th
	Turkish	tr
	Ukrainian	uk
	Urdu	ur
	Uzbek	uz
	Vietnamese	vi
	Welsh	cy
	Xhosa	xh
	Yiddish	yi
	Yoruba	yo
	Zulu	zu
