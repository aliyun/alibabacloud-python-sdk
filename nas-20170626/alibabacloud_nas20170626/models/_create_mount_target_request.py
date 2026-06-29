# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMountTargetRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        dry_run: bool = None,
        enable_ipv_6: bool = None,
        file_system_id: str = None,
        network_type: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required if the file system is a General-purpose NAS or Extreme NAS file system.
        # 
        # Default permission group: DEFAULT_VPC_GROUP_NAME (the default permission group for VPCs).
        self.access_group_name = access_group_name
        # Specifies whether to check for existing mount targets. Only CPFS file systems are supported.
        # 
        # A dry run checks parameter validity and inventory without actually creating a mount target or incurring fees.
        # 
        # - true: sends a dry run request without creating a mount target. The check items include required parameters, request format, business limits, and CPFS inventory. If the check fails, the corresponding error is returned. If the check passes, `200 HttpCode` is returned, but `MountTargetDomain` is empty.
        # - false (default): sends a normal request. After the check passes, a mount target is created.
        self.dry_run = dry_run
        # Specifies whether to create an IPv6 mount target.
        # 
        # Valid values:
        # 
        # - true: creates an IPv6 mount target.
        # - false (default): does not create an IPv6 mount target.
        # 
        # > IPv6 is supported only by Extreme NAS file systems in all regions in the Chinese mainland. The file system must have IPv6 enabled.
        self.enable_ipv_6 = enable_ipv_6
        # The file system ID.
        # 
        # - General-purpose NAS: 31a8e4\\*\\*\\*\\*.
        # 
        # - Extreme NAS: The ID must start with `extreme-`, such as extreme-0015\\*\\*\\*\\*.
        # 
        # - Cloud Parallel File Storage (CPFS): The ID must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The network type of the mount target. Set the value to **Vpc**, which indicates a virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.network_type = network_type
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        # 
        # This parameter is required and valid only when the network type is VPC.
        # For example:
        # If NetworkType is set to VPC, VSwitchId is required.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # This parameter is required and valid only when the network type is VPC.
        # For example:
        # If NetworkType is set to VPC, VpcId is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

