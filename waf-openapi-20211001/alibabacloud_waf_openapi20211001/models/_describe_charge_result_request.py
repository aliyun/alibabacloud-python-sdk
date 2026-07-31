# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeChargeResultRequest(DaraModel):
    def __init__(
        self,
        charge_cycle: str = None,
        charge_modules: List[main_models.DescribeChargeResultRequestChargeModules] = None,
        charge_unit: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # The billing cycle for the calculation. Valid values:
        # - **Year**: Calculates the billing result for one year.
        # - **Month**: Calculates the billing result for one month.
        # - **Day**: Calculates the billing result for one day.
        self.charge_cycle = charge_cycle
        # The list of billing modules to calculate.
        # 
        # This parameter is required.
        self.charge_modules = charge_modules
        # The metering unit.
        self.charge_unit = charge_unit
        # The billing type of the instance. Valid values:
        # - **POSTPAY**: pay-as-you-go WAF instance.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        if self.charge_modules:
            for v1 in self.charge_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_cycle is not None:
            result['ChargeCycle'] = self.charge_cycle

        result['ChargeModules'] = []
        if self.charge_modules is not None:
            for k1 in self.charge_modules:
                result['ChargeModules'].append(k1.to_map() if k1 else None)

        if self.charge_unit is not None:
            result['ChargeUnit'] = self.charge_unit

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeCycle') is not None:
            self.charge_cycle = m.get('ChargeCycle')

        self.charge_modules = []
        if m.get('ChargeModules') is not None:
            for k1 in m.get('ChargeModules'):
                temp_model = main_models.DescribeChargeResultRequestChargeModules()
                self.charge_modules.append(temp_model.from_map(k1))

        if m.get('ChargeUnit') is not None:
            self.charge_unit = m.get('ChargeUnit')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

class DescribeChargeResultRequestChargeModules(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        usage: int = None,
    ):
        # The pricing module identifier.
        self.module_code = module_code
        # The usage of the pricing module.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

