#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

import sys
import time
import json
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ( accuracy_score, precision_score, recall_score, f1_score )
import pickle

def count_mm(txt): return txt.count("mailman.enron.com")
def count_by(txt): return txt.count("by")
def count_td(txt): return txt.count('<td')
def count_font(txt): return txt.count("<font")
def count_tr(txt): return txt.count("<tr>\n")
def count_tr2(txt): return txt.count("<tr>\r\n")
def count_tr3(txt): return txt.count("</tr>\n")
def count_menor(txt): return txt.count("<")
def count_menora(txt): return txt.count("<a")
def count_menorp(txt): return txt.count("<p")
def count_n(txt): return txt.count("\n")
def count_spaces(txt): return txt.count(" ")
def count_viagra(txt): return txt.count("viagra")
def count_sex(txt): return txt.count("sex")
def count_vagina(txt): return txt.count("vagina")
def count_penis(txt): return txt.count("penis")
def count_money(txt): return txt.count("money")
def count_earn(txt): return txt.count("earn")
def count_free(txt): return txt.count("free")
def count_now(txt): return txt.count("now")
def count_VIAGRA(txt): return txt.count("VIAGRA")
def count_SEX(txt): return txt.count("SEX")
def count_VAGINA(txt): return txt.count("VAGINA")
def count_PENIS(txt): return txt.count("PENIS")
def count_MONEY(txt): return txt.count("MONEY")
def count_EARN(txt): return txt.count("EARN")
def count_FREE(txt): return txt.count("FREE")
def count_NOW(txt): return txt.count("NOW")
def count_help(txt): return txt.count("help")
def count_excl(txt): return txt.count("!")
def count_lose(txt): return txt.count("lose")
def count_weig(txt): return txt.count("weight")
def count_vote(txt): return txt.count("vote")
def count_join(txt): return txt.count("join")
def count_send(txt): return txt.count("send")
def count_offer(txt): return txt.count("offer")
def count_deal(txt): return txt.count("deal")
def count_cum(txt): return txt.count("cum")
def count_huge(txt): return txt.count("huge")
def count_medium(txt): return txt.count("medium")
def count_from(txt): return txt.count("from")
def count_from2(txt): return txt.count("from:")
def count_pill(txt): return txt.count("pill")
def count_hours(txt): return txt.count("hours")
def count_preg(txt): return txt.count("?")
def count_dol(txt): return txt.count("$")
def count_dollar(txt): return txt.count("dollar")
def count_dollars(txt): return txt.count("dollars")
def count_1(txt): return txt.count("1")
def count_2(txt): return txt.count("2")
def count_3(txt): return txt.count("3")
def count_4(txt): return txt.count("4")
def count_5(txt): return txt.count("5")
def count_6(txt): return txt.count("6")
def count_7(txt): return txt.count("7")
def count_8(txt): return txt.count("8")
def count_9(txt): return txt.count("9")
def count_0(txt): return txt.count("0")
def count_work(txt): return txt.count("work")
def count_arr(txt): return txt.count("@")
def count_hash(txt): return txt.count("#")
def count_and(txt): return txt.count("&")
def count_apare(txt): return txt.count("(")
def count_acor(txt): return txt.count("[")
def count_plus(txt): return txt.count("+")
def count_mult(txt): return txt.count("*")
def count_porc(txt): return txt.count("%")
def count_equal(txt): return txt.count("=")
def count_dot(txt): return txt.count(".")
def count_dotc(txt): return txt.count(";")
def count_apos(txt): return txt.count("'")
def count_com(txt): return txt.count("\"")
def count_guionba(txt): return txt.count("_")
def count_dosp(txt): return txt.count(":")
def count_ref(txt): return txt.count("href")
def count_id(txt): return txt.count("id")
def count_px(txt): return txt.count("1px")
def count_ESMTP(txt): return txt.count('ESMTP')
def count_SMTPRS(txt): return txt.count('SMTPRS')
def count_menos(txt): return txt.count('-')
def count_sombrero(txt): return txt.count('^')
def count_aparen(txt): return txt.count('(')
def count_cparen(txt): return txt.count(')')
def count_helvetica(txt): return txt.count('helvetica')
def count_arial(txt): return txt.count('arial')
def count_nigeria(txt): return txt.count('nigeria')
def count_win(txt): return txt.count('win')
def count_HTML(txt): return txt.count("HTML")
def count_html(txt): return txt.count("html")
def count_solid(txt): return txt.count("solid;")
def count_microsoft(txt): return txt.count("microsoft")
def count_technologies(txt): return txt.count("Technologies")
def count_content(txt): return txt.count("(Content")
def count_0600(txt): return txt.count("-0600\nReceived:")
def count_2002(txt): return txt.count("2002")
def count_2004(txt): return txt.count("2004")
def count_2005(txt): return txt.count("2005")
def count_corp(txt): return txt.count("(8.11.4/8.11.4/corp-1.06)")
def count_nahou(txt): return txt.count("nahou-mscnx06p.corp.enron.com")
def count_ip(txt): return txt.count("([192.168.110.237])")
def count_ip2(txt): return txt.count("([192.168.110.224])")
def count_with(txt): return txt.count("with")
def count_your(txt): return txt.count("your")
def count_0800(txt): return txt.count("-0800\nReceived:")
def count_unv(txt): return txt.count("(unverified)")
def count_sat(txt): return txt.count('Sat,')
def count_sun(txt): return txt.count('Sun,')
def count_mar(txt): return txt.count('Mar')
def count_may(txt): return txt.count('May')
def count_apr(txt): return txt.count('Apr')
def count_Jun(txt): return txt.count('Jun')
def count_Jul(txt): return txt.count('Jul')
def count_jun(txt): return txt.count('jun')
def count_jul(txt): return txt.count('jul')
def count_aug(txt): return txt.count('Aug')
def count_face(txt): return txt.count('face=3darial')
def count_produced(txt): return txt.count('produced')
def count_mimeole(txt): return txt.count('mimeole')
def count_align(txt): return txt.count('align=3dmiddle')
def count_mime300(txt): return txt.count('+0300\r\nmime-version:')
def count_encoding(txt): return txt.count('text/html;\r\n\tcharset="iso-8859-7"\r\ncontent-transfer-encoding:')
def count_normal(txt): return txt.count('normal\r\nx-mimeole:')
def count_prior(txt): return txt.count('3\r\nx-msmail-priority:')
def count_style(txt): return txt.count('style=3d"border-right:')
def count_style2(txt): return txt.count('style=3d"font-size:')
def count_none(txt): return txt.count('none;')
def count_td2(txt): return txt.count('<td=20\r\n')
def count_TD(txt): return txt.count('<TD')
def count_quot(txt): return txt.count('quoted-printable\r\nx-priority:')
def count_face2(txt): return txt.count('face=3dverdana')
def count_face3(txt): return txt.count('face="arial,')
def count_face4(txt): return txt.count('face=3DArial')
def count_statements(txt): return txt.count('statements')
def count_0500(txt): return txt.count('-0500')
def count_bb(txt): return txt.count('border-bottom:')
def count_425(txt): return txt.count('4.2.5)')
def count_msg(txt): return txt.count('message')
def count_w3c(txt): return txt.count('"-//w3c//dtd')
def count_SMTPSVC(txt): return txt.count('SMTPSVC(5.0.2195.2966);\n\t')
def count_3d(txt): return txt.count('content=3d"text/html;')
def count_public(txt): return txt.count('public')
def count_0cm(txt): return txt.count('0cm')
def count_paliourg(txt): return txt.count('<paliourg#####>\r\nsubject:')
def count_bt(txt): return txt.count('border-top:')
def count_mp(txt): return txt.count('multi-part')
def count_ff(txt): return txt.count('font-family:')
def count_img(txt): return txt.count('<img')
def count_smtp(txt): return txt.count('smtp;')
def count_http3d(txt): return txt.count('http-equiv=3d"content-type"')
def count_b0(txt): return txt.count('border="0"')
def count_table(txt): return txt.count('<table')
def count_recv(txt): return txt.count('received:')
def count_ms(txt): return txt.count('#####mailserver')
def count_Mail(txt): return txt.count('3\nX-MSMail-Priority:')
def count_solid2(txt): return txt.count('solid"=20\r\n')
def count_cec(txt): return txt.count('corp.enron.com')
def count_cecn(txt): return txt.count('corp.enron.com\n')
def count_bl(txt): return txt.count('=\r\nborder-left:')
def count_Adobe(txt): return txt.count('Adobe')
def count_421(txt): return txt.count('4.2.1)')
def count_fs(txt): return txt.count('font-size:')
def count_2900(txt): return txt.count('v6.00.2900.2527\r\n\r\n<!doctype')
def count_div(txt): return txt.count('<div')
def count_size2(txt): return txt.count('size="2"')
def count_Helvetica(txt): return txt.count('Helvetica,')
def count_software(txt): return txt.count('software')
def count_upper(txt): return sum([c.isupper() for c in txt])
def count_num(txt): return sum([c.isnumeric() for c in txt])
def count_title(txt): return sum([c.istitle() for c in txt])
def lprom(txt): return sum([len(c) for c in txt])/(len(txt))
def lmax(txt): return max([len(c) for c in txt])


