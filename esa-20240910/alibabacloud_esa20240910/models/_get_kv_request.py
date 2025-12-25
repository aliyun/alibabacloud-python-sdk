# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKvRequest(DaraModel):
    def __init__(
        self,
        base_64: bool = None,
        key: str = None,
        namespace: str = None,
    ):
        # Specifies whether to decode the value by using Base 64. If you call the [PutKv](https://help.aliyun.com/document_detail/2850482.html) operation and set the Base64 parameter to true, set this parameter to true to read the original content.
        self.base_64 = base_64
        # The key name for the query.
        # 
        # This parameter is required.
        self.key = key
        # The name of the namespace that you specify when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64 is not None:
            result['Base64'] = self.base_64

        if self.key is not None:
            result['Key'] = self.key

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Base64') is not None:
            self.base_64 = m.get('Base64')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

