# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class NodeDrainParameters(DaraModel):
    def __init__(
        self,
        pod_from_sub_products: List[str] = None,
        pod_names: List[str] = None,
    ):
        self.pod_from_sub_products = pod_from_sub_products
        self.pod_names = pod_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pod_from_sub_products is not None:
            result['PodFromSubProducts'] = self.pod_from_sub_products

        if self.pod_names is not None:
            result['PodNames'] = self.pod_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodFromSubProducts') is not None:
            self.pod_from_sub_products = m.get('PodFromSubProducts')

        if m.get('PodNames') is not None:
            self.pod_names = m.get('PodNames')

        return self

