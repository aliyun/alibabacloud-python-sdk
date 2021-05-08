# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeEndpointRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        service_code: str = None,
        password: str = None,
    ):
        self.id = id
        self.service_code = service_code
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class DescribeEndpointResponseBodyProtocols(TeaModel):
    def __init__(
        self,
        protocols: List[str] = None,
    ):
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        return self


class DescribeEndpointResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        request_id: str = None,
        endpoint: str = None,
        namespace: str = None,
        serivce_code: str = None,
        id: str = None,
        protocols: DescribeEndpointResponseBodyProtocols = None,
    ):
        self.type = type
        self.request_id = request_id
        self.endpoint = endpoint
        self.namespace = namespace
        self.serivce_code = serivce_code
        self.id = id
        self.protocols = protocols

    def validate(self):
        if self.protocols:
            self.protocols.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.serivce_code is not None:
            result['SerivceCode'] = self.serivce_code
        if self.id is not None:
            result['Id'] = self.id
        if self.protocols is not None:
            result['Protocols'] = self.protocols.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SerivceCode') is not None:
            self.serivce_code = m.get('SerivceCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Protocols') is not None:
            temp_model = DescribeEndpointResponseBodyProtocols()
            self.protocols = temp_model.from_map(m['Protocols'])
        return self


class DescribeEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndpointResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        service_code: str = None,
        type: str = None,
    ):
        self.id = id
        self.service_code = service_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeEndpointsResponseBodyEndpointsEndpointProtocols(TeaModel):
    def __init__(
        self,
        protocols: List[str] = None,
    ):
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        return self


class DescribeEndpointsResponseBodyEndpointsEndpoint(TeaModel):
    def __init__(
        self,
        type: str = None,
        namespace: str = None,
        serivce_code: str = None,
        id: str = None,
        endpoint: str = None,
        protocols: DescribeEndpointsResponseBodyEndpointsEndpointProtocols = None,
    ):
        self.type = type
        self.namespace = namespace
        self.serivce_code = serivce_code
        self.id = id
        self.endpoint = endpoint
        self.protocols = protocols

    def validate(self):
        if self.protocols:
            self.protocols.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.serivce_code is not None:
            result['SerivceCode'] = self.serivce_code
        if self.id is not None:
            result['Id'] = self.id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.protocols is not None:
            result['Protocols'] = self.protocols.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('SerivceCode') is not None:
            self.serivce_code = m.get('SerivceCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Protocols') is not None:
            temp_model = DescribeEndpointsResponseBodyEndpointsEndpointProtocols()
            self.protocols = temp_model.from_map(m['Protocols'])
        return self


class DescribeEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        endpoint: List[DescribeEndpointsResponseBodyEndpointsEndpoint] = None,
    ):
        self.endpoint = endpoint

    def validate(self):
        if self.endpoint:
            for k in self.endpoint:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoint'] = []
        if self.endpoint is not None:
            for k in self.endpoint:
                result['Endpoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint = []
        if m.get('Endpoint') is not None:
            for k in m.get('Endpoint'):
                temp_model = DescribeEndpointsResponseBodyEndpointsEndpoint()
                self.endpoint.append(temp_model.from_map(k))
        return self


class DescribeEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
        endpoints: DescribeEndpointsResponseBodyEndpoints = None,
    ):
        self.success = success
        self.request_id = request_id
        self.endpoints = endpoints

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Endpoints') is not None:
            temp_model = DescribeEndpointsResponseBodyEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        return self


class DescribeEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        password: str = None,
    ):
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class DescribeRegionsResponseBodyRegionIds(TeaModel):
    def __init__(
        self,
        region_ids: List[str] = None,
    ):
        self.region_ids = region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        region_ids: DescribeRegionsResponseBodyRegionIds = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.region_ids = region_ids

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RegionIds') is not None:
            temp_model = DescribeRegionsResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        password: str = None,
    ):
        self.region_id = region_id
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class DescribeServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        services: List[str] = None,
    ):
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class DescribeServicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        services: DescribeServicesResponseBodyServices = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.services = services

    def validate(self):
        if self.services:
            self.services.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services is not None:
            result['Services'] = self.services.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Services') is not None:
            temp_model = DescribeServicesResponseBodyServices()
            self.services = temp_model.from_map(m['Services'])
        return self


class DescribeServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointsRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        id: str = None,
        serivce_code: str = None,
    ):
        self.namespace = namespace
        self.id = id
        self.serivce_code = serivce_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.id is not None:
            result['Id'] = self.id
        if self.serivce_code is not None:
            result['SerivceCode'] = self.serivce_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SerivceCode') is not None:
            self.serivce_code = m.get('SerivceCode')
        return self


