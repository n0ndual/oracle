import re
from xml.dom import minidom
from urllib2 import urlopen
from base64 import b64decode,b64encode


snapshotID = 'snap-03bae56722ceec3f0'
imageID = 'ami-1f447c65'

#oracle_modulus = "CFB05119FCC076B916E7D7AB252F20CB7FC48D166331087E952E4205B6EEE81982A7674A899E468791A409BD72AC7F7280881485EBE6CA8C6FEA399C0BECFBE05B58E911E1DFDCBC4F2E5C6A137B19921F2E49ECC3ED5044E5287EE32392142A5E134F6A4535FBC890F9998E9C6F560224A0268C8C3AF81E7A8C2D7E5D25C61F88DB8C4B31065E2C6A751489E753D199F8653ABF2B62553CCDE73D49EBAA5DCDB088EB99AA9D8ED32DE5BB0AF0FA70226D53E1DF8FAAE83188752902264C3B3F599493D65535E9734AD0BF9C9CE49ABFE840A86948028C4AB827E87E437B6CBDDDC44DEC91B062C040A501328072AFF9B9FFB46CC680DB4BCA23EF04810E9A16A317E492489C49288CA32A918FAB21613985C9CCF78B0098ADCFF047D294B8768C21A52308F2F7366D8FE12F3C363A8E3A806A2B3FEA98248BF694AEDD45B8001344B97314354B36CCC70EB0CE7ADBD25FFAC76AD8C1614673221CD0B9FB89B1600176D6DFAED8477D58D74B8FAC246E45EE196D1A6039D98589061CD2B7228E2316E156376C00735744CC03473260A7C6CDFBE3E94E70609BE3C0E50F4FA61B8B51555E5C4A2029A1FDC1AF580828E7340D60316508363BFA83D37CFB0AE843EABC2333B082D700EA1F82711F1725E292B069D5EDDA19C7A26838609E96BFA732CF3176ABEDF82C0DD6C3DF27A6C0F60F1B9EBCDB9ABC86CF5389673A18AF99"

#oracle_modulus = "D4AC36C6DB894E75C241CB5253455D66CBCFAFAF4A6EFA15288E1282F53787CDDB0971B77E13B15793E1BC357B455D57326A4CDEFDFE436C4718769D2620DD26D1F8FA56E93A162E74242BB1ED3799F94B8DF6023F6D7172F830E584E8905499E699829EE20B62DF751B22492671A2670522FEBB0D53E535ABBCAFFDF948BEDF196D4E9B040D0AD49DF1860A0AB78478808CF06A1AD9F04345CB97A361E318FEFAADADBA0E215C191A46CE2FCF90D1A80CDB60805DE9DCAA7B5BD64CE8D71F5ABE57BCD2FF52E271DF7AE47BE597BC21E889DE030F6452518623C50B0EEC91009931945651EE15FA9529B4C746AC0D7E6C783D5F4214E0F074F52B5E984551663294CFC0A091E2C128D8F0C267ABBBC4544284C62333432EEAF54409EEE9481C67CE0543A3AA85A8CE1C16D4222F5BB73EEAC9785DCEDA3DCA4FCB86D1CCFCCFA008F24C78040119B8AC71D72482B1648C670B49308D518662E293D246760DE0FFA0702E0CD6176A2C28CAE2BCA468FC8AB2270081D9F8D2FEB6E1A86669508215DF379DA350C773FD03AF1090F999E91873589AE9B6741EFF4B81F5FF0F2D212F905A8145F99D5E549ABF973740E3E22B5F50C4831247044B220D82825735412945AF3B06247352B29A5ECD36CC3250ECDEDBC21131F93B96DD8317D01F7F56EACF0F1D5EC7EF1A3658A725AD088BC087FCD3AA4ADE64C7D0EB417EA470FAF9"

