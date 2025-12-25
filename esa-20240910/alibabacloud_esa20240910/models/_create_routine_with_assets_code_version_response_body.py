# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateRoutineWithAssetsCodeVersionResponseBody(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        oss_post_config: main_models.CreateRoutineWithAssetsCodeVersionResponseBodyOssPostConfig = None,
        request_id: str = None,
        status: str = None,
    ):
        self.code_version = code_version
        self.oss_post_config = oss_post_config
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.oss_post_config:
            self.oss_post_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.oss_post_config is not None:
            result['OssPostConfig'] = self.oss_post_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('OssPostConfig') is not None:
            temp_model = main_models.CreateRoutineWithAssetsCodeVersionResponseBodyOssPostConfig()
            self.oss_post_config = temp_model.from_map(m.get('OssPostConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateRoutineWithAssetsCodeVersionResponseBodyOssPostConfig(DaraModel):
    def __init__(
        self,
        key: str = None,
        ossaccess_key_id: str = None,
        policy: str = None,
        signature: str = None,
        url: str = None,
        xoss_security_token: str = None,
    ):
        self.key = key
        self.ossaccess_key_id = ossaccess_key_id
        self.policy = policy
        self.signature = signature
        self.url = url
        self.xoss_security_token = xoss_security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.ossaccess_key_id is not None:
            result['OSSAccessKeyId'] = self.ossaccess_key_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.url is not None:
            result['Url'] = self.url

        if self.xoss_security_token is not None:
            result['XOssSecurityToken'] = self.xoss_security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OSSAccessKeyId') is not None:
            self.ossaccess_key_id = m.get('OSSAccessKeyId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('XOssSecurityToken') is not None:
            self.xoss_security_token = m.get('XOssSecurityToken')

        return self

