# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGrantRulesToCenRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        enabled_ipv_6: bool = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The CEN instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of the network instance that you want to query.
        self.child_instance_id = child_instance_id
        # The ID of the Alibaba Cloud account to which the network instance belongs.
        self.child_instance_owner_id = child_instance_owner_id
        # Specifies whether to enable IPv6.
        # 
        # 1.  This parameter takes effect only if ProductType is set to VPC.
        # 2.  true: enables IPv6. false: disables IPv6. If you do not specify a value, network instances are not filtered based on this parameter.
        self.enabled_ipv_6 = enabled_ipv_6
        # *   If you do not set **MaxResults**, it indicates that you do not need to query results in batches. The value of **MaxResults** in the response indicates the total number of entries returned.
        # *   If you specify a value for **MaxResults**, it indicates that you need to query results in batches. The value of **MaxResults** indicates the number of entries to return in each batch. Valid values: **1** to **100**. The value of **MaxResults** in the response indicates the number of entries in the current batch. We recommend that you set **MaxResults** to **20**.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of **NextToken**.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**
        # *   **VBR**
        # *   **CCN**
        # *   **VPN**
        # 
        # This parameter is required.
        self.product_type = product_type
        # The region ID of the network instance.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id

        if self.enabled_ipv_6 is not None:
            result['EnabledIpv6'] = self.enabled_ipv_6

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')

        if m.get('EnabledIpv6') is not None:
            self.enabled_ipv_6 = m.get('EnabledIpv6')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

