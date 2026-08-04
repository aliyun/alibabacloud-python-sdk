# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateAccountProfileInfoRequest(DaraModel):
    def __init__(
        self,
        account_attribute: str = None,
        address: str = None,
        address_2: str = None,
        bind_alipay_no: str = None,
        cert_type: str = None,
        city_json_string: Dict[str, Any] = None,
        contact_method: str = None,
        district_json_string: Dict[str, Any] = None,
        fax: str = None,
        first_name: str = None,
        head: str = None,
        head_color: str = None,
        last_name: str = None,
        pk: str = None,
        phone: str = None,
        post_code: str = None,
        province_json_string: Dict[str, Any] = None,
        self_servicing_business_reg_num: str = None,
        self_servicing_identification_num: str = None,
        true_name: str = None,
    ):
        self.account_attribute = account_attribute
        self.address = address
        self.address_2 = address_2
        self.bind_alipay_no = bind_alipay_no
        self.cert_type = cert_type
        self.city_json_string = city_json_string
        self.contact_method = contact_method
        self.district_json_string = district_json_string
        self.fax = fax
        self.first_name = first_name
        self.head = head
        self.head_color = head_color
        self.last_name = last_name
        self.pk = pk
        self.phone = phone
        self.post_code = post_code
        self.province_json_string = province_json_string
        self.self_servicing_business_reg_num = self_servicing_business_reg_num
        self.self_servicing_identification_num = self_servicing_identification_num
        self.true_name = true_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_attribute is not None:
            result['AccountAttribute'] = self.account_attribute

        if self.address is not None:
            result['Address'] = self.address

        if self.address_2 is not None:
            result['Address2'] = self.address_2

        if self.bind_alipay_no is not None:
            result['BindAlipayNo'] = self.bind_alipay_no

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.city_json_string is not None:
            result['CityJsonString'] = self.city_json_string

        if self.contact_method is not None:
            result['ContactMethod'] = self.contact_method

        if self.district_json_string is not None:
            result['DistrictJsonString'] = self.district_json_string

        if self.fax is not None:
            result['Fax'] = self.fax

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.head is not None:
            result['Head'] = self.head

        if self.head_color is not None:
            result['HeadColor'] = self.head_color

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.pk is not None:
            result['PK'] = self.pk

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.post_code is not None:
            result['PostCode'] = self.post_code

        if self.province_json_string is not None:
            result['ProvinceJsonString'] = self.province_json_string

        if self.self_servicing_business_reg_num is not None:
            result['SelfServicingBusinessRegNum'] = self.self_servicing_business_reg_num

        if self.self_servicing_identification_num is not None:
            result['SelfServicingIdentificationNum'] = self.self_servicing_identification_num

        if self.true_name is not None:
            result['TrueName'] = self.true_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAttribute') is not None:
            self.account_attribute = m.get('AccountAttribute')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Address2') is not None:
            self.address_2 = m.get('Address2')

        if m.get('BindAlipayNo') is not None:
            self.bind_alipay_no = m.get('BindAlipayNo')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CityJsonString') is not None:
            self.city_json_string = m.get('CityJsonString')

        if m.get('ContactMethod') is not None:
            self.contact_method = m.get('ContactMethod')

        if m.get('DistrictJsonString') is not None:
            self.district_json_string = m.get('DistrictJsonString')

        if m.get('Fax') is not None:
            self.fax = m.get('Fax')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('Head') is not None:
            self.head = m.get('Head')

        if m.get('HeadColor') is not None:
            self.head_color = m.get('HeadColor')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')

        if m.get('ProvinceJsonString') is not None:
            self.province_json_string = m.get('ProvinceJsonString')

        if m.get('SelfServicingBusinessRegNum') is not None:
            self.self_servicing_business_reg_num = m.get('SelfServicingBusinessRegNum')

        if m.get('SelfServicingIdentificationNum') is not None:
            self.self_servicing_identification_num = m.get('SelfServicingIdentificationNum')

        if m.get('TrueName') is not None:
            self.true_name = m.get('TrueName')

        return self