oracle_modulus = "F4B97B86E7779BF02D1F78B7B8A456F964D49DC474C11DA734B70AE37731B3EBB0C686FE230FD0D5B919F8ACF870DAA0D2C34B676BF9BC8CB12F8C2BD2FEDD89F3E2501FA514C384D2715674B4CC45A6B419185F89D7B8A4CE287785374CBECF45C72E5CA7D83957D6E2EB55B07AE6C2EF40EDCD633C466108B351AA34DB528482958C7394BF9E6F03163AA34FD78EEFCBFFCAE0789B552CB55AA51B872338403CF3337B085C98E0B26B31EEA88610F6BF107FD63C677A745BD5D8F7B9B18E100106205125883B04C6D24AEA3F1E92F00F3457A83DD34CDD24DF3E09250F481CCFFDF022C678161DAEA14B605200B82FE5936D5D9B7A93202937C6E36D147D8CB9CEF83DE484BB69B608E556070D961525BDA0D7B7AE8408530F9BEFBC43D16668F4CFA650CAF4AD4161E4D905370B94702C577865C22DD5825A771C47DCFD9B4F68F6CB2B83CF97E21B6FC6FAF441ADCDA8E5E4AF414AC0FF8CA234F58BDA5AED1BDF839E29A98AC64BA7D2A9815659F987D1ABC4DA10BB5C81D220D13FDAA8EA251C30431AF42792EA1FFF08C7C7D54AFC70EB2F07B5F8DD0C9A705652692112C486ED679E64AED4C3501BEB03556553221D24810BF580BD90B679202E3D43A1ED4D8B8372399872899D7995EEBB325EDDF365C5DF0BF56C12E49EF5639C68EF420D79779CFF6C960569BA78E4964F6F2952E3783D1E2A11753B9CAAF8C2ED"

