# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcpeer20220101 import models as main_models
from darabonba.model import DaraModel

class GetVpcPeerConnectionAttributeResponseBody(DaraModel):
    def __init__(
        self,
        accepting_owner_uid: int = None,
        accepting_region_id: str = None,
        accepting_vpc: main_models.GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc = None,
        bandwidth: int = None,
        biz_status: str = None,
        description: str = None,
        enable_jumbo_frame: bool = None,
        gmt_create: str = None,
        gmt_expired: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        link_type: str = None,
        managed_service: str = None,
        name: str = None,
        owner_id: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetVpcPeerConnectionAttributeResponseBodyTags] = None,
        vpc: main_models.GetVpcPeerConnectionAttributeResponseBodyVpc = None,
    ):
        # The Alibaba Cloud account ID of the acceptor of the VPC peering connection.
        self.accepting_owner_uid = accepting_owner_uid
        # The region ID of the acceptor of the VPC peering connection.
        self.accepting_region_id = accepting_region_id
        # The details of the acceptor VPC-connected instance.
        self.accepting_vpc = accepting_vpc
        # The bandwidth of the VPC peering connection. Unit: Mbit/s. Valid values: integers greater than 0.
        # 
        # > A value of -1 indicates that the bandwidth is not limited.
        # 
        # Default values:
        # - The default bandwidth of a cross-region VPC peering connection is 1024 Mbit/s.
        # - The default bandwidth of an intra-region VPC peering connection is -1 Mbit/s, which indicates that the bandwidth is not limited.
        self.bandwidth = bandwidth
        # The billing status of the VPC peering connection. Valid values:
        # 
        # - **Normal**: Normal.
        # - **FinancialLocked**: Locked due to overdue payments.
        self.biz_status = biz_status
        # The description of the VPC peering connection.
        self.description = description
        # Indicates whether the jumbo frame feature is enabled for the VPC peering connection. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.enable_jumbo_frame = enable_jumbo_frame
        # The time when the VPC peering connection was created. The time is displayed in UTC in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.gmt_create = gmt_create
        # The expiration time of the VPC peering connection.
        # 
        # A specific expiration time is returned only when the **Status** of the VPC peering connection is **Accepting** or **Expired**. If the VPC peering connection is in other states, **null** is returned.
        self.gmt_expired = gmt_expired
        # The time when the VPC peering connection was modified. The time is displayed in UTC in the `YYYY-MM-DDThh:mm:ssZ` format.
        self.gmt_modified = gmt_modified
        # The instance ID of the VPC peering connection.
        self.instance_id = instance_id
        # The link type of the VPC peering connection.
        # 
        # Default values:
        # - The default link type of a cross-region VPC peering connection is Gold.
        # - The default link type of an intra-region VPC peering connection is empty.
        self.link_type = link_type
        # The associated cloud service.
        self.managed_service = managed_service
        # The name of the VPC peering connection.
        self.name = name
        # The Alibaba Cloud account ID of the requester of the VPC peering connection.
        self.owner_id = owner_id
        # The region ID of the requester of the VPC peering connection.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the VPC peering connection. Valid values:
        # 
        # - **Creating**: Creating.
        # - **Accepting**: Accepting.
        # - **Updating**: Updating.
        # - **Rejected**: Rejected.
        # - **Expired**: Expired.
        # - **Activated**: Activated.
        # - **Deleting**: Deleting.
        # - **Deleted**: Deleted. 
        # 
        # For more information about the statuses of VPC peering connections, see [VPC peering connection overview](https://help.aliyun.com/document_detail/418507.html).
        self.status = status
        # The tags.
        self.tags = tags
        # The details of the requester VPC-connected instance.
        self.vpc = vpc

    def validate(self):
        if self.accepting_vpc:
            self.accepting_vpc.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepting_owner_uid is not None:
            result['AcceptingOwnerUid'] = self.accepting_owner_uid

        if self.accepting_region_id is not None:
            result['AcceptingRegionId'] = self.accepting_region_id

        if self.accepting_vpc is not None:
            result['AcceptingVpc'] = self.accepting_vpc.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.link_type is not None:
            result['LinkType'] = self.link_type

        if self.managed_service is not None:
            result['ManagedService'] = self.managed_service

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc is not None:
            result['Vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptingOwnerUid') is not None:
            self.accepting_owner_uid = m.get('AcceptingOwnerUid')

        if m.get('AcceptingRegionId') is not None:
            self.accepting_region_id = m.get('AcceptingRegionId')

        if m.get('AcceptingVpc') is not None:
            temp_model = main_models.GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc()
            self.accepting_vpc = temp_model.from_map(m.get('AcceptingVpc'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')

        if m.get('ManagedService') is not None:
            self.managed_service = m.get('ManagedService')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetVpcPeerConnectionAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Vpc') is not None:
            temp_model = main_models.GetVpcPeerConnectionAttributeResponseBodyVpc()
            self.vpc = temp_model.from_map(m.get('Vpc'))

        return self

class GetVpcPeerConnectionAttributeResponseBodyVpc(DaraModel):
    def __init__(
        self,
        ipv_4cidrs: List[str] = None,
        ipv_6cidrs: List[str] = None,
        vpc_id: str = None,
    ):
        # The IPv4 CIDR blocks of the requester.
        self.ipv_4cidrs = ipv_4cidrs
        # The IPv6 CIDR blocks of the requester.
        self.ipv_6cidrs = ipv_6cidrs
        # The instance ID of the requester VPC-connected instance.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetVpcPeerConnectionAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc(DaraModel):
    def __init__(
        self,
        ipv_4cidrs: List[str] = None,
        ipv_6cidrs: List[str] = None,
        vpc_id: str = None,
    ):
        # The IPv4 CIDR blocks of the acceptor.
        self.ipv_4cidrs = ipv_4cidrs
        # The IPv6 CIDR blocks of the acceptor.
        self.ipv_6cidrs = ipv_6cidrs
        # The instance ID of the acceptor VPC-connected instance.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

