# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Quota(DaraModel):
    def __init__(
        self,
        compute_resource: int = None,
        doc_size: int = None,
        order_type: str = None,
        spec: str = None,
    ):
        self.compute_resource = compute_resource
        self.doc_size = doc_size
        self.order_type = order_type
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.doc_size is not None:
            result['docSize'] = self.doc_size

        if self.order_type is not None:
            result['orderType'] = self.order_type

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('docSize') is not None:
            self.doc_size = m.get('docSize')

        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

