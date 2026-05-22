# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchPutKvRequest(DaraModel):
    def __init__(
        self,
        kv_list: List[main_models.BatchPutKvRequestKvList] = None,
        namespace: str = None,
    ):
        # The key-value pairs that you want to configure at a time. The total size can be up to 2 MB (2 × 1000 × 1000).
        # 
        # This parameter is required.
        self.kv_list = kv_list
        # The name of the namespace that you specify when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        if self.kv_list:
            for v1 in self.kv_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KvList'] = []
        if self.kv_list is not None:
            for k1 in self.kv_list:
                result['KvList'].append(k1.to_map() if k1 else None)

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kv_list = []
        if m.get('KvList') is not None:
            for k1 in m.get('KvList'):
                temp_model = main_models.BatchPutKvRequestKvList()
                self.kv_list.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

class BatchPutKvRequestKvList(DaraModel):
    def __init__(
        self,
        expiration: int = None,
        expiration_ttl: int = None,
        key: str = None,
        value: str = None,
    ):
        # The time when the key-value pair expires, which cannot be earlier than the current time. The value is a timestamp in seconds. If you specify both Expiration and ExpirationTtl, only ExpirationTtl takes effect.
        self.expiration = expiration
        # The relative expiration time. Unit: seconds. If you specify both Expiration and ExpirationTtl, only ExpirationTtl takes effect.
        self.expiration_ttl = expiration_ttl
        # The key name. The name can be up to 512 characters in length and cannot contain spaces or backslashes (\\\\).
        # 
        # This parameter is required.
        self.key = key
        # The key content.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.expiration_ttl is not None:
            result['ExpirationTtl'] = self.expiration_ttl

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('ExpirationTtl') is not None:
            self.expiration_ttl = m.get('ExpirationTtl')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

