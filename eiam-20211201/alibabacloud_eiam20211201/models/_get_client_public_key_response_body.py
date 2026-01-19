# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetClientPublicKeyResponseBody(DaraModel):
    def __init__(
        self,
        client_public_key: main_models.GetClientPublicKeyResponseBodyClientPublicKey = None,
        request_id: str = None,
    ):
        self.client_public_key = client_public_key
        self.request_id = request_id

    def validate(self):
        if self.client_public_key:
            self.client_public_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_public_key is not None:
            result['ClientPublicKey'] = self.client_public_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientPublicKey') is not None:
            temp_model = main_models.GetClientPublicKeyResponseBodyClientPublicKey()
            self.client_public_key = temp_model.from_map(m.get('ClientPublicKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClientPublicKeyResponseBodyClientPublicKey(DaraModel):
    def __init__(
        self,
        algorithm_type: str = None,
        application_id: str = None,
        client_public_key_id: str = None,
        create_time: int = None,
        instance_id: str = None,
        last_used_time: int = None,
        primary: bool = None,
        public_key: str = None,
        status: str = None,
    ):
        # IDaaS EIAM 应用公私钥对算法类型 rsa2048、ecc256
        self.algorithm_type = algorithm_type
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        # IDaaS EIAM 应用公私钥对Id
        self.client_public_key_id = client_public_key_id
        # IDaaS EIAM 应用公私钥对创建时间
        self.create_time = create_time
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        self.last_used_time = last_used_time
        # IDaaS EIAM 应用当前是否为首要使用的公私钥对
        self.primary = primary
        # IDaaS EIAM 应用公钥
        self.public_key = public_key
        # IDaaS EIAM 应用公私钥对状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_public_key_id is not None:
            result['ClientPublicKeyId'] = self.client_public_key_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientPublicKeyId') is not None:
            self.client_public_key_id = m.get('ClientPublicKeyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

