# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        bandwidth: str = None,
        client_token: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        name: str = None,
        service_location: str = None,
    ):
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.description = description
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.name = name
        self.service_location = service_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class AllocateAnycastEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.anycast_id = anycast_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateAnycastEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AllocateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAnycastEipAddressRequestPopLocations(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class AssociateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        association_mode: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        pop_locations: List[AssociateAnycastEipAddressRequestPopLocations] = None,
        private_ip_address: str = None,
    ):
        self.anycast_id = anycast_id
        self.association_mode = association_mode
        self.bind_instance_id = bind_instance_id
        self.bind_instance_region_id = bind_instance_region_id
        self.bind_instance_type = bind_instance_type
        self.client_token = client_token
        self.dry_run = dry_run
        self.pop_locations = pop_locations
        self.private_ip_address = private_ip_address

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = AssociateAnycastEipAddressRequestPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class AssociateAnycastEipAddressResponseBody(TeaModel):
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


class AssociateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateAnycastEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = AssociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bind_instance_id: str = None,
        ip: str = None,
    ):
        self.anycast_id = anycast_id
        self.bind_instance_id = bind_instance_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList(TeaModel):
    def __init__(
        self,
        association_mode: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        bind_time: str = None,
        pop_locations: List[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations] = None,
        private_ip_address: str = None,
        status: str = None,
    ):
        self.association_mode = association_mode
        self.bind_instance_id = bind_instance_id
        self.bind_instance_region_id = bind_instance_region_id
        self.bind_instance_type = bind_instance_type
        self.bind_time = bind_time
        self.pop_locations = pop_locations
        self.private_ip_address = private_ip_address
        self.status = status

    def validate(self):
        if self.pop_locations:
            for k in self.pop_locations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        result['PopLocations'] = []
        if self.pop_locations is not None:
            for k in self.pop_locations:
                result['PopLocations'].append(k.to_map() if k else None)
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        self.pop_locations = []
        if m.get('PopLocations') is not None:
            for k in m.get('PopLocations'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoListPopLocations()
                self.pop_locations.append(temp_model.from_map(k))
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAnycastEipAddressResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        anycast_eip_bind_info_list: List[DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList] = None,
        anycast_id: str = None,
        bandwidth: int = None,
        bid: str = None,
        business_status: str = None,
        create_time: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        request_id: str = None,
        service_location: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list
        self.anycast_id = anycast_id
        self.bandwidth = bandwidth
        self.bid = bid
        self.business_status = business_status
        self.create_time = create_time
        self.description = description
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.ip_address = ip_address
        self.name = name
        self.request_id = request_id
        self.service_location = service_location
        self.status = status

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = DescribeAnycastEipAddressResponseBodyAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastPopLocationsRequest(TeaModel):
    def __init__(
        self,
        service_location: str = None,
    ):
        self.service_location = service_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastPopLocationsResponseBody(TeaModel):
    def __init__(
        self,
        anycast_pop_location_list: List[DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList] = None,
        count: str = None,
        request_id: str = None,
    ):
        self.anycast_pop_location_list = anycast_pop_location_list
        self.count = count
        self.request_id = request_id

    def validate(self):
        if self.anycast_pop_location_list:
            for k in self.anycast_pop_location_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastPopLocationList'] = []
        if self.anycast_pop_location_list is not None:
            for k in self.anycast_pop_location_list:
                result['AnycastPopLocationList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_pop_location_list = []
        if m.get('AnycastPopLocationList') is not None:
            for k in m.get('AnycastPopLocationList'):
                temp_model = DescribeAnycastPopLocationsResponseBodyAnycastPopLocationList()
                self.anycast_pop_location_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastPopLocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastPopLocationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeAnycastPopLocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnycastServerRegionsRequest(TeaModel):
    def __init__(
        self,
        service_location: str = None,
    ):
        self.service_location = service_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        return self


class DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeAnycastServerRegionsResponseBody(TeaModel):
    def __init__(
        self,
        anycast_server_region_list: List[DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList] = None,
        count: str = None,
        request_id: str = None,
    ):
        self.anycast_server_region_list = anycast_server_region_list
        self.count = count
        self.request_id = request_id

    def validate(self):
        if self.anycast_server_region_list:
            for k in self.anycast_server_region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastServerRegionList'] = []
        if self.anycast_server_region_list is not None:
            for k in self.anycast_server_region_list:
                result['AnycastServerRegionList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_server_region_list = []
        if m.get('AnycastServerRegionList') is not None:
            for k in m.get('AnycastServerRegionList'):
                temp_model = DescribeAnycastServerRegionsResponseBodyAnycastServerRegionList()
                self.anycast_server_region_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAnycastServerRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnycastServerRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeAnycastServerRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnycastEipAddressesRequest(TeaModel):
    def __init__(
        self,
        anycast_eip_address: str = None,
        anycast_id: str = None,
        anycast_ids: List[str] = None,
        bind_instance_ids: List[str] = None,
        business_status: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        service_location: str = None,
        status: str = None,
    ):
        self.anycast_eip_address = anycast_eip_address
        self.anycast_id = anycast_id
        self.anycast_ids = anycast_ids
        self.bind_instance_ids = bind_instance_ids
        self.business_status = business_status
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.service_location = service_location
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_eip_address is not None:
            result['AnycastEipAddress'] = self.anycast_eip_address
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.anycast_ids is not None:
            result['AnycastIds'] = self.anycast_ids
        if self.bind_instance_ids is not None:
            result['BindInstanceIds'] = self.bind_instance_ids
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastEipAddress') is not None:
            self.anycast_eip_address = m.get('AnycastEipAddress')
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AnycastIds') is not None:
            self.anycast_ids = m.get('AnycastIds')
        if m.get('BindInstanceIds') is not None:
            self.bind_instance_ids = m.get('BindInstanceIds')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList(TeaModel):
    def __init__(
        self,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        bind_time: str = None,
    ):
        self.bind_instance_id = bind_instance_id
        self.bind_instance_region_id = bind_instance_region_id
        self.bind_instance_type = bind_instance_type
        self.bind_time = bind_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.bind_time is not None:
            result['BindTime'] = self.bind_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('BindTime') is not None:
            self.bind_time = m.get('BindTime')
        return self


class ListAnycastEipAddressesResponseBodyAnycastList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        anycast_eip_bind_info_list: List[ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList] = None,
        anycast_id: str = None,
        bandwidth: int = None,
        business_status: str = None,
        create_time: str = None,
        description: str = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        service_location: str = None,
        service_managed: int = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.anycast_eip_bind_info_list = anycast_eip_bind_info_list
        self.anycast_id = anycast_id
        self.bandwidth = bandwidth
        self.business_status = business_status
        self.create_time = create_time
        self.description = description
        self.instance_charge_type = instance_charge_type
        self.internet_charge_type = internet_charge_type
        self.ip_address = ip_address
        self.name = name
        self.service_location = service_location
        self.service_managed = service_managed
        self.status = status

    def validate(self):
        if self.anycast_eip_bind_info_list:
            for k in self.anycast_eip_bind_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['AnycastEipBindInfoList'] = []
        if self.anycast_eip_bind_info_list is not None:
            for k in self.anycast_eip_bind_info_list:
                result['AnycastEipBindInfoList'].append(k.to_map() if k else None)
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location
        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.anycast_eip_bind_info_list = []
        if m.get('AnycastEipBindInfoList') is not None:
            for k in m.get('AnycastEipBindInfoList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastListAnycastEipBindInfoList()
                self.anycast_eip_bind_info_list.append(temp_model.from_map(k))
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')
        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAnycastEipAddressesResponseBody(TeaModel):
    def __init__(
        self,
        anycast_list: List[ListAnycastEipAddressesResponseBodyAnycastList] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.anycast_list = anycast_list
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.anycast_list:
            for k in self.anycast_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnycastList'] = []
        if self.anycast_list is not None:
            for k in self.anycast_list:
                result['AnycastList'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anycast_list = []
        if m.get('AnycastList') is not None:
            for k in m.get('AnycastList'):
                temp_model = ListAnycastEipAddressesResponseBodyAnycastList()
                self.anycast_list.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAnycastEipAddressesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnycastEipAddressesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ListAnycastEipAddressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressAttributeRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        description: str = None,
        name: str = None,
    ):
        self.anycast_id = anycast_id
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyAnycastEipAddressAttributeResponseBody(TeaModel):
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


class ModifyAnycastEipAddressAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAnycastEipAddressAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyAnycastEipAddressAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAnycastEipAddressSpecRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bandwidth: str = None,
    ):
        self.anycast_id = anycast_id
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyAnycastEipAddressSpecResponseBody(TeaModel):
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


class ModifyAnycastEipAddressSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAnycastEipAddressSpecResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ModifyAnycastEipAddressSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        client_token: str = None,
    ):
        self.anycast_id = anycast_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class ReleaseAnycastEipAddressResponseBody(TeaModel):
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


class ReleaseAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseAnycastEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReleaseAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateAnycastEipAddressRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        bind_instance_id: str = None,
        bind_instance_region_id: str = None,
        bind_instance_type: str = None,
        client_token: str = None,
        dry_run: str = None,
        private_ip_address: str = None,
    ):
        self.anycast_id = anycast_id
        self.bind_instance_id = bind_instance_id
        self.bind_instance_region_id = bind_instance_region_id
        self.bind_instance_type = bind_instance_type
        self.client_token = client_token
        self.dry_run = dry_run
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.bind_instance_region_id is not None:
            result['BindInstanceRegionId'] = self.bind_instance_region_id
        if self.bind_instance_type is not None:
            result['BindInstanceType'] = self.bind_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('BindInstanceRegionId') is not None:
            self.bind_instance_region_id = m.get('BindInstanceRegionId')
        if m.get('BindInstanceType') is not None:
            self.bind_instance_type = m.get('BindInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class UnassociateAnycastEipAddressResponseBody(TeaModel):
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


class UnassociateAnycastEipAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnassociateAnycastEipAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UnassociateAnycastEipAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationAddList(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList(TeaModel):
    def __init__(
        self,
        pop_location: str = None,
    ):
        self.pop_location = pop_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pop_location is not None:
            result['PopLocation'] = self.pop_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PopLocation') is not None:
            self.pop_location = m.get('PopLocation')
        return self


class UpdateAnycastEipAddressAssociationsRequest(TeaModel):
    def __init__(
        self,
        anycast_id: str = None,
        association_mode: str = None,
        bind_instance_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        pop_location_add_list: List[UpdateAnycastEipAddressAssociationsRequestPopLocationAddList] = None,
        pop_location_delete_list: List[UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList] = None,
    ):
        self.anycast_id = anycast_id
        self.association_mode = association_mode
        self.bind_instance_id = bind_instance_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.pop_location_add_list = pop_location_add_list
        self.pop_location_delete_list = pop_location_delete_list

    def validate(self):
        if self.pop_location_add_list:
            for k in self.pop_location_add_list:
                if k:
                    k.validate()
        if self.pop_location_delete_list:
            for k in self.pop_location_delete_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anycast_id is not None:
            result['AnycastId'] = self.anycast_id
        if self.association_mode is not None:
            result['AssociationMode'] = self.association_mode
        if self.bind_instance_id is not None:
            result['BindInstanceId'] = self.bind_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['PopLocationAddList'] = []
        if self.pop_location_add_list is not None:
            for k in self.pop_location_add_list:
                result['PopLocationAddList'].append(k.to_map() if k else None)
        result['PopLocationDeleteList'] = []
        if self.pop_location_delete_list is not None:
            for k in self.pop_location_delete_list:
                result['PopLocationDeleteList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnycastId') is not None:
            self.anycast_id = m.get('AnycastId')
        if m.get('AssociationMode') is not None:
            self.association_mode = m.get('AssociationMode')
        if m.get('BindInstanceId') is not None:
            self.bind_instance_id = m.get('BindInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.pop_location_add_list = []
        if m.get('PopLocationAddList') is not None:
            for k in m.get('PopLocationAddList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationAddList()
                self.pop_location_add_list.append(temp_model.from_map(k))
        self.pop_location_delete_list = []
        if m.get('PopLocationDeleteList') is not None:
            for k in m.get('PopLocationDeleteList'):
                temp_model = UpdateAnycastEipAddressAssociationsRequestPopLocationDeleteList()
                self.pop_location_delete_list.append(temp_model.from_map(k))
        return self


class UpdateAnycastEipAddressAssociationsResponseBody(TeaModel):
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


class UpdateAnycastEipAddressAssociationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAnycastEipAddressAssociationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateAnycastEipAddressAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


