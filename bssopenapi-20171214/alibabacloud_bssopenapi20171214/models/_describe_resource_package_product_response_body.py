# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeResourcePackageProductResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResourcePackageProductResponseBodyData = None,
        message: str = None,
        order_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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

        if self.order_id is not None:
            result['OrderId'] = self.order_id

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
            temp_model = main_models.DescribeResourcePackageProductResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourcePackageProductResponseBodyData(DaraModel):
    def __init__(
        self,
        resource_packages: main_models.DescribeResourcePackageProductResponseBodyDataResourcePackages = None,
    ):
        # The details about the resource plans.
        self.resource_packages = resource_packages

    def validate(self):
        if self.resource_packages:
            self.resource_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_packages is not None:
            result['ResourcePackages'] = self.resource_packages.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourcePackages') is not None:
            temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackages()
            self.resource_packages = temp_model.from_map(m.get('ResourcePackages'))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackages(DaraModel):
    def __init__(
        self,
        resource_package: List[main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage] = None,
    ):
        self.resource_package = resource_package

    def validate(self):
        if self.resource_package:
            for v1 in self.resource_package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourcePackage'] = []
        if self.resource_package is not None:
            for k1 in self.resource_package:
                result['ResourcePackage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package = []
        if m.get('ResourcePackage') is not None:
            for k1 in m.get('ResourcePackage'):
                temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage()
                self.resource_package.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage(DaraModel):
    def __init__(
        self,
        name: str = None,
        package_types: main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes = None,
        product_code: str = None,
        product_type: str = None,
    ):
        # The name of the resource plan.
        self.name = name
        # The types of the resource plans.
        self.package_types = package_types
        # The code of the service.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type

    def validate(self):
        if self.package_types:
            self.package_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.package_types is not None:
            result['PackageTypes'] = self.package_types.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageTypes') is not None:
            temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes()
            self.package_types = temp_model.from_map(m.get('PackageTypes'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes(DaraModel):
    def __init__(
        self,
        package_type: List[main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType] = None,
    ):
        self.package_type = package_type

    def validate(self):
        if self.package_type:
            for v1 in self.package_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PackageType'] = []
        if self.package_type is not None:
            for k1 in self.package_type:
                result['PackageType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package_type = []
        if m.get('PackageType') is not None:
            for k1 in m.get('PackageType'):
                temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType()
                self.package_type.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        properties: main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties = None,
        specifications: main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications = None,
    ):
        # The code of the resource plan.
        self.code = code
        # The name of the resource plan type.
        self.name = name
        # The properties of the resource plan.
        self.properties = properties
        # The specifications of the resource plan.
        self.specifications = specifications

    def validate(self):
        if self.properties:
            self.properties.validate()
        if self.specifications:
            self.specifications.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.specifications is not None:
            result['Specifications'] = self.specifications.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('Specifications') is not None:
            temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications()
            self.specifications = temp_model.from_map(m.get('Specifications'))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications(DaraModel):
    def __init__(
        self,
        specification: List[main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification] = None,
    ):
        self.specification = specification

    def validate(self):
        if self.specification:
            for v1 in self.specification:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Specification'] = []
        if self.specification is not None:
            for k1 in self.specification:
                result['Specification'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specification = []
        if m.get('Specification') is not None:
            for k1 in m.get('Specification'):
                temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification()
                self.specification.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification(DaraModel):
    def __init__(
        self,
        available_durations: main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations = None,
        name: str = None,
        value: str = None,
    ):
        # The validity periods available for the resource plan.
        self.available_durations = available_durations
        # The name of the specification.
        self.name = name
        # The value of the specification.
        self.value = value

    def validate(self):
        if self.available_durations:
            self.available_durations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_durations is not None:
            result['AvailableDurations'] = self.available_durations.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDurations') is not None:
            temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations()
            self.available_durations = temp_model.from_map(m.get('AvailableDurations'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations(DaraModel):
    def __init__(
        self,
        available_duration: List[main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration] = None,
    ):
        self.available_duration = available_duration

    def validate(self):
        if self.available_duration:
            for v1 in self.available_duration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableDuration'] = []
        if self.available_duration is not None:
            for k1 in self.available_duration:
                result['AvailableDuration'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_duration = []
        if m.get('AvailableDuration') is not None:
            for k1 in m.get('AvailableDuration'):
                temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration()
                self.available_duration.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration(DaraModel):
    def __init__(
        self,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The name of the validity period.
        self.name = name
        # The unit of the validity period for the resource plan. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month.
        self.unit = unit
        # The value of the validity period.
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

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties(DaraModel):
    def __init__(
        self,
        property: List[main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty] = None,
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
                temp_model = main_models.DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty()
                self.property.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the property.
        self.name = name
        # The value of the property.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

