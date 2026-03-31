# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateDiscoveredResourceRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_option: int = None,
        region: str = None,
        resource_account_id: int = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # Specifies whether to query the compliance results of the resource. Valid values:
        # 
        # *   0 (default): does not query the compliance results of the resource.
        # *   1: queries the compliance results of the resource.
        self.compliance_option = compliance_option
        # The ID of the region in which the resource resides.
        # 
        # For more information about how to query the ID of a region in which the resource resides, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/411691.html).
        # 
        # This parameter is required.
        self.region = region
        # Required. The ID of the Alibaba Cloud account to which the specified resource belongs in the account group.
        self.resource_account_id = resource_account_id
        # The resource ID.
        # 
        # For more information about how to obtain the ID of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/411691.html).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # The type of the resource.
        # 
        # For more information about how to obtain the type of a resource, see [ListAggregateDiscoveredResources](https://help.aliyun.com/document_detail/411691.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_option is not None:
            result['ComplianceOption'] = self.compliance_option

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ComplianceOption') is not None:
            self.compliance_option = m.get('ComplianceOption')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

