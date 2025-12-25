# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeChargeModuleResponseBody(DaraModel):
    def __init__(
        self,
        charge_modules: List[main_models.DescribeChargeModuleResponseBodyChargeModules] = None,
        request_id: str = None,
    ):
        self.charge_modules = charge_modules
        self.request_id = request_id

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
        result['ChargeModules'] = []
        if self.charge_modules is not None:
            for k1 in self.charge_modules:
                result['ChargeModules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.charge_modules = []
        if m.get('ChargeModules') is not None:
            for k1 in m.get('ChargeModules'):
                temp_model = main_models.DescribeChargeModuleResponseBodyChargeModules()
                self.charge_modules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChargeModuleResponseBodyChargeModules(DaraModel):
    def __init__(
        self,
        charge_mode: str = None,
        charge_mode_details: List[str] = None,
        module_code: str = None,
        period_type: str = None,
        usage_type: str = None,
        usage_unit_factor: int = None,
    ):
        self.charge_mode = charge_mode
        self.charge_mode_details = charge_mode_details
        self.module_code = module_code
        self.period_type = period_type
        self.usage_type = usage_type
        self.usage_unit_factor = usage_unit_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_mode is not None:
            result['ChargeMode'] = self.charge_mode

        if self.charge_mode_details is not None:
            result['ChargeModeDetails'] = self.charge_mode_details

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        if self.usage_unit_factor is not None:
            result['UsageUnitFactor'] = self.usage_unit_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeMode') is not None:
            self.charge_mode = m.get('ChargeMode')

        if m.get('ChargeModeDetails') is not None:
            self.charge_mode_details = m.get('ChargeModeDetails')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        if m.get('UsageUnitFactor') is not None:
            self.usage_unit_factor = m.get('UsageUnitFactor')

        return self

