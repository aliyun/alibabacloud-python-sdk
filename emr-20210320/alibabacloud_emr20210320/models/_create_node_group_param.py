# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CreateNodeGroupParam(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        data_disks: List[main_models.DiskInfo] = None,
        instance_types: List[str] = None,
        node_count: int = None,
        node_group_name: str = None,
        node_group_type: str = None,
        node_key_pair_name: str = None,
        node_ram_role: str = None,
        node_root_password: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        security_group_id: str = None,
        spot_strategy: str = None,
        system_disk: main_models.SystemDiskParam = None,
        v_switch_ids: List[str] = None,
        with_public_ip: bool = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_renew_duration_unit = auto_renew_duration_unit
        self.data_disks = data_disks
        self.instance_types = instance_types
        self.node_count = node_count
        self.node_group_name = node_group_name
        self.node_group_type = node_group_type
        self.node_key_pair_name = node_key_pair_name
        self.node_ram_role = node_ram_role
        self.node_root_password = node_root_password
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        self.payment_type = payment_type
        self.security_group_id = security_group_id
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk
        self.v_switch_ids = v_switch_ids
        self.with_public_ip = with_public_ip
        self.zone_id = zone_id

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.node_key_pair_name is not None:
            result['NodeKeyPairName'] = self.node_key_pair_name

        if self.node_ram_role is not None:
            result['NodeRamRole'] = self.node_ram_role

        if self.node_root_password is not None:
            result['NodeRootPassword'] = self.node_root_password

        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration

        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.with_public_ip is not None:
            result['WithPublicIp'] = self.with_public_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.DiskInfo()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('NodeKeyPairName') is not None:
            self.node_key_pair_name = m.get('NodeKeyPairName')

        if m.get('NodeRamRole') is not None:
            self.node_ram_role = m.get('NodeRamRole')

        if m.get('NodeRootPassword') is not None:
            self.node_root_password = m.get('NodeRootPassword')

        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')

        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.SystemDiskParam()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('WithPublicIp') is not None:
            self.with_public_ip = m.get('WithPublicIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

