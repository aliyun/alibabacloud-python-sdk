# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeDeliveryAddressResponseBodyAddressesArea(TeaModel):
    def __init__(
        self,
        area_id: int = None,
        area_name: str = None,
    ):
        self.area_id = area_id
        self.area_name = area_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesCity(TeaModel):
    def __init__(
        self,
        city_id: int = None,
        city_name: str = None,
    ):
        self.city_id = city_id
        self.city_name = city_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.city_name is not None:
            result['CityName'] = self.city_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesProvince(TeaModel):
    def __init__(
        self,
        province_id: int = None,
        province_name: str = None,
    ):
        self.province_id = province_id
        self.province_name = province_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.province_id is not None:
            result['ProvinceId'] = self.province_id
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        return self


class DescribeDeliveryAddressResponseBodyAddressesTown(TeaModel):
    def __init__(
        self,
        town_id: int = None,
        town_name: str = None,
    ):
        self.town_id = town_id
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.town_id is not None:
            result['TownId'] = self.town_id
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TownId') is not None:
            self.town_id = m.get('TownId')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class DescribeDeliveryAddressResponseBodyAddresses(TeaModel):
    def __init__(
        self,
        area: DescribeDeliveryAddressResponseBodyAddressesArea = None,
        city: DescribeDeliveryAddressResponseBodyAddressesCity = None,
        contacts: str = None,
        default_address: bool = None,
        detail: str = None,
        mobile: str = None,
        postal_code: str = None,
        province: DescribeDeliveryAddressResponseBodyAddressesProvince = None,
        town: DescribeDeliveryAddressResponseBodyAddressesTown = None,
    ):
        self.area = area
        self.city = city
        self.contacts = contacts
        self.default_address = default_address
        self.detail = detail
        self.mobile = mobile
        self.postal_code = postal_code
        self.province = province
        self.town = town

    def validate(self):
        if self.area:
            self.area.validate()
        if self.city:
            self.city.validate()
        if self.province:
            self.province.validate()
        if self.town:
            self.town.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area is not None:
            result['Area'] = self.area.to_map()
        if self.city is not None:
            result['City'] = self.city.to_map()
        if self.contacts is not None:
            result['Contacts'] = self.contacts
        if self.default_address is not None:
            result['DefaultAddress'] = self.default_address
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province.to_map()
        if self.town is not None:
            result['Town'] = self.town.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesArea()
            self.area = temp_model.from_map(m['Area'])
        if m.get('City') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesCity()
            self.city = temp_model.from_map(m['City'])
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')
        if m.get('DefaultAddress') is not None:
            self.default_address = m.get('DefaultAddress')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesProvince()
            self.province = temp_model.from_map(m['Province'])
        if m.get('Town') is not None:
            temp_model = DescribeDeliveryAddressResponseBodyAddressesTown()
            self.town = temp_model.from_map(m['Town'])
        return self


class DescribeDeliveryAddressResponseBody(TeaModel):
    def __init__(
        self,
        addresses: List[DescribeDeliveryAddressResponseBodyAddresses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.addresses = addresses
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.addresses:
            for k in self.addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addresses'] = []
        if self.addresses is not None:
            for k in self.addresses:
                result['Addresses'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k in m.get('Addresses'):
                temp_model = DescribeDeliveryAddressResponseBodyAddresses()
                self.addresses.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeliveryAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeliveryAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDeliveryAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackageDeductionsRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        package_ids: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        resource_type: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.package_ids = package_ids
        self.page_num = page_num
        self.page_size = page_size
        # This parameter is required.
        self.resource_type = resource_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribePackageDeductionsResponseBodyDeductions(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_type: str = None,
        end_time: str = None,
        instance_state: str = None,
        memory: int = None,
        os_type: str = None,
        region_id: str = None,
        resource_type: str = None,
        sta_time: str = None,
        used_core_time: float = None,
        used_time: int = None,
    ):
        self.cpu = cpu
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_type = desktop_type
        self.end_time = end_time
        self.instance_state = instance_state
        self.memory = memory
        self.os_type = os_type
        self.region_id = region_id
        self.resource_type = resource_type
        self.sta_time = sta_time
        self.used_core_time = used_core_time
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sta_time is not None:
            result['StaTime'] = self.sta_time
        if self.used_core_time is not None:
            result['UsedCoreTime'] = self.used_core_time
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StaTime') is not None:
            self.sta_time = m.get('StaTime')
        if m.get('UsedCoreTime') is not None:
            self.used_core_time = m.get('UsedCoreTime')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class DescribePackageDeductionsResponseBody(TeaModel):
    def __init__(
        self,
        deductions: List[DescribePackageDeductionsResponseBodyDeductions] = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_used_core_time: float = None,
        total_used_time: int = None,
    ):
        self.deductions = deductions
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_used_core_time = total_used_core_time
        self.total_used_time = total_used_time

    def validate(self):
        if self.deductions:
            for k in self.deductions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deductions'] = []
        if self.deductions is not None:
            for k in self.deductions:
                result['Deductions'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_used_core_time is not None:
            result['TotalUsedCoreTime'] = self.total_used_core_time
        if self.total_used_time is not None:
            result['TotalUsedTime'] = self.total_used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deductions = []
        if m.get('Deductions') is not None:
            for k in m.get('Deductions'):
                temp_model = DescribePackageDeductionsResponseBodyDeductions()
                self.deductions.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalUsedCoreTime') is not None:
            self.total_used_core_time = m.get('TotalUsedCoreTime')
        if m.get('TotalUsedTime') is not None:
            self.total_used_time = m.get('TotalUsedTime')
        return self


class DescribePackageDeductionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePackageDeductionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePackageDeductionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstancePropertiesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_ids: List[str] = None,
        key: str = None,
        resource_type: str = None,
        value: str = None,
    ):
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.key = key
        # This parameter is required.
        self.resource_type = resource_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstancePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstancePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstancePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyInstancePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


