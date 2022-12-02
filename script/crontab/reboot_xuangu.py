#:  -*- coding: utf-8 -*-
import json
import time

from chanlun import zixuan
from chanlun.cl_interface import *
from chanlun.cl_utils import web_batch_get_cl_datas
from chanlun.exchange.exchange_tdx import ExchangeTDX
from chanlun.xuangu import xuangu

"""
沪深A股 选股程序
不要在这个文件进行修改，请 copy 并命名为 my_reboot_a_xuangu.py 进行修改并运行，维护自己写的选股程序
"""

ex = ExchangeTDX()

"""
运行的股票代码，可通过 joinquant 目录中的脚本，在聚宽平台运行后获取（可根据自己的基本面选股方法进行选择）
"""
codes = ["SZ.000001", "SZ.000002", "SZ.000009", "SZ.000012", "SZ.000016", "SZ.000021", "SZ.000027", "SZ.000028",
         "SZ.000031", "SZ.000032", "SZ.000035", "SZ.000039", "SZ.000046", "SZ.000048", "SZ.000049", "SZ.000050",
         "SZ.000059", "SZ.000060", "SZ.000061", "SZ.000062", "SZ.000063", "SZ.000066", "SZ.000069", "SZ.000088",
         "SZ.000089", "SZ.000090", "SZ.000100", "SZ.000155", "SZ.000156", "SZ.000157", "SZ.000166", "SZ.000301",
         "SZ.000333", "SZ.000338", "SZ.000400", "SZ.000401", "SZ.000402", "SZ.000403", "SZ.000415", "SZ.000422",
         "SZ.000423", "SZ.000425", "SZ.000426", "SZ.000429", "SZ.000488", "SZ.000498", "SZ.000513", "SZ.000516",
         "SZ.000519", "SZ.000528", "SZ.000537", "SZ.000538", "SZ.000539", "SZ.000540", "SZ.000547", "SZ.000550",
         "SZ.000553", "SZ.000555", "SZ.000559", "SZ.000563", "SZ.000568", "SZ.000581", "SZ.000582", "SZ.000591",
         "SZ.000596", "SZ.000598", "SZ.000617", "SZ.000623", "SZ.000625", "SZ.000627", "SZ.000629", "SZ.000630",
         "SZ.000651", "SZ.000656", "SZ.000657", "SZ.000661", "SZ.000671", "SZ.000672", "SZ.000683", "SZ.000685",
         "SZ.000686", "SZ.000688", "SZ.000690", "SZ.000703", "SZ.000708", "SZ.000709", "SZ.000712", "SZ.000717",
         "SZ.000718", "SZ.000723", "SZ.000725", "SZ.000727", "SZ.000728", "SZ.000729", "SZ.000733", "SZ.000738",
         "SZ.000739", "SZ.000750", "SZ.000761", "SZ.000762", "SZ.000768", "SZ.000776", "SZ.000778", "SZ.000783",
         "SZ.000785", "SZ.000786", "SZ.000789", "SZ.000792", "SZ.000799", "SZ.000800", "SZ.000807", "SZ.000810",
         "SZ.000818", "SZ.000825", "SZ.000828", "SZ.000829", "SZ.000830", "SZ.000831", "SZ.000858", "SZ.000860",
         "SZ.000869", "SZ.000875", "SZ.000876", "SZ.000877", "SZ.000878", "SZ.000883", "SZ.000887", "SZ.000893",
         "SZ.000895", "SZ.000898", "SZ.000902", "SZ.000921", "SZ.000923", "SZ.000927", "SZ.000930", "SZ.000932",
         "SZ.000933", "SZ.000935", "SZ.000937", "SZ.000938", "SZ.000951", "SZ.000958", "SZ.000959", "SZ.000960",
         "SZ.000961", "SZ.000963", "SZ.000967", "SZ.000970", "SZ.000975", "SZ.000977", "SZ.000983", "SZ.000987",
         "SZ.000988", "SZ.000990", "SZ.000997", "SZ.000998", "SZ.000999", "SZ.001872", "SZ.001914", "SZ.001965",
         "SZ.001979", "SZ.002001", "SZ.002002", "SZ.002004", "SZ.002007", "SZ.002008", "SZ.002010", "SZ.002013",
         "SZ.002015", "SZ.002019", "SZ.002024", "SZ.002025", "SZ.002027", "SZ.002028", "SZ.002030", "SZ.002032",
         "SZ.002036", "SZ.002038", "SZ.002041", "SZ.002044", "SZ.002048", "SZ.002049", "SZ.002050", "SZ.002051",
         "SZ.002056", "SZ.002064", "SZ.002065", "SZ.002074", "SZ.002075", "SZ.002078", "SZ.002080", "SZ.002081",
         "SZ.002091", "SZ.002092", "SZ.002099", "SZ.002100", "SZ.002110", "SZ.002120", "SZ.002124", "SZ.002127",
         "SZ.002128", "SZ.002129", "SZ.002131", "SZ.002135", "SZ.002138", "SZ.002139", "SZ.002142", "SZ.002145",
         "SZ.002146", "SZ.002151", "SZ.002152", "SZ.002153", "SZ.002155", "SZ.002156", "SZ.002157", "SZ.002171",
         "SZ.002176", "SZ.002179", "SZ.002180", "SZ.002182", "SZ.002183", "SZ.002185", "SZ.002191", "SZ.002192",
         "SZ.002195", "SZ.002202", "SZ.002203", "SZ.002212", "SZ.002216", "SZ.002221", "SZ.002223", "SZ.002226",
         "SZ.002230", "SZ.002233", "SZ.002236", "SZ.002237", "SZ.002240", "SZ.002241", "SZ.002242", "SZ.002243",
         "SZ.002244", "SZ.002245", "SZ.002249", "SZ.002250", "SZ.002252", "SZ.002254", "SZ.002258", "SZ.002262",
         "SZ.002266", "SZ.002268", "SZ.002271", "SZ.002273", "SZ.002274", "SZ.002281", "SZ.002291", "SZ.002293",
         "SZ.002294", "SZ.002299", "SZ.002302", "SZ.002304", "SZ.002311", "SZ.002312", "SZ.002314", "SZ.002317",
         "SZ.002318", "SZ.002320", "SZ.002324", "SZ.002326", "SZ.002335", "SZ.002340", "SZ.002352", "SZ.002353",
         "SZ.002368", "SZ.002371", "SZ.002372", "SZ.002373", "SZ.002382", "SZ.002384", "SZ.002385", "SZ.002389",
         "SZ.002390", "SZ.002396", "SZ.002399", "SZ.002402", "SZ.002405", "SZ.002407", "SZ.002408", "SZ.002409",
         "SZ.002410", "SZ.002414", "SZ.002415", "SZ.002416", "SZ.002422", "SZ.002423", "SZ.002424", "SZ.002429",
         "SZ.002430", "SZ.002432", "SZ.002434", "SZ.002436", "SZ.002439", "SZ.002444", "SZ.002453", "SZ.002456",
         "SZ.002459", "SZ.002460", "SZ.002461", "SZ.002463", "SZ.002465", "SZ.002466", "SZ.002468", "SZ.002472",
         "SZ.002475", "SZ.002481", "SZ.002484", "SZ.002487", "SZ.002493", "SZ.002497", "SZ.002498", "SZ.002500",
         "SZ.002505", "SZ.002506", "SZ.002507", "SZ.002508", "SZ.002511", "SZ.002531", "SZ.002532", "SZ.002534",
         "SZ.002537", "SZ.002539", "SZ.002541", "SZ.002544", "SZ.002545", "SZ.002555", "SZ.002556", "SZ.002557",
         "SZ.002558", "SZ.002563", "SZ.002567", "SZ.002568", "SZ.002572", "SZ.002585", "SZ.002594", "SZ.002595",
         "SZ.002597", "SZ.002600", "SZ.002601", "SZ.002602", "SZ.002603", "SZ.002607", "SZ.002610", "SZ.002617",
         "SZ.002624", "SZ.002625", "SZ.002626", "SZ.002643", "SZ.002645", "SZ.002648", "SZ.002653", "SZ.002670",
         "SZ.002673", "SZ.002683", "SZ.002690", "SZ.002698", "SZ.002701", "SZ.002705", "SZ.002706", "SZ.002709",
         "SZ.002714", "SZ.002726", "SZ.002727", "SZ.002736", "SZ.002738", "SZ.002745", "SZ.002747", "SZ.002756",
         "SZ.002773", "SZ.002791", "SZ.002793", "SZ.002797", "SZ.002810", "SZ.002812", "SZ.002815", "SZ.002821",
         "SZ.002831", "SZ.002832", "SZ.002839", "SZ.002841", "SZ.002850", "SZ.002851", "SZ.002865", "SZ.002867",
         "SZ.002901", "SZ.002906", "SZ.002916", "SZ.002920", "SZ.002925", "SZ.002926", "SZ.002928", "SZ.002936",
         "SZ.002938", "SZ.002939", "SZ.002941", "SZ.002945", "SZ.002946", "SZ.002948", "SZ.002958", "SZ.002960",
         "SZ.002966", "SZ.002967", "SZ.002978", "SZ.002984", "SZ.002985", "SZ.003022", "SZ.003035", "SZ.003040",
         "SZ.003816", "SZ.300001", "SZ.300012", "SZ.300014", "SZ.300015", "SZ.300017", "SZ.300024", "SZ.300033",
         "SZ.300034", "SZ.300035", "SZ.300037", "SZ.300054", "SZ.300059", "SZ.300070", "SZ.300072", "SZ.300073",
         "SZ.300077", "SZ.300087", "SZ.300088", "SZ.300115", "SZ.300118", "SZ.300122", "SZ.300136", "SZ.300144",
         "SZ.300146", "SZ.300158", "SZ.300171", "SZ.300185", "SZ.300188", "SZ.300207", "SZ.300212", "SZ.300223",
         "SZ.300233", "SZ.300236", "SZ.300244", "SZ.300251", "SZ.300253", "SZ.300257", "SZ.300274", "SZ.300285",
         "SZ.300294", "SZ.300308", "SZ.300316", "SZ.300327", "SZ.300343", "SZ.300347", "SZ.300357", "SZ.300358",
         "SZ.300363", "SZ.300390", "SZ.300395", "SZ.300398", "SZ.300408", "SZ.300409", "SZ.300413", "SZ.300418",
         "SZ.300432", "SZ.300438", "SZ.300450", "SZ.300451", "SZ.300454", "SZ.300456", "SZ.300457", "SZ.300463",
         "SZ.300476", "SZ.300482", "SZ.300487", "SZ.300496", "SZ.300498", "SZ.300502", "SZ.300529", "SZ.300558",
         "SZ.300567", "SZ.300568", "SZ.300587", "SZ.300595", "SZ.300601", "SZ.300604", "SZ.300613", "SZ.300618",
         "SZ.300623", "SZ.300627", "SZ.300628", "SZ.300630", "SZ.300633", "SZ.300638", "SZ.300661", "SZ.300666",
         "SZ.300672", "SZ.300674", "SZ.300676", "SZ.300677", "SZ.300679", "SZ.300682", "SZ.300685", "SZ.300696",
         "SZ.300699", "SZ.300702", "SZ.300724", "SZ.300725", "SZ.300726", "SZ.300737", "SZ.300741", "SZ.300747",
         "SZ.300748", "SZ.300750", "SZ.300751", "SZ.300755", "SZ.300759", "SZ.300760", "SZ.300761", "SZ.300763",
         "SZ.300768", "SZ.300769", "SZ.300773", "SZ.300775", "SZ.300776", "SZ.300777", "SZ.300782", "SZ.300783",
         "SZ.300803", "SZ.300821", "SZ.300832", "SZ.300841", "SZ.300850", "SZ.300861", "SZ.300866", "SZ.300869",
         "SZ.300888", "SZ.300896", "SZ.300919", "SZ.300957", "SZ.300973", "SZ.300979", "SZ.300999", "SZ.301035",
         "SZ.301071", "SZ.301080", "SH.600000", "SH.600004", "SH.600007", "SH.600008", "SH.600009", "SH.600010",
         "SH.600011", "SH.600012", "SH.600015", "SH.600016", "SH.600018", "SH.600019", "SH.600021", "SH.600025",
         "SH.600026", "SH.600027", "SH.600028", "SH.600029", "SH.600030", "SH.600031", "SH.600036", "SH.600038",
         "SH.600039", "SH.600048", "SH.600050", "SH.600056", "SH.600057", "SH.600060", "SH.600061", "SH.600062",
         "SH.600066", "SH.600075", "SH.600079", "SH.600085", "SH.600089", "SH.600095", "SH.600104", "SH.600109",
         "SH.600110", "SH.600111", "SH.600115", "SH.600116", "SH.600118", "SH.600120", "SH.600123", "SH.600131",
         "SH.600132", "SH.600141", "SH.600143", "SH.600150", "SH.600151", "SH.600153", "SH.600155", "SH.600160",
         "SH.600161", "SH.600167", "SH.600170", "SH.600171", "SH.600172", "SH.600176", "SH.600177", "SH.600179",
         "SH.600183", "SH.600185", "SH.600188", "SH.600195", "SH.600196", "SH.600197", "SH.600199", "SH.600201",
         "SH.600206", "SH.600208", "SH.600216", "SH.600219", "SH.600223", "SH.600233", "SH.600236", "SH.600248",
         "SH.600252", "SH.600256", "SH.600258", "SH.600259", "SH.600271", "SH.600273", "SH.600276", "SH.600282",
         "SH.600295", "SH.600297", "SH.600298", "SH.600299", "SH.600305", "SH.600309", "SH.600315", "SH.600316",
         "SH.600323", "SH.600325", "SH.600328", "SH.600329", "SH.600332", "SH.600338", "SH.600340", "SH.600346",
         "SH.600348", "SH.600350", "SH.600352", "SH.600362", "SH.600363", "SH.600369", "SH.600372", "SH.600373",
         "SH.600376", "SH.600377", "SH.600378", "SH.600380", "SH.600383", "SH.600388", "SH.600389", "SH.600392",
         "SH.600395", "SH.600398", "SH.600399", "SH.600406", "SH.600409", "SH.600415", "SH.600416", "SH.600418",
         "SH.600420", "SH.600426", "SH.600436", "SH.600438", "SH.600446", "SH.600452", "SH.600459", "SH.600460",
         "SH.600483", "SH.600486", "SH.600487", "SH.600489", "SH.600498", "SH.600499", "SH.600500", "SH.600507",
         "SH.600510", "SH.600511", "SH.600516", "SH.600518", "SH.600519", "SH.600521", "SH.600522", "SH.600529",
         "SH.600536", "SH.600546", "SH.600547", "SH.600548", "SH.600549", "SH.600556", "SH.600559", "SH.600562",
         "SH.600563", "SH.600566", "SH.600567", "SH.600570", "SH.600580", "SH.600582", "SH.600583", "SH.600584",
         "SH.600585", "SH.600588", "SH.600596", "SH.600597", "SH.600598", "SH.600600", "SH.600606", "SH.600612",
         "SH.600621", "SH.600635", "SH.600637", "SH.600639", "SH.600641", "SH.600642", "SH.600643", "SH.600648",
         "SH.600655", "SH.600657", "SH.600660", "SH.600663", "SH.600667", "SH.600673", "SH.600674", "SH.600682",
         "SH.600685", "SH.600688", "SH.600690", "SH.600699", "SH.600702", "SH.600703", "SH.600704", "SH.600705",
         "SH.600711", "SH.600728", "SH.600729", "SH.600737", "SH.600739", "SH.600740", "SH.600741", "SH.600745",
         "SH.600754", "SH.600755", "SH.600760", "SH.600763", "SH.600764", "SH.600765", "SH.600776", "SH.600777",
         "SH.600779", "SH.600782", "SH.600787", "SH.600795", "SH.600801", "SH.600803", "SH.600808", "SH.600809",
         "SH.600811", "SH.600820", "SH.600823", "SH.600827", "SH.600835", "SH.600837", "SH.600845", "SH.600848",
         "SH.600850", "SH.600859", "SH.600862", "SH.600863", "SH.600867", "SH.600871", "SH.600872", "SH.600873",
         "SH.600874", "SH.600875", "SH.600876", "SH.600882", "SH.600884", "SH.600885", "SH.600886", "SH.600887",
         "SH.600888", "SH.600893", "SH.600895", "SH.600900", "SH.600905", "SH.600909", "SH.600918", "SH.600919",
         "SH.600926", "SH.600956", "SH.600958", "SH.600966", "SH.600967", "SH.600968", "SH.600970", "SH.600985",
         "SH.600988", "SH.600989", "SH.600998", "SH.600999", "SH.601000", "SH.601001", "SH.601003", "SH.601005",
         "SH.601006", "SH.601009", "SH.601012", "SH.601015", "SH.601016", "SH.601018", "SH.601019", "SH.601021",
         "SH.601038", "SH.601058", "SH.601066", "SH.601077", "SH.601088", "SH.601098", "SH.601099", "SH.601100",
         "SH.601101", "SH.601107", "SH.601108", "SH.601111", "SH.601117", "SH.601128", "SH.601138", "SH.601139",
         "SH.601155", "SH.601156", "SH.601158", "SH.601162", "SH.601166", "SH.601168", "SH.601169", "SH.601186",
         "SH.601187", "SH.601198", "SH.601200", "SH.601208", "SH.601211", "SH.601216", "SH.601222", "SH.601225",
         "SH.601229", "SH.601231", "SH.601233", "SH.601236", "SH.601238", "SH.601288", "SH.601298", "SH.601311",
         "SH.601318", "SH.601319", "SH.601326", "SH.601328", "SH.601333", "SH.601336", "SH.601360", "SH.601369",
         "SH.601375", "SH.601377", "SH.601390", "SH.601398", "SH.601456", "SH.601515", "SH.601555", "SH.601567",
         "SH.601577", "SH.601598", "SH.601600", "SH.601601", "SH.601607", "SH.601608", "SH.601615", "SH.601618",
         "SH.601628", "SH.601633", "SH.601636", "SH.601658", "SH.601665", "SH.601666", "SH.601668", "SH.601669",
         "SH.601677", "SH.601678", "SH.601688", "SH.601689", "SH.601696", "SH.601699", "SH.601717", "SH.601727",
         "SH.601766", "SH.601788", "SH.601799", "SH.601800", "SH.601801", "SH.601808", "SH.601811", "SH.601816",
         "SH.601818", "SH.601827", "SH.601828", "SH.601838", "SH.601857", "SH.601865", "SH.601866", "SH.601868",
         "SH.601869", "SH.601872", "SH.601877", "SH.601878", "SH.601880", "SH.601881", "SH.601888", "SH.601898",
         "SH.601899", "SH.601901", "SH.601908", "SH.601916", "SH.601919", "SH.601928", "SH.601933", "SH.601939",
         "SH.601952", "SH.601958", "SH.601963", "SH.601965", "SH.601966", "SH.601985", "SH.601988", "SH.601989",
         "SH.601990", "SH.601991", "SH.601992", "SH.601995", "SH.601997", "SH.601998", "SH.603000", "SH.603005",
         "SH.603008", "SH.603010", "SH.603019", "SH.603025", "SH.603026", "SH.603027", "SH.603039", "SH.603043",
         "SH.603056", "SH.603063", "SH.603077", "SH.603087", "SH.603098", "SH.603113", "SH.603127", "SH.603128",
         "SH.603129", "SH.603160", "SH.603179", "SH.603185", "SH.603195", "SH.603198", "SH.603218", "SH.603225",
         "SH.603228", "SH.603233", "SH.603236", "SH.603259", "SH.603260", "SH.603267", "SH.603279", "SH.603288",
         "SH.603290", "SH.603298", "SH.603300", "SH.603305", "SH.603317", "SH.603323", "SH.603338", "SH.603345",
         "SH.603355", "SH.603369", "SH.603392", "SH.603444", "SH.603456", "SH.603477", "SH.603486", "SH.603489",
         "SH.603501", "SH.603515", "SH.603517", "SH.603520", "SH.603529", "SH.603565", "SH.603568", "SH.603588",
         "SH.603589", "SH.603596", "SH.603599", "SH.603605", "SH.603606", "SH.603613", "SH.603638", "SH.603650",
         "SH.603658", "SH.603659", "SH.603666", "SH.603678", "SH.603690", "SH.603707", "SH.603712", "SH.603713",
         "SH.603719", "SH.603733", "SH.603737", "SH.603786", "SH.603799", "SH.603806", "SH.603816", "SH.603833",
         "SH.603858", "SH.603866", "SH.603868", "SH.603876", "SH.603882", "SH.603883", "SH.603885", "SH.603893",
         "SH.603899", "SH.603906", "SH.603915", "SH.603919", "SH.603927", "SH.603939", "SH.603986", "SH.603989",
         "SH.603993", "SH.603995", "SH.605111", "SH.605117", "SH.605123", "SH.605358", "SH.605369", "SH.605376",
         "SH.605499", "SH.688002", "SH.688005", "SH.688006", "SH.688008", "SH.688009", "SH.688012", "SH.688016",
         "SH.688019", "SH.688023", "SH.688029", "SH.688036", "SH.688037", "SH.688066", "SH.688088", "SH.688099",
         "SH.688111", "SH.688116", "SH.688122", "SH.688126", "SH.688131", "SH.688139", "SH.688169", "SH.688180",
         "SH.688185", "SH.688187", "SH.688188", "SH.688198", "SH.688200", "SH.688202", "SH.688208", "SH.688233",
         "SH.688289", "SH.688298", "SH.688321", "SH.688333", "SH.688356", "SH.688363", "SH.688366", "SH.688385",
         "SH.688388", "SH.688390", "SH.688396", "SH.688499", "SH.688516", "SH.688521", "SH.688536", "SH.688568",
         "SH.688598", "SH.688599", "SH.688617", "SH.688639", "SH.688680", "SH.688690", "SH.688696", "SH.688707",
         "SH.688776", "SH.688981", "SH.689009"]
