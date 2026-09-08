# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGrantRulesToResourceRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_type: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # - If you do not specify the **MaxResults** parameter, paged query is not required. The value of **MaxResults** in the response indicates the total number of entries.
        # - If you specify the **MaxResults** parameter, paged query is required. The value of **MaxResults** specifies the number of entries to return per page. Valid values: **1** to **100**. The value of **MaxResults** in the response indicates the number of entries in the current page. We recommend that you set **MaxResults** to **20**.
        self.max_results = max_results
        # The pagination token. Valid values:
        # 
        # - You do not need to specify this parameter for the first request or if no subsequent query exists.
        # - If a subsequent query exists, set the value to the **NextToken** value returned by the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The type of the network instance. Valid values:
        # 
        # - **VPC**: Virtual Private Cloud (VPC) instance.
        # - **ExpressConnect**: Virtual border router (VBR) instance.
        # - **VPN**: IPsec connection.
        # - **ECR**: Express Connect Router (ECR) instance.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The region ID of the network instance.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        self.region_id = region_id
        # The network instance ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

