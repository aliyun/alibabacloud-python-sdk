# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class BatchDeleteKvWithHighCapacityAdvanceRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        url_object: BinaryIO = None,
    ):
        # The name of the namespace that you specify when you call the [CreateKvNamespace](https://help.aliyun.com/document_detail/2850317.html) operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The download URL of the key-value pairs that you want to delete. This parameter is automatically filled in when you use the SDK to call the operation.
        # 
        # This parameter is required.
        self.url_object = url_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.url_object is not None:
            result['Url'] = self.url_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Url') is not None:
            self.url_object = m.get('Url')

        return self

