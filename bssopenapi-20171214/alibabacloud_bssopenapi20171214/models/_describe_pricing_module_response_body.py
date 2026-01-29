# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribePricingModuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePricingModuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePricingModuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribePricingModuleResponseBodyData(DaraModel):
    def __init__(
        self,
        attribute_list: main_models.DescribePricingModuleResponseBodyDataAttributeList = None,
        module_list: main_models.DescribePricingModuleResponseBodyDataModuleList = None,
    ):
        # The module attributes.
        self.attribute_list = attribute_list
        # The pricing information of modules.
        self.module_list = module_list

    def validate(self):
        if self.attribute_list:
            self.attribute_list.validate()
        if self.module_list:
            self.module_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_list is not None:
            result['AttributeList'] = self.attribute_list.to_map()

        if self.module_list is not None:
            result['ModuleList'] = self.module_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeList') is not None:
            temp_model = main_models.DescribePricingModuleResponseBodyDataAttributeList()
            self.attribute_list = temp_model.from_map(m.get('AttributeList'))

        if m.get('ModuleList') is not None:
            temp_model = main_models.DescribePricingModuleResponseBodyDataModuleList()
            self.module_list = temp_model.from_map(m.get('ModuleList'))

        return self

class DescribePricingModuleResponseBodyDataModuleList(DaraModel):
    def __init__(
        self,
        module: List[main_models.DescribePricingModuleResponseBodyDataModuleListModule] = None,
    ):
        self.module = module

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.DescribePricingModuleResponseBodyDataModuleListModule()
                self.module.append(temp_model.from_map(k1))

        return self

class DescribePricingModuleResponseBodyDataModuleListModule(DaraModel):
    def __init__(
        self,
        config_list: main_models.DescribePricingModuleResponseBodyDataModuleListModuleConfigList = None,
        currency: str = None,
        module_code: str = None,
        module_name: str = None,
        price_type: str = None,
    ):
        self.config_list = config_list
        # The currency. Default value: CNY.
        self.currency = currency
        # The code of the pricing module.
        self.module_code = module_code
        # The name of the pricing module.
        self.module_name = module_name
        # The price type. Valid values:
        # 
        # *   Usage: usage price
        # *   Hour: hourly price
        # *   Day: daily price
        # *   Week: weekly price
        # *   Month: monthly price
        # *   Year: annual price
        self.price_type = price_type

    def validate(self):
        if self.config_list:
            self.config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_list is not None:
            result['ConfigList'] = self.config_list.to_map()

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.price_type is not None:
            result['PriceType'] = self.price_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            temp_model = main_models.DescribePricingModuleResponseBodyDataModuleListModuleConfigList()
            self.config_list = temp_model.from_map(m.get('ConfigList'))

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')

        return self

class DescribePricingModuleResponseBodyDataModuleListModuleConfigList(DaraModel):
    def __init__(
        self,
        config_list: List[str] = None,
    ):
        self.config_list = config_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        return self

class DescribePricingModuleResponseBodyDataAttributeList(DaraModel):
    def __init__(
        self,
        attribute: List[main_models.DescribePricingModuleResponseBodyDataAttributeListAttribute] = None,
    ):
        self.attribute = attribute

    def validate(self):
        if self.attribute:
            for v1 in self.attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attribute'] = []
        if self.attribute is not None:
            for k1 in self.attribute:
                result['Attribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute = []
        if m.get('Attribute') is not None:
            for k1 in m.get('Attribute'):
                temp_model = main_models.DescribePricingModuleResponseBodyDataAttributeListAttribute()
                self.attribute.append(temp_model.from_map(k1))

        return self

class DescribePricingModuleResponseBodyDataAttributeListAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        unit: str = None,
        values: main_models.DescribePricingModuleResponseBodyDataAttributeListAttributeValues = None,
    ):
        # The code of the attribute.
        self.code = code
        # The name of the attribute.
        self.name = name
        # The unit of the attribute.
        self.unit = unit
        # The attribute values.
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.values is not None:
            result['Values'] = self.values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Values') is not None:
            temp_model = main_models.DescribePricingModuleResponseBodyDataAttributeListAttributeValues()
            self.values = temp_model.from_map(m.get('Values'))

        return self

class DescribePricingModuleResponseBodyDataAttributeListAttributeValues(DaraModel):
    def __init__(
        self,
        attribute_value: List[main_models.DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue] = None,
    ):
        self.attribute_value = attribute_value

    def validate(self):
        if self.attribute_value:
            for v1 in self.attribute_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeValue'] = []
        if self.attribute_value is not None:
            for k1 in self.attribute_value:
                result['AttributeValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_value = []
        if m.get('AttributeValue') is not None:
            for k1 in m.get('AttributeValue'):
                temp_model = main_models.DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue()
                self.attribute_value.append(temp_model.from_map(k1))

        return self

class DescribePricingModuleResponseBodyDataAttributeListAttributeValuesAttributeValue(DaraModel):
    def __init__(
        self,
        name: str = None,
        remark: str = None,
        type: str = None,
        value: str = None,
    ):
        # The attribute value that corresponds to the module code.
        self.name = name
        # The description of the module values.
        self.remark = remark
        # The type of the attribute value that corresponds to the module code. Valid values:
        # 
        # *   single_float: single value
        # *   range_float: range value
        self.type = type
        # The attribute value that corresponds to the module code.
        # 
        # >  If the Type parameter is set to range_float, the valid values of this parameter range from 1024 to 1024000. A value of 1024 indicates that the step size is 1024.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

