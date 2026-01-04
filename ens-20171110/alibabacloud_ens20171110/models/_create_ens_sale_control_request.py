# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateEnsSaleControlRequest(DaraModel):
    def __init__(
        self,
        ali_uid_account: str = None,
        commodity_code: str = None,
        custom_account: str = None,
        sale_controls: List[main_models.CreateEnsSaleControlRequestSaleControls] = None,
    ):
        self.ali_uid_account = ali_uid_account
        # This parameter is required.
        self.commodity_code = commodity_code
        self.custom_account = custom_account
        # This parameter is required.
        self.sale_controls = sale_controls

    def validate(self):
        if self.sale_controls:
            for v1 in self.sale_controls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid_account is not None:
            result['AliUidAccount'] = self.ali_uid_account

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.custom_account is not None:
            result['CustomAccount'] = self.custom_account

        result['SaleControls'] = []
        if self.sale_controls is not None:
            for k1 in self.sale_controls:
                result['SaleControls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUidAccount') is not None:
            self.ali_uid_account = m.get('AliUidAccount')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CustomAccount') is not None:
            self.custom_account = m.get('CustomAccount')

        self.sale_controls = []
        if m.get('SaleControls') is not None:
            for k1 in m.get('SaleControls'):
                temp_model = main_models.CreateEnsSaleControlRequestSaleControls()
                self.sale_controls.append(temp_model.from_map(k1))

        return self

class CreateEnsSaleControlRequestSaleControls(DaraModel):
    def __init__(
        self,
        condition_controls: List[main_models.CreateEnsSaleControlRequestSaleControlsConditionControls] = None,
        description: str = None,
        module_code: str = None,
        module_value: main_models.CreateEnsSaleControlRequestSaleControlsModuleValue = None,
        operator: str = None,
        order_type: str = None,
    ):
        self.condition_controls = condition_controls
        self.description = description
        # This parameter is required.
        self.module_code = module_code
        # This parameter is required.
        self.module_value = module_value
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.order_type = order_type

    def validate(self):
        if self.condition_controls:
            for v1 in self.condition_controls:
                 if v1:
                    v1.validate()
        if self.module_value:
            self.module_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConditionControls'] = []
        if self.condition_controls is not None:
            for k1 in self.condition_controls:
                result['ConditionControls'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_value is not None:
            result['ModuleValue'] = self.module_value.to_map()

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.condition_controls = []
        if m.get('ConditionControls') is not None:
            for k1 in m.get('ConditionControls'):
                temp_model = main_models.CreateEnsSaleControlRequestSaleControlsConditionControls()
                self.condition_controls.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleValue') is not None:
            temp_model = main_models.CreateEnsSaleControlRequestSaleControlsModuleValue()
            self.module_value = temp_model.from_map(m.get('ModuleValue'))

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

class CreateEnsSaleControlRequestSaleControlsModuleValue(DaraModel):
    def __init__(
        self,
        module_max_value: str = None,
        module_min_value: str = None,
        module_value: List[str] = None,
    ):
        self.module_max_value = module_max_value
        self.module_min_value = module_min_value
        self.module_value = module_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_max_value is not None:
            result['ModuleMaxValue'] = self.module_max_value

        if self.module_min_value is not None:
            result['ModuleMinValue'] = self.module_min_value

        if self.module_value is not None:
            result['ModuleValue'] = self.module_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleMaxValue') is not None:
            self.module_max_value = m.get('ModuleMaxValue')

        if m.get('ModuleMinValue') is not None:
            self.module_min_value = m.get('ModuleMinValue')

        if m.get('ModuleValue') is not None:
            self.module_value = m.get('ModuleValue')

        return self

class CreateEnsSaleControlRequestSaleControlsConditionControls(DaraModel):
    def __init__(
        self,
        condition_control_module_code: str = None,
        condition_control_module_value: str = None,
    ):
        self.condition_control_module_code = condition_control_module_code
        self.condition_control_module_value = condition_control_module_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_control_module_code is not None:
            result['ConditionControlModuleCode'] = self.condition_control_module_code

        if self.condition_control_module_value is not None:
            result['ConditionControlModuleValue'] = self.condition_control_module_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionControlModuleCode') is not None:
            self.condition_control_module_code = m.get('ConditionControlModuleCode')

        if m.get('ConditionControlModuleValue') is not None:
            self.condition_control_module_value = m.get('ConditionControlModuleValue')

        return self

