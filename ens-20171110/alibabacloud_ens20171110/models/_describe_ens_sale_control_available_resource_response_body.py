# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsSaleControlAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sale_control_available_resource: List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResource] = None,
    ):
        self.request_id = request_id
        self.sale_control_available_resource = sale_control_available_resource

    def validate(self):
        if self.sale_control_available_resource:
            for v1 in self.sale_control_available_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SaleControlAvailableResource'] = []
        if self.sale_control_available_resource is not None:
            for k1 in self.sale_control_available_resource:
                result['SaleControlAvailableResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sale_control_available_resource = []
        if m.get('SaleControlAvailableResource') is not None:
            for k1 in m.get('SaleControlAvailableResource'):
                temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResource()
                self.sale_control_available_resource.append(temp_model.from_map(k1))

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResource(DaraModel):
    def __init__(
        self,
        available_disk_type: List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableDiskType] = None,
        available_region: List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableRegion] = None,
        available_spec: List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableSpec] = None,
        available_storage_type: main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageType = None,
        commodity_code: str = None,
        order_type: str = None,
    ):
        self.available_disk_type = available_disk_type
        self.available_region = available_region
        self.available_spec = available_spec
        self.available_storage_type = available_storage_type
        self.commodity_code = commodity_code
        self.order_type = order_type

    def validate(self):
        if self.available_disk_type:
            for v1 in self.available_disk_type:
                 if v1:
                    v1.validate()
        if self.available_region:
            for v1 in self.available_region:
                 if v1:
                    v1.validate()
        if self.available_spec:
            for v1 in self.available_spec:
                 if v1:
                    v1.validate()
        if self.available_storage_type:
            self.available_storage_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableDiskType'] = []
        if self.available_disk_type is not None:
            for k1 in self.available_disk_type:
                result['AvailableDiskType'].append(k1.to_map() if k1 else None)

        result['AvailableRegion'] = []
        if self.available_region is not None:
            for k1 in self.available_region:
                result['AvailableRegion'].append(k1.to_map() if k1 else None)

        result['AvailableSpec'] = []
        if self.available_spec is not None:
            for k1 in self.available_spec:
                result['AvailableSpec'].append(k1.to_map() if k1 else None)

        if self.available_storage_type is not None:
            result['AvailableStorageType'] = self.available_storage_type.to_map()

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_disk_type = []
        if m.get('AvailableDiskType') is not None:
            for k1 in m.get('AvailableDiskType'):
                temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableDiskType()
                self.available_disk_type.append(temp_model.from_map(k1))

        self.available_region = []
        if m.get('AvailableRegion') is not None:
            for k1 in m.get('AvailableRegion'):
                temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableRegion()
                self.available_region.append(temp_model.from_map(k1))

        self.available_spec = []
        if m.get('AvailableSpec') is not None:
            for k1 in m.get('AvailableSpec'):
                temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableSpec()
                self.available_spec.append(temp_model.from_map(k1))

        if m.get('AvailableStorageType') is not None:
            temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageType()
            self.available_storage_type = temp_model.from_map(m.get('AvailableStorageType'))

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageType(DaraModel):
    def __init__(
        self,
        available_default_storage_type: List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableDefaultStorageType] = None,
        available_special_storage_type: List[List[main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableSpecialStorageType]] = None,
    ):
        self.available_default_storage_type = available_default_storage_type
        self.available_special_storage_type = available_special_storage_type

    def validate(self):
        if self.available_default_storage_type:
            for v1 in self.available_default_storage_type:
                 if v1:
                    v1.validate()
        if self.available_special_storage_type:
            for v1 in self.available_special_storage_type:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableDefaultStorageType'] = []
        if self.available_default_storage_type is not None:
            for k1 in self.available_default_storage_type:
                result['AvailableDefaultStorageType'].append(k1.to_map() if k1 else None)

        result['AvailableSpecialStorageType'] = []
        if self.available_special_storage_type is not None:
            for k1 in self.available_special_storage_type:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['AvailableSpecialStorageType'].append(l1)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_default_storage_type = []
        if m.get('AvailableDefaultStorageType') is not None:
            for k1 in m.get('AvailableDefaultStorageType'):
                temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableDefaultStorageType()
                self.available_default_storage_type.append(temp_model.from_map(k1))

        self.available_special_storage_type = []
        if m.get('AvailableSpecialStorageType') is not None:
            for k1 in m.get('AvailableSpecialStorageType'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableSpecialStorageType()
                    l1.append(temp_model.from_map(k2))
                self.available_special_storage_type.append(l1)

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableSpecialStorageType(DaraModel):
    def __init__(
        self,
        storage_type: str = None,
        storage_name: str = None,
        ens_region_id: str = None,
    ):
        self.storage_type = storage_type
        self.storage_name = storage_name
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.storage_name is not None:
            result['StorageName'] = self.storage_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StorageName') is not None:
            self.storage_name = m.get('StorageName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableStorageTypeAvailableDefaultStorageType(DaraModel):
    def __init__(
        self,
        storage_name: str = None,
        storage_type: str = None,
    ):
        self.storage_name = storage_name
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_name is not None:
            result['StorageName'] = self.storage_name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageName') is not None:
            self.storage_name = m.get('StorageName')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableSpec(DaraModel):
    def __init__(
        self,
        cores: str = None,
        memory: str = None,
        spec_name: str = None,
        spec_value: str = None,
    ):
        self.cores = cores
        self.memory = memory
        self.spec_name = spec_name
        self.spec_value = spec_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        if self.spec_value is not None:
            result['SpecValue'] = self.spec_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        if m.get('SpecValue') is not None:
            self.spec_value = m.get('SpecValue')

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableRegion(DaraModel):
    def __init__(
        self,
        area: str = None,
        city: str = None,
        country: str = None,
        ens_region_id: str = None,
        ens_region_name: str = None,
        isp: str = None,
        province: str = None,
    ):
        self.area = area
        self.city = city
        self.country = country
        self.ens_region_id = ens_region_id
        self.ens_region_name = ens_region_name
        self.isp = isp
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_name is not None:
            result['EnsRegionName'] = self.ens_region_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionName') is not None:
            self.ens_region_name = m.get('EnsRegionName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

class DescribeEnsSaleControlAvailableResourceResponseBodySaleControlAvailableResourceAvailableDiskType(DaraModel):
    def __init__(
        self,
        disk_name: str = None,
        disk_type: str = None,
    ):
        self.disk_name = disk_name
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        return self

