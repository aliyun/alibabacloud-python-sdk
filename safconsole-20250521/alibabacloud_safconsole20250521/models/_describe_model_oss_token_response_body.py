# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_safconsole20250521 import models as main_models
from darabonba.model import DaraModel

class DescribeModelOssTokenResponseBody(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        code: int = None,
        host: str = None,
        http_status_code: int = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        result_object: main_models.DescribeModelOssTokenResponseBodyResultObject = None,
        signature: str = None,
        success: bool = None,
        xoss_security_token: str = None,
    ):
        self.access_id = access_id
        self.code = code
        self.host = host
        self.http_status_code = http_status_code
        self.key = key
        self.policy = policy
        self.request_id = request_id
        self.result_object = result_object
        self.signature = signature
        self.success = success
        self.xoss_security_token = xoss_security_token

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.code is not None:
            result['Code'] = self.code

        if self.host is not None:
            result['Host'] = self.host

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.key is not None:
            result['Key'] = self.key

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.success is not None:
            result['Success'] = self.success

        if self.xoss_security_token is not None:
            result['XOssSecurityToken'] = self.xoss_security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeModelOssTokenResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('XOssSecurityToken') is not None:
            self.xoss_security_token = m.get('XOssSecurityToken')

        return self

class DescribeModelOssTokenResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        signature: str = None,
        xoss_security_token: str = None,
    ):
        self.access_id = access_id
        self.host = host
        self.key = key
        self.policy = policy
        self.signature = signature
        self.xoss_security_token = xoss_security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.host is not None:
            result['Host'] = self.host

        if self.key is not None:
            result['Key'] = self.key

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.xoss_security_token is not None:
            result['XOssSecurityToken'] = self.xoss_security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('XOssSecurityToken') is not None:
            self.xoss_security_token = m.get('XOssSecurityToken')

        return self

