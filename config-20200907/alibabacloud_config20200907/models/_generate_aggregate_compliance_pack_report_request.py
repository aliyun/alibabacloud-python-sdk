# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAggregateCompliancePackReportRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_id: str = None,
        multi_files: bool = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the compliance package.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListAggregateCompliancePacks](https://help.aliyun.com/document_detail/262059.html).
        # 
        # This parameter is required.
        self.compliance_pack_id = compliance_pack_id
        self.multi_files = multi_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.multi_files is not None:
            result['MultiFiles'] = self.multi_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('MultiFiles') is not None:
            self.multi_files = m.get('MultiFiles')

        return self

