# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGovernanceItemReportRequest(DaraModel):
    def __init__(
        self,
        governance_item_type: str = None,
        marker: str = None,
        max_items: str = None,
    ):
        self.governance_item_type = governance_item_type
        self.marker = marker
        self.max_items = max_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.governance_item_type is not None:
            result['GovernanceItemType'] = self.governance_item_type

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.max_items is not None:
            result['MaxItems'] = self.max_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernanceItemType') is not None:
            self.governance_item_type = m.get('GovernanceItemType')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        return self

