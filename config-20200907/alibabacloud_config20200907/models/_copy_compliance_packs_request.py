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
        # The IDs of the destination account groups into which the compliance packages are replicated. Separate multiple account group IDs with commas (,).
        # 
        # > If this parameter is left empty, the compliance packages are replicated to the current account group.
        self.des_aggregator_ids = des_aggregator_ids
        # The ID of the account group to which the compliance packages belong.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.src_aggregator_id = src_aggregator_id
        # The IDs of the compliance packages. Separate multiple compliance package IDs with commas (,).
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListCompliancePacks](https://help.aliyun.com/document_detail/263332.html).
        # 
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

