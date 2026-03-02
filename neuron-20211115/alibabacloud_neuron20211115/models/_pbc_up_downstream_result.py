# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PbcUpDownstreamResult(DaraModel):
    def __init__(
        self,
        pbc_items: List[main_models.PbcRelationItem] = None,
        request_id: str = None,
    ):
        self.pbc_items = pbc_items
        self.request_id = request_id

    def validate(self):
        if self.pbc_items:
            for v1 in self.pbc_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pbcItems'] = []
        if self.pbc_items is not None:
            for k1 in self.pbc_items:
                result['pbcItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pbc_items = []
        if m.get('pbcItems') is not None:
            for k1 in m.get('pbcItems'):
                temp_model = main_models.PbcRelationItem()
                self.pbc_items.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

