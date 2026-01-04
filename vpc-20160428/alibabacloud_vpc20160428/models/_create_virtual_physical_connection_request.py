# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVirtualPhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        order_mode: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        tag: List[main_models.CreateVirtualPhysicalConnectionRequestTag] = None,
        token: str = None,
        vlan_id: int = None,
        vpconn_ali_uid: int = None,
    ):
        # The description of the hosted connection.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run, without performing the actual request. Default value: 45104. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including required parameters, request syntax, and instance status. If the request fails the dry run, an error code is returned. If the request passes the dry run, `DRYRUN.SUCCESS` is returned.
        # *   **false**: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The name of the hosted connection.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter but cannot start with `http://` or `https://`.
        self.name = name
        # The payer for the hosted connection. Valid values:
        # 
        # *   **PayByPhysicalConnectionOwner**: The partner pays for the hosted connection.
        # *   **PayByVirtualPhysicalConnectionOwner**: The tenant pays for the hosted connection.
        # 
        # This parameter is required.
        self.order_mode = order_mode
        # The ID of the Express Connect circuit over which the hosted connection is created.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the hosted connection.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the hosted connection belongs.
        self.resource_group_id = resource_group_id
        # The bandwidth value of the hosted connection.
        # 
        # Valid values: **50M**, **100M**, **200M**, **300M**, **400M**, **500M**, **1G**, **2G**, **5G**, **8G**, and **10G**.
        # 
        # >  **2G**, **5G**, **8G**, and **10G** are unavailable by default. If you want to use these bandwidth values, contact your account manager.
        # 
        # **M** indicates Mbit/s and **G** indicates Gbit/s.
        # 
        # This parameter is required.
        self.spec = spec
        # The tags.
        self.tag = tag
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.token = token
        # The virtual local area network (VLAN) ID of the hosted connection. Valid values: **0** to **2999**.
        # 
        # *   If the VLAN ID is set to **0**, it indicates that the switch port of the virtual border router (VBR) is a Layer 3 router interface instead of a VLAN interface. When a Layer 3 router interface is used, each Express Connect circuit corresponds to a VBR.
        # *   If the VLAN ID is set to a value from **1** to **2999**, the switch port of the VBR is a Layer 3 VLAN subinterface. When a Layer 3 VLAN subinterface is used, each VLAN ID corresponds to one VBR. In this case, the Express Connect circuit with which the VBR is associated can be used to connect to virtual private clouds (VPCs) that belong to different Alibaba Cloud accounts. VBRs in different VLANs are isolated from each other at Layer 2.
        # 
        # This parameter is required.
        self.vlan_id = vlan_id
        # The Alibaba Cloud account ID of the tenant.
        # 
        # This parameter is required.
        self.vpconn_ali_uid = vpconn_ali_uid

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
        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.name is not None:
            result['Name'] = self.name

        if self.order_mode is not None:
            result['OrderMode'] = self.order_mode

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['Token'] = self.token

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vpconn_ali_uid is not None:
            result['VpconnAliUid'] = self.vpconn_ali_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderMode') is not None:
            self.order_mode = m.get('OrderMode')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateVirtualPhysicalConnectionRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VpconnAliUid') is not None:
            self.vpconn_ali_uid = m.get('VpconnAliUid')

        return self

class CreateVirtualPhysicalConnectionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. You can specify at most 20 tag values. The tag value can be an empty string.
        # 
        # The value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The value must start with a letter but cannot start with `aliyun` or `acs:`. The value cannot contain `http://` or `https://`.
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

