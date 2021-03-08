# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class ActivateLicenseRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        license_publisher: str = None,
        license_code: str = None,
    ):
        self.biz_type = biz_type
        self.license_publisher = license_publisher
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.license_publisher is not None:
            result['LicensePublisher'] = self.license_publisher
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('LicensePublisher') is not None:
            self.license_publisher = m.get('LicensePublisher')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivateLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


