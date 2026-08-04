# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAccountProfileInfoResponseBody(DaraModel):
    def __init__(
        self,
        profile_info: main_models.QueryAccountProfileInfoResponseBodyProfileInfo = None,
        request_id: str = None,
    ):
        self.profile_info = profile_info
        self.request_id = request_id

    def validate(self):
        if self.profile_info:
            self.profile_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.profile_info is not None:
            result['ProfileInfo'] = self.profile_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProfileInfo') is not None:
            temp_model = main_models.QueryAccountProfileInfoResponseBodyProfileInfo()
            self.profile_info = temp_model.from_map(m.get('ProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAccountProfileInfoResponseBodyProfileInfo(DaraModel):
    def __init__(
        self,
        account_attr: str = None,
        account_certify_type: str = None,
        active_not_set_mobile: str = None,
        address: str = None,
        address_2: str = None,
        address_3: str = None,
        address_4: str = None,
        address_5: str = None,
        address_6: str = None,
        alipay_account: str = None,
        alipay_uid: str = None,
        aliyun_id: str = None,
        aliyun_pk: str = None,
        auth_alipay: str = None,
        auth_domain_user_id: str = None,
        b_2bhid: str = None,
        bank_id: str = None,
        bank_name: str = None,
        bei_an_auth_cid: str = None,
        bei_an_icp_number: str = None,
        bei_an_mobile: str = None,
        bind_alipay_no: str = None,
        cert_type: str = None,
        certified_from: str = None,
        certified_time: str = None,
        city: main_models.QueryAccountProfileInfoResponseBodyProfileInfoCity = None,
        contact_method: str = None,
        create_time: str = None,
        district: main_models.QueryAccountProfileInfoResponseBodyProfileInfoDistrict = None,
        eid: str = None,
        email: str = None,
        fax: str = None,
        first_name: str = None,
        fyl: str = None,
        havana_id: str = None,
        head: str = None,
        head_url: str = None,
        idnumber: str = None,
        is_bank_idauth: str = None,
        is_certified: str = None,
        last_name: str = None,
        mobile: str = None,
        nationality_code: str = None,
        nick_name: str = None,
        own: str = None,
        phone: str = None,
        post_code: str = None,
        preferred_language: str = None,
        processing_enterprise_certify: bool = None,
        province: main_models.QueryAccountProfileInfoResponseBodyProfileInfoProvince = None,
        register_ip: str = None,
        security_mobile: str = None,
        security_question_exists: bool = None,
        self_servicing_business_reg_num: str = None,
        self_servicing_identification_num: str = None,
        show_nick_name: str = None,
        src: str = None,
        taobao_account: str = None,
        taobao_nick_from_havana: str = None,
        tbhid: str = None,
        true_name: str = None,
        update_time: str = None,
        yahoo_email: str = None,
    ):
        self.account_attr = account_attr
        self.account_certify_type = account_certify_type
        self.active_not_set_mobile = active_not_set_mobile
        self.address = address
        self.address_2 = address_2
        self.address_3 = address_3
        self.address_4 = address_4
        self.address_5 = address_5
        self.address_6 = address_6
        self.alipay_account = alipay_account
        self.alipay_uid = alipay_uid
        self.aliyun_id = aliyun_id
        self.aliyun_pk = aliyun_pk
        self.auth_alipay = auth_alipay
        self.auth_domain_user_id = auth_domain_user_id
        self.b_2bhid = b_2bhid
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.bei_an_auth_cid = bei_an_auth_cid
        self.bei_an_icp_number = bei_an_icp_number
        self.bei_an_mobile = bei_an_mobile
        self.bind_alipay_no = bind_alipay_no
        self.cert_type = cert_type
        self.certified_from = certified_from
        self.certified_time = certified_time
        self.city = city
        self.contact_method = contact_method
        self.create_time = create_time
        self.district = district
        self.eid = eid
        self.email = email
        self.fax = fax
        self.first_name = first_name
        self.fyl = fyl
        self.havana_id = havana_id
        self.head = head
        self.head_url = head_url
        self.idnumber = idnumber
        self.is_bank_idauth = is_bank_idauth
        self.is_certified = is_certified
        self.last_name = last_name
        self.mobile = mobile
        self.nationality_code = nationality_code
        self.nick_name = nick_name
        self.own = own
        self.phone = phone
        self.post_code = post_code
        self.preferred_language = preferred_language
        self.processing_enterprise_certify = processing_enterprise_certify
        self.province = province
        self.register_ip = register_ip
        self.security_mobile = security_mobile
        self.security_question_exists = security_question_exists
        self.self_servicing_business_reg_num = self_servicing_business_reg_num
        self.self_servicing_identification_num = self_servicing_identification_num
        self.show_nick_name = show_nick_name
        self.src = src
        self.taobao_account = taobao_account
        self.taobao_nick_from_havana = taobao_nick_from_havana
        self.tbhid = tbhid
        self.true_name = true_name
        self.update_time = update_time
        self.yahoo_email = yahoo_email

    def validate(self):
        if self.city:
            self.city.validate()
        if self.district:
            self.district.validate()
        if self.province:
            self.province.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_attr is not None:
            result['AccountAttr'] = self.account_attr

        if self.account_certify_type is not None:
            result['AccountCertifyType'] = self.account_certify_type

        if self.active_not_set_mobile is not None:
            result['ActiveNotSetMobile'] = self.active_not_set_mobile

        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.address_3 is not None:
            result['Address3'] = self.address_3

        if self.address_4 is not None:
            result['Address4'] = self.address_4

        if self.address_5 is not None:
            result['Address5'] = self.address_5

        if self.address_6 is not None:
            result['Address6'] = self.address_6

        if self.alipay_account is not None:
            result['AlipayAccount'] = self.alipay_account

        if self.alipay_uid is not None:
            result['AlipayUid'] = self.alipay_uid

        if self.aliyun_id is not None:
            result['AliyunID'] = self.aliyun_id

        if self.aliyun_pk is not None:
            result['AliyunPK'] = self.aliyun_pk

        if self.auth_alipay is not None:
            result['AuthAlipay'] = self.auth_alipay

        if self.auth_domain_user_id is not None:
            result['AuthDomainUserId'] = self.auth_domain_user_id

        if self.b_2bhid is not None:
            result['B2bhid'] = self.b_2bhid

        if self.bank_id is not None:
            result['BankId'] = self.bank_id

        if self.bank_name is not None:
            result['BankName'] = self.bank_name

        if self.bei_an_auth_cid is not None:
            result['BeiAnAuthCId'] = self.bei_an_auth_cid

        if self.bei_an_icp_number is not None:
            result['BeiAnIcpNumber'] = self.bei_an_icp_number

        if self.bei_an_mobile is not None:
            result['BeiAnMobile'] = self.bei_an_mobile

        if self.bind_alipay_no is not None:
            result['BindAlipayNo'] = self.bind_alipay_no

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certified_from is not None:
            result['CertifiedFrom'] = self.certified_from

        if self.certified_time is not None:
            result['CertifiedTime'] = self.certified_time

        if self.city is not None:
            result['City'] = self.city.to_map()

        if self.contact_method is not None:
            result['ContactMethod'] = self.contact_method

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.district is not None:
            result['District'] = self.district.to_map()

        if self.eid is not None:
            result['Eid'] = self.eid

        if self.email is not None:
            result['Email'] = self.email

        if self.fax is not None:
            result['Fax'] = self.fax

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.fyl is not None:
            result['Fyl'] = self.fyl

        if self.havana_id is not None:
            result['HavanaId'] = self.havana_id

        if self.head is not None:
            result['Head'] = self.head

        if self.head_url is not None:
            result['HeadUrl'] = self.head_url

        if self.idnumber is not None:
            result['IDNumber'] = self.idnumber

        if self.is_bank_idauth is not None:
            result['IsBankIDAuth'] = self.is_bank_idauth

        if self.is_certified is not None:
            result['IsCertified'] = self.is_certified

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nationality_code is not None:
            result['NationalityCode'] = self.nationality_code

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.own is not None:
            result['Own'] = self.own

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.preferred_language is not None:
            result['PreferredLanguage'] = self.preferred_language

        if self.processing_enterprise_certify is not None:
            result['ProcessingEnterpriseCertify'] = self.processing_enterprise_certify

        if self.province is not None:
            result['Province'] = self.province.to_map()

        if self.register_ip is not None:
            result['RegisterIP'] = self.register_ip

        if self.security_mobile is not None:
            result['SecurityMobile'] = self.security_mobile

        if self.security_question_exists is not None:
            result['SecurityQuestionExists'] = self.security_question_exists

        if self.self_servicing_business_reg_num is not None:
            result['SelfServicingBusinessRegNum'] = self.self_servicing_business_reg_num

        if self.self_servicing_identification_num is not None:
            result['SelfServicingIdentificationNum'] = self.self_servicing_identification_num

        if self.show_nick_name is not None:
            result['ShowNickName'] = self.show_nick_name

        if self.src is not None:
            result['Src'] = self.src

        if self.taobao_account is not None:
            result['TaobaoAccount'] = self.taobao_account

        if self.taobao_nick_from_havana is not None:
            result['TaobaoNickFromHavana'] = self.taobao_nick_from_havana

        if self.tbhid is not None:
            result['Tbhid'] = self.tbhid

        if self.true_name is not None:
            result['TrueName'] = self.true_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.yahoo_email is not None:
            result['YahooEmail'] = self.yahoo_email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAttr') is not None:
            self.account_attr = m.get('AccountAttr')

        if m.get('AccountCertifyType') is not None:
            self.account_certify_type = m.get('AccountCertifyType')

        if m.get('ActiveNotSetMobile') is not None:
            self.active_not_set_mobile = m.get('ActiveNotSetMobile')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('Address3') is not None:
            self.address_3 = m.get('Address3')

        if m.get('Address4') is not None:
            self.address_4 = m.get('Address4')

        if m.get('Address5') is not None:
            self.address_5 = m.get('Address5')

        if m.get('Address6') is not None:
            self.address_6 = m.get('Address6')

        if m.get('AlipayAccount') is not None:
            self.alipay_account = m.get('AlipayAccount')

        if m.get('AlipayUid') is not None:
            self.alipay_uid = m.get('AlipayUid')

        if m.get('AliyunID') is not None:
            self.aliyun_id = m.get('AliyunID')

        if m.get('AliyunPK') is not None:
            self.aliyun_pk = m.get('AliyunPK')

        if m.get('AuthAlipay') is not None:
            self.auth_alipay = m.get('AuthAlipay')

        if m.get('AuthDomainUserId') is not None:
            self.auth_domain_user_id = m.get('AuthDomainUserId')

        if m.get('B2bhid') is not None:
            self.b_2bhid = m.get('B2bhid')

        if m.get('BankId') is not None:
            self.bank_id = m.get('BankId')

        if m.get('BankName') is not None:
            self.bank_name = m.get('BankName')

        if m.get('BeiAnAuthCId') is not None:
            self.bei_an_auth_cid = m.get('BeiAnAuthCId')

        if m.get('BeiAnIcpNumber') is not None:
            self.bei_an_icp_number = m.get('BeiAnIcpNumber')

        if m.get('BeiAnMobile') is not None:
            self.bei_an_mobile = m.get('BeiAnMobile')

        if m.get('BindAlipayNo') is not None:
            self.bind_alipay_no = m.get('BindAlipayNo')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertifiedFrom') is not None:
            self.certified_from = m.get('CertifiedFrom')

        if m.get('CertifiedTime') is not None:
            self.certified_time = m.get('CertifiedTime')

        if m.get('City') is not None:
            temp_model = main_models.QueryAccountProfileInfoResponseBodyProfileInfoCity()
            self.city = temp_model.from_map(m.get('City'))

        if m.get('ContactMethod') is not None:
            self.contact_method = m.get('ContactMethod')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('District') is not None:
            temp_model = main_models.QueryAccountProfileInfoResponseBodyProfileInfoDistrict()
            self.district = temp_model.from_map(m.get('District'))

        if m.get('Eid') is not None:
            self.eid = m.get('Eid')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Fax') is not None:
            self.fax = m.get('Fax')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('Fyl') is not None:
            self.fyl = m.get('Fyl')

        if m.get('HavanaId') is not None:
            self.havana_id = m.get('HavanaId')

        if m.get('Head') is not None:
            self.head = m.get('Head')

        if m.get('HeadUrl') is not None:
            self.head_url = m.get('HeadUrl')

        if m.get('IDNumber') is not None:
            self.idnumber = m.get('IDNumber')

        if m.get('IsBankIDAuth') is not None:
            self.is_bank_idauth = m.get('IsBankIDAuth')

        if m.get('IsCertified') is not None:
            self.is_certified = m.get('IsCertified')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('NationalityCode') is not None:
            self.nationality_code = m.get('NationalityCode')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Own') is not None:
            self.own = m.get('Own')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('PreferredLanguage') is not None:
            self.preferred_language = m.get('PreferredLanguage')

        if m.get('ProcessingEnterpriseCertify') is not None:
            self.processing_enterprise_certify = m.get('ProcessingEnterpriseCertify')

        if m.get('Province') is not None:
            temp_model = main_models.QueryAccountProfileInfoResponseBodyProfileInfoProvince()
            self.province = temp_model.from_map(m.get('Province'))

        if m.get('RegisterIP') is not None:
            self.register_ip = m.get('RegisterIP')

        if m.get('SecurityMobile') is not None:
            self.security_mobile = m.get('SecurityMobile')

        if m.get('SecurityQuestionExists') is not None:
            self.security_question_exists = m.get('SecurityQuestionExists')

        if m.get('SelfServicingBusinessRegNum') is not None:
            self.self_servicing_business_reg_num = m.get('SelfServicingBusinessRegNum')

        if m.get('SelfServicingIdentificationNum') is not None:
            self.self_servicing_identification_num = m.get('SelfServicingIdentificationNum')

        if m.get('ShowNickName') is not None:
            self.show_nick_name = m.get('ShowNickName')

        if m.get('Src') is not None:
            self.src = m.get('Src')

        if m.get('TaobaoAccount') is not None:
            self.taobao_account = m.get('TaobaoAccount')

        if m.get('TaobaoNickFromHavana') is not None:
            self.taobao_nick_from_havana = m.get('TaobaoNickFromHavana')

        if m.get('Tbhid') is not None:
            self.tbhid = m.get('Tbhid')

        if m.get('TrueName') is not None:
            self.true_name = m.get('TrueName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('YahooEmail') is not None:
            self.yahoo_email = m.get('YahooEmail')

        return self

class QueryAccountProfileInfoResponseBodyProfileInfoProvince(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryAccountProfileInfoResponseBodyProfileInfoDistrict(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryAccountProfileInfoResponseBodyProfileInfoCity(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

