# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryResourcePackageInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryResourcePackageInstancesResponseBodyData = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page = page
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of returned entries.
        self.total = total

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

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryResourcePackageInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryResourcePackageInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        instances: main_models.QueryResourcePackageInstancesResponseBodyDataInstances = None,
        page_num: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The ID of the host.
        self.host_id = host_id
        # The details of the instances.
        self.instances = instances
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Instances') is not None:
            temp_model = main_models.QueryResourcePackageInstancesResponseBodyDataInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryResourcePackageInstancesResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.QueryResourcePackageInstancesResponseBodyDataInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.QueryResourcePackageInstancesResponseBodyDataInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class QueryResourcePackageInstancesResponseBodyDataInstancesInstance(DaraModel):
    def __init__(
        self,
        applicable_products: main_models.QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts = None,
        commodity_code: str = None,
        deduct_type: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        instance_id: str = None,
        package_type: str = None,
        region: str = None,
        remaining_amount: str = None,
        remaining_amount_unit: str = None,
        remark: str = None,
        status: str = None,
        total_amount: str = None,
        total_amount_unit: str = None,
    ):
        # The services to which the resource plan is applicable.
        self.applicable_products = applicable_products
        # The commodity code.
        self.commodity_code = commodity_code
        # The deduction type. Example: Absolute.
        self.deduct_type = deduct_type
        # The time when the resource plan took effect.
        self.effective_time = effective_time
        # The time when the resource plan expired.
        self.expiry_time = expiry_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The type of the resource plan.
        self.package_type = package_type
        # The ID of the region.
        self.region = region
        # The remaining quota.
        self.remaining_amount = remaining_amount
        # The unit of the remaining quota.
        self.remaining_amount_unit = remaining_amount_unit
        # The remarks on the resource plan. The remarks must be made in Chinese.
        self.remark = remark
        # The status of the resource plan. Valid values:
        # 
        # *   Available
        # *   Expired
        self.status = status
        # The total quota of the resource plan.
        self.total_amount = total_amount
        # The unit of the total quota.
        self.total_amount_unit = total_amount_unit

    def validate(self):
        if self.applicable_products:
            self.applicable_products.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.deduct_type is not None:
            result['DeductType'] = self.deduct_type

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.region is not None:
            result['Region'] = self.region

        if self.remaining_amount is not None:
            result['RemainingAmount'] = self.remaining_amount

        if self.remaining_amount_unit is not None:
            result['RemainingAmountUnit'] = self.remaining_amount_unit

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.total_amount_unit is not None:
            result['TotalAmountUnit'] = self.total_amount_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            temp_model = main_models.QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts()
            self.applicable_products = temp_model.from_map(m.get('ApplicableProducts'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DeductType') is not None:
            self.deduct_type = m.get('DeductType')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RemainingAmount') is not None:
            self.remaining_amount = m.get('RemainingAmount')

        if m.get('RemainingAmountUnit') is not None:
            self.remaining_amount_unit = m.get('RemainingAmountUnit')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('TotalAmountUnit') is not None:
            self.total_amount_unit = m.get('TotalAmountUnit')

        return self

class QueryResourcePackageInstancesResponseBodyDataInstancesInstanceApplicableProducts(DaraModel):
    def __init__(
        self,
        product: List[str] = None,
    ):
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['Product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')

        return self