dnames = ['len','count_td','count_td2','count_TD','count_by','count_ESMTP','count_SMTPRS','count_menora', 'count_n','count_upper','count_mm','count_ref','count_guionba'
,'count_menorp','count_px','count_from','count_from2','count_id', 'count_spaces','count_cum','count_viagra','count_sex','count_vagina','count_penis'
,'count_money','count_earn','count_free','count_now','count_help','count_excl','count_preg','count_dol','count_dollar','count_dollars'
,'count_1','count_2','count_3','count_4','count_5','count_6','count_7','count_8','count_9','count_0'
,'count_work','count_arr','count_hash','count_and','count_apare','count_acor','count_plus','count_mult','count_porc','count_equal'
,'count_dot','count_dotc','count_apos','count_com','count_send','count_menor','count_dosp','count_offer','count_deal','count_join'
,'count_vote','count_weig','count_lose','count_menos','count_sombrero','count_aparen','count_cparen','count_num','count_title','count_helvetica'
,'count_arial','count_nigeria','count_win','count_FREE','count_VIAGRA','count_SEX','count_VAGINA','count_PENIS','count_MONEY','count_EARN'
,'count_NOW','count_html','count_pill','count_hours','lprom','lmax','count_solid','count_font','count_tr','count_tr2','count_tr3','count_microsoft'
,'count_HTML','count_0600','count_2002','count_2004','count_2005','count_nahou','count_with','count_your','count_0800','count_unv','count_sat','count_sun','count_mar','count_may','count_apr','count_aug','count_jun','count_jul','count_Jun','count_Jul','count_aug'
,'count_huge','count_medium','count_encoding','count_mime300','count_align','count_mimeole','count_produced','count_face','count_face2','count_face3','count_face4','count_corp'
,'count_content','count_technologies','count_ip','count_ip2','count_normal','count_prior','count_style','count_none','count_quot','count_statements'
,'count_0500','count_bb','count_425','count_msg','count_w3c','count_SMTPSVC','count_3d','count_public','count_0cm','count_paliourg','count_bt','count_mp','count_ff','count_img','count_smtp','count_http3d','count_b0','count_table','count_recv','count_ms','count_Mail','count_solid2','count_cec','count_cecn','count_bl','count_Adobe','count_421','count_fs','count_2900','count_div','count_size2','count_Helvetica','count_software']

