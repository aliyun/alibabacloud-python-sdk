# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainSpecialBizInfoByDomainResponseBody(DaraModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        synchro: bool = None,
    ):
        # Indicates whether retries are allowed.
        self.allow_retry = allow_retry
        # The name of the application for which the error code is returned.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The array of error parameters that are returned.
        self.error_args = error_args
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code that is directly returned.
        self.http_status_code = http_status_code
        # The returned data.
        self.module = module
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false
        self.success = success
        # Indicates whether to perform synchronous processing.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Module') is not None:
            temp_model = main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class QueryDomainSpecialBizInfoByDomainResponseBodyModule(DaraModel):
    def __init__(
        self,
        audit_msg: str = None,
        biz_name: str = None,
        biz_no: str = None,
        biz_status: str = None,
        biz_type: str = None,
        create_time: int = None,
        domain_name: str = None,
        domain_special_biz_contact: main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizContact = None,
        domain_special_biz_credentials: List[main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizCredentials] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        order_id: str = None,
        product_id: str = None,
        sale_id: str = None,
        status: int = None,
        status_desc: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The review information.
        self.audit_msg = audit_msg
        # The business name.
        self.biz_name = biz_name
        # The business ID.
        self.biz_no = biz_no
        # The business status.
        self.biz_status = biz_status
        # The business type.
        self.biz_type = biz_type
        # The time when the business was created.
        self.create_time = create_time
        # The domain name.
        self.domain_name = domain_name
        # The contact information.
        self.domain_special_biz_contact = domain_special_biz_contact
        # The certificate information.
        self.domain_special_biz_credentials = domain_special_biz_credentials
        # The time when the business was created.
        self.gmt_create = gmt_create
        # The time when the business was modified.
        self.gmt_modified = gmt_modified
        # The primary key.
        self.id = id
        # The order ID.
        self.order_id = order_id
        # The service ID.
        self.product_id = product_id
        # The instance ID.
        self.sale_id = sale_id
        # The business status.
        self.status = status
        # The description of business status.
        self.status_desc = status_desc
        # The time when the business was updated.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.domain_special_biz_contact:
            self.domain_special_biz_contact.validate()
        if self.domain_special_biz_credentials:
            for v1 in self.domain_special_biz_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_msg is not None:
            result['AuditMsg'] = self.audit_msg

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.biz_no is not None:
            result['BizNo'] = self.biz_no

        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_special_biz_contact is not None:
            result['DomainSpecialBizContact'] = self.domain_special_biz_contact.to_map()

        result['DomainSpecialBizCredentials'] = []
        if self.domain_special_biz_credentials is not None:
            for k1 in self.domain_special_biz_credentials:
                result['DomainSpecialBizCredentials'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMsg') is not None:
            self.audit_msg = m.get('AuditMsg')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('BizNo') is not None:
            self.biz_no = m.get('BizNo')

        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainSpecialBizContact') is not None:
            temp_model = main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizContact()
            self.domain_special_biz_contact = temp_model.from_map(m.get('DomainSpecialBizContact'))

        self.domain_special_biz_credentials = []
        if m.get('DomainSpecialBizCredentials') is not None:
            for k1 in m.get('DomainSpecialBizCredentials'):
                temp_model = main_models.QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizCredentials()
                self.domain_special_biz_credentials.append(temp_model.from_map(k1))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizCredentials(DaraModel):
    def __init__(
        self,
        biz_id: int = None,
        credential_no: str = None,
        credential_type: str = None,
        credential_url: str = None,
        domain_name: str = None,
        holder_cert: int = None,
        sale_id: str = None,
    ):
        # The ID of the associated workflow.
        self.biz_id = biz_id
        # The certificate number.
        self.credential_no = credential_no
        # The certificate type.
        self.credential_type = credential_type
        # The certificate URL.
        self.credential_url = credential_url
        # The domain name.
        self.domain_name = domain_name
        # Indicates whether the certificate belongs to the registrant.
        self.holder_cert = holder_cert
        # The instance ID.
        self.sale_id = sale_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.credential_url is not None:
            result['CredentialUrl'] = self.credential_url

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.holder_cert is not None:
            result['HolderCert'] = self.holder_cert

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('CredentialUrl') is not None:
            self.credential_url = m.get('CredentialUrl')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('HolderCert') is not None:
            self.holder_cert = m.get('HolderCert')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        return self

class QueryDomainSpecialBizInfoByDomainResponseBodyModuleDomainSpecialBizContact(DaraModel):
    def __init__(
        self,
        biz_id: int = None,
        ccity: str = None,
        ccompany: str = None,
        ccountry: str = None,
        cname: str = None,
        cprovince: str = None,
        cvenu: str = None,
        ecity: str = None,
        ecompany: str = None,
        ename: str = None,
        eprovince: str = None,
        evenu: str = None,
        email: str = None,
        extend: str = None,
        fax_area: str = None,
        fax_ext: str = None,
        fax_main: str = None,
        mobile: str = None,
        postalcode: str = None,
        reg_type: int = None,
        registrant_id: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        tel_main: str = None,
        vsp_contact_id: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The city.
        self.ccity = ccity
        # The organization name.
        self.ccompany = ccompany
        # The country code.
        self.ccountry = ccountry
        # The contact name.
        self.cname = cname
        # The province.
        self.cprovince = cprovince
        # The address.
        self.cvenu = cvenu
        # The city in English.
        self.ecity = ecity
        # The organization name in English.
        self.ecompany = ecompany
        # The contact name in English.
        self.ename = ename
        # The province in English.
        self.eprovince = eprovince
        # The address in English.
        self.evenu = evenu
        # The email address.
        self.email = email
        # The extended information.
        self.extend = extend
        # The fax country code.
        self.fax_area = fax_area
        # The fax extension number.
        self.fax_ext = fax_ext
        # The fax number with an area code or mobile number.
        self.fax_main = fax_main
        # The mobile number.
        self.mobile = mobile
        # The zip code.
        self.postalcode = postalcode
        # The contact type. Valid values: 1: individual. 2: enterprise.
        self.reg_type = reg_type
        # The registrant ID.
        self.registrant_id = registrant_id
        # The calling code of the country or region where the domain name contact is located.
        self.tel_area = tel_area
        # The telephone extension number.
        self.tel_ext = tel_ext
        # The landline number with an area code or mobile number.
        self.tel_main = tel_main
        # The VSP contact ID.
        self.vsp_contact_id = vsp_contact_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.ccity is not None:
            result['CCity'] = self.ccity

        if self.ccompany is not None:
            result['CCompany'] = self.ccompany

        if self.ccountry is not None:
            result['CCountry'] = self.ccountry

        if self.cname is not None:
            result['CName'] = self.cname

        if self.cprovince is not None:
            result['CProvince'] = self.cprovince

        if self.cvenu is not None:
            result['CVenu'] = self.cvenu

        if self.ecity is not None:
            result['ECity'] = self.ecity

        if self.ecompany is not None:
            result['ECompany'] = self.ecompany

        if self.ename is not None:
            result['EName'] = self.ename

        if self.eprovince is not None:
            result['EProvince'] = self.eprovince

        if self.evenu is not None:
            result['EVenu'] = self.evenu

        if self.email is not None:
            result['Email'] = self.email

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.fax_area is not None:
            result['FaxArea'] = self.fax_area

        if self.fax_ext is not None:
            result['FaxExt'] = self.fax_ext

        if self.fax_main is not None:
            result['FaxMain'] = self.fax_main

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.postalcode is not None:
            result['Postalcode'] = self.postalcode

        if self.reg_type is not None:
            result['RegType'] = self.reg_type

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.tel_main is not None:
            result['TelMain'] = self.tel_main

        if self.vsp_contact_id is not None:
            result['VspContactId'] = self.vsp_contact_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CCity') is not None:
            self.ccity = m.get('CCity')

        if m.get('CCompany') is not None:
            self.ccompany = m.get('CCompany')

        if m.get('CCountry') is not None:
            self.ccountry = m.get('CCountry')

        if m.get('CName') is not None:
            self.cname = m.get('CName')

        if m.get('CProvince') is not None:
            self.cprovince = m.get('CProvince')

        if m.get('CVenu') is not None:
            self.cvenu = m.get('CVenu')

        if m.get('ECity') is not None:
            self.ecity = m.get('ECity')

        if m.get('ECompany') is not None:
            self.ecompany = m.get('ECompany')

        if m.get('EName') is not None:
            self.ename = m.get('EName')

        if m.get('EProvince') is not None:
            self.eprovince = m.get('EProvince')

        if m.get('EVenu') is not None:
            self.evenu = m.get('EVenu')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('FaxArea') is not None:
            self.fax_area = m.get('FaxArea')

        if m.get('FaxExt') is not None:
            self.fax_ext = m.get('FaxExt')

        if m.get('FaxMain') is not None:
            self.fax_main = m.get('FaxMain')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Postalcode') is not None:
            self.postalcode = m.get('Postalcode')

        if m.get('RegType') is not None:
            self.reg_type = m.get('RegType')

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('TelMain') is not None:
            self.tel_main = m.get('TelMain')

        if m.get('VspContactId') is not None:
            self.vsp_contact_id = m.get('VspContactId')

        return self

