# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        result_object: main_models.DescribeUserInfoResponseBodyResultObject = None,
        success: bool = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Returned object
        self.result_object = result_object
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeUserInfoResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class DescribeUserInfoResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        sub_id: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # Client IP.
        self.client_ip = client_ip
        # Sub-account ID
        self.sub_id = sub_id
        # User UID
        self.user_id = user_id
        # User name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['clientIp'] = self.client_ip

        if self.sub_id is not None:
            result['subId'] = self.sub_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientIp') is not None:
            self.client_ip = m.get('clientIp')

        if m.get('subId') is not None:
            self.sub_id = m.get('subId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

