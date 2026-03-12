# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20160511 import models as main_models
from darabonba.model import DaraModel

class QueryContactTemplateResponseBody(DaraModel):
    def __init__(
        self,
        contact_templates: main_models.QueryContactTemplateResponseBodyContactTemplates = None,
        current_page_num: int = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.contact_templates = contact_templates
        self.current_page_num = current_page_num
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.contact_templates:
            self.contact_templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_templates is not None:
            result['ContactTemplates'] = self.contact_templates.to_map()

        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplates') is not None:
            temp_model = main_models.QueryContactTemplateResponseBodyContactTemplates()
            self.contact_templates = temp_model.from_map(m.get('ContactTemplates'))

        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryContactTemplateResponseBodyContactTemplates(DaraModel):
    def __init__(
        self,
        contact_template: List[main_models.QueryContactTemplateResponseBodyContactTemplatesContactTemplate] = None,
    ):
        self.contact_template = contact_template

    def validate(self):
        if self.contact_template:
            for v1 in self.contact_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactTemplate'] = []
        if self.contact_template is not None:
            for k1 in self.contact_template:
                result['ContactTemplate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_template = []
        if m.get('ContactTemplate') is not None:
            for k1 in m.get('ContactTemplate'):
                temp_model = main_models.QueryContactTemplateResponseBodyContactTemplatesContactTemplate()
                self.contact_template.append(temp_model.from_map(k1))

        return self

class QueryContactTemplateResponseBodyContactTemplatesContactTemplate(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        ccity: str = None,
        ccompany: str = None,
        ccountry: str = None,
        cname: str = None,
        cprovince: str = None,
        cvenu: str = None,
        contact_template_id: int = None,
        create_time: str = None,
        default_template: bool = None,
        ecity: str = None,
        ecompany: str = None,
        ename: str = None,
        eprovince: str = None,
        evenu: str = None,
        email: str = None,
        email_verification_status: int = None,
        postal_code: str = None,
        reg_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        tel_main: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.audit_status = audit_status
        self.ccity = ccity
        self.ccompany = ccompany
        self.ccountry = ccountry
        self.cname = cname
        self.cprovince = cprovince
        self.cvenu = cvenu
        self.contact_template_id = contact_template_id
        self.create_time = create_time
        self.default_template = default_template
        self.ecity = ecity
        self.ecompany = ecompany
        self.ename = ename
        self.eprovince = eprovince
        self.evenu = evenu
        self.email = email
        self.email_verification_status = email_verification_status
        self.postal_code = postal_code
        self.reg_type = reg_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.tel_main = tel_main
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

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

        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_template is not None:
            result['DefaultTemplate'] = self.default_template

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

        if self.email_verification_status is not None:
            result['EmailVerificationStatus'] = self.email_verification_status

        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code

        if self.reg_type is not None:
            result['RegType'] = self.reg_type

        if self.tel_area is not None:
            result['TelArea'] = self.tel_area

        if self.tel_ext is not None:
            result['TelExt'] = self.tel_ext

        if self.tel_main is not None:
            result['TelMain'] = self.tel_main

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

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

        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultTemplate') is not None:
            self.default_template = m.get('DefaultTemplate')

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

        if m.get('EmailVerificationStatus') is not None:
            self.email_verification_status = m.get('EmailVerificationStatus')

        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')

        if m.get('RegType') is not None:
            self.reg_type = m.get('RegType')

        if m.get('TelArea') is not None:
            self.tel_area = m.get('TelArea')

        if m.get('TelExt') is not None:
            self.tel_ext = m.get('TelExt')

        if m.get('TelMain') is not None:
            self.tel_main = m.get('TelMain')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

