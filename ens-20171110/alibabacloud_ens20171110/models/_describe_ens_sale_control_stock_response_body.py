# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsSaleControlStockResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sale_control: List[main_models.DescribeEnsSaleControlStockResponseBodySaleControl] = None,
    ):
        self.request_id = request_id
        self.sale_control = sale_control

    def validate(self):
        if self.sale_control:
            for v1 in self.sale_control:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SaleControl'] = []
        if self.sale_control is not None:
            for k1 in self.sale_control:
                result['SaleControl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sale_control = []
        if m.get('SaleControl') is not None:
            for k1 in m.get('SaleControl'):
                temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControl()
                self.sale_control.append(temp_model.from_map(k1))

        return self

class DescribeEnsSaleControlStockResponseBodySaleControl(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        order_type: str = None,
        sale_control_items: List[main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItems] = None,
    ):
        self.commodity_code = commodity_code
        self.order_type = order_type
        self.sale_control_items = sale_control_items

    def validate(self):
        if self.sale_control_items:
            for v1 in self.sale_control_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        result['SaleControlItems'] = []
        if self.sale_control_items is not None:
            for k1 in self.sale_control_items:
                result['SaleControlItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        self.sale_control_items = []
        if m.get('SaleControlItems') is not None:
            for k1 in m.get('SaleControlItems'):
                temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItems()
                self.sale_control_items.append(temp_model.from_map(k1))

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItems(DaraModel):
    def __init__(
        self,
        module_code: str = None,
        sale_control_item: main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItem = None,
    ):
        self.module_code = module_code
        self.sale_control_item = sale_control_item

    def validate(self):
        if self.sale_control_item:
            self.sale_control_item.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.sale_control_item is not None:
            result['SaleControlItem'] = self.sale_control_item.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('SaleControlItem') is not None:
            temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItem()
            self.sale_control_item = temp_model.from_map(m.get('SaleControlItem'))

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItem(DaraModel):
    def __init__(
        self,
        basic_sale_control: main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControl = None,
        condition_sale_control: List[main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControl] = None,
    ):
        self.basic_sale_control = basic_sale_control
        self.condition_sale_control = condition_sale_control

    def validate(self):
        if self.basic_sale_control:
            self.basic_sale_control.validate()
        if self.condition_sale_control:
            for v1 in self.condition_sale_control:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_sale_control is not None:
            result['BasicSaleControl'] = self.basic_sale_control.to_map()

        result['ConditionSaleControl'] = []
        if self.condition_sale_control is not None:
            for k1 in self.condition_sale_control:
                result['ConditionSaleControl'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicSaleControl') is not None:
            temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControl()
            self.basic_sale_control = temp_model.from_map(m.get('BasicSaleControl'))

        self.condition_sale_control = []
        if m.get('ConditionSaleControl') is not None:
            for k1 in m.get('ConditionSaleControl'):
                temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControl()
                self.condition_sale_control.append(temp_model.from_map(k1))

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControl(DaraModel):
    def __init__(
        self,
        condition_control: main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlConditionControl = None,
        module_value: main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlModuleValue = None,
        stock_value: str = None,
    ):
        self.condition_control = condition_control
        self.module_value = module_value
        self.stock_value = stock_value

    def validate(self):
        if self.condition_control:
            self.condition_control.validate()
        if self.module_value:
            self.module_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_control is not None:
            result['ConditionControl'] = self.condition_control.to_map()

        if self.module_value is not None:
            result['ModuleValue'] = self.module_value.to_map()

        if self.stock_value is not None:
            result['StockValue'] = self.stock_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionControl') is not None:
            temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlConditionControl()
            self.condition_control = temp_model.from_map(m.get('ConditionControl'))

        if m.get('ModuleValue') is not None:
            temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlModuleValue()
            self.module_value = temp_model.from_map(m.get('ModuleValue'))

        if m.get('StockValue') is not None:
            self.stock_value = m.get('StockValue')

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlModuleValue(DaraModel):
    def __init__(
        self,
        module_max_value: str = None,
        module_min_value: str = None,
    ):
        self.module_max_value = module_max_value
        self.module_min_value = module_min_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleMaxValue') is not None:
            self.module_max_value = m.get('ModuleMaxValue')

        if m.get('ModuleMinValue') is not None:
            self.module_min_value = m.get('ModuleMinValue')

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemConditionSaleControlConditionControl(DaraModel):
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

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControl(DaraModel):
    def __init__(
        self,
        module_value: main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControlModuleValue = None,
        stock_value: str = None,
    ):
        self.module_value = module_value
        self.stock_value = stock_value

    def validate(self):
        if self.module_value:
            self.module_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_value is not None:
            result['ModuleValue'] = self.module_value.to_map()

        if self.stock_value is not None:
            result['StockValue'] = self.stock_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleValue') is not None:
            temp_model = main_models.DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControlModuleValue()
            self.module_value = temp_model.from_map(m.get('ModuleValue'))

        if m.get('StockValue') is not None:
            self.stock_value = m.get('StockValue')

        return self

class DescribeEnsSaleControlStockResponseBodySaleControlSaleControlItemsSaleControlItemBasicSaleControlModuleValue(DaraModel):
    def __init__(
        self,
        module_max_value: str = None,
        module_min_value: str = None,
    ):
        self.module_max_value = module_max_value
        self.module_min_value = module_min_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleMaxValue') is not None:
            self.module_max_value = m.get('ModuleMaxValue')

        if m.get('ModuleMinValue') is not None:
            self.module_min_value = m.get('ModuleMinValue')

        return self

