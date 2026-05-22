# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchDeleteKvShrinkRequest(DaraModel):
    def __init__(
        self,
        keys_shrink: str = None,
        namespace: str = None,
    ):
        # The keys that you want to delete. You can delete a maximum of 10,000 key-value pairs at a time.
        # 
        # This parameter is required.
        self.keys_shrink = keys_shrink
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
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

