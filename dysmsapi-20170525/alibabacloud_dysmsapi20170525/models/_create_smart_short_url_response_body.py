# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreateSmartShortUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: List[main_models.CreateSmartShortUrlResponseBodyModel] = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id

    def validate(self):
        if self.model:
            for v1 in self.model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Model'] = []
        if self.model is not None:
            for k1 in self.model:
                result['Model'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.model = []
        if m.get('Model') is not None:
            for k1 in m.get('Model'):
                temp_model = main_models.CreateSmartShortUrlResponseBodyModel()
                self.model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateSmartShortUrlResponseBodyModel(DaraModel):
    def __init__(
        self,
        domain: str = None,
        expiration: int = None,
        phone_number: str = None,
        short_name: str = None,
        short_url: str = None,
    ):
        self.domain = domain
        self.expiration = expiration
        self.phone_number = phone_number
        self.short_name = short_name
        self.short_url = short_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.short_name is not None:
            result['ShortName'] = self.short_name

        if self.short_url is not None:
            result['ShortUrl'] = self.short_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ShortName') is not None:
            self.short_name = m.get('ShortName')

        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')

        return self