"""
运行的周期，根据自己的选股方法，来设置周期参数
"""
frequencys = ['d', '30m']

"""
这里设置选股缠论计算的参数，要与前台展示的配置一致，不然这里选出的股票符合条件，前台页面有可能看不到
"""
cl_config = {
    # 分型默认配置
    'fx_qj': Config.FX_QJ_K.value,
    'fx_bh': Config.FX_BH_YES.value,
    # 笔默认配置
    'bi_type': Config.BI_TYPE_NEW.value,
    'bi_bzh': Config.BI_BZH_NO.value,
    'bi_fx_cgd': Config.BI_FX_CHD_YES.value,
    'bi_qj': Config.BI_QJ_CK.value,
    # 线段默认配置
    'xd_bzh': Config.XD_BZH_NO.value,
    'xd_qj': Config.XD_QJ_DD.value,
    # 走势段默认配置
    'zsd_bzh': Config.ZSD_BZH_YES.value,
    'zsd_qj': Config.ZSD_QJ_DD.value,
    # 中枢默认配置
    'zs_bi_type': Config.ZS_TYPE_DN.value,  # 笔中枢类型
    'zs_xd_type': Config.ZS_TYPE_DN.value,  # 走势中枢类型
    'zs_qj': Config.ZS_QJ_DD.value,
    'zs_wzgx': Config.ZS_WZGX_ZGD.value,
}

