# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchPutKvShrinkRequest(DaraModel):
    def __init__(
        self,
        kv_list_shrink: str = None,
        namespace: str = None,
    ):
        # The key-value pairs that you want to configure at a time. The total size can be up to 2 MB (2 × 1000 × 1000).
        # 
        # This parameter is required.
        self.kv_list_shrink = kv_list_shrink
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
        if self.kv_list_shrink is not None:
            result['KvList'] = self.kv_list_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvList') is not None:
            self.kv_list_shrink = m.get('KvList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

