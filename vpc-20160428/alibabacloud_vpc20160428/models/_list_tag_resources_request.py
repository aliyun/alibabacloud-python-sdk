# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
    ):
        # The number of entries per page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If this is the first query or no next query exists, you do not need to set this parameter.
        # 
        # - If a next query exists, set the value to the **NextToken** value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources. You can specify up to 50 resource IDs.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # - **VPC**: VPC instance.
        # - **VSWITCH**: vSwitch instance.
        # - **ROUTETABLE**: route table instance.
        # - **EIP**: Elastic IP Address (EIP) instance.
        # - **VPNGATEWAY**: VPN gateway instance.
        # - **NATGATEWAY**: NAT gateway instance.
        # - **COMMONBANDWIDTHPACKAGE**: EIP bandwidth plan instance.
        # - **PREFIXLIST**: prefix list instance.
        # - **PUBLICIPADDRESSPOOL**: IP address pool instance.
        # - **IPV4GATEWAY**: IPv4 gateway instance.
        # - **IPV6GATEWAY**: IPv6 gateway instance.
        # - **NETWORKACL**: network ACL instance.
        # - **TRAFFICMIRRORFILTER**: traffic mirroring filter instance.
        # - **TRAFFICMIRRORSESSION**: traffic mirroring session instance.
        # - **FLOWLOG**: flow log instance.
        # - **HAVIP**: high-availability virtual IP address (HAVIP) instance.
        # - **DHCPOPTIONSSET**: DHCP options set instance.
        # - **GATEWAYENDPOINT**: gateway endpoint instance.
        # - **IPV6ADDRESS**: IPv6 address instance.
        # 
        # > The resource type value is case-insensitive.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag information.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 20 tag keys.
        # 
        # The tag key can be up to 128 characters in length. It cannot be an empty string. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # > You must specify at least one of the **ResourceId.N** and **Tag.N** (**Tag.N.Key** and **Tag.N.Value**) parameters.
        self.key = key
        # The value of the tag. You can specify up to 20 tag values.
        # 
        # The tag value can be up to 128 characters in length and can be an empty string. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # > You must specify at least one of the **ResourceId.N** and **Tag.N** (**Tag.N.Key** and **Tag.N.Value**) parameters.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

