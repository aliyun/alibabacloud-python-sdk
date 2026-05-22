# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceResponseBody(DaraModel):
    def __init__(
        self,
        active_address: str = None,
        app_json: str = None,
        auto_renewal: str = None,
        began_on: int = None,
        component_json: str = None,
        constraints: str = None,
        created_on: int = None,
        end_on: int = None,
        extend_json: str = None,
        host_json: str = None,
        instance_id: int = None,
        is_trial: bool = None,
        license_code: str = None,
        modules: main_models.DescribeInstanceResponseBodyModules = None,
        order_id: int = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_code: str = None,
        product_type: str = None,
        relational_data: main_models.DescribeInstanceResponseBodyRelationalData = None,
        status: str = None,
        supplier_name: str = None,
    ):
        self.active_address = active_address
        self.app_json = app_json
        self.auto_renewal = auto_renewal
        self.began_on = began_on
        self.component_json = component_json
        self.constraints = constraints
        self.created_on = created_on
        self.end_on = end_on
        self.extend_json = extend_json
        self.host_json = host_json
        self.instance_id = instance_id
        self.is_trial = is_trial
        self.license_code = license_code
        self.modules = modules
        self.order_id = order_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_code = product_sku_code
        self.product_type = product_type
        self.relational_data = relational_data
        self.status = status
        self.supplier_name = supplier_name

    def validate(self):
        if self.modules:
            self.modules.validate()
        if self.relational_data:
            self.relational_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address is not None:
            result['ActiveAddress'] = self.active_address

        if self.app_json is not None:
            result['AppJson'] = self.app_json

        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal

        if self.began_on is not None:
            result['BeganOn'] = self.began_on

        if self.component_json is not None:
            result['ComponentJson'] = self.component_json

        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.created_on is not None:
            result['CreatedOn'] = self.created_on

        if self.end_on is not None:
            result['EndOn'] = self.end_on

        if self.extend_json is not None:
            result['ExtendJson'] = self.extend_json

        if self.host_json is not None:
            result['HostJson'] = self.host_json

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.modules is not None:
            result['Modules'] = self.modules.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_sku_code is not None:
            result['ProductSkuCode'] = self.product_sku_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.relational_data is not None:
            result['RelationalData'] = self.relational_data.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddress') is not None:
            self.active_address = m.get('ActiveAddress')

        if m.get('AppJson') is not None:
            self.app_json = m.get('AppJson')

        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')

        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')

        if m.get('ComponentJson') is not None:
            self.component_json = m.get('ComponentJson')

        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')

        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')

        if m.get('ExtendJson') is not None:
            self.extend_json = m.get('ExtendJson')

        if m.get('HostJson') is not None:
            self.host_json = m.get('HostJson')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('Modules') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyModules()
            self.modules = temp_model.from_map(m.get('Modules'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductSkuCode') is not None:
            self.product_sku_code = m.get('ProductSkuCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RelationalData') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyRelationalData()
            self.relational_data = temp_model.from_map(m.get('RelationalData'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        return self

class DescribeInstanceResponseBodyRelationalData(DaraModel):
    def __init__(
        self,
        service_status: str = None,
    ):
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

class DescribeInstanceResponseBodyModules(DaraModel):
    def __init__(
        self,
        module: List[main_models.DescribeInstanceResponseBodyModulesModule] = None,
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
                temp_model = main_models.DescribeInstanceResponseBodyModulesModule()
                self.module.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyModulesModule(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        name: str = None,
        properties: main_models.DescribeInstanceResponseBodyModulesModuleProperties = None,
    ):
        self.code = code
        self.id = id
        self.name = name
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyModulesModuleProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        return self

class DescribeInstanceResponseBodyModulesModuleProperties(DaraModel):
    def __init__(
        self,
        property: List[main_models.DescribeInstanceResponseBodyModulesModulePropertiesProperty] = None,
    ):
        self.property = property

    def validate(self):
        if self.property:
            for v1 in self.property:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Property'] = []
        if self.property is not None:
            for k1 in self.property:
                result['Property'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k1 in m.get('Property'):
                temp_model = main_models.DescribeInstanceResponseBodyModulesModulePropertiesProperty()
                self.property.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyModulesModulePropertiesProperty(DaraModel):
    def __init__(
        self,
        display_unit: str = None,
        key: str = None,
        name: str = None,
        property_values: main_models.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues = None,
        show_type: str = None,
    ):
        self.display_unit = display_unit
        self.key = key
        self.name = name
        self.property_values = property_values
        self.show_type = show_type

    def validate(self):
        if self.property_values:
            self.property_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_unit is not None:
            result['DisplayUnit'] = self.display_unit

        if self.key is not None:
            result['Key'] = self.key

        if self.name is not None:
            result['Name'] = self.name

        if self.property_values is not None:
            result['PropertyValues'] = self.property_values.to_map()

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayUnit') is not None:
            self.display_unit = m.get('DisplayUnit')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PropertyValues') is not None:
            temp_model = main_models.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues()
            self.property_values = temp_model.from_map(m.get('PropertyValues'))

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        return self

class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValues(DaraModel):
    def __init__(
        self,
        property_value: List[main_models.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue] = None,
    ):
        self.property_value = property_value

    def validate(self):
        if self.property_value:
            for v1 in self.property_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyValue'] = []
        if self.property_value is not None:
            for k1 in self.property_value:
                result['PropertyValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value = []
        if m.get('PropertyValue') is not None:
            for k1 in m.get('PropertyValue'):
                temp_model = main_models.DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue()
                self.property_value.append(temp_model.from_map(k1))

        return self

class DescribeInstanceResponseBodyModulesModulePropertiesPropertyPropertyValuesPropertyValue(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        max: str = None,
        min: str = None,
        remark: str = None,
        step: str = None,
        type: str = None,
        value: str = None,
    ):
        self.display_name = display_name
        self.max = max
        self.min = min
        self.remark = remark
        self.step = step
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.step is not None:
            result['Step'] = self.step

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

