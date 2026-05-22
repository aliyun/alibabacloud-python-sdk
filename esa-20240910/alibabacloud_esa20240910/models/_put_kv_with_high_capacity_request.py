# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutKvWithHighCapacityRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        namespace: str = None,
        url: str = None,
    ):
        # The key name. The name can be up to 512 characters in length and cannot contain spaces or backslashes (\\\\).
        # 
        # This parameter is required.
        self.key = key
        # The name of the namespace that you specify when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The download URL of the key-value pair that you want to upload. This parameter is automatically filled in when you use the SDK to call the operation.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

