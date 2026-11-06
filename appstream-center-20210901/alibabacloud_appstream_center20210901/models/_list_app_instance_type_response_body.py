# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAppInstanceTypeResponseBody(DaraModel):
    def __init__(
        self,
        app_instance_type_models: List[main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModels] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of session instance types on the current page.
        self.app_instance_type_models = app_instance_type_models
        # The page number used in this query, which corresponds to the request parameters and the total number of entries.
        self.page_number = page_number
        # The number of entries per page used in this query.
        self.page_size = page_size
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id
        # The total number of instance types that meet all filtering conditions, not the number of entries on the current page.
        self.total_count = total_count

    def validate(self):
        if self.app_instance_type_models:
            for v1 in self.app_instance_type_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppInstanceTypeModels'] = []
        if self.app_instance_type_models is not None:
            for k1 in self.app_instance_type_models:
                result['AppInstanceTypeModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_instance_type_models = []
        if m.get('AppInstanceTypeModels') is not None:
            for k1 in m.get('AppInstanceTypeModels'):
                temp_model = main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModels()
                self.app_instance_type_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAppInstanceTypeResponseBodyAppInstanceTypeModels(DaraModel):
    def __init__(
        self,
        app_instance_type: str = None,
        app_instance_type_family: str = None,
        cpu: str = None,
        data_disk_size: int = None,
        gpu: str = None,
        gpu_memory: int = None,
        gpu_spec: str = None,
        id: int = None,
        instance_type_name: str = None,
        inventory_info: main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfo = None,
        memory: int = None,
        product_type: str = None,
        system_disk_size: int = None,
    ):
        # The session instance type code, which can be used as the session instance type parameter for subsequent operations.
        self.app_instance_type = app_instance_type
        # The instance type family code to which the session instance type belongs.
        self.app_instance_type_family = app_instance_type_family
        # The number of CPU cores included in the instance type, represented by a numeric string. Unit: cores.
        self.cpu = cpu
        # The data cloud disk capacity of the instance type. Unit: GB.
        self.data_disk_size = data_disk_size
        # Not enabled yet. The example value is only used to demonstrate the format and does not represent the actual number of GPUs returned by this operation.
        self.gpu = gpu
        # The GPU memory capacity of the instance type. Unit: MB.
        self.gpu_memory = gpu_memory
        # The display value or display range of the GPU memory. Display it as the returned text. Do not directly use it as a numeric value for capacity conversion.
        self.gpu_spec = gpu_spec
        # The identifier of the instance type record. When integrating with pricing or creation operations, use `AppInstanceType`. Do not use this field to replace the instance type code.
        self.id = id
        # The display name of the instance type. The Chinese name is used only when `Language` is set to `zh-CN`. For other values or when omitted, the instance type code is used.
        self.instance_type_name = instance_type_name
        # The inventory information of the instance type. This parameter is returned only when the inventory is queried and the relevant information is obtained. If this parameter is not returned, it does not mean that the inventory is 0.
        self.inventory_info = inventory_info
        # The memory capacity of the instance type. Unit: MB.
        self.memory = memory
        # The type of the product to which the instance type belongs. The current document displays the following values:
        # 
        # - `CloudApp`: Wuying Cloud Application.
        self.product_type = product_type
        # The system cloud disk capacity of the instance type. Unit: GB.
        self.system_disk_size = system_disk_size

    def validate(self):
        if self.inventory_info:
            self.inventory_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type

        if self.app_instance_type_family is not None:
            result['AppInstanceTypeFamily'] = self.app_instance_type_family

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_type_name is not None:
            result['InstanceTypeName'] = self.instance_type_name

        if self.inventory_info is not None:
            result['InventoryInfo'] = self.inventory_info.to_map()

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')

        if m.get('AppInstanceTypeFamily') is not None:
            self.app_instance_type_family = m.get('AppInstanceTypeFamily')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceTypeName') is not None:
            self.instance_type_name = m.get('InstanceTypeName')

        if m.get('InventoryInfo') is not None:
            temp_model = main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfo()
            self.inventory_info = temp_model.from_map(m.get('InventoryInfo'))

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfo(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
        zone_inventory_info: List[main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfoZoneInventoryInfo] = None,
    ):
        # The business region ID corresponding to the inventory query.
        self.region_id = region_id
        # The instance type inventory status obtained in the current query.
        # 
        # - `Available`: The total inventory of the queried zones is greater than 0.
        # - `SoldOut`: The total inventory of the queried zones is not greater than 0.
        self.status = status
        # The list of inventory information returned by zone.
        self.zone_inventory_info = zone_inventory_info

    def validate(self):
        if self.zone_inventory_info:
            for v1 in self.zone_inventory_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        result['ZoneInventoryInfo'] = []
        if self.zone_inventory_info is not None:
            for k1 in self.zone_inventory_info:
                result['ZoneInventoryInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.zone_inventory_info = []
        if m.get('ZoneInventoryInfo') is not None:
            for k1 in m.get('ZoneInventoryInfo'):
                temp_model = main_models.ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfoZoneInventoryInfo()
                self.zone_inventory_info.append(temp_model.from_map(k1))

        return self

class ListAppInstanceTypeResponseBodyAppInstanceTypeModelsInventoryInfoZoneInventoryInfo(DaraModel):
    def __init__(
        self,
        amount: str = None,
        zone_id: str = None,
    ):
        # The available quantity in the zone obtained in this query. Unit: instances. This value is an inventory snapshot and does not indicate that resources have been reserved for the current account.
        self.amount = amount
        # The zone ID, which can be queried by calling the [ListZones](https://api.aliyun.com/document/appstream-center/2021-09-01/ListZones) operation.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

