# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRCSSignatureRequest(DaraModel):
    def __init__(
        self,
        background_image: str = None,
        bubble_color: str = None,
        category: int = None,
        description: str = None,
        latitude: str = None,
        logo: str = None,
        longitude: str = None,
        office_address: str = None,
        service_email: str = None,
        service_phone: str = None,
        service_terms: str = None,
        service_website: str = None,
        sign_name: str = None,
    ):
        # 背景图片ossKey
        self.background_image = background_image
        # 气泡颜色
        self.bubble_color = bubble_color
        # 行业类型
        self.category = category
        # 描述信息
        self.description = description
        # 纬度
        self.latitude = latitude
        # logo图片ossKey
        self.logo = logo
        # 经度
        self.longitude = longitude
        # 办公地址
        self.office_address = office_address
        # 服务邮箱
        self.service_email = service_email
        # 服务电话
        self.service_phone = service_phone
        # 服务条款URL
        self.service_terms = service_terms
        # 服务官网URL
        self.service_website = service_website
        # 签名名称（用于定位5G签名）
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_image is not None:
            result['BackgroundImage'] = self.background_image

        if self.bubble_color is not None:
            result['BubbleColor'] = self.bubble_color

        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address

        if self.service_email is not None:
            result['ServiceEmail'] = self.service_email

        if self.service_phone is not None:
            result['ServicePhone'] = self.service_phone

        if self.service_terms is not None:
            result['ServiceTerms'] = self.service_terms

        if self.service_website is not None:
            result['ServiceWebsite'] = self.service_website

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundImage') is not None:
            self.background_image = m.get('BackgroundImage')

        if m.get('BubbleColor') is not None:
            self.bubble_color = m.get('BubbleColor')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')

        if m.get('ServiceEmail') is not None:
            self.service_email = m.get('ServiceEmail')

        if m.get('ServicePhone') is not None:
            self.service_phone = m.get('ServicePhone')

        if m.get('ServiceTerms') is not None:
            self.service_terms = m.get('ServiceTerms')

        if m.get('ServiceWebsite') is not None:
            self.service_website = m.get('ServiceWebsite')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

