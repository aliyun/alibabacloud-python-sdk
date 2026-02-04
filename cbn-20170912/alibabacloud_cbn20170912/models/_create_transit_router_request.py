# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTransitRouterRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        support_multicast: bool = None,
        tag: List[main_models.CreateTransitRouterRequestTag] = None,
        transit_router_cidr_list: List[main_models.CreateTransitRouterRequestTransitRouterCidrList] = None,
        transit_router_description: str = None,
        transit_router_name: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses **RequestId** as **ClientToken**. The value of **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Check items include permissions and the status of the specified cloud resources. Valid values:
        # 
        # *   **false** (default): sends the request. If the request passes the check, an Enterprise Edition transit router is created.
        # *   **true**: checks the request but does not create the Enterprise Edition transit router. If you use this value, the system checks whether the required parameters are set, and whether the request syntax is valid. If the request fails the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Enterprise Edition transit router is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable the multicast feature for the Enterprise Edition transit router. Valid values:
        # 
        # *   **false** (default): no
        # *   **true**: yes
        # 
        # The multicast feature is supported only in specific regions. You can call [ListTransitRouterAvailableResource](https://help.aliyun.com/document_detail/261356.html) to query the regions that support multicast.
        self.support_multicast = support_multicast
        # The tags.
        self.tag = tag
        # The CIDR blocks to be added to the transit router.
        self.transit_router_cidr_list = transit_router_cidr_list
        # The description of the Enterprise Edition transit router instance.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_description = transit_router_description
        # The name of the Enterprise Edition transit router.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with http:// or https://. You can also leave this parameter empty.
        self.transit_router_name = transit_router_name

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.transit_router_cidr_list:
            for v1 in self.transit_router_cidr_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        result['TransitRouterCidrList'] = []
        if self.transit_router_cidr_list is not None:
            for k1 in self.transit_router_cidr_list:
                result['TransitRouterCidrList'].append(k1.to_map() if k1 else None)

        if self.transit_router_description is not None:
            result['TransitRouterDescription'] = self.transit_router_description

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateTransitRouterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        self.transit_router_cidr_list = []
        if m.get('TransitRouterCidrList') is not None:
            for k1 in m.get('TransitRouterCidrList'):
                temp_model = main_models.CreateTransitRouterRequestTransitRouterCidrList()
                self.transit_router_cidr_list.append(temp_model.from_map(k1))

        if m.get('TransitRouterDescription') is not None:
            self.transit_router_description = m.get('TransitRouterDescription')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        return self

class CreateTransitRouterRequestTransitRouterCidrList(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
        name: str = None,
        publish_cidr_route: bool = None,
    ):
        # The CIDR block of the transit router.
        self.cidr = cidr
        # The description of the transit router CIDR block.
        # 
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The name of the transit router CIDR block.
        # 
        # The name must be 1 to 128 characters in length.
        self.name = name
        # Specifies whether to allow the system to automatically add a route that points to the CIDR block to the route table of the transit router.
        # 
        # *   **true** (default)
        # 
        #     If you set the value to true, after you create a VPN attachment on a private VPN gateway and enable route learning for the VPN attachment, the system automatically adds the following route to the route table of the transit router that is in route learning relationship with the VPN attachment:
        # 
        #     A blackhole route whose destination CIDR block is the transit router CIDR block, which refers to the CIDR block from which gateway IP addresses are allocated to the IPsec-VPN connection.
        # 
        #     The blackhole route is advertised only to the route tables of virtual border routers (VBRs) connected to the transit router.
        # 
        # *   **false**
        self.publish_cidr_route = publish_cidr_route

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_cidr_route is not None:
            result['PublishCidrRoute'] = self.publish_cidr_route

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishCidrRoute') is not None:
            self.publish_cidr_route = m.get('PublishCidrRoute')

        return self

class CreateTransitRouterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag keys cannot be an empty string. The tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys in each call.
        self.key = key
        # The tag value.
        # 
        # The tag value can be an empty string or up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each key-value must be unique. You can specify at most 20 tag values in each call.
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

