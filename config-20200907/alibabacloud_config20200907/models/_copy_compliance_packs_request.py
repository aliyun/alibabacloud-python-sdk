# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyCompliancePacksRequest(DaraModel):
    def __init__(
        self,
        des_aggregator_ids: str = None,
        src_aggregator_id: str = None,
        src_compliance_pack_ids: str = None,
    ):
        self.des_aggregator_ids = des_aggregator_ids
        self.src_aggregator_id = src_aggregator_id
        # This parameter is required.
        self.src_compliance_pack_ids = src_compliance_pack_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.des_aggregator_ids is not None:
            result['DesAggregatorIds'] = self.des_aggregator_ids

        if self.src_aggregator_id is not None:
            result['SrcAggregatorId'] = self.src_aggregator_id

        if self.src_compliance_pack_ids is not None:
            result['SrcCompliancePackIds'] = self.src_compliance_pack_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesAggregatorIds') is not None:
            self.des_aggregator_ids = m.get('DesAggregatorIds')

        if m.get('SrcAggregatorId') is not None:
            self.src_aggregator_id = m.get('SrcAggregatorId')

        if m.get('SrcCompliancePackIds') is not None:
            self.src_compliance_pack_ids = m.get('SrcCompliancePackIds')

        return self

