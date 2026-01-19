# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListClientPublicKeysResponseBody(DaraModel):
    def __init__(
        self,
        client_public_keys: List[main_models.ListClientPublicKeysResponseBodyClientPublicKeys] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.client_public_keys = client_public_keys
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.client_public_keys:
            for v1 in self.client_public_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClientPublicKeys'] = []
        if self.client_public_keys is not None:
            for k1 in self.client_public_keys:
                result['ClientPublicKeys'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_public_keys = []
        if m.get('ClientPublicKeys') is not None:
            for k1 in m.get('ClientPublicKeys'):
                temp_model = main_models.ListClientPublicKeysResponseBodyClientPublicKeys()
                self.client_public_keys.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListClientPublicKeysResponseBodyClientPublicKeys(DaraModel):
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
        # IDaaS EIAM 应用ClientPublicKey的算法类型 rsa2048、ecc256
        self.algorithm_type = algorithm_type
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        # IDaaS EIAM 应用ClientPublicKey的Id
        self.client_public_key_id = client_public_key_id
        # IDaaS EIAM 应用ClientPublicKey的创建时间
        self.create_time = create_time
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        self.last_used_time = last_used_time
        # IDaaS EIAM 应用当前是否为首要使用的应用ClientPublicKey的
        self.primary = primary
        # IDaaS EIAM 应用ClientPublicKey的公钥
        self.public_key = public_key
        # IDaaS EIAM 应用ClientPublicKey的状态
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

