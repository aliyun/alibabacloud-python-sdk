# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeLicenseResponseBody(DaraModel):
    def __init__(
        self,
        license: main_models.DescribeLicenseResponseBodyLicense = None,
        request_id: str = None,
    ):
        self.license = license
        self.request_id = request_id

    def validate(self):
        if self.license:
            self.license.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license is not None:
            result['License'] = self.license.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('License') is not None:
            temp_model = main_models.DescribeLicenseResponseBodyLicense()
            self.license = temp_model.from_map(m.get('License'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLicenseResponseBodyLicense(DaraModel):
    def __init__(
        self,
        activate_time: str = None,
        create_time: str = None,
        expired_time: str = None,
        extend_array: main_models.DescribeLicenseResponseBodyLicenseExtendArray = None,
        extend_info: main_models.DescribeLicenseResponseBodyLicenseExtendInfo = None,
        instance_id: str = None,
        license_code: str = None,
        license_status: str = None,
        product_code: str = None,
        product_name: str = None,
        product_sku_id: str = None,
        supplier_name: str = None,
    ):
        self.activate_time = activate_time
        self.create_time = create_time
        self.expired_time = expired_time
        self.extend_array = extend_array
        self.extend_info = extend_info
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_status = license_status
        self.product_code = product_code
        self.product_name = product_name
        self.product_sku_id = product_sku_id
        self.supplier_name = supplier_name

    def validate(self):
        if self.extend_array:
            self.extend_array.validate()
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.extend_array is not None:
            result['ExtendArray'] = self.extend_array.to_map()

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.license_status is not None:
            result['LicenseStatus'] = self.license_status

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.product_sku_id is not None:
            result['ProductSkuId'] = self.product_sku_id

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('ExtendArray') is not None:
            temp_model = main_models.DescribeLicenseResponseBodyLicenseExtendArray()
            self.extend_array = temp_model.from_map(m.get('ExtendArray'))

        if m.get('ExtendInfo') is not None:
            temp_model = main_models.DescribeLicenseResponseBodyLicenseExtendInfo()
            self.extend_info = temp_model.from_map(m.get('ExtendInfo'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('LicenseStatus') is not None:
            self.license_status = m.get('LicenseStatus')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('ProductSkuId') is not None:
            self.product_sku_id = m.get('ProductSkuId')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        return self

class DescribeLicenseResponseBodyLicenseExtendInfo(DaraModel):
    def __init__(
        self,
        account_quantity: int = None,
        ali_uid: int = None,
        email: str = None,
        mobile: str = None,
    ):
        self.account_quantity = account_quantity
        self.ali_uid = ali_uid
        self.email = email
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.email is not None:
            result['Email'] = self.email

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        return self

class DescribeLicenseResponseBodyLicenseExtendArray(DaraModel):
    def __init__(
        self,
        license_attribute: List[main_models.DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute] = None,
    ):
        self.license_attribute = license_attribute

    def validate(self):
        if self.license_attribute:
            for v1 in self.license_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LicenseAttribute'] = []
        if self.license_attribute is not None:
            for k1 in self.license_attribute:
                result['LicenseAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.license_attribute = []
        if m.get('LicenseAttribute') is not None:
            for k1 in m.get('LicenseAttribute'):
                temp_model = main_models.DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute()
                self.license_attribute.append(temp_model.from_map(k1))

        return self

class DescribeLicenseResponseBodyLicenseExtendArrayLicenseAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        self.code = code
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