class ListEndpointsResponseBodyEndpointListItemEndpointProtocols(TeaModel):
    def __init__(
        self,
        protocols: List[str] = None,
    ):
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        return self


class ListEndpointsResponseBodyEndpointListItemEndpoint(TeaModel):
    def __init__(
        self,
        type: str = None,
        namespace: str = None,
        product: str = None,
        id: str = None,
        endpoint: str = None,
        protocols: ListEndpointsResponseBodyEndpointListItemEndpointProtocols = None,
    ):
        self.type = type
        self.namespace = namespace
        self.product = product
        self.id = id
        self.endpoint = endpoint
        self.protocols = protocols

    def validate(self):
        if self.protocols:
            self.protocols.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.product is not None:
            result['Product'] = self.product
        if self.id is not None:
            result['Id'] = self.id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.protocols is not None:
            result['Protocols'] = self.protocols.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Protocols') is not None:
            temp_model = ListEndpointsResponseBodyEndpointListItemEndpointProtocols()
            self.protocols = temp_model.from_map(m['Protocols'])
        return self


class ListEndpointsResponseBodyEndpointList(TeaModel):
    def __init__(
        self,
        item_endpoint: List[ListEndpointsResponseBodyEndpointListItemEndpoint] = None,
    ):
        self.item_endpoint = item_endpoint

    def validate(self):
        if self.item_endpoint:
            for k in self.item_endpoint:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemEndpoint'] = []
        if self.item_endpoint is not None:
            for k in self.item_endpoint:
                result['ItemEndpoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_endpoint = []
        if m.get('ItemEndpoint') is not None:
            for k in m.get('ItemEndpoint'):
                temp_model = ListEndpointsResponseBodyEndpointListItemEndpoint()
                self.item_endpoint.append(temp_model.from_map(k))
        return self


class ListEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
        endpoint_list: ListEndpointsResponseBodyEndpointList = None,
    ):
        self.success = success
        self.request_id = request_id
        self.endpoint_list = endpoint_list

    def validate(self):
        if self.endpoint_list:
            self.endpoint_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint_list is not None:
            result['EndpointList'] = self.endpoint_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndpointList') is not None:
            temp_model = ListEndpointsResponseBodyEndpointList()
            self.endpoint_list = temp_model.from_map(m['EndpointList'])
        return self


class ListEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointsByIpRequest(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class ListEndpointsByIpResponseBodyEndpointListItemEndpointProtocols(TeaModel):
    def __init__(
        self,
        protocols: List[str] = None,
    ):
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        return self


class ListEndpointsByIpResponseBodyEndpointListItemEndpoint(TeaModel):
    def __init__(
        self,
        type: str = None,
        namespace: str = None,
        product: str = None,
        id: str = None,
        endpoint: str = None,
        protocols: ListEndpointsByIpResponseBodyEndpointListItemEndpointProtocols = None,
    ):
        self.type = type
        self.namespace = namespace
        self.product = product
        self.id = id
        self.endpoint = endpoint
        self.protocols = protocols

    def validate(self):
        if self.protocols:
            self.protocols.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.product is not None:
            result['Product'] = self.product
        if self.id is not None:
            result['Id'] = self.id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.protocols is not None:
            result['Protocols'] = self.protocols.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Protocols') is not None:
            temp_model = ListEndpointsByIpResponseBodyEndpointListItemEndpointProtocols()
            self.protocols = temp_model.from_map(m['Protocols'])
        return self


class ListEndpointsByIpResponseBodyEndpointList(TeaModel):
    def __init__(
        self,
        item_endpoint: List[ListEndpointsByIpResponseBodyEndpointListItemEndpoint] = None,
    ):
        self.item_endpoint = item_endpoint

    def validate(self):
        if self.item_endpoint:
            for k in self.item_endpoint:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemEndpoint'] = []
        if self.item_endpoint is not None:
            for k in self.item_endpoint:
                result['ItemEndpoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_endpoint = []
        if m.get('ItemEndpoint') is not None:
            for k in m.get('ItemEndpoint'):
                temp_model = ListEndpointsByIpResponseBodyEndpointListItemEndpoint()
                self.item_endpoint.append(temp_model.from_map(k))
        return self


class ListEndpointsByIpResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        request_id: str = None,
        endpoint_list: ListEndpointsByIpResponseBodyEndpointList = None,
    ):
        self.success = success
        self.request_id = request_id
        self.endpoint_list = endpoint_list

    def validate(self):
        if self.endpoint_list:
            self.endpoint_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint_list is not None:
            result['EndpointList'] = self.endpoint_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndpointList') is not None:
            temp_model = ListEndpointsByIpResponseBodyEndpointList()
            self.endpoint_list = temp_model.from_map(m['EndpointList'])
        return self


class ListEndpointsByIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEndpointsByIpResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEndpointsByIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


