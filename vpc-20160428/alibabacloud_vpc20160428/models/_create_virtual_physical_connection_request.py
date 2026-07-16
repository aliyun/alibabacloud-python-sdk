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
        # The description of the shared Express Connect circuits.
        # 
        # The description must be 2 to 256 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without creating the shared Express Connect circuits. The system checks the required parameters, request format, and instance status. If the check fails, the corresponding error is returned. If the check succeeds, `DRYRUN.SUCCESS` is returned.
        # - **false** (default): sends a Normal request. After the request passes the check, the shared Express Connect circuits are created.
        self.dry_run = dry_run
        # The name of the shared Express Connect circuits.
        # 
        # The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, underscores (_), and hyphens (-) but cannot start with `http://` or `https://`.
        self.name = name
        # The payer of the shared Express Connect circuits. Valid values:
        # 
        # - **PayByPhysicalConnectionOwner**: The partner pays.
        # - **PayByVirtualPhysicalConnectionOwner**: The tenant pays.
        # 
        # This parameter is required.
        self.order_mode = order_mode
        # The ID of the Express Connect circuit associated with the shared Express Connect circuits.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the shared Express Connect circuits.
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the shared Express Connect circuits belong.
        self.resource_group_id = resource_group_id
        # The bandwidth value of the shared Express Connect circuits.
        # 
        # Valid values: **50M**, **100M**, **200M**, **300M**, **400M**, **500M**, **1G**, **2G**, **5G**, **8G**, and **10G**.
        # 
        # <props="china">
        # > The bandwidth values **2G**, **5G**, **8G**, and **10G** are not available by default. To use these values, contact your account manager.
        # 
        # <props="intl">
        # > The bandwidth values **2G**, **5G**, **8G**, and **10G** are not available by default. To use these values, contact your account manager.
        # 
        # Unit: **M** indicates Mbit/s. **G** indicates Gbit/s.
        # 
        # This parameter is required.
        self.spec = spec
        # The list of tags.
        self.tag = tag
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.token = token
        # The VLAN ID of the shared Express Connect circuits. Valid values: **0** to **2999**.
        # 
        # - If the VLAN ID is set to **0**, the physical switch port of the Virtual Border Router (VBR) uses Layer 3 routing interface mode instead of VLAN mode. In Layer 3 routing interface mode, each Express Connect circuit corresponds to one VBR.
        # - If the VLAN ID is set to a value from **1** to **2999**, the physical switch port of the VBR uses VLAN-based Layer 3 subinterface mode. In Layer 3 subinterface mode, each VLAN ID corresponds to one VBR. In this case, the Express Connect circuit of the VBR can connect to VPCs under multiple accounts. VBRs in different VLANs have Layer 2 network isolation and cannot communicate with each other.
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
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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