oracle = {'name':'tlsnotarygroup5',
                "IP":"54.158.251.14",
                "port":"10011",
                'DI':'https://ec2.us-east-1.amazonaws.com/?AWSAccessKeyId=AKIAIHZGACNJKBHFWOTQ&Action=DescribeInstances&Expires=2025-01-01&InstanceId=i-0858c02ad9a33c579&SignatureMethod=HmacSHA256&SignatureVersion=2&Version=2014-10-01&Signature=AWkxF%2FlBVL%2FBl2WhQC62qGJ80qhL%2B%2B%2FJXvSp8mm5sIg%3D',
'DV':'https://ec2.us-east-1.amazonaws.com/?AWSAccessKeyId=AKIAIHZGACNJKBHFWOTQ&Action=DescribeVolumes&Expires=2025-01-01&SignatureMethod=HmacSHA256&SignatureVersion=2&Version=2014-10-01&VolumeId=vol-056223d4e1ce55d9c&Signature=DCYnV1vNqE3cyTm6bmtNS1idGdBT7DcbeLtZfcm3ljo%3D',
'GCO':'https://ec2.us-east-1.amazonaws.com/?AWSAccessKeyId=AKIAIHZGACNJKBHFWOTQ&Action=GetConsoleOutput&Expires=2025-01-01&InstanceId=i-0858c02ad9a33c579&SignatureMethod=HmacSHA256&SignatureVersion=2&Version=2014-10-01&Signature=I%2F1kp7oSli9GvYrrP5HD52D6nOy7yCq9dowaDomSAOQ%3D',
'GU':'https://iam.amazonaws.com/?AWSAccessKeyId=AKIAIHZGACNJKBHFWOTQ&Action=GetUser&Expires=2025-01-01&SignatureMethod=HmacSHA256&SignatureVersion=2&Version=2010-05-08&Signature=N%2BsdNA6z3QReVsHsf7RV4uZLzS5Pqi0n3QSfqBAMs8o%3D',
'DIA':'https://ec2.us-east-1.amazonaws.com/?AWSAccessKeyId=AKIAIHZGACNJKBHFWOTQ&Action=DescribeInstanceAttribute&Attribute=userData&Expires=2025-01-01&InstanceId=i-0858c02ad9a33c579&SignatureMethod=HmacSHA256&SignatureVersion=2&Version=2014-10-01&Signature=ENM%2Bw9WkB4U4kYDMN6kowJhZenuCEX3c1G7xSuu6GZA%3D',
                'instanceId': 'i-0858c02ad9a33c579',
                "modulus":[186,187,68,57,92,215,243,62,188,248,16,13,3,29,40,217,208,206,78,13,202,184,82,121,26,51,203,41,169,11,4,102,228,127,110,117,170,48,210,212,160,51,175,246,110,178,43,106,94,255,69,0,217,91,225,7,84,133,193,43,177,254,75,191,109,50,212,190,177,61,64,230,188,105,56,252,40,3,91,190,117,1,52,30,210,137,136,13,216,110,83,21,164,56,248,215,33,159,129,149,85,236,130,194,79,227,184,135,133,61,85,201,243,225,121,233,36,84,207,218,86,68,99,21,150,252,28,220,4,93,81,57,214,94,147,56,234,236,0,178,93,39,48,143,21,120,241,33,73,239,185,255,255,79,112,194,72,226,84,158,182,96,159,33,111,57,212,27,23,133,223,152,101,240,98,181,94,38,147,195,187,245,226,158,11,102,91,91,47,146,178,65,180,73,176,209,32,27,99,183,254,161,115,38,186,31,132,165,252,189,226,72,152,219,177,52,47,178,121,45,30,143,78,142,223,133,112,136,72,165,166,225,18,62,249,119,157,198,68,114,69,199,32,121,201,72,159,13,37,66,160,210,83,163,131,128,54,178,219,5,74,94,214,244,43,123,140,156,192,89,120,211,61,192,76,70,176,122,247,198,21,220,79,212,200,192,88,126,200,115,71,102,66,92,102,60,179,213,125,123,86,195,67,204,71,222,249,46,242,179,11,111,12,158,91,189,215,72,190,15,165,11,102,51,1,91,116,127,31,12,55,193,249,170,15,231,13,189,60,73,8,239,238,18,44,131,78,190,164,46,41,169,139,43,230,105,2,170,231,202,203,126,74,202,172,112,217,194,26,202,140,71,183,45,239,213,254,213,139,27,95,163,172,27,176,189,233,59,181,49,225,220,125,90,182,120,183,236,62,100,170,130,122,202,206,193,77,130,250,167,187,238,39,197,216,183,56,203,72,122,168,64,217,225,8,233,13,164,224,23,255,239,230,44,90,31,149,106,207,28,9,249,154,163,84,231,149,167,59,194,193,41,106,239,30,137,188,78,45,66,30,224,233,181,132,146,106,227,135,229,106,71,168,69,149,167,154,150,106,29,130,114,109,11,66,120,42,128,247,166,248,152,103,131,56,88,37,46,19,240,110,135,15,234,44,39,87,65,232,105,2,163]
}


def get_xhr(url):
    xml = urlopen(url).read()
    return minidom.parseString(xml)

def getChildNodes(x):
    return [a for a in x[0].childNodes if not a.nodeName=='#text']

#assuming both events happened on the same day, get the time
#difference between them in seconds
#the time string looks like "2015-04-15T19:00:59.000Z"
def getSecondsDelta (later, sooner):
    assert (len(later) == 24)
    if (later[:11] != sooner[:11]):
      return 999999; #not on the same day
    laterTime = later[11:19].split(':')
    soonerTime = sooner[11:19].split(':')
    laterSecs = int(laterTime[0])*3600+int(laterTime[1])*60+int(laterTime[2])
    soonerSecs = int(soonerTime[0])*3600+int(soonerTime[1])*60+int(soonerTime[2])
    return laterSecs - soonerSecs


def modulus_from_pubkey(pem_pubkey):
    b64_str = ''
    lines = pem_pubkey.split('\n')
    #omit header and footer lines
    for i in range(1,len(lines)-1):
        b64_str += lines[i]
    der = b64decode(b64_str)
    #last 5 bytes are 2 DER bytes and 3 bytes exponent, our pubkey is the preceding 512 bytes
    pubkey = der[len(der)-517:len(der)-5]
    return pubkey

