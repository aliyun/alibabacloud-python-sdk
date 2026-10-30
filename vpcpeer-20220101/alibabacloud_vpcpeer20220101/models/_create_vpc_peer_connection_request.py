# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcpeer20220101 import models as main_models
from darabonba.model import DaraModel

class CreateVpcPeerConnectionRequest(DaraModel):
    def __init__(
        self,
        accepting_ali_uid: int = None,
        accepting_region_id: str = None,
        accepting_vpc_id: str = None,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        enable_jumbo_frame: bool = None,
        link_type: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateVpcPeerConnectionRequestTag] = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the acceptor of the VPC peering connection belongs.
        # 
        # - If you enter your own Alibaba Cloud account ID, a same-account VPC peering connection is created.
        # 
        # - If you enter the ID of another Alibaba Cloud account, a cross-account VPC peering connection is created.
        #    
        # > If the acceptor account is a Resource Access Management (RAM) user, you must enter the ID of the Alibaba Cloud account to which the RAM user belongs in **AcceptingAliUid**.
        # 
        # This parameter is required.
        self.accepting_ali_uid = accepting_ali_uid
        # The ID of the region where the acceptor of the VPC peering connection is deployed.
        # 
        # - To create an intra-region VPC peering connection, enter the same region ID as the initiator.
        # 
        # - To create an inter-region VPC peering connection, enter a region ID different from that of the initiator.
        # 
        # This parameter is required.
        self.accepting_region_id = accepting_region_id
        # The ID of the VPC that acts as the acceptor of the VPC peering connection.
        # 
        # This parameter is required.
        self.accepting_vpc_id = accepting_vpc_id
        # The bandwidth of the VPC peering connection. Unit: Mbit/s. The value must be a positive integer.
        # > If you want to specify this parameter, make sure that you are creating an inter-region peering connection.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the VPC peering connection. The description must be 2 to 256 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform only a dry run for this request. Valid values:
        # 
        # - **true**: performs a dry run and does not create a VPC peering connection. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a Normal request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Specifies whether to enable the jumbo frame feature for the VPC peering connection. Valid values:
        # - true: enabled.
        # - false: disabled.
        # > Note: If you want to specify this parameter, make sure that you are creating an inter-region peering connection.
        self.enable_jumbo_frame = enable_jumbo_frame
        # The link type.
        # 
        # Valid values: Platinum and Gold. Default value: Gold.
        # 
        # > If you want to specify this parameter, make sure that you are creating an inter-region peering connection.
        self.link_type = link_type
        # The name of the VPC peering connection. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and can contain digits, underscores (_), and hyphens (-).
        self.name = name
        # The ID of the region where you want to create a VPC peering connection. 
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group?](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        # The tag information.
        self.tag = tag
        # The ID create a VPC that acts as the initiator create a VPC peering connection.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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
        if self.accepting_ali_uid is not None:
            result['AcceptingAliUid'] = self.accepting_ali_uid

        if self.accepting_region_id is not None:
            result['AcceptingRegionId'] = self.accepting_region_id

        if self.accepting_vpc_id is not None:
            result['AcceptingVpcId'] = self.accepting_vpc_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.link_type is not None:
            result['LinkType'] = self.link_type

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptingAliUid') is not None:
            self.accepting_ali_uid = m.get('AcceptingAliUid')

        if m.get('AcceptingRegionId') is not None:
            self.accepting_region_id = m.get('AcceptingRegionId')

        if m.get('AcceptingVpcId') is not None:
            self.accepting_vpc_id = m.get('AcceptingVpcId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('LinkType') is not None:
            self.link_type = m.get('LinkType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVpcPeerConnectionRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateVpcPeerConnectionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You must specify at least one tag key and can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You must specify at least one tag value and can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

