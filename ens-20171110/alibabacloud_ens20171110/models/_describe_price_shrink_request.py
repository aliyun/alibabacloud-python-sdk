# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.DescribePriceShrinkRequestDataDisk] = None,
        system_disk: main_models.DescribePriceShrinkRequestSystemDisk = None,
        data_disks_shrink: str = None,
        ens_region_id: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        quantity: int = None,
    ):
        self.data_disk = data_disk
        self.system_disk = system_disk
        # If you leave DataDisk.1.Size empty, the value that you specified for this parameter is used.
        self.data_disks_shrink = data_disks_shrink
        # The ID of the ENS node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The specifications of instances.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The bandwidth metering method of the instance. Valid values:
        # 
        # *   BandwidthByDay: Pay by daily peak bandwidth
        # *   95BandwidthByMonth: Pay by monthly 95th percentile bandwidth
        # *   PayByBandwidth4thMonth: Pay by monthly fourth peak bandwidth
        # *   PayByBandwidth: Pay by fixed bandwidth
        # 
        # This parameter is required.
        self.internet_charge_type = internet_charge_type
        # The subscription duration of the instance.
        # 
        # *   If you leave the PeriodUnit parameter empty, the instance is purchased on a monthly basis. Valid values: Day and Month.
        # *   If you set PeriodUnit to Day, you can set Period only to 3.
        # *   If you set PeriodUnit to Month, you can set Period to a number from 1 to 9, or set Period to 12.
        # 
        # This parameter is required.
        self.period = period
        # The billing cycle of the ENS instance. Valid values:
        # 
        # *   Month (default):
        # *   Day
        self.period_unit = period_unit
        # The number of instances.
        # 
        # This parameter is required.
        self.quantity = quantity

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.data_disks_shrink is not None:
            result['DataDisks'] = self.data_disks_shrink

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.DescribePriceShrinkRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.DescribePriceShrinkRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('DataDisks') is not None:
            self.data_disks_shrink = m.get('DataDisks')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

class DescribePriceShrinkRequestSystemDisk(DaraModel):
    def __init__(
        self,
        size: int = None,
    ):
        # The size of the system disk. Unit: GB.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribePriceShrinkRequestDataDisk(DaraModel):
    def __init__(
        self,
        size: int = None,
    ):
        # The size of the data disk. Unit: GB. If you specify this parameter, this parameter takes precedence over the Size property in DataDisks.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