def checkDescribeInstances(xmlDoc, instanceId, IP):
  try:
    rs = xmlDoc.getElementsByTagName('reservationSet')
    assert rs.length == 1
    rs_items = getChildNodes(rs)
    assert len(rs_items) == 1
    ownerId = rs_items[0].getElementsByTagName('ownerId')[0].firstChild.data
    isets = rs_items[0].getElementsByTagName('instancesSet')
    assert isets.length == 1
    instances = getChildNodes(isets)
    assert len(instances) == 1
    parent = instances[0]
    assert parent.getElementsByTagName('instanceId')[0].firstChild.data == instanceId
    assert parent.getElementsByTagName('imageId')[0].firstChild.data == imageID
    assert parent.getElementsByTagName('instanceState')[0].getElementsByTagName('name')[0].firstChild.data == 'running'
    launchTime = parent.getElementsByTagName('launchTime')[0].firstChild.data
    assert parent.getElementsByTagName('ipAddress')[0].firstChild.data == IP
    assert parent.getElementsByTagName('rootDeviceType')[0].firstChild.data == 'ebs'
    assert parent.getElementsByTagName('rootDeviceName')[0].firstChild.data == '/dev/xvda'
    devices = parent.getElementsByTagName('blockDeviceMapping')[0].getElementsByTagName('item')
    assert devices.length == 1
    assert devices[0].getElementsByTagName('deviceName')[0].firstChild.data == '/dev/xvda'
    assert devices[0].getElementsByTagName('ebs')[0].getElementsByTagName('status')[0].firstChild.data == 'attached'
    volAttachTime = devices[0].getElementsByTagName('ebs')[0].getElementsByTagName('attachTime')[0].firstChild.data
    volumeId = devices[0].getElementsByTagName('ebs')[0].getElementsByTagName('volumeId')[0].firstChild.data
    #get seconds from "2015-04-15T19:00:59.000Z"
    assert getSecondsDelta(volAttachTime, launchTime) <= 3
    assert parent.getElementsByTagName('virtualizationType')[0].firstChild.data == 'hvm'
    return {'ownerId':ownerId, 'volumeId':volumeId, 'volAttachTime':volAttachTime, 'launchTime':launchTime}
  except:
    return False


def checkDescribeVolumes(xmlDoc, instanceId, volumeId, volAttachTime):
  try:
    v = xmlDoc.getElementsByTagName('volumeSet')
    volumes = getChildNodes(v)
    assert len(volumes) == 1
    volume = volumes[0]
    assert volume.getElementsByTagName('volumeId')[0].firstChild.data == volumeId
    assert volume.getElementsByTagName('snapshotId')[0].firstChild.data == snapshotID
    assert volume.getElementsByTagName('status')[0].firstChild.data == 'in-use'
    volCreateTime = volume.getElementsByTagName('createTime')[0].firstChild.data
    attVolumes = volume.getElementsByTagName('attachmentSet')[0].getElementsByTagName('item')
    assert attVolumes.length == 1
    attVolume = attVolumes[0];
    assert attVolume.getElementsByTagName('volumeId')[0].firstChild.data == volumeId
    assert attVolume.getElementsByTagName('instanceId')[0].firstChild.data == instanceId
    assert attVolume.getElementsByTagName('device')[0].firstChild.data == '/dev/xvda'
    assert attVolume.getElementsByTagName('status')[0].firstChild.data == 'attached'
    attTime = attVolume.getElementsByTagName('attachTime')[0].firstChild.data
    assert volAttachTime == attTime
    #Crucial: volume was created from snapshot and attached at the same instant
    #this guarantees that there was no time window to modify it
    assert getSecondsDelta(attTime, volCreateTime) == 0
    return True
  except:
    return False



