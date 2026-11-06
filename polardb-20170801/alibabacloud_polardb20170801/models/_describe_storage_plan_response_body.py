# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeStoragePlanResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeStoragePlanResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of storage plans.
        self.items = items
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeStoragePlanResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeStoragePlanResponseBodyItems(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        commodity_code: str = None,
        end_times: str = None,
        init_capa_city_view_unit: str = None,
        init_capacity_view_value: str = None,
        instance_id: str = None,
        period_capa_city_view_unit: str = None,
        period_capacity_view_value: str = None,
        period_time: str = None,
        prod_code: str = None,
        purchase_times: str = None,
        start_times: str = None,
        status: str = None,
        storage_type: str = None,
        template_name: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The commodity code.
        self.commodity_code = commodity_code
        # The expiration time of the storage plan.
        self.end_times = end_times
        # The capacity unit of the storage plan.
        self.init_capa_city_view_unit = init_capa_city_view_unit
        # The total capacity of the storage plan.
        self.init_capacity_view_value = init_capacity_view_value
        # The instance ID.
        self.instance_id = instance_id
        # The periodic capacity unit of the storage plan.
        self.period_capa_city_view_unit = period_capa_city_view_unit
        # The periodic capacity of the storage plan. The periodic capacity gradually decreases as the storage plan is used.
        self.period_capacity_view_value = period_capacity_view_value
        # The period duration, which indicates that the capacity of the storage plan is measured and consumed on an hourly basis.
        self.period_time = period_time
        # The product name.
        self.prod_code = prod_code
        # The purchase time of the storage plan.
        self.purchase_times = purchase_times
        # The effective period of the storage plan.
        self.start_times = start_times
        # The status of the storage plan. Valid values:
        # 
        # - **Valid**: The storage plan is valid.
        # 
        # - **Invalid**: The storage plan is invalid.
        self.status = status
        # The type of the storage plan. Valid values:
        # 
        # - **Overseas**: Hong Kong (China) and regions outside the Chinese mainland.
        # 
        # - **Mainland**: The Chinese mainland.
        # 
        # - **Financial**: Alibaba Finance Cloud.
        self.storage_type = storage_type
        # The type of the resource plan. Valid values:
        # 
        #  - **FPT_polardb_package_absolute_1540888383**: The Chinese mainland.
        # 
        # - **FPT_polardb_package_absolute_1540890081**: Hong Kong (China) and regions outside the Chinese mainland.
        # 
        # - **FPT_polardb_package_absolute_1567151499**: Alibaba Finance Cloud.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.end_times is not None:
            result['EndTimes'] = self.end_times

        if self.init_capa_city_view_unit is not None:
            result['InitCapaCityViewUnit'] = self.init_capa_city_view_unit

        if self.init_capacity_view_value is not None:
            result['InitCapacityViewValue'] = self.init_capacity_view_value

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period_capa_city_view_unit is not None:
            result['PeriodCapaCityViewUnit'] = self.period_capa_city_view_unit

        if self.period_capacity_view_value is not None:
            result['PeriodCapacityViewValue'] = self.period_capacity_view_value

        if self.period_time is not None:
            result['PeriodTime'] = self.period_time

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.purchase_times is not None:
            result['PurchaseTimes'] = self.purchase_times

        if self.start_times is not None:
            result['StartTimes'] = self.start_times

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('EndTimes') is not None:
            self.end_times = m.get('EndTimes')

        if m.get('InitCapaCityViewUnit') is not None:
            self.init_capa_city_view_unit = m.get('InitCapaCityViewUnit')

        if m.get('InitCapacityViewValue') is not None:
            self.init_capacity_view_value = m.get('InitCapacityViewValue')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PeriodCapaCityViewUnit') is not None:
            self.period_capa_city_view_unit = m.get('PeriodCapaCityViewUnit')

        if m.get('PeriodCapacityViewValue') is not None:
            self.period_capacity_view_value = m.get('PeriodCapacityViewValue')

        if m.get('PeriodTime') is not None:
            self.period_time = m.get('PeriodTime')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('PurchaseTimes') is not None:
            self.purchase_times = m.get('PurchaseTimes')

        if m.get('StartTimes') is not None:
            self.start_times = m.get('StartTimes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