def cargando_atributos(df):
	dfuncs = [len,count_td,count_td2,count_TD,count_by,count_ESMTP,count_SMTPRS,count_menora, count_n,count_upper,count_mm,count_ref,count_guionba
,count_menorp,count_px,count_from,count_from2,count_id, count_spaces,count_cum,count_viagra,count_sex,count_vagina,count_penis
,count_money,count_earn,count_free,count_now,count_help,count_excl,count_preg,count_dol,count_dollar,count_dollars
,count_1,count_2,count_3,count_4,count_5,count_6,count_7,count_8,count_9,count_0
,count_work,count_arr,count_hash,count_and,count_apare,count_acor,count_plus,count_mult,count_porc,count_equal
,count_dot,count_dotc,count_apos,count_com,count_send,count_menor,count_dosp,count_offer,count_deal,count_join
,count_vote,count_weig,count_lose,count_menos,count_sombrero,count_aparen,count_cparen,count_num,count_title,count_helvetica
,count_arial,count_nigeria,count_win,count_FREE,count_VIAGRA,count_SEX,count_VAGINA,count_PENIS,count_MONEY,count_EARN
,count_NOW,count_html,count_pill,count_hours,lprom,lmax,count_solid,count_font,count_tr,count_tr2,count_tr3,count_microsoft
,count_HTML,count_0600,count_2002,count_2004,count_2005,count_nahou,count_with,count_your,count_0800,count_unv,count_sat,count_sun,count_mar,count_may,count_apr,count_jun,count_jul,count_Jun,count_Jul,count_aug
,count_huge,count_medium,count_encoding,count_mime300,count_align,count_mimeole,count_produced,count_face,count_face2,count_face3,count_face4,count_ip,count_ip2,count_corp
,count_content,count_technologies,count_normal,count_prior,count_style,count_style2,count_none,count_quot,count_statements
,count_0500,count_bb,count_425,count_msg,count_w3c,count_SMTPSVC,count_3d,count_public,count_0cm,count_paliourg,count_bt,count_mp,count_ff,count_img,count_smtp,count_http3d,count_b0,count_table,count_recv,count_ms,count_Mail,count_solid2,count_cec,count_cecn,count_bl,count_Adobe,count_421,count_fs,count_2900,count_div,count_size2,count_Helvetica,count_software]

	for i in range(len(dnames)):
		df[dnames[i]] = map(dfuncs[i], df.text)
	return df, dnames

if __name__ == '__main__':
	if len(sys.argv) > 1:
		test = json.load(open(sys.argv[1]))
	else:
		print u'Faltan parámetros!'
		exit()
	metodo = "RforestComp.pickle"
	df = pd.DataFrame(test, columns=['text'])
	df, dnames = cargando_atributos(df)
	# Transformar si es necesario (PCA, ICA, etc.)
	clf = pickle.load(open(metodo))
	predy = list(clf.predict(df[dnames].values))
	for p in predy:
		print p
