# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        default_city: str = None,
        default_country: str = None,
        default_district: str = None,
        default_province: str = None,
        latitude: str = None,
        longitude: str = None,
        mobile: str = None,
        product_code: str = None,
        text: str = None,
        verify_type: str = None,
    ):
        # Verification address type:
        # - “0”: Text address
        # - “1”: Latitude and longitude
        # 
        # This parameter is required.
        self.address_type = address_type
        # Default city
        self.default_city = default_city
        # Country name, currently only supports: China
        # 
        # This parameter is required.
        self.default_country = default_country
        # Default district
        self.default_district = default_district
        # Default province
        self.default_province = default_province
        # Latitude.
        self.latitude = latitude
        # Longitude.
        self.longitude = longitude
        # Supports Chinese mobile phone numbers.
        # 
        # This parameter is required.
        self.mobile = mobile
        # Fixed value: ADD_VERIFY_PRO
        # 
        # This parameter is required.
        self.product_code = product_code
        # Detailed address text content
        self.text = text
        # Address verification method:
        # - HOME: Home address verification
        # - WORK: Work address verification
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.default_city is not None:
            result['DefaultCity'] = self.default_city

        if self.default_country is not None:
            result['DefaultCountry'] = self.default_country

        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district

        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.text is not None:
            result['Text'] = self.text

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')

        if m.get('DefaultCountry') is not None:
            self.default_country = m.get('DefaultCountry')

        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')

        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

