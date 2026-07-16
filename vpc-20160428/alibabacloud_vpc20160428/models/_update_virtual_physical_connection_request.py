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
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run to check for required parameters, the request format, and the instance status. The VLAN ID of the virtual physical connection is not modified. If the check fails, an error message is returned. If it passes, the request ID is returned.
        # 
        # - **false** (default): Sends the request. If the check passes, the VLAN ID of the virtual physical connection is modified.
        self.dry_run = dry_run
        # The expected bandwidth of the virtual physical connection. The new bandwidth takes effect only after the payment is complete.
        # 
        # Valid values: **50M**, **100M**, **200M**, **300M**, **400M**, **500M**, **1G**, **2G**, **5G**, **8G**, and **10G**.
        # 
        # <props="china">
        # 
        # > Bandwidth settings of **2G**, **5G**, **8G**, and **10G** are not enabled by default. To use these settings, contact your account manager.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > Bandwidth settings of **2G**, **5G**, **8G**, and **10G** are not enabled by default. To use these settings, contact your account manager.
        # 
        # 
        # 
        # Units: **M** indicates Mbps and **G** indicates Gbps.
        self.expect_spec = expect_spec
        # The ID of the virtual physical connection instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the virtual physical connection is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to obtain region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The client token that ensures the idempotence of the request.
        # 
        # A client-generated value that must be unique across requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** is different for each request.
        self.token = token
        # The VLAN ID of the virtual physical connection. Valid values: **0** to **2999**.
        # 
        # - If you set the VLAN ID to **0**, the physical switch port of the Virtual Border Router (VBR) operates in Layer 3 routed interface mode. In this mode, one physical connection corresponds to one VBR.
        # 
        # - If you set the VLAN ID to a value from **1** to **2999**, the physical switch port of the VBR uses a VLAN-based Layer 3 subinterface. In this mode, each VLAN ID corresponds to one VBR. The physical connection can be attached to VPCs that belong to different accounts. VBRs in different VLANs are isolated at Layer 2 and cannot communicate with each other.
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

