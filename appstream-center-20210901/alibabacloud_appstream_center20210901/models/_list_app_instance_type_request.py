# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppInstanceTypeRequest(DaraModel):
    def __init__(
        self,
        app_center_image_id: str = None,
        app_instance_type: str = None,
        app_instance_type_family: str = None,
        app_instance_type_list: List[str] = None,
        biz_region_id: str = None,
        category: str = None,
        charge_type: str = None,
        cpu: str = None,
        gpu_memory: int = None,
        language: str = None,
        memory: int = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        query_inventory: bool = None,
    ):
        # The application image ID. The current session instance type query does not filter based on this parameter. Omit this parameter. Do not infer image compatibility based on whether this parameter is specified.
        self.app_center_image_id = app_center_image_id
        # The session instance type code. Exact match is performed based on the complete code. If this parameter and `AppInstanceTypeList` are specified at the same time, the results are filtered by intersection. You can perform a conditional query without this condition first, and then select the returned codes.
        self.app_instance_type = app_instance_type
        # The instance type family code. Exact match is performed based on the complete code. Use the instance type family value from the query results. Do not extract it from the instance type name.
        self.app_instance_type_family = app_instance_type_family
        # The list of session instance type codes. A maximum of 100 items are supported. This parameter takes effect by intersection with other filtering conditions. If this parameter and `AppInstanceType` are specified at the same time, the results must also match the single code.
        self.app_instance_type_list = app_instance_type_list
        # The business region ID. If this parameter is omitted, the region of the current request is used. The available instance types may vary by region and account. You can call the [ListRegions](https://api.aliyun.com/document/appstream-center/2021-09-01/ListRegions) operation to obtain the business region ID.
        self.biz_region_id = biz_region_id
        # The instance type category filtering condition. If this parameter is omitted, no category filtering condition is added. Valid values:
        # 
        # - `Cpu`: CPU instance type.
        # - `Gpu`: GPU instance type.
        self.category = category
        # The billing method used to filter available instance types. If this parameter is omitted, no billing method condition is added. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        self.charge_type = charge_type
        # The number of CPU cores for exact filtering. Use a decimal numeric string. Unit: cores. If this parameter is omitted, the number of CPU cores is not limited.
        self.cpu = cpu
        # The GPU memory capacity for exact filtering. Unit: MB. If this parameter is omitted, the GPU memory capacity is not limited.
        self.gpu_memory = gpu_memory
        # The language of the instance type name.
        # 
        # - `zh-CN`: Use the Chinese name of the instance type.
        # - Other values or omitted: Use the instance type code as the name.
        # 
        # This parameter only affects the display of `InstanceTypeName` and does not change the instance type code.
        self.language = language
        # The memory capacity for exact filtering. Unit: MB. If this parameter is omitted, the memory capacity is not limited.
        self.memory = memory
        # The operating system type. In the Wuying Cloud Application (CloudApp) scenario, set the value to:
        # 
        # - `Windows`: Windows operating system.
        # 
        # If this parameter is omitted, no operating system filtering condition is added.
        self.os_type = os_type
        # The page number. Explicitly specify a page number starting from 1. If this parameter is omitted, the default value 0 is used to query the first batch of results. For subsequent pages, request in the order of 1, 2, and 3.
        self.page_number = page_number
        # The number of instance types returned per page. Unit: entries. Default value: 200. Explicitly set a positive integer that meets your business requirements. The default value here does not represent the maximum value allowed by the service.
        self.page_size = page_size
        # The product type. Set the value to the following fixed value when you call this operation:
        # 
        # - `CloudApp`: Wuying Cloud Application.
        # 
        # This parameter is required.
        self.product_type = product_type
        # Specifies whether to query the instance type inventory at the same time. Default value: `false`.
        # 
        # - `true`: Queries the inventory and returns InventoryInfo when the inventory information is available.
        # - `false`: Queries only the instance types and does not query the inventory.
        self.query_inventory = query_inventory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id

        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        if self.app_instance_type_family is not None:
            result['AppInstanceTypeFamily'] = self.app_instance_type_family

        if self.app_instance_type_list is not None:
            result['AppInstanceTypeList'] = self.app_instance_type_list

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.category is not None:
            result['Category'] = self.category

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.language is not None:
            result['Language'] = self.language

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.query_inventory is not None:
            result['QueryInventory'] = self.query_inventory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')

        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        if m.get('AppInstanceTypeFamily') is not None:
            self.app_instance_type_family = m.get('AppInstanceTypeFamily')

        if m.get('AppInstanceTypeList') is not None:
            self.app_instance_type_list = m.get('AppInstanceTypeList')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('QueryInventory') is not None:
            self.query_inventory = m.get('QueryInventory')

        return self

