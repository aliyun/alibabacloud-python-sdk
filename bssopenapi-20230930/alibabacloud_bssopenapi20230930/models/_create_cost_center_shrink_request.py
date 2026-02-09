# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCostCenterShrinkRequest(DaraModel):
    def __init__(
        self,
        cost_center_entity_list_shrink: str = None,
        nbid: str = None,
    ):
        # This parameter is required.
        self.cost_center_entity_list_shrink = cost_center_entity_list_shrink
        self.nbid = nbid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_entity_list_shrink is not None:
            result['CostCenterEntityList'] = self.cost_center_entity_list_shrink

        if self.nbid is not None:
            result['Nbid'] = self.nbid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCenterEntityList') is not None:
            self.cost_center_entity_list_shrink = m.get('CostCenterEntityList')

        if m.get('Nbid') is not None:
            self.nbid = m.get('Nbid')

        return self

