import requests
from lxml import html

headers = {
		'Host':'162.217.184.82',
		'Connection':'keep-alive',
		'Content-Length':'2488',
		'Origin':' http://162.217.184.82',
		'X-Requested-With':' XMLHttpRequest',
		'Cache-Control':'no-cache',
		'X-MicrosoftAjax':'Delta=true',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
		'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
		'Accept':' */*',
		'Referer':'http://162.217.184.82/i2/default.aspx?AspxAutoDetectCookieSupport=0',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'en-US,en;q=0.8',
		'Cookie': 'AspxAutoDetectCookieSupport=1; ASP.NET_SessionId=svs5rb45szy1ux55oca5aovs'
}
payload={
	'SearchFormEx1$PINTextBox4' : '0000',
	'SearchFormEx1$PINTextBox3' : '013',
	'SearchFormEx1$PINTextBox2' : '402',
	'SearchFormEx1$PINTextBox1' : '08',
	'SearchFormEx1$PINTextBox0' : '07',
	'SearchFormEx1$btnSearch' : 'Search',
	'SearchFormEx1$ACSTextBox_UnitNo' : '',
	'SearchFormEx1$ACSTextBox_Subdivision' : '',
	'SearchFormEx1$ACSTextBox_Quarter3' : '',
	'SearchFormEx1$ACSTextBox_Quarter2' : '',
	'SearchFormEx1$ACSTextBox_Quarter1' : '',
	'SearchFormEx1$ACSTextBox_PartOfLotNo' : '',
	'SearchFormEx1$ACSTextBox_Part2Code' : '',
	'SearchFormEx1$ACSTextBox_Part1Code' : '',
	'SearchFormEx1$ACSTextBox_OneHalfCode' : '',
	'SearchFormEx1$ACSTextBox_LotNo' : '',
	'SearchFormEx1$ACSTextBox_DeclarationCondoNo' : '',
	'SearchFormEx1$ACSTextBox_BuildingNo':'',
	'SearchFormEx1$ACSTextBox_BlockNo' : '',
	'SearchFormEx1$ACSTextBox_AcresNo' : '',
	'ScriptManager1_HiddenField' : ';;AjaxControlToolkit, Version=3.5.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:1547e793-5b7e-48fe-8490-03a375b13a33:effe2a26;;AjaxControlToolkit, Version=3.5.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:1547e793-5b7e-48fe-8490-03a375b13a33:475a4ef5:5546a2b:497ef277:a43b07eb:d2e10b12:37e2e5c9:5a682656:1d3ed089:f9029856:d1a1d569;',
	'ScriptManager1' : 'SearchFormEx1$UpdatePanel|SearchFormEx1$btnSearch',
	'PTAXViewer1$ScrollPosChange' : '',
	'PTAXViewer1$ScrollPos':'',
	'PTAXViewer1$isImageViewerVisible':'true',
	'PTAXViewer1$hdnWidgetSize':'',
	'PTAXViewer1$DragResizeExtender_ClientState':'',
	'PTAXViewer1$_imgContainerWidth':'0',
	'PTAXViewer1$_imgContainerHeight':'0',
	'OrderList1$ctl03':'',
	'OrderList1$ctl01' : '',
	'Navigator1$SearchOptions1$DocImagesCheck' : 'on',
	'NameList1$ScrollPosChange':'',
	'NameList1$ScrollPos':'',
	'NameList1$ctl05':'',
	'NameList1$ctl03':'',
	'NameList1$_SortExpression':'',
	'ImageViewer1$ScrollPosChange':'',
	'ImageViewer1$ScrollPos':'',
	'ImageViewer1$isImageViewerVisible':'true',
	'ImageViewer1$hdnWidgetSize':'',
	'ImageViewer1$DragResizeExtender_ClientState':'',
	'ImageViewer1$_imgContainerWidth':'0',
	'ImageViewer1$_imgContainerHeight':'0',
	'DocList1$ctl11':'',
	'DocList1$ctl09':'',
	'DocDetails1$SortExpression':'',
	'DocDetails1$PageSize':'',
	'DocDetails1$PageIndex':'',
	'CertificateViewer1$ScrollPosChange':'',
	'CertificateViewer1$ScrollPos':'',
	'CertificateViewer1$isImageViewerVisible':'true',
	'CertificateViewer1$hdnWidgetSize':'',
	'CertificateViewer1$DragResizeExtender_ClientState':'',
	'CertificateViewer1$_imgContainerWidth':'0',
	'CertificateViewer1$_imgContainerHeight':'0',
	'BasketCtrl1$ctl03':'',
	'BasketCtrl1$ctl01':'',
	'__VIEWSTATE':'',
	'__LASTFOCUS':'',
	'__EVENTTARGET':'',
	'__EVENTARGUMENT':'',
	'__ASYNCPOST':'true',
}

url='http://162.217.184.82/i2/default.aspx?AspxAutoDetectCookieSupport=0'
r = requests.post(url,headers=headers,data=payload)
fo = open("foo.txt", "wb")
fo.write(r.content);
fo.close()
print(r)
#print(r.apparent_encoding)

#tree = html.formstring(r.content)
#first = tree.xpath('//')