print('运行股票数量：', len(codes))

"""
直接放入自选组
这个需要确保在 config.py 中有进行配置
"""
zx = zixuan.ZiXuan('a')
zx_group = '选股'

# 清空选股自选
zx.clear_zx_stocks(zx_group)

choice_stocks = []  # 保存符合要求的股票列表
_stime = time.time()
for code in codes:
    try:
        klines = {}
        for f in frequencys:
            k = ex.klines(code, f)
            klines[f] = k
        cds: List[ICL] = web_batch_get_cl_datas('a', code, klines, cl_config)
        """
        *** 这里使用自己需要的选股条件方法进行判断 ***
        """
        msg = xuangu.xg_multiple_xd_bi_mmd(cds)
        if msg is not None:
            stocks = ex.stock_info(code)
            print('【%s - %s 】 出现机会：%s' % (stocks['code'], stocks['name'], msg))
            choice_stocks.append(stocks)
            zx.add_stock(zx_group, stocks['code'], stocks['name'])

        """
        *** 这里也可以在写其他的选股条件，执行多个选股策略；复制以上的并改变选股条件 ***
        """
        # ...
    except Exception as e:
        print('Code : %s Run Exception : %s' % (code, e))

print('运行时间：%s' % (time.time() - _stime))
print('Done')
print(json.dumps(choice_stocks, ensure_ascii=False))
