# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVirtualPhysicalConnectionRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        expect_spec: str = None,
        instance_id: str = None,
        region_id: str = None,
        token: str = None,
        vlan_id: int = None,
    ):
        # Specifies whether to only perform a dry run for the request. Valid values:
        # 
        # - **true**: The system performs a dry run without modifying the VLAN ID of the shared Express Connect circuit. The system checks whether the required parameters are specified, the request format, and the instance status. If the request fails the dry run, the corresponding error is returned. If the request passes the dry run, the corresponding request ID is returned.
        # - **false** (default): The system sends a normal request. After the request passes the dry run, the VLAN ID of the shared Express Connect circuit is modified.
        self.dry_run = dry_run
        # The expected bandwidth of the shared Express Connect circuit. The bandwidth takes effect only after the payment is completed.
        # 
        # Valid values: **50M**, **100M**, **200M**, **300M**, **400M**, **500M**, **1G**, **2G**, **5G**, **8G**, and **10G**.
        # 
        # <props="china">
        # > The bandwidth values of **2G**, **5G**, **8G**, and **10G** are not available by default. To use these values, contact your account manager.
        # 
        # <props="intl">
        # > The bandwidth values of **2G**, **5G**, **8G**, and **10G** are not available by default. To use these values, contact your account manager.
        # 
        # Unit: **M** indicates Mbps, and **G** indicates Gbps.
        self.expect_spec = expect_spec
        # The instance ID of the shared Express Connect circuit.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the shared Express Connect circuit.
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.token = token
        # The VLAN ID of the shared Express Connect circuit. Valid values: **0** to **2999**.
        # 
        # - A value of **0** specifies that the physical vSwitch port of the Virtual Border Router (VBR), which acts as a vRouter, does not use the VLAN mode, but uses the Layer 3 routing interface mode. In the Layer 3 routing interface mode, each Express Connect circuit corresponds to one VBR.
        # - A value of **1** to **2999** specifies that the physical vSwitch port of the VBR uses a VLAN-based Layer 3 subinterface. In the Layer 3 subinterface mode, each VLAN ID corresponds to one VBR. In this case, the Express Connect circuit of the VBR can be used to connect VPCs that belong to different Alibaba Cloud accounts. Layer 2 network isolation is implemented for VBRs in different VLANs, and they cannot communicate with each other.
        # 
        # This parameter is required.
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.expect_spec is not None:
            result['ExpectSpec'] = self.expect_spec

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.token is not None:
            result['Token'] = self.token

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ExpectSpec') is not None:
            self.expect_spec = m.get('ExpectSpec')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

