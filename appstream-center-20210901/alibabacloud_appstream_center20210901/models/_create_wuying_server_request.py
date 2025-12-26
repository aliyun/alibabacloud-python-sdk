# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateWuyingServerRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth: int = None,
        biz_region_id: str = None,
        charge_type: str = None,
        data_disk: List[main_models.CreateWuyingServerRequestDataDisk] = None,
        host_name: str = None,
        idempotence_token: str = None,
        image_id: str = None,
        max_price: float = None,
        network_strategy_type: str = None,
        office_site_id: str = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        saving_plan_id: str = None,
        server_instance_type: str = None,
        server_port_range: str = None,
        sub_pay_type: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        v_switch_ids: List[str] = None,
        virtual_node_pool_id: str = None,
        wuying_server_name: str = None,
    ):
        # Quantity.
        self.amount = amount
        # Auto payment.
        self.auto_pay = auto_pay
        # Auto-renewal.
        self.auto_renew = auto_renew
        # bandwidth value, the NetworkStrategyType is valid for DirectIp. Unit: Mbps, range 2~100
        self.bandwidth = bandwidth
        # Region.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PrePaid: subscription
        self.charge_type = charge_type
        # The list of data disks.
        self.data_disk = data_disk
        self.host_name = host_name
        # Idempotence token to ensure operation uniqueness
        self.idempotence_token = idempotence_token
        # The ID of the image.
        self.image_id = image_id
        self.max_price = max_price
        # The type of the network policy (in invitational preview).
        self.network_strategy_type = network_strategy_type
        # The office network IDs.
        self.office_site_id = office_site_id
        # Workstation login password.
        self.password = password
        # The subscription period.
        self.period = period
        # The time unit.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        self.period_unit = period_unit
        # The ID of the discount.
        # 
        # >  If PromotionId is set, it will try to apply the corresponding discount.
        self.promotion_id = promotion_id
        self.saving_plan_id = saving_plan_id
        # Workstation specifications.
        self.server_instance_type = server_instance_type
        self.server_port_range = server_port_range
        self.sub_pay_type = sub_pay_type
        # The system disk category.
        # 
        # Valid values:
        # 
        # *   cloud_auto.
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Unit: GB.
        self.system_disk_size = system_disk_size
        # The list of office network vSwitches.
        self.v_switch_ids = v_switch_ids
        self.virtual_node_pool_id = virtual_node_pool_id
        # The name of the workstation. The numeric suffix is automatically added when multiple workstations are created.
        self.wuying_server_name = wuying_server_name

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.idempotence_token is not None:
            result['IdempotenceToken'] = self.idempotence_token

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.network_strategy_type is not None:
            result['NetworkStrategyType'] = self.network_strategy_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.password is not None:
            result['Password'] = self.password

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.saving_plan_id is not None:
            result['SavingPlanId'] = self.saving_plan_id

        if self.server_instance_type is not None:
            result['ServerInstanceType'] = self.server_instance_type

        if self.server_port_range is not None:
            result['ServerPortRange'] = self.server_port_range

        if self.sub_pay_type is not None:
            result['SubPayType'] = self.sub_pay_type

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.virtual_node_pool_id is not None:
            result['VirtualNodePoolId'] = self.virtual_node_pool_id

        if self.wuying_server_name is not None:
            result['WuyingServerName'] = self.wuying_server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateWuyingServerRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('IdempotenceToken') is not None:
            self.idempotence_token = m.get('IdempotenceToken')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('NetworkStrategyType') is not None:
            self.network_strategy_type = m.get('NetworkStrategyType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SavingPlanId') is not None:
            self.saving_plan_id = m.get('SavingPlanId')

        if m.get('ServerInstanceType') is not None:
            self.server_instance_type = m.get('ServerInstanceType')

        if m.get('ServerPortRange') is not None:
            self.server_port_range = m.get('ServerPortRange')

        if m.get('SubPayType') is not None:
            self.sub_pay_type = m.get('SubPayType')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VirtualNodePoolId') is not None:
            self.virtual_node_pool_id = m.get('VirtualNodePoolId')

        if m.get('WuyingServerName') is not None:
            self.wuying_server_name = m.get('WuyingServerName')

        return self

class CreateWuyingServerRequestDataDisk(DaraModel):
    def __init__(
        self,
        data_disk_category: str = None,
        data_disk_performance_level: str = None,
        data_disk_size: int = None,
    ):
        # The data disk category.
        # 
        # Valid values:
        # 
        # *   cloud_auto.
        self.data_disk_category = data_disk_category
        # The PL of the data disk.
        self.data_disk_performance_level = data_disk_performance_level
        # The data disk size.
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.data_disk_performance_level is not None:
            result['DataDiskPerformanceLevel'] = self.data_disk_performance_level

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('DataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('DataDiskPerformanceLevel')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        return self

