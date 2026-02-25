# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class RestoreInstanceRequest(DaraModel):
    def __init__(
        self,
        admin_password: str = None,
        auto_renew: bool = None,
        backup_task_id: str = None,
        duration: int = None,
        instance_name: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.RestoreInstanceRequestTags] = None,
        v_switches: List[main_models.RestoreInstanceRequestVSwitches] = None,
        vpc_id: str = None,
    ):
        self.admin_password = admin_password
        self.auto_renew = auto_renew
        self.backup_task_id = backup_task_id
        self.duration = duration
        self.instance_name = instance_name
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tags = tags
        self.v_switches = v_switches
        # vpc ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.v_switches:
            for v1 in self.v_switches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.backup_task_id is not None:
            result['BackupTaskId'] = self.backup_task_id

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['VSwitches'] = []
        if self.v_switches is not None:
            for k1 in self.v_switches:
                result['VSwitches'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BackupTaskId') is not None:
            self.backup_task_id = m.get('BackupTaskId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.RestoreInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k1 in m.get('VSwitches'):
                temp_model = main_models.RestoreInstanceRequestVSwitches()
                self.v_switches.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class RestoreInstanceRequestVSwitches(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class RestoreInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