def checkGetConsoleOutput(xmlDoc, instanceId, launchTime):
  try:
    assert xmlDoc.getElementsByTagName('instanceId')[0].firstChild.data == instanceId
    timestamp = xmlDoc.getElementsByTagName('timestamp')[0].firstChild.data
    #prevent funny business: last consoleLog entry no later than 5 minutes after instance starts
    assert getSecondsDelta(timestamp, launchTime) <= 300
    b64data = xmlDoc.getElementsByTagName('output')[0].firstChild.data
    logstr = b64decode(b64data)
    sigmark = 'PageSigner public key for verification'
    pkstartmark = '-----BEGIN PUBLIC KEY-----'
    pkendmark = '-----END PUBLIC KEY-----'

    mark_start = logstr.index(sigmark)
    assert mark_start != -1
    pubkhey_start = mark_start + logstr[mark_start:].index(pkstartmark)
    pubkey_end = pubkey_start+ logstr[pubkey_start:].index(pkendmark) + len(pkendmark)
    pk = logstr[pubkey_start:pubkey_end]
    assert len(pk) > 0
    return pk
  except:
    return False




# "userData" allows to pass an arbitrary script to the instance at launch. It MUST be empty.
# This is a sanity check because the instance is stripped of the code which parses userData.
def checkDescribeInstanceAttribute(xmlDoc, instanceId):
  try:
    assert xmlDoc.getElementsByTagName('instanceId')[0].firstChild.data == instanceId
    assert not xmlDoc.getElementsByTagName('userData')[0].firstChild
    return True
  except:
    return False

def checkGetUser(xmlDoc, ownerId):
    #try:
    assert xmlDoc.getElementsByTagName('UserId')[0].firstChild.data == ownerId
    assert xmlDoc.getElementsByTagName('Arn')[0].firstChild.data[-(len(ownerId) + len(':root')):] == ownerId+':root'
    #except:
    #return False
    return True

def check_oracle(o):
    print ('Verifying PageSigner AWS oracle server, this may take up to a minute...')
    xmlDoc = get_xhr(o['DI'])
    CDIresult = checkDescribeInstances(xmlDoc, o['instanceId'], o['IP'])
    if not CDIresult:
      raise Exception('checkDescribeInstances')
    print ('check 1 of 5 successful')
    
    xmlDoc = get_xhr(o['DV'])
    CDVresult = checkDescribeVolumes(xmlDoc, o['instanceId'], CDIresult['volumeId'], CDIresult['volAttachTime'])
    if not CDVresult:
      raise Exception('checkDescribeVolumes')
    print ('check 2 of 5 successful')
    
    xmlDoc = get_xhr(o['GU'])
    CGUresult = checkGetUser(xmlDoc, CDIresult['ownerId'])
    if not CGUresult:
      raise Exception('checkGetUser')
    print ('check 3 of 5 successful')
    
    xmlDoc = get_xhr(o['GCO'])
    GCOresult = checkGetConsoleOutput(xmlDoc, o['instanceId'], CDIresult['launchTime'])
    if not GCOresult:
      raise Exception('checkGetConsoleOutput')
    print ('check 4 of 5 successful')
    
    sigmod_binary = bytearray('').join(map(chr,o['modulus']))
    if modulus_from_pubkey(GCOresult) != sigmod_binary:
      raise Exception("modulus from pubkey")

    xmlDoc = get_xhr(o['DIA'])
    DIAresult = checkDescribeInstanceAttribute(xmlDoc, o['instanceId'])
    if not DIAresult:
      raise Exception('checkDescribeInstanceAttribute')
    print ('check 5 of 5 successful')
     
    mark = 'AWSAccessKeyId=';
    ids = [];
    #"AWSAccessKeyId" should be the same to prove that the queries are made on behalf of AWS user "root".
    #The attacker can be a user with limited privileges for whom the API would report only partial information.
    for url in [o['DI'], o['DV'], o['GU'], o['GCO'], o['DIA']]:
      start = url.index(mark)+len(mark);
      ids.append(url[start:start + url[start:].index('&')])
    assert len(set(ids)) == 1
    print('oracle verification successfully finished')
