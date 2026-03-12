# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveContactTemplateRequest(DaraModel):
    def __init__(
        self,
        ccity: str = None,
        ccompany: str = None,
        ccountry: str = None,
        cname: str = None,
        cprovince: str = None,
        cvenu: str = None,
        contact_template_id: int = None,
        default_template: bool = None,
        ecity: str = None,
        ecompany: str = None,
        ename: str = None,
        eprovince: str = None,
        evenu: str = None,
        email: str = None,
        lang: str = None,
        postal_code: str = None,
        reg_type: str = None,
        tel_area: str = None,
        tel_ext: str = None,
        tel_main: str = None,
        user_client_ip: str = None,
    ):
        self.ccity = ccity
        self.ccompany = ccompany
        self.ccountry = ccountry
        self.cname = cname
        self.cprovince = cprovince
        self.cvenu = cvenu
        self.contact_template_id = contact_template_id
        self.default_template = default_template
        self.ecity = ecity
        self.ecompany = ecompany
        self.ename = ename
        self.eprovince = eprovince
        self.evenu = evenu
        self.email = email
        self.lang = lang
        self.postal_code = postal_code
        self.reg_type = reg_type
        self.tel_area = tel_area
        self.tel_ext = tel_ext
        self.tel_main = tel_main
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.lang is not None:
            result['Lang'] = self.lang

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

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

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

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

