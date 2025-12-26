# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lingmou20250527 import models as main_models
from darabonba.model import DaraModel

class GetUploadPolicyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetUploadPolicyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetUploadPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetUploadPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        oss_key: str = None,
        oss_policy: main_models.GetUploadPolicyResponseBodyDataOssPolicy = None,
    ):
        self.oss_key = oss_key
        self.oss_policy = oss_policy

    def validate(self):
        if self.oss_policy:
            self.oss_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        if self.oss_policy is not None:
            result['ossPolicy'] = self.oss_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        if m.get('ossPolicy') is not None:
            temp_model = main_models.GetUploadPolicyResponseBodyDataOssPolicy()
            self.oss_policy = temp_model.from_map(m.get('ossPolicy'))

        return self

class GetUploadPolicyResponseBodyDataOssPolicy(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        # accessId。
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['accessId'] = self.access_id

        if self.dir is not None:
            result['dir'] = self.dir

        if self.expire is not None:
            result['expire'] = self.expire

        if self.host is not None:
            result['host'] = self.host

        if self.policy is not None:
            result['policy'] = self.policy

        if self.signature is not None:
            result['signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')

        if m.get('dir') is not None:
            self.dir = m.get('dir')

        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('host') is not None:
            self.host = m.get('host')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        return self

