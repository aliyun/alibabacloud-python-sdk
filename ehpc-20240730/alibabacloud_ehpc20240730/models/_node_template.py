# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class NodeTemplate(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        data_disks: List[main_models.NodeTemplateDataDisks] = None,
        duration: int = None,
        enable_ht: bool = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        period: int = None,
        period_unit: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        system_disk: main_models.NodeTemplateSystemDisk = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.data_disks = data_disks
        self.duration = duration
        self.enable_ht = enable_ht
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.period = period
        self.period_unit = period_unit
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk = system_disk

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

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.NodeTemplateDataDisks()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.NodeTemplateSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        return self

class NodeTemplateSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        level: str = None,
        size: int = None,
    ):
        self.category = category
        self.level = level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.level is not None:
            result['Level'] = self.level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class NodeTemplateDataDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        delete_with_instance: bool = None,
        device: str = None,
        level: str = None,
        mount_dir: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.category = category
        self.delete_with_instance = delete_with_instance
        self.device = device
        self.level = level
        self.mount_dir = mount_dir
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.device is not None:
            result['Device'] = self.device

        if self.level is not None:
            result['Level'] = self.level

        if self.mount_dir is not None:
            result['MountDir'] = self.mount_dir

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MountDir') is not None:
            self.mount_dir = m.get('MountDir')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

