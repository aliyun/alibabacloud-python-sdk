# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDeviceRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        group_id: str = None,
        owner_id: int = None,
        protocol: str = None,
    ):
        self.config = config
        self.group_id = group_id
        self.owner_id = owner_id
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class AddDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDeviceResponseBody = None,
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
            temp_model = AddDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRegisteredDeviceRequest(TeaModel):
    def __init__(
        self,
        dsn: str = None,
        owner_id: int = None,
        register_code: str = None,
        secret_key: str = None,
        vendor: str = None,
    ):
        self.dsn = dsn
        self.owner_id = owner_id
        self.register_code = register_code
        self.secret_key = secret_key
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredDeviceResponseBody(TeaModel):
    def __init__(
        self,
        dsn: str = None,
        id: str = None,
        register_code: str = None,
        request_id: str = None,
        secret_key: str = None,
        vendor: str = None,
    ):
        self.dsn = dsn
        self.id = id
        self.register_code = register_code
        self.request_id = request_id
        self.secret_key = secret_key
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.id is not None:
            result['Id'] = self.id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRegisteredDeviceResponseBody = None,
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
            temp_model = AddRegisteredDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRegisteredVendorRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner_id: int = None,
    ):
        self.description = description
        self.name = name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class AddRegisteredVendorResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        request_id: str = None,
        vendor: str = None,
    ):
        self.description = description
        self.name = name
        self.request_id = request_id
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddRegisteredVendorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRegisteredVendorResponseBody = None,
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
            temp_model = AddRegisteredVendorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRenderingDeviceInternetPortsRequest(TeaModel):
    def __init__(
        self,
        isp: str = None,
        instance_ids: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        owner_id: int = None,
    ):
        self.isp = isp
        self.instance_ids = instance_ids
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class AddRenderingDeviceInternetPortsResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddRenderingDeviceInternetPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRenderingDeviceInternetPortsResponseBody = None,
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
            temp_model = AddRenderingDeviceInternetPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(
        self,
        always: str = None,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.always = always
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.source_url = source_url
        self.start_time = start_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always is not None:
            result['Always'] = self.always
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Always') is not None:
            self.always = m.get('Always')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class AddVsPullStreamInfoConfigResponseBody(TeaModel):
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


class AddVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVsPullStreamInfoConfigResponseBody = None,
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
            temp_model = AddVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindDirectoriesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchBindDirectoriesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        error: str = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        return self


class BatchBindDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchBindDirectoriesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindDirectoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchBindDirectoriesResponseBody = None,
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
            temp_model = BatchBindDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindParentPlatformDevicesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchBindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        error: str = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.error = error
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchBindParentPlatformDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchBindParentPlatformDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindParentPlatformDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindParentPlatformDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchBindParentPlatformDevicesResponseBody = None,
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
            temp_model = BatchBindParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindPurchasedDevicesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        region: str = None,
    ):
        self.device_id = device_id
        self.group_id = group_id
        self.owner_id = owner_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BatchBindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        error: str = None,
        group_id: str = None,
        region: str = None,
    ):
        self.device_id = device_id
        self.error = error
        self.group_id = group_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BatchBindPurchasedDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchBindPurchasedDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindPurchasedDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindPurchasedDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchBindPurchasedDevicesResponseBody = None,
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
            temp_model = BatchBindPurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindTemplateRequest(TeaModel):
    def __init__(
        self,
        apply_all: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        replace: bool = None,
        template_id: str = None,
    ):
        self.apply_all = apply_all
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.replace = replace
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchBindTemplateResponseBodyBindings(TeaModel):
    def __init__(
        self,
        error: str = None,
        instance_id: str = None,
        instance_type: str = None,
        template_id: str = None,
    ):
        self.error = error
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchBindTemplateResponseBody(TeaModel):
    def __init__(
        self,
        bindings: List[BatchBindTemplateResponseBodyBindings] = None,
        request_id: str = None,
    ):
        self.bindings = bindings
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchBindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchBindTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchBindTemplateResponseBody = None,
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
            temp_model = BatchBindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchBindTemplatesRequest(TeaModel):
    def __init__(
        self,
        apply_all: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        replace: bool = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.apply_all = apply_all
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.replace = replace
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BatchBindTemplatesResponseBodyResults(TeaModel):
    def __init__(
        self,
        error: str = None,
        instance_id: str = None,
        instance_type: str = None,
        template_id: str = None,
    ):
        self.error = error
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchBindTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchBindTemplatesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchBindTemplatesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchBindTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchBindTemplatesResponseBody = None,
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
            temp_model = BatchBindTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteDevicesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchDeleteDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
    ):
        self.error = error
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class BatchDeleteDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchDeleteDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchDeleteDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchDeleteDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteDevicesResponseBody = None,
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
            temp_model = BatchDeleteDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteVsDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        function_names: str = None,
        owner_id: int = None,
    ):
        self.domain_names = domain_names
        self.function_names = function_names
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchDeleteVsDomainConfigsResponseBody(TeaModel):
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


class BatchDeleteVsDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteVsDomainConfigsResponseBody = None,
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
            temp_model = BatchDeleteVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchForbidVsStreamRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        oneshot: str = None,
        owner_id: int = None,
        resume_time: str = None,
    ):
        self.channel = channel
        self.control_stream_action = control_stream_action
        self.domain_name = domain_name
        self.live_stream_type = live_stream_type
        self.oneshot = oneshot
        self.owner_id = owner_id
        self.resume_time = resume_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        return self


class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
    ):
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo(TeaModel):
    def __init__(
        self,
        channels: BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels = None,
        count: int = None,
        detail: str = None,
        result: str = None,
    ):
        self.channels = channels
        self.count = count
        self.detail = detail
        self.result = result

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchForbidVsStreamResponseBodyForbidResult(TeaModel):
    def __init__(
        self,
        forbid_result_info: List[BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo] = None,
    ):
        self.forbid_result_info = forbid_result_info

    def validate(self):
        if self.forbid_result_info:
            for k in self.forbid_result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForbidResultInfo'] = []
        if self.forbid_result_info is not None:
            for k in self.forbid_result_info:
                result['ForbidResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forbid_result_info = []
        if m.get('ForbidResultInfo') is not None:
            for k in m.get('ForbidResultInfo'):
                temp_model = BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo()
                self.forbid_result_info.append(temp_model.from_map(k))
        return self


class BatchForbidVsStreamResponseBody(TeaModel):
    def __init__(
        self,
        forbid_result: BatchForbidVsStreamResponseBodyForbidResult = None,
        request_id: str = None,
    ):
        self.forbid_result = forbid_result
        self.request_id = request_id

    def validate(self):
        if self.forbid_result:
            self.forbid_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forbid_result is not None:
            result['ForbidResult'] = self.forbid_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbidResult') is not None:
            temp_model = BatchForbidVsStreamResponseBodyForbidResult()
            self.forbid_result = temp_model.from_map(m['ForbidResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchForbidVsStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchForbidVsStreamResponseBody = None,
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
            temp_model = BatchForbidVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchResumeVsStreamRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        owner_id: int = None,
    ):
        self.channel = channel
        self.control_stream_action = control_stream_action
        self.domain_name = domain_name
        self.live_stream_type = live_stream_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
    ):
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        return self


class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo(TeaModel):
    def __init__(
        self,
        channels: BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels = None,
        count: int = None,
        detail: str = None,
        result: str = None,
    ):
        self.channels = channels
        self.count = count
        self.detail = detail
        self.result = result

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        if self.count is not None:
            result['Count'] = self.count
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels()
            self.channels = temp_model.from_map(m['Channels'])
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class BatchResumeVsStreamResponseBodyResumeResult(TeaModel):
    def __init__(
        self,
        resume_result_info: List[BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo] = None,
    ):
        self.resume_result_info = resume_result_info

    def validate(self):
        if self.resume_result_info:
            for k in self.resume_result_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResumeResultInfo'] = []
        if self.resume_result_info is not None:
            for k in self.resume_result_info:
                result['ResumeResultInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resume_result_info = []
        if m.get('ResumeResultInfo') is not None:
            for k in m.get('ResumeResultInfo'):
                temp_model = BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo()
                self.resume_result_info.append(temp_model.from_map(k))
        return self


class BatchResumeVsStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resume_result: BatchResumeVsStreamResponseBodyResumeResult = None,
    ):
        self.request_id = request_id
        self.resume_result = resume_result

    def validate(self):
        if self.resume_result:
            self.resume_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resume_result is not None:
            result['ResumeResult'] = self.resume_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResumeResult') is not None:
            temp_model = BatchResumeVsStreamResponseBodyResumeResult()
            self.resume_result = temp_model.from_map(m['ResumeResult'])
        return self


class BatchResumeVsStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchResumeVsStreamResponseBody = None,
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
            temp_model = BatchResumeVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchSetVsDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_id: int = None,
    ):
        self.domain_names = domain_names
        self.functions = functions
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.functions is not None:
            result['Functions'] = self.functions
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('Functions') is not None:
            self.functions = m.get('Functions')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchSetVsDomainConfigsResponseBody(TeaModel):
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


class BatchSetVsDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchSetVsDomainConfigsResponseBody = None,
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
            temp_model = BatchSetVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartDevicesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchStartDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
        name: str = None,
    ):
        self.error = error
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BatchStartDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        id: str = None,
        streams: List[BatchStartDevicesResponseBodyResultsStreams] = None,
    ):
        self.id = id
        self.streams = streams

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = BatchStartDevicesResponseBodyResultsStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class BatchStartDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchStartDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStartDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStartDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStartDevicesResponseBody = None,
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
            temp_model = BatchStartDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartStreamsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchStartStreamsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
        name: str = None,
    ):
        self.error = error
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BatchStartStreamsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchStartStreamsResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStartStreamsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStartStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStartStreamsResponseBody = None,
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
            temp_model = BatchStartStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopDevicesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopDevicesResponseBodyResultsStreams(TeaModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
        name: str = None,
    ):
        self.error = error
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BatchStopDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        id: str = None,
        streams: List[BatchStopDevicesResponseBodyResultsStreams] = None,
    ):
        self.id = id
        self.streams = streams

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = BatchStopDevicesResponseBodyResultsStreams()
                self.streams.append(temp_model.from_map(k))
        return self


class BatchStopDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchStopDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStopDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStopDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopDevicesResponseBody = None,
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
            temp_model = BatchStopDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopStreamsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class BatchStopStreamsResponseBodyResults(TeaModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
        name: str = None,
    ):
        self.error = error
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class BatchStopStreamsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchStopStreamsResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchStopStreamsResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchStopStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchStopStreamsResponseBody = None,
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
            temp_model = BatchStopStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindDirectoriesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchUnbindDirectoriesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        error: str = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        return self


class BatchUnbindDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchUnbindDirectoriesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindDirectoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUnbindDirectoriesResponseBody = None,
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
            temp_model = BatchUnbindDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindParentPlatformDevicesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchUnbindParentPlatformDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        error: str = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.error = error
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BatchUnbindParentPlatformDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchUnbindParentPlatformDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindParentPlatformDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindParentPlatformDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUnbindParentPlatformDevicesResponseBody = None,
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
            temp_model = BatchUnbindParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindPurchasedDevicesRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BatchUnbindPurchasedDevicesResponseBodyResults(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        error: str = None,
    ):
        self.device_id = device_id
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        return self


class BatchUnbindPurchasedDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchUnbindPurchasedDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindPurchasedDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindPurchasedDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUnbindPurchasedDevicesResponseBody = None,
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
            temp_model = BatchUnbindPurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindTemplateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BatchUnbindTemplateResponseBodyBindings(TeaModel):
    def __init__(
        self,
        error: str = None,
        instance_id: str = None,
        instance_type: str = None,
        template_id: str = None,
    ):
        self.error = error
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BatchUnbindTemplateResponseBody(TeaModel):
    def __init__(
        self,
        bindings: List[BatchUnbindTemplateResponseBodyBindings] = None,
        request_id: str = None,
    ):
        self.bindings = bindings
        self.request_id = request_id

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = BatchUnbindTemplateResponseBodyBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchUnbindTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUnbindTemplateResponseBody = None,
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
            temp_model = BatchUnbindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUnbindTemplatesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BatchUnbindTemplatesResponseBodyResults(TeaModel):
    def __init__(
        self,
        error: str = None,
        instance_id: str = None,
        instance_type: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.error = error
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BatchUnbindTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[BatchUnbindTemplatesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = BatchUnbindTemplatesResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class BatchUnbindTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchUnbindTemplatesResponseBody = None,
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
            temp_model = BatchUnbindTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindDirectoryRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class BindDirectoryResponseBody(TeaModel):
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


class BindDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindDirectoryResponseBody = None,
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
            temp_model = BindDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindParentPlatformDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class BindParentPlatformDeviceResponseBody(TeaModel):
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


class BindParentPlatformDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindParentPlatformDeviceResponseBody = None,
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
            temp_model = BindParentPlatformDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPurchasedDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        group_id: str = None,
        owner_id: int = None,
        region: str = None,
    ):
        self.device_id = device_id
        self.group_id = group_id
        self.owner_id = owner_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class BindPurchasedDeviceResponseBody(TeaModel):
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


class BindPurchasedDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindPurchasedDeviceResponseBody = None,
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
            temp_model = BindPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindTemplateRequest(TeaModel):
    def __init__(
        self,
        apply_all: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        replace: bool = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.apply_all = apply_all
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.replace = replace
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_all is not None:
            result['ApplyAll'] = self.apply_all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyAll') is not None:
            self.apply_all = m.get('ApplyAll')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class BindTemplateResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        request_id: str = None,
        template_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class BindTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindTemplateResponseBody = None,
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
            temp_model = BindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CaptureDeviceSnapshotRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        mode: str = None,
        owner_id: int = None,
        snapshot_config: str = None,
        stream_id: str = None,
    ):
        self.device_id = device_id
        self.mode = mode
        self.owner_id = owner_id
        self.snapshot_config = snapshot_config
        self.stream_id = stream_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class CaptureDeviceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CaptureDeviceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CaptureDeviceSnapshotResponseBody = None,
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
            temp_model = CaptureDeviceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuousAdjustRequest(TeaModel):
    def __init__(
        self,
        focus: str = None,
        id: str = None,
        iris: str = None,
        owner_id: int = None,
    ):
        self.focus = focus
        self.id = id
        self.iris = iris
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ContinuousAdjustResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ContinuousAdjustResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContinuousAdjustResponseBody = None,
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
            temp_model = ContinuousAdjustResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuousMoveRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        pan: str = None,
        tilt: str = None,
        zoom: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
        return self


class ContinuousMoveResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ContinuousMoveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContinuousMoveResponseBody = None,
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
            temp_model = ContinuousMoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAIConfigRequest(TeaModel):
    def __init__(
        self,
        capture_interval: int = None,
        configs: str = None,
        description: str = None,
        end_time: int = None,
        features: str = None,
        instance_id: int = None,
        instance_type: str = None,
        owner_id: int = None,
        start_time: int = None,
        status: str = None,
    ):
        self.capture_interval = capture_interval
        self.configs = configs
        self.description = description
        self.end_time = end_time
        self.features = features
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAIConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        request_id: str = None,
    ):
        self.config_id = config_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAIConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAIConfigResponseBody = None,
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
            temp_model = CreateAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        internal_ports: str = None,
        maintain_time: str = None,
        name: str = None,
        owner_id: int = None,
        security_group_id: str = None,
    ):
        self.description = description
        self.internal_ports = internal_ports
        self.maintain_time = maintain_time
        self.name = name
        self.owner_id = owner_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.internal_ports is not None:
            result['InternalPorts'] = self.internal_ports
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InternalPorts') is not None:
            self.internal_ports = m.get('InternalPorts')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateClusterResponseBody = None,
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        description: str = None,
        directory_id: str = None,
        dsn: str = None,
        gb_id: str = None,
        group_id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        owner_id: int = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        self.alarm_method = alarm_method
        self.auto_pos = auto_pos
        self.auto_start = auto_start
        self.description = description
        self.directory_id = directory_id
        self.dsn = dsn
        self.gb_id = gb_id
        self.group_id = group_id
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.owner_id = owner_id
        self.params = params
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.pos_interval = pos_interval
        self.type = type
        self.url = url
        self.username = username
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceResponseBody = None,
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
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm: int = None,
        channel_id: int = None,
        end_time: int = None,
        expire: int = None,
        id: str = None,
        object_type: int = None,
        owner_id: int = None,
        start_time: int = None,
        sub_alarm: int = None,
    ):
        self.alarm = alarm
        self.channel_id = channel_id
        self.end_time = end_time
        self.expire = expire
        self.id = id
        self.object_type = object_type
        self.owner_id = owner_id
        self.start_time = start_time
        self.sub_alarm = sub_alarm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm is not None:
            result['Alarm'] = self.alarm
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_alarm is not None:
            result['SubAlarm'] = self.sub_alarm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarm') is not None:
            self.alarm = m.get('Alarm')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubAlarm') is not None:
            self.sub_alarm = m.get('SubAlarm')
        return self


class CreateDeviceAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_delay: int = None,
        alarm_id: str = None,
        expire: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.alarm_delay = alarm_delay
        self.alarm_id = alarm_id
        self.expire = expire
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_delay is not None:
            result['AlarmDelay'] = self.alarm_delay
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmDelay') is not None:
            self.alarm_delay = m.get('AlarmDelay')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateDeviceAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceAlarmResponseBody = None,
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
            temp_model = CreateDeviceAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceSnapshotRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        mode: str = None,
        owner_id: int = None,
        snapshot_config: str = None,
        stream_id: str = None,
    ):
        self.device_id = device_id
        self.mode = mode
        self.owner_id = owner_id
        self.snapshot_config = snapshot_config
        self.stream_id = stream_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class CreateDeviceSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceSnapshotResponseBody = None,
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
            temp_model = CreateDeviceSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDirectoryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        name: str = None,
        owner_id: int = None,
        parent_id: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.name = name
        self.owner_id = owner_id
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class CreateDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDirectoryResponseBody = None,
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
            temp_model = CreateDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        callback: str = None,
        description: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
    ):
        self.app = app
        self.callback = callback
        self.description = description
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        self.name = name
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: int = None,
        id: str = None,
        request_id: str = None,
    ):
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParentPlatformRequest(TeaModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_password: str = None,
        client_username: str = None,
        description: str = None,
        gb_id: str = None,
        ip: str = None,
        name: str = None,
        owner_id: int = None,
        port: int = None,
        protocol: str = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_password = client_password
        self.client_username = client_username
        self.description = description
        self.gb_id = gb_id
        self.ip = ip
        self.name = name
        self.owner_id = owner_id
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class CreateParentPlatformResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateParentPlatformResponseBody = None,
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
            temp_model = CreateParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRenderingDeviceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cluster_id: str = None,
        count: int = None,
        description: str = None,
        edge_node_name: str = None,
        isp: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        owner_id: int = None,
        password: str = None,
        period: int = None,
        period_unit: str = None,
        security_group_id: str = None,
        specification: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.cluster_id = cluster_id
        self.count = count
        self.description = description
        self.edge_node_name = edge_node_name
        self.isp = isp
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_name = instance_name
        self.owner_id = owner_id
        self.password = password
        self.period = period
        self.period_unit = period_unit
        self.security_group_id = security_group_id
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.count is not None:
            result['Count'] = self.count
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class CreateRenderingDeviceResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRenderingDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRenderingDeviceResponseBody = None,
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
            temp_model = CreateRenderingDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamSnapshotRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        location: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.location = location
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateStreamSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        format: str = None,
        height: int = None,
        id: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        request_id: str = None,
        timestamp: int = None,
        url: str = None,
        width: int = None,
    ):
        self.format = format
        self.height = height
        self.id = id
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_object = oss_object
        self.request_id = request_id
        self.timestamp = timestamp
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class CreateStreamSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStreamSnapshotResponseBody = None,
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
            temp_model = CreateStreamSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        callback: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        interval: int = None,
        jpg_on_demand: str = None,
        jpg_overwrite: str = None,
        jpg_sequence: str = None,
        mp_4: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        owner_id: int = None,
        region: str = None,
        retention: int = None,
        trans_configs_json: str = None,
        trigger: str = None,
        type: str = None,
    ):
        self.callback = callback
        self.description = description
        self.file_format = file_format
        self.flv = flv
        self.hls_m3u_8 = hls_m3u_8
        self.hls_ts = hls_ts
        self.interval = interval
        self.jpg_on_demand = jpg_on_demand
        self.jpg_overwrite = jpg_overwrite
        self.jpg_sequence = jpg_sequence
        self.mp_4 = mp_4
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_file_prefix = oss_file_prefix
        self.owner_id = owner_id
        self.region = region
        self.retention = retention
        self.trans_configs_json = trans_configs_json
        self.trigger = trigger
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAIConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        owner_id: int = None,
    ):
        self.config_id = config_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteAIConfigResponseBody(TeaModel):
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


class DeleteAIConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAIConfigResponseBody = None,
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
            temp_model = DeleteAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBucketRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        owner_id: int = None,
    ):
        self.bucket_name = bucket_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteBucketResponseBody(TeaModel):
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


class DeleteBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBucketResponseBody = None,
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
            temp_model = DeleteBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        owner_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteClusterResponseBody(TeaModel):
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


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteClusterResponseBody = None,
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteDeviceResponseBody(TeaModel):
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


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceResponseBody = None,
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
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoryRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteDirectoryResponseBody(TeaModel):
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


class DeleteDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDirectoryResponseBody = None,
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
            temp_model = DeleteDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteGroupResponseBody(TeaModel):
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


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGroupResponseBody = None,
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
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParentPlatformRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteParentPlatformResponseBody(TeaModel):
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


class DeleteParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteParentPlatformResponseBody = None,
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
            temp_model = DeleteParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePresetRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        preset_id: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.preset_id = preset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        return self


class DeletePresetResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePresetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePresetResponseBody = None,
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
            temp_model = DeletePresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePurchasedDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeletePurchasedDeviceResponseBody(TeaModel):
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


class DeletePurchasedDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePurchasedDeviceResponseBody = None,
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
            temp_model = DeletePurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRenderingDeviceInternetPortsRequest(TeaModel):
    def __init__(
        self,
        isp: str = None,
        instance_ids: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        owner_id: int = None,
    ):
        self.isp = isp
        self.instance_ids = instance_ids
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
    ):
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        return self


class DeleteRenderingDeviceInternetPortsResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds = None,
        request_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            temp_model = DeleteRenderingDeviceInternetPortsResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRenderingDeviceInternetPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRenderingDeviceInternetPortsResponseBody = None,
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
            temp_model = DeleteRenderingDeviceInternetPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRenderingDevicesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
    ):
        self.instance_ids = instance_ids
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteRenderingDevicesResponseBody(TeaModel):
    def __init__(
        self,
        failed_ids: List[str] = None,
        request_id: str = None,
    ):
        self.failed_ids = failed_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRenderingDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRenderingDevicesResponseBody = None,
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
            temp_model = DeleteRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteTemplateResponseBody(TeaModel):
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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        owner_id: int = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DeleteVsPullStreamInfoConfigResponseBody(TeaModel):
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


class DeleteVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVsPullStreamInfoConfigResponseBody = None,
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
            temp_model = DeleteVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteVsStreamsNotifyUrlConfigResponseBody(TeaModel):
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


class DeleteVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVsStreamsNotifyUrlConfigResponseBody = None,
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
            temp_model = DeleteVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAIConfigRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        owner_id: int = None,
    ):
        self.config_id = config_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAIConfigResponseBodyAIConfig(TeaModel):
    def __init__(
        self,
        capture_interval: int = None,
        configs: str = None,
        description: str = None,
        end_time: int = None,
        features: str = None,
        instance_id: int = None,
        instance_type: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.capture_interval = capture_interval
        self.configs = configs
        self.description = description
        self.end_time = end_time
        self.features = features
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAIConfigResponseBody(TeaModel):
    def __init__(
        self,
        aiconfig: DescribeAIConfigResponseBodyAIConfig = None,
        request_id: str = None,
    ):
        self.aiconfig = aiconfig
        self.request_id = request_id

    def validate(self):
        if self.aiconfig:
            self.aiconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiconfig is not None:
            result['AIConfig'] = self.aiconfig.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIConfig') is not None:
            temp_model = DescribeAIConfigResponseBodyAIConfig()
            self.aiconfig = temp_model.from_map(m['AIConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAIConfigResponseBody = None,
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
            temp_model = DescribeAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAIConfigListRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAIConfigListResponseBodyAIConfigListAIConfigList(TeaModel):
    def __init__(
        self,
        capture_interval: int = None,
        config_id: str = None,
        configs: str = None,
        description: str = None,
        end_time: int = None,
        features: str = None,
        instance_id: int = None,
        instance_type: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.capture_interval = capture_interval
        self.config_id = config_id
        self.configs = configs
        self.description = description
        self.end_time = end_time
        self.features = features
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAIConfigListResponseBodyAIConfigList(TeaModel):
    def __init__(
        self,
        aiconfig_list: List[DescribeAIConfigListResponseBodyAIConfigListAIConfigList] = None,
    ):
        self.aiconfig_list = aiconfig_list

    def validate(self):
        if self.aiconfig_list:
            for k in self.aiconfig_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AIConfigList'] = []
        if self.aiconfig_list is not None:
            for k in self.aiconfig_list:
                result['AIConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aiconfig_list = []
        if m.get('AIConfigList') is not None:
            for k in m.get('AIConfigList'):
                temp_model = DescribeAIConfigListResponseBodyAIConfigListAIConfigList()
                self.aiconfig_list.append(temp_model.from_map(k))
        return self


class DescribeAIConfigListResponseBody(TeaModel):
    def __init__(
        self,
        aiconfig_list: DescribeAIConfigListResponseBodyAIConfigList = None,
        request_id: str = None,
    ):
        self.aiconfig_list = aiconfig_list
        self.request_id = request_id

    def validate(self):
        if self.aiconfig_list:
            self.aiconfig_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aiconfig_list is not None:
            result['AIConfigList'] = self.aiconfig_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIConfigList') is not None:
            temp_model = DescribeAIConfigListResponseBodyAIConfigList()
            self.aiconfig_list = temp_model.from_map(m['AIConfigList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIConfigListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAIConfigListResponseBody = None,
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
            temp_model = DescribeAIConfigListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAIEventListRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        feature: str = None,
        instance_id: int = None,
        instance_type: str = None,
        owner_id: int = None,
        start_time: int = None,
        triggered: bool = None,
    ):
        self.end_time = end_time
        self.feature = feature
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.start_time = start_time
        self.triggered = triggered

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.triggered is not None:
            result['Triggered'] = self.triggered
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Triggered') is not None:
            self.triggered = m.get('Triggered')
        return self


class DescribeAIEventListResponseBody(TeaModel):
    def __init__(
        self,
        aievent_list: str = None,
        request_id: str = None,
    ):
        self.aievent_list = aievent_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aievent_list is not None:
            result['AIEventList'] = self.aievent_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIEventList') is not None:
            self.aievent_list = m.get('AIEventList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAIEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAIEventListResponseBody = None,
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
            temp_model = DescribeAIEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountStatRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeAccountStatResponseBody(TeaModel):
    def __init__(
        self,
        group_limit: int = None,
        group_num: int = None,
        id: str = None,
        request_id: str = None,
        template_limit: int = None,
        template_num: int = None,
    ):
        self.group_limit = group_limit
        self.group_num = group_num
        self.id = id
        self.request_id = request_id
        self.template_limit = template_limit
        self.template_num = template_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_limit is not None:
            result['GroupLimit'] = self.group_limit
        if self.group_num is not None:
            result['GroupNum'] = self.group_num
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_limit is not None:
            result['TemplateLimit'] = self.template_limit
        if self.template_num is not None:
            result['TemplateNum'] = self.template_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupLimit') is not None:
            self.group_limit = m.get('GroupLimit')
        if m.get('GroupNum') is not None:
            self.group_num = m.get('GroupNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateLimit') is not None:
            self.template_limit = m.get('TemplateLimit')
        if m.get('TemplateNum') is not None:
            self.template_num = m.get('TemplateNum')
        return self


class DescribeAccountStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccountStatResponseBody = None,
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
            temp_model = DescribeAccountStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        owner_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeClusterResponseBodyInternalPorts(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        platform: str = None,
        port: List[str] = None,
    ):
        self.ip_protocol = ip_protocol
        self.platform = platform
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        internal_ports: List[DescribeClusterResponseBodyInternalPorts] = None,
        maintain_time: str = None,
        name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.internal_ports = internal_ports
        self.maintain_time = maintain_time
        self.name = name
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.internal_ports:
            for k in self.internal_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['InternalPorts'] = []
        if self.internal_ports is not None:
            for k in self.internal_ports:
                result['InternalPorts'].append(k.to_map() if k else None)
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.internal_ports = []
        if m.get('InternalPorts') is not None:
            for k in m.get('InternalPorts'):
                temp_model = DescribeClusterResponseBodyInternalPorts()
                self.internal_ports.append(temp_model.from_map(k))
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterResponseBody = None,
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
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterDevicesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        edge_node_name: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        platform: str = None,
        specification: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.edge_node_name = edge_node_name
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.platform = platform
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class DescribeClusterDevicesResponseBodyDevicesIpInfos(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        isp: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_type: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.isp = isp
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.nat_type = nat_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        return self


class DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork(TeaModel):
    def __init__(
        self,
        container_ports: str = None,
        external_ip: str = None,
        external_ports: str = None,
    ):
        self.container_ports = container_ports
        self.external_ip = external_ip
        self.external_ports = external_ports

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_ports is not None:
            result['ExternalPorts'] = self.external_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPorts') is not None:
            self.external_ports = m.get('ExternalPorts')
        return self


class DescribeClusterDevicesResponseBodyDevicesPodInfos(TeaModel):
    def __init__(
        self,
        network: List[DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork] = None,
        pod_id: str = None,
        status: str = None,
    ):
        self.network = network
        self.pod_id = pod_id
        self.status = status

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesPodInfosNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        description: str = None,
        edge_node_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        ip_infos: List[DescribeClusterDevicesResponseBodyDevicesIpInfos] = None,
        mac_address: str = None,
        period: int = None,
        period_unit: str = None,
        platform_type: str = None,
        pod_infos: List[DescribeClusterDevicesResponseBodyDevicesPodInfos] = None,
        server: str = None,
        status: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.description = description
        self.edge_node_name = edge_node_name
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.ip_infos = ip_infos
        self.mac_address = mac_address
        self.period = period
        self.period_unit = period_unit
        self.platform_type = platform_type
        self.pod_infos = pod_infos
        self.server = server
        self.status = status

    def validate(self):
        if self.ip_infos:
            for k in self.ip_infos:
                if k:
                    k.validate()
        if self.pod_infos:
            for k in self.pod_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpInfos'] = []
        if self.ip_infos is not None:
            for k in self.ip_infos:
                result['IpInfos'].append(k.to_map() if k else None)
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        result['PodInfos'] = []
        if self.pod_infos is not None:
            for k in self.pod_infos:
                result['PodInfos'].append(k.to_map() if k else None)
        if self.server is not None:
            result['Server'] = self.server
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_infos = []
        if m.get('IpInfos') is not None:
            for k in m.get('IpInfos'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesIpInfos()
                self.ip_infos.append(temp_model.from_map(k))
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        self.pod_infos = []
        if m.get('PodInfos') is not None:
            for k in m.get('PodInfos'):
                temp_model = DescribeClusterDevicesResponseBodyDevicesPodInfos()
                self.pod_infos.append(temp_model.from_map(k))
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClusterDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[DescribeClusterDevicesResponseBodyDevices] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.devices = devices
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeClusterDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeClusterDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterDevicesResponseBody = None,
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
            temp_model = DescribeClusterDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeClustersResponseBodyClustersInternalPorts(TeaModel):
    def __init__(
        self,
        ip_protocol: str = None,
        platform: str = None,
        port: List[str] = None,
    ):
        self.ip_protocol = ip_protocol
        self.platform = platform
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        internal_ports: List[DescribeClustersResponseBodyClustersInternalPorts] = None,
        maintain_time: str = None,
        name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.internal_ports = internal_ports
        self.maintain_time = maintain_time
        self.name = name
        self.status = status

    def validate(self):
        if self.internal_ports:
            for k in self.internal_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        result['InternalPorts'] = []
        if self.internal_ports is not None:
            for k in self.internal_ports:
                result['InternalPorts'].append(k.to_map() if k else None)
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.internal_ports = []
        if m.get('InternalPorts') is not None:
            for k in m.get('InternalPorts'):
                temp_model = DescribeClustersResponseBodyClustersInternalPorts()
                self.internal_ports.append(temp_model.from_map(k))
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeClustersResponseBodyClusters] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.clusters = clusters
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClustersResponseBody = None,
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
            temp_model = DescribeClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContainerInstanceIdRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        owner_id: int = None,
        pod_index: int = None,
    ):
        self.node_name = node_name
        self.owner_id = owner_id
        self.pod_index = pod_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_index is not None:
            result['PodIndex'] = self.pod_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodIndex') is not None:
            self.pod_index = m.get('PodIndex')
        return self


class DescribeContainerInstanceIdResponseBodyInstanceDetail(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeContainerInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        instance_detail: DescribeContainerInstanceIdResponseBodyInstanceDetail = None,
        request_id: str = None,
    ):
        self.instance_detail = instance_detail
        self.request_id = request_id

    def validate(self):
        if self.instance_detail:
            self.instance_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_detail is not None:
            result['InstanceDetail'] = self.instance_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceDetail') is not None:
            temp_model = DescribeContainerInstanceIdResponseBodyInstanceDetail()
            self.instance_detail = temp_model.from_map(m['InstanceDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeContainerInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContainerInstanceIdResponseBody = None,
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
            temp_model = DescribeContainerInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        include_directory: bool = None,
        include_stats: bool = None,
        owner_id: int = None,
    ):
        self.id = id
        self.include_directory = include_directory
        self.include_stats = include_stats
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDeviceResponseBodyDirectory(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDeviceResponseBodyStats(TeaModel):
    def __init__(
        self,
        channel_num: int = None,
        failed_num: int = None,
        offline_num: int = None,
        online_num: int = None,
        stream_num: int = None,
    ):
        self.channel_num = channel_num
        self.failed_num = failed_num
        self.offline_num = offline_num
        self.online_num = online_num
        self.stream_num = stream_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        return self


class DescribeDeviceResponseBody(TeaModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        channel_sync_time: str = None,
        created_time: str = None,
        description: str = None,
        directory: DescribeDeviceResponseBodyDirectory = None,
        directory_id: str = None,
        dsn: str = None,
        enabled: bool = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        protocol: str = None,
        registered_time: str = None,
        request_id: str = None,
        stats: DescribeDeviceResponseBodyStats = None,
        status: str = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        self.alarm_method = alarm_method
        self.auto_pos = auto_pos
        self.auto_start = auto_start
        self.channel_sync_time = channel_sync_time
        self.created_time = created_time
        self.description = description
        self.directory = directory
        self.directory_id = directory_id
        self.dsn = dsn
        self.enabled = enabled
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.params = params
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.pos_interval = pos_interval
        self.protocol = protocol
        self.registered_time = registered_time
        self.request_id = request_id
        self.stats = stats
        self.status = status
        self.type = type
        self.url = url
        self.username = username
        self.vendor = vendor

    def validate(self):
        if self.directory:
            self.directory.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = DescribeDeviceResponseBodyDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stats') is not None:
            temp_model = DescribeDeviceResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceResponseBody = None,
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
            temp_model = DescribeDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceChannelsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(
        self,
        channel_id: int = None,
        device_id: str = None,
        device_status: str = None,
        gb_id: str = None,
        name: str = None,
        params: str = None,
        stream_id: str = None,
        stream_status: str = None,
    ):
        self.channel_id = channel_id
        self.device_id = device_id
        self.device_status = device_status
        self.gb_id = gb_id
        self.name = name
        self.params = params
        self.stream_id = stream_id
        self.stream_status = stream_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class DescribeDeviceChannelsResponseBody(TeaModel):
    def __init__(
        self,
        channels: List[DescribeDeviceChannelsResponseBodyChannels] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.channels = channels
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = DescribeDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeviceChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceChannelsResponseBody = None,
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
            temp_model = DescribeDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceGatewayRequest(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        expire: int = None,
        id: str = None,
        owner_id: int = None,
    ):
        self.client_ip = client_ip
        self.expire = expire
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDeviceGatewayResponseBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        protocol: str = None,
        request_id: str = None,
        token: str = None,
    ):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.request_id = request_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeDeviceGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceGatewayResponseBody = None,
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
            temp_model = DescribeDeviceGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeviceURLRequest(TeaModel):
    def __init__(
        self,
        auth: bool = None,
        expire: int = None,
        id: str = None,
        mode: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        stream: str = None,
        type: str = None,
    ):
        self.auth = auth
        self.expire = expire
        self.id = id
        self.mode = mode
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        self.stream = stream
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDeviceURLResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.expire_time = expire_time
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeDeviceURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeviceURLResponseBody = None,
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
            temp_model = DescribeDeviceURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        dsn: str = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        include_directory: bool = None,
        include_stats: bool = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        sort_direction: str = None,
        status: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.directory_id = directory_id
        self.dsn = dsn
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.include_directory = include_directory
        self.include_stats = include_stats
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.parent_id = parent_id
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.status = status
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.include_directory is not None:
            result['IncludeDirectory'] = self.include_directory
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeDirectory') is not None:
            self.include_directory = m.get('IncludeDirectory')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeDevicesResponseBodyDevicesDirectory(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDevicesResponseBodyDevicesStats(TeaModel):
    def __init__(
        self,
        channel_num: int = None,
        failed_num: int = None,
        offline_num: int = None,
        online_num: int = None,
        stream_num: int = None,
    ):
        self.channel_num = channel_num
        self.failed_num = failed_num
        self.offline_num = offline_num
        self.online_num = online_num
        self.stream_num = stream_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num
        if self.offline_num is not None:
            result['OfflineNum'] = self.offline_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.stream_num is not None:
            result['StreamNum'] = self.stream_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')
        if m.get('OfflineNum') is not None:
            self.offline_num = m.get('OfflineNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('StreamNum') is not None:
            self.stream_num = m.get('StreamNum')
        return self


class DescribeDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_directory: bool = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        channel_sync_time: str = None,
        created_time: str = None,
        description: str = None,
        directory: DescribeDevicesResponseBodyDevicesDirectory = None,
        directory_id: str = None,
        dsn: str = None,
        enabled: bool = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        protocol: str = None,
        registered_time: str = None,
        stats: DescribeDevicesResponseBodyDevicesStats = None,
        status: str = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        self.alarm_method = alarm_method
        self.auto_directory = auto_directory
        self.auto_pos = auto_pos
        self.auto_start = auto_start
        self.channel_sync_time = channel_sync_time
        self.created_time = created_time
        self.description = description
        self.directory = directory
        self.directory_id = directory_id
        self.dsn = dsn
        self.enabled = enabled
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.params = params
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.pos_interval = pos_interval
        self.protocol = protocol
        self.registered_time = registered_time
        self.stats = stats
        self.status = status
        self.type = type
        self.url = url
        self.username = username
        self.vendor = vendor

    def validate(self):
        if self.directory:
            self.directory.validate()
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_directory is not None:
            result['AutoDirectory'] = self.auto_directory
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.channel_sync_time is not None:
            result['ChannelSyncTime'] = self.channel_sync_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.registered_time is not None:
            result['RegisteredTime'] = self.registered_time
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoDirectory') is not None:
            self.auto_directory = m.get('AutoDirectory')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ChannelSyncTime') is not None:
            self.channel_sync_time = m.get('ChannelSyncTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegisteredTime') is not None:
            self.registered_time = m.get('RegisteredTime')
        if m.get('Stats') is not None:
            temp_model = DescribeDevicesResponseBodyDevicesStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[DescribeDevicesResponseBodyDevices] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.devices = devices
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDevicesResponseBody = None,
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
            temp_model = DescribeDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        no_pagination: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        sort_direction: str = None,
    ):
        self.group_id = group_id
        self.no_pagination = no_pagination
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.parent_id = parent_id
        self.sort_by = sort_by
        self.sort_direction = sort_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.no_pagination is not None:
            result['NoPagination'] = self.no_pagination
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NoPagination') is not None:
            self.no_pagination = m.get('NoPagination')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        directories: List[DescribeDirectoriesResponseBodyDirectories] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.directories = directories
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDirectoriesResponseBody = None,
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
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoryRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
        request_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDirectoryResponseBody = None,
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
            temp_model = DescribeDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExternalStreamURLRequest(TeaModel):
    def __init__(
        self,
        kind: str = None,
        owner_id: int = None,
        profile: str = None,
        tx_id: str = None,
        url: str = None,
    ):
        self.kind = kind
        self.owner_id = owner_id
        self.profile = profile
        self.tx_id = tx_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['Kind'] = self.kind
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeExternalStreamURLResponseBody(TeaModel):
    def __init__(
        self,
        ip: str = None,
        out_protocol: str = None,
        port: int = None,
        profile: str = None,
        request_id: str = None,
        tx_id: str = None,
        url: str = None,
    ):
        self.ip = ip
        self.out_protocol = out_protocol
        self.port = port
        self.profile = profile
        self.request_id = request_id
        self.tx_id = tx_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeExternalStreamURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExternalStreamURLResponseBody = None,
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
            temp_model = DescribeExternalStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        include_stats: bool = None,
        owner_id: int = None,
    ):
        self.id = id
        self.include_stats = include_stats
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeGroupResponseBodyStats(TeaModel):
    def __init__(
        self,
        device_num: int = None,
        ied_num: int = None,
        ipc_num: int = None,
        platform_num: int = None,
    ):
        self.device_num = device_num
        self.ied_num = ied_num
        self.ipc_num = ipc_num
        self.platform_num = platform_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        return self


class DescribeGroupResponseBody(TeaModel):
    def __init__(
        self,
        alias_id: str = None,
        app: str = None,
        callback: str = None,
        created_time: str = None,
        description: str = None,
        enabled: bool = None,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: int = None,
        gb_tcp_ports: List[str] = None,
        gb_udp_ports: List[str] = None,
        id: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
        request_id: str = None,
        stats: DescribeGroupResponseBodyStats = None,
        status: str = None,
    ):
        self.alias_id = alias_id
        self.app = app
        self.callback = callback
        self.created_time = created_time
        self.description = description
        self.enabled = enabled
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.gb_tcp_ports = gb_tcp_ports
        self.gb_udp_ports = gb_udp_ports
        self.id = id
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        self.name = name
        self.out_protocol = out_protocol
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region
        self.request_id = request_id
        self.stats = stats
        self.status = status

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupResponseBodyStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupResponseBody = None,
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
            temp_model = DescribeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        in_protocol: str = None,
        include_stats: bool = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
        sort_by: str = None,
        sort_direction: str = None,
        status: str = None,
    ):
        self.id = id
        self.in_protocol = in_protocol
        self.include_stats = include_stats
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.region = region
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.include_stats is not None:
            result['IncludeStats'] = self.include_stats
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('IncludeStats') is not None:
            self.include_stats = m.get('IncludeStats')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGroupsResponseBodyGroupsStats(TeaModel):
    def __init__(
        self,
        device_num: int = None,
        ied_num: int = None,
        ipc_num: int = None,
        platform_num: int = None,
    ):
        self.device_num = device_num
        self.ied_num = ied_num
        self.ipc_num = ipc_num
        self.platform_num = platform_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.ied_num is not None:
            result['IedNum'] = self.ied_num
        if self.ipc_num is not None:
            result['IpcNum'] = self.ipc_num
        if self.platform_num is not None:
            result['PlatformNum'] = self.platform_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('IedNum') is not None:
            self.ied_num = m.get('IedNum')
        if m.get('IpcNum') is not None:
            self.ipc_num = m.get('IpcNum')
        if m.get('PlatformNum') is not None:
            self.platform_num = m.get('PlatformNum')
        return self


class DescribeGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        alias_id: str = None,
        app: str = None,
        callback: str = None,
        created_time: str = None,
        description: str = None,
        enabled: bool = None,
        gb_id: str = None,
        gb_ip: str = None,
        gb_port: int = None,
        gb_tcp_ports: List[str] = None,
        gb_udp_ports: List[str] = None,
        id: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
        stats: DescribeGroupsResponseBodyGroupsStats = None,
        status: str = None,
    ):
        self.alias_id = alias_id
        self.app = app
        self.callback = callback
        self.created_time = created_time
        self.description = description
        self.enabled = enabled
        self.gb_id = gb_id
        self.gb_ip = gb_ip
        self.gb_port = gb_port
        self.gb_tcp_ports = gb_tcp_ports
        self.gb_udp_ports = gb_udp_ports
        self.id = id
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        self.name = name
        self.out_protocol = out_protocol
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region
        self.stats = stats
        self.status = status

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_id is not None:
            result['AliasId'] = self.alias_id
        if self.app is not None:
            result['App'] = self.app
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.gb_ip is not None:
            result['GbIp'] = self.gb_ip
        if self.gb_port is not None:
            result['GbPort'] = self.gb_port
        if self.gb_tcp_ports is not None:
            result['GbTcpPorts'] = self.gb_tcp_ports
        if self.gb_udp_ports is not None:
            result['GbUdpPorts'] = self.gb_udp_ports
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        if self.stats is not None:
            result['Stats'] = self.stats.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasId') is not None:
            self.alias_id = m.get('AliasId')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GbIp') is not None:
            self.gb_ip = m.get('GbIp')
        if m.get('GbPort') is not None:
            self.gb_port = m.get('GbPort')
        if m.get('GbTcpPorts') is not None:
            self.gb_tcp_ports = m.get('GbTcpPorts')
        if m.get('GbUdpPorts') is not None:
            self.gb_udp_ports = m.get('GbUdpPorts')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Stats') is not None:
            temp_model = DescribeGroupsResponseBodyGroupsStats()
            self.stats = temp_model.from_map(m['Stats'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[DescribeGroupsResponseBodyGroups] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.groups = groups
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupsResponseBody = None,
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
            temp_model = DescribeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeDevicesInfoRequest(TeaModel):
    def __init__(
        self,
        node_name: str = None,
        owner_id: int = None,
    ):
        self.node_name = node_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        name: str = None,
        server: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.name = name
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.server is not None:
            result['Server'] = self.server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        return self


class DescribeNodeDevicesInfoResponseBodyNodeDevices(TeaModel):
    def __init__(
        self,
        device_infos: List[DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos] = None,
        node_name: str = None,
    ):
        self.device_infos = device_infos
        self.node_name = node_name

    def validate(self):
        if self.device_infos:
            for k in self.device_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k in self.device_infos:
                result['DeviceInfos'].append(k.to_map() if k else None)
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k in m.get('DeviceInfos'):
                temp_model = DescribeNodeDevicesInfoResponseBodyNodeDevicesDeviceInfos()
                self.device_infos.append(temp_model.from_map(k))
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class DescribeNodeDevicesInfoResponseBody(TeaModel):
    def __init__(
        self,
        node_devices: List[DescribeNodeDevicesInfoResponseBodyNodeDevices] = None,
        request_id: str = None,
    ):
        self.node_devices = node_devices
        self.request_id = request_id

    def validate(self):
        if self.node_devices:
            for k in self.node_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeDevices'] = []
        if self.node_devices is not None:
            for k in self.node_devices:
                result['NodeDevices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_devices = []
        if m.get('NodeDevices') is not None:
            for k in m.get('NodeDevices'):
                temp_model = DescribeNodeDevicesInfoResponseBodyNodeDevices()
                self.node_devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeDevicesInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNodeDevicesInfoResponseBody = None,
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
            temp_model = DescribeNodeDevicesInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeParentPlatformResponseBody(TeaModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_gb_id: str = None,
        client_ip: str = None,
        client_password: str = None,
        client_port: int = None,
        client_username: str = None,
        created_time: str = None,
        description: str = None,
        gb_id: str = None,
        id: str = None,
        ip: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_gb_id = client_gb_id
        self.client_ip = client_ip
        self.client_password = client_password
        self.client_port = client_port
        self.client_username = client_username
        self.created_time = created_time
        self.description = description
        self.gb_id = gb_id
        self.id = id
        self.ip = ip
        self.name = name
        self.port = port
        self.protocol = protocol
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParentPlatformResponseBody = None,
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
            temp_model = DescribeParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformDevicesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_direction: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_direction = sort_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeParentPlatformDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        return self


class DescribeParentPlatformDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[DescribeParentPlatformDevicesResponseBodyDevices] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.devices = devices
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeParentPlatformDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParentPlatformDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParentPlatformDevicesResponseBody = None,
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
            temp_model = DescribeParentPlatformDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParentPlatformsRequest(TeaModel):
    def __init__(
        self,
        gb_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_direction: str = None,
        status: str = None,
    ):
        self.gb_id = gb_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeParentPlatformsResponseBodyPlatforms(TeaModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_gb_id: str = None,
        client_ip: str = None,
        client_password: str = None,
        client_port: int = None,
        client_username: str = None,
        created_time: str = None,
        description: str = None,
        gb_id: str = None,
        id: str = None,
        ip: str = None,
        name: str = None,
        port: int = None,
        protocol: str = None,
        status: str = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_gb_id = client_gb_id
        self.client_ip = client_ip
        self.client_password = client_password
        self.client_port = client_port
        self.client_username = client_username
        self.created_time = created_time
        self.description = description
        self.gb_id = gb_id
        self.id = id
        self.ip = ip
        self.name = name
        self.port = port
        self.protocol = protocol
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_gb_id is not None:
            result['ClientGbId'] = self.client_gb_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientGbId') is not None:
            self.client_gb_id = m.get('ClientGbId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeParentPlatformsResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        platforms: List[DescribeParentPlatformsResponseBodyPlatforms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.platforms = platforms
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['Platforms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.platforms = []
        if m.get('Platforms') is not None:
            for k in m.get('Platforms'):
                temp_model = DescribeParentPlatformsResponseBodyPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParentPlatformsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParentPlatformsResponseBody = None,
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
            temp_model = DescribeParentPlatformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePresetsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribePresetsResponseBodyPresets(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePresetsResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        presets: List[DescribePresetsResponseBodyPresets] = None,
        request_id: str = None,
    ):
        self.id = id
        self.presets = presets
        self.request_id = request_id

    def validate(self):
        if self.presets:
            for k in self.presets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['Presets'] = []
        if self.presets is not None:
            for k in self.presets:
                result['Presets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.presets = []
        if m.get('Presets') is not None:
            for k in m.get('Presets'):
                temp_model = DescribePresetsResponseBodyPresets()
                self.presets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePresetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePresetsResponseBody = None,
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
            temp_model = DescribePresetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribePurchasedDeviceResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        order_id: str = None,
        region: str = None,
        register_code: str = None,
        request_id: str = None,
        sub_type: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.id = id
        self.name = name
        self.order_id = order_id
        self.region = region
        self.register_code = register_code
        self.request_id = request_id
        self.sub_type = sub_type
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region is not None:
            result['Region'] = self.region
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribePurchasedDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePurchasedDeviceResponseBody = None,
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
            temp_model = DescribePurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedDevicesRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_direction: str = None,
        sub_type: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.group_id = group_id
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.sub_type = sub_type
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribePurchasedDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        order_id: str = None,
        region: str = None,
        register_code: str = None,
        sub_type: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.id = id
        self.name = name
        self.order_id = order_id
        self.region = region
        self.register_code = register_code
        self.sub_type = sub_type
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.region is not None:
            result['Region'] = self.region
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribePurchasedDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[DescribePurchasedDevicesResponseBodyDevices] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.devices = devices
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribePurchasedDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePurchasedDevicesResponseBody = None,
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
            temp_model = DescribePurchasedDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        private_bucket: bool = None,
        sort_by: str = None,
        sort_direction: str = None,
        start_time: str = None,
        stream_id: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.private_bucket = private_bucket
        self.sort_by = sort_by
        self.sort_direction = sort_direction
        self.start_time = start_time
        self.stream_id = stream_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.private_bucket is not None:
            result['PrivateBucket'] = self.private_bucket
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrivateBucket') is not None:
            self.private_bucket = m.get('PrivateBucket')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        file_format: str = None,
        height: int = None,
        id: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        start_time: str = None,
        stream_id: str = None,
        template_id: str = None,
        type: str = None,
        url: str = None,
        width: int = None,
    ):
        self.end_time = end_time
        self.file_format = file_format
        self.height = height
        self.id = id
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_object = oss_object
        self.start_time = start_time
        self.stream_id = stream_id
        self.template_id = template_id
        self.type = type
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_object is not None:
            result['OssObject'] = self.oss_object
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeRecordsResponseBody(TeaModel):
    def __init__(
        self,
        next_start_time: str = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        records: List[DescribeRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.next_start_time = next_start_time
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordsResponseBody = None,
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
            temp_model = DescribeRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRenderingDevicesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
    ):
        self.instance_ids = instance_ids
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeRenderingDevicesResponseBodyDevicesIpInfos(TeaModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        isp: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_type: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.isp = isp
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.nat_type = nat_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_port is not None:
            result['ExternalPort'] = self.external_port
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip
        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.nat_type is not None:
            result['NatType'] = self.nat_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')
        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('NatType') is not None:
            self.nat_type = m.get('NatType')
        return self


class DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork(TeaModel):
    def __init__(
        self,
        container_ports: str = None,
        external_ip: str = None,
        external_ports: str = None,
    ):
        self.container_ports = container_ports
        self.external_ip = external_ip
        self.external_ports = external_ports

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_ports is not None:
            result['ContainerPorts'] = self.container_ports
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip
        if self.external_ports is not None:
            result['ExternalPorts'] = self.external_ports
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerPorts') is not None:
            self.container_ports = m.get('ContainerPorts')
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')
        if m.get('ExternalPorts') is not None:
            self.external_ports = m.get('ExternalPorts')
        return self


class DescribeRenderingDevicesResponseBodyDevicesPodInfos(TeaModel):
    def __init__(
        self,
        network: List[DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork] = None,
        pod_id: str = None,
        status: str = None,
    ):
        self.network = network
        self.pod_id = pod_id
        self.status = status

    def validate(self):
        if self.network:
            for k in self.network:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Network'] = []
        if self.network is not None:
            for k in self.network:
                result['Network'].append(k.to_map() if k else None)
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network = []
        if m.get('Network') is not None:
            for k in m.get('Network'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesPodInfosNetwork()
                self.network.append(temp_model.from_map(k))
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRenderingDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cluster_id: str = None,
        description: str = None,
        edge_node_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        ip_infos: List[DescribeRenderingDevicesResponseBodyDevicesIpInfos] = None,
        mac_address: str = None,
        period: int = None,
        period_unit: str = None,
        platform_type: str = None,
        pod_infos: List[DescribeRenderingDevicesResponseBodyDevicesPodInfos] = None,
        server_name: str = None,
        specification: str = None,
        status: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.cluster_id = cluster_id
        self.description = description
        self.edge_node_name = edge_node_name
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.ip_infos = ip_infos
        self.mac_address = mac_address
        self.period = period
        self.period_unit = period_unit
        self.platform_type = platform_type
        self.pod_infos = pod_infos
        self.server_name = server_name
        self.specification = specification
        self.status = status

    def validate(self):
        if self.ip_infos:
            for k in self.ip_infos:
                if k:
                    k.validate()
        if self.pod_infos:
            for k in self.pod_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.edge_node_name is not None:
            result['EdgeNodeName'] = self.edge_node_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpInfos'] = []
        if self.ip_infos is not None:
            for k in self.ip_infos:
                result['IpInfos'].append(k.to_map() if k else None)
        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type
        result['PodInfos'] = []
        if self.pod_infos is not None:
            for k in self.pod_infos:
                result['PodInfos'].append(k.to_map() if k else None)
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EdgeNodeName') is not None:
            self.edge_node_name = m.get('EdgeNodeName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_infos = []
        if m.get('IpInfos') is not None:
            for k in m.get('IpInfos'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesIpInfos()
                self.ip_infos.append(temp_model.from_map(k))
        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')
        self.pod_infos = []
        if m.get('PodInfos') is not None:
            for k in m.get('PodInfos'):
                temp_model = DescribeRenderingDevicesResponseBodyDevicesPodInfos()
                self.pod_infos.append(temp_model.from_map(k))
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRenderingDevicesResponseBody(TeaModel):
    def __init__(
        self,
        devices: List[DescribeRenderingDevicesResponseBodyDevices] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.devices = devices
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = DescribeRenderingDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRenderingDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRenderingDevicesResponseBody = None,
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
            temp_model = DescribeRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeStreamResponseBody(TeaModel):
    def __init__(
        self,
        app: str = None,
        created_time: str = None,
        device_id: str = None,
        enabled: bool = None,
        group_id: str = None,
        height: int = None,
        id: str = None,
        name: str = None,
        play_domain: str = None,
        protocol: str = None,
        push_domain: str = None,
        request_id: str = None,
        status: str = None,
        width: int = None,
    ):
        self.app = app
        self.created_time = created_time
        self.device_id = device_id
        self.enabled = enabled
        self.group_id = group_id
        self.height = height
        self.id = id
        self.name = name
        self.play_domain = play_domain
        self.protocol = protocol
        self.push_domain = push_domain
        self.request_id = request_id
        self.status = status
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamResponseBody = None,
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
            temp_model = DescribeStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamURLRequest(TeaModel):
    def __init__(
        self,
        auth: bool = None,
        auth_key: str = None,
        end_time: int = None,
        expire: int = None,
        id: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        start_time: int = None,
        transcode: str = None,
        type: str = None,
    ):
        self.auth = auth
        self.auth_key = auth_key
        self.end_time = end_time
        self.expire = expire
        self.id = id
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        self.start_time = start_time
        self.transcode = transcode
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.id is not None:
            result['Id'] = self.id
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeStreamURLResponseBody(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.expire_time = expire_time
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeStreamURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamURLResponseBody = None,
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
            temp_model = DescribeStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamVodListRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        id: str = None,
        owner_id: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.id = id
        self.owner_id = owner_id
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
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeStreamVodListResponseBodyRecords(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeStreamVodListResponseBody(TeaModel):
    def __init__(
        self,
        records: List[DescribeStreamVodListResponseBodyRecords] = None,
        request_id: str = None,
    ):
        self.records = records
        self.request_id = request_id

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeStreamVodListResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeStreamVodListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamVodListResponseBody = None,
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
            temp_model = DescribeStreamVodListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStreamsRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        device_id: str = None,
        domain: str = None,
        group_id: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        parent_id: str = None,
        sort_by: str = None,
        sort_direction: str = None,
    ):
        self.app = app
        self.device_id = device_id
        self.domain = domain
        self.group_id = group_id
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.parent_id = parent_id
        self.sort_by = sort_by
        self.sort_direction = sort_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        return self


class DescribeStreamsResponseBodyStreams(TeaModel):
    def __init__(
        self,
        app: str = None,
        created_time: str = None,
        device_id: str = None,
        enabled: bool = None,
        group_id: str = None,
        height: int = None,
        id: str = None,
        name: str = None,
        play_domain: str = None,
        protocol: str = None,
        push_domain: str = None,
        status: str = None,
        width: int = None,
    ):
        self.app = app
        self.created_time = created_time
        self.device_id = device_id
        self.enabled = enabled
        self.group_id = group_id
        self.height = height
        self.id = id
        self.name = name
        self.play_domain = play_domain
        self.protocol = protocol
        self.push_domain = push_domain
        self.status = status
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.status is not None:
            result['Status'] = self.status
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeStreamsResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        streams: List[DescribeStreamsResponseBodyStreams] = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.streams = streams
        self.total_count = total_count

    def validate(self):
        if self.streams:
            for k in self.streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Streams'] = []
        if self.streams is not None:
            for k in self.streams:
                result['Streams'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.streams = []
        if m.get('Streams') is not None:
            for k in m.get('Streams'):
                temp_model = DescribeStreamsResponseBodyStreams()
                self.streams.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStreamsResponseBody = None,
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
            temp_model = DescribeStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeTemplateResponseBodyTransConfigs(TeaModel):
    def __init__(
        self,
        fps: int = None,
        gop: int = None,
        height: int = None,
        id: str = None,
        name: str = None,
        video_bitrate: int = None,
        video_codec: str = None,
        width: int = None,
    ):
        self.fps = fps
        self.gop = gop
        self.height = height
        self.id = id
        self.name = name
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.height is not None:
            result['Height'] = self.height
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeTemplateResponseBody(TeaModel):
    def __init__(
        self,
        callback: str = None,
        created_time: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        id: str = None,
        interval: int = None,
        jpg_on_demand: str = None,
        jpg_overwrite: str = None,
        jpg_sequence: str = None,
        mp_4: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        region: str = None,
        request_id: str = None,
        retention: int = None,
        trans_configs: List[DescribeTemplateResponseBodyTransConfigs] = None,
        trigger: str = None,
        type: str = None,
    ):
        self.callback = callback
        self.created_time = created_time
        self.description = description
        self.file_format = file_format
        self.flv = flv
        self.hls_m3u_8 = hls_m3u_8
        self.hls_ts = hls_ts
        self.id = id
        self.interval = interval
        self.jpg_on_demand = jpg_on_demand
        self.jpg_overwrite = jpg_overwrite
        self.jpg_sequence = jpg_sequence
        self.mp_4 = mp_4
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_file_prefix = oss_file_prefix
        self.region = region
        self.request_id = request_id
        self.retention = retention
        self.trans_configs = trans_configs
        self.trigger = trigger
        self.type = type

    def validate(self):
        if self.trans_configs:
            for k in self.trans_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention is not None:
            result['Retention'] = self.retention
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplateResponseBodyTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTemplateResponseBody = None,
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
            temp_model = DescribeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_direction: str = None,
        type: str = None,
    ):
        self.id = id
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
        self.sort_direction = sort_direction
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTemplatesResponseBodyTemplatesTransConfigs(TeaModel):
    def __init__(
        self,
        fps: int = None,
        gop: int = None,
        height: int = None,
        name: str = None,
        video_bitrate: int = None,
        video_codec: str = None,
        width: int = None,
        id: str = None,
    ):
        self.fps = fps
        self.gop = gop
        self.height = height
        self.name = name
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec
        self.width = width
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fps is not None:
            result['Fps'] = self.fps
        if self.gop is not None:
            result['Gop'] = self.gop
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.width is not None:
            result['Width'] = self.width
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fps') is not None:
            self.fps = m.get('Fps')
        if m.get('Gop') is not None:
            self.gop = m.get('Gop')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        callback: str = None,
        created_time: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        id: str = None,
        interval: int = None,
        jpg_on_demand: str = None,
        jpg_overwrite: str = None,
        jpg_sequence: str = None,
        mp_4: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        region: str = None,
        retention: int = None,
        trans_configs: List[DescribeTemplatesResponseBodyTemplatesTransConfigs] = None,
        trigger: str = None,
        type: str = None,
    ):
        self.callback = callback
        self.created_time = created_time
        self.description = description
        self.file_format = file_format
        self.flv = flv
        self.hls_m3u_8 = hls_m3u_8
        self.hls_ts = hls_ts
        self.id = id
        self.interval = interval
        self.jpg_on_demand = jpg_on_demand
        self.jpg_overwrite = jpg_overwrite
        self.jpg_sequence = jpg_sequence
        self.mp_4 = mp_4
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_file_prefix = oss_file_prefix
        self.region = region
        self.retention = retention
        self.trans_configs = trans_configs
        self.trigger = trigger
        self.type = type

    def validate(self):
        if self.trans_configs:
            for k in self.trans_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        result['TransConfigs'] = []
        if self.trans_configs is not None:
            for k in self.trans_configs:
                result['TransConfigs'].append(k.to_map() if k else None)
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        self.trans_configs = []
        if m.get('TransConfigs') is not None:
            for k in m.get('TransConfigs'):
                temp_model = DescribeTemplatesResponseBodyTemplatesTransConfigs()
                self.trans_configs.append(temp_model.from_map(k))
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        templates: List[DescribeTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.templates = templates
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTemplatesResponseBody = None,
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
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVodStreamURLRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        tx_id: str = None,
        url: str = None,
    ):
        self.owner_id = owner_id
        self.tx_id = tx_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeVodStreamURLResponseBody(TeaModel):
    def __init__(
        self,
        out_protocol: str = None,
        port: int = None,
        request_id: str = None,
        tx_id: str = None,
        url: str = None,
    ):
        self.out_protocol = out_protocol
        self.port = port
        self.request_id = request_id
        self.tx_id = tx_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tx_id is not None:
            result['TxId'] = self.tx_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TxId') is not None:
            self.tx_id = m.get('TxId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeVodStreamURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVodStreamURLResponseBody = None,
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
            temp_model = DescribeVodStreamURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        owner_id: int = None,
    ):
        self.cert_name = cert_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        cert: str = None,
        cert_id: int = None,
        cert_name: str = None,
        key: str = None,
        request_id: str = None,
    ):
        self.cert = cert
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.key = key
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.key is not None:
            result['Key'] = self.key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsCertificateDetailResponseBody = None,
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
            temp_model = DescribeVsCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsCertificateListRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModelCertList(TeaModel):
    def __init__(
        self,
        cert_id: int = None,
        cert_name: str = None,
        common: str = None,
        fingerprint: str = None,
        issuer: str = None,
        last_time: int = None,
    ):
        self.cert_id = cert_id
        self.cert_name = cert_name
        self.common = common
        self.fingerprint = fingerprint
        self.issuer = issuer
        self.last_time = last_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.common is not None:
            result['Common'] = self.common
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        return self


class DescribeVsCertificateListResponseBodyCertificateListModel(TeaModel):
    def __init__(
        self,
        cert_list: List[DescribeVsCertificateListResponseBodyCertificateListModelCertList] = None,
        count: int = None,
    ):
        self.cert_list = cert_list
        self.count = count

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribeVsCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeVsCertificateListResponseBody(TeaModel):
    def __init__(
        self,
        certificate_list_model: DescribeVsCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        self.certificate_list_model = certificate_list_model
        self.request_id = request_id

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = DescribeVsCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m['CertificateListModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsCertificateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsCertificateListResponseBody = None,
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
            temp_model = DescribeVsCertificateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDevicesDataRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        group_id: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.group_id = group_id
        self.owner_id = owner_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        devices_data_value: str = None,
        time_stamp: str = None,
    ):
        self.devices_data_value = devices_data_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.devices_data_value is not None:
            result['DevicesDataValue'] = self.devices_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicesDataValue') is not None:
            self.devices_data_value = m.get('DevicesDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDevicesDataResponseBodyDevicesDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDevicesDataResponseBodyDevicesDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDevicesDataResponseBody(TeaModel):
    def __init__(
        self,
        devices_data_per_interval: DescribeVsDevicesDataResponseBodyDevicesDataPerInterval = None,
        request_id: str = None,
    ):
        self.devices_data_per_interval = devices_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.devices_data_per_interval:
            self.devices_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.devices_data_per_interval is not None:
            result['DevicesDataPerInterval'] = self.devices_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicesDataPerInterval') is not None:
            temp_model = DescribeVsDevicesDataResponseBodyDevicesDataPerInterval()
            self.devices_data_per_interval = temp_model.from_map(m['DevicesDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDevicesDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDevicesDataResponseBody = None,
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
            temp_model = DescribeVsDevicesDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        bps_value: str = None,
        time_stamp: str = None,
    ):
        self.bps_value = bps_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_value is not None:
            result['BpsValue'] = self.bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsValue') is not None:
            self.bps_value = m.get('BpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        bps_data_per_interval: DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.bps_data_per_interval = bps_data_per_interval
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m['BpsDataPerInterval'])
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainBpsDataResponseBody = None,
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
            temp_model = DescribeVsDomainBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainCertificateInfoRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo(TeaModel):
    def __init__(
        self,
        cert_domain_name: str = None,
        cert_expire_time: str = None,
        cert_life: str = None,
        cert_name: str = None,
        cert_org: str = None,
        cert_type: str = None,
        domain_name: str = None,
        sslpub: str = None,
        server_certificate_status: str = None,
        status: str = None,
    ):
        self.cert_domain_name = cert_domain_name
        self.cert_expire_time = cert_expire_time
        self.cert_life = cert_life
        self.cert_name = cert_name
        self.cert_org = cert_org
        self.cert_type = cert_type
        self.domain_name = domain_name
        self.sslpub = sslpub
        self.server_certificate_status = server_certificate_status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVsDomainCertificateInfoResponseBodyCertInfos(TeaModel):
    def __init__(
        self,
        cert_info: List[DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo] = None,
    ):
        self.cert_info = cert_info

    def validate(self):
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_info = []
        if m.get('CertInfo') is not None:
            for k in m.get('CertInfo'):
                temp_model = DescribeVsDomainCertificateInfoResponseBodyCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainCertificateInfoResponseBody(TeaModel):
    def __init__(
        self,
        cert_infos: DescribeVsDomainCertificateInfoResponseBodyCertInfos = None,
        request_id: str = None,
    ):
        self.cert_infos = cert_infos
        self.request_id = request_id

    def validate(self):
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertInfos') is not None:
            temp_model = DescribeVsDomainCertificateInfoResponseBodyCertInfos()
            self.cert_infos = temp_model.from_map(m['CertInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDomainCertificateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainCertificateInfoResponseBody = None,
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
            temp_model = DescribeVsDomainCertificateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainConfigsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        function_names: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.function_names = function_names
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.function_names is not None:
            result['FunctionNames'] = self.function_names
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs(TeaModel):
    def __init__(
        self,
        arg_name: str = None,
        arg_value: str = None,
    ):
        self.arg_name = arg_name
        self.arg_value = arg_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arg_name is not None:
            result['ArgName'] = self.arg_name
        if self.arg_value is not None:
            result['ArgValue'] = self.arg_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArgName') is not None:
            self.arg_name = m.get('ArgName')
        if m.get('ArgValue') is not None:
            self.arg_value = m.get('ArgValue')
        return self


class DescribeVsDomainConfigsResponseBodyDomainConfigs(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        function_args: List[DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs] = None,
        function_name: str = None,
        status: str = None,
    ):
        self.config_id = config_id
        self.function_args = function_args
        self.function_name = function_name
        self.status = status

    def validate(self):
        if self.function_args:
            for k in self.function_args:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        result['FunctionArgs'] = []
        if self.function_args is not None:
            for k in self.function_args:
                result['FunctionArgs'].append(k.to_map() if k else None)
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        self.function_args = []
        if m.get('FunctionArgs') is not None:
            for k in m.get('FunctionArgs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigsFunctionArgs()
                self.function_args.append(temp_model.from_map(k))
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVsDomainConfigsResponseBody(TeaModel):
    def __init__(
        self,
        domain_configs: List[DescribeVsDomainConfigsResponseBodyDomainConfigs] = None,
        request_id: str = None,
    ):
        self.domain_configs = domain_configs
        self.request_id = request_id

    def validate(self):
        if self.domain_configs:
            for k in self.domain_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainConfigs'] = []
        if self.domain_configs is not None:
            for k in self.domain_configs:
                result['DomainConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_configs = []
        if m.get('DomainConfigs') is not None:
            for k in m.get('DomainConfigs'):
                temp_model = DescribeVsDomainConfigsResponseBodyDomainConfigs()
                self.domain_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDomainConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainConfigsResponseBody = None,
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
            temp_model = DescribeVsDomainConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainDetailRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsDomainDetailResponseBodyDomainConfig(TeaModel):
    def __init__(
        self,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        domain_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        region: str = None,
        sslprotocol: str = None,
        scope: str = None,
    ):
        self.cname = cname
        self.description = description
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.domain_type = domain_type
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.region = region
        self.sslprotocol = sslprotocol
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.domain_type is not None:
            result['DomainType'] = self.domain_type
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.region is not None:
            result['Region'] = self.region
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class DescribeVsDomainDetailResponseBody(TeaModel):
    def __init__(
        self,
        domain_config: DescribeVsDomainDetailResponseBodyDomainConfig = None,
        request_id: str = None,
    ):
        self.domain_config = domain_config
        self.request_id = request_id

    def validate(self):
        if self.domain_config:
            self.domain_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_config is not None:
            result['DomainConfig'] = self.domain_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainConfig') is not None:
            temp_model = DescribeVsDomainDetailResponseBodyDomainConfig()
            self.domain_config = temp_model.from_map(m['DomainConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDomainDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainDetailResponseBody = None,
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
            temp_model = DescribeVsDomainDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainOnlineUserNumRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        query_time: str = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.query_time = query_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo(TeaModel):
    def __init__(
        self,
        transcode_template: str = None,
        user_number: int = None,
    ):
        self.transcode_template = transcode_template
        self.user_number = user_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transcode_template is not None:
            result['TranscodeTemplate'] = self.transcode_template
        if self.user_number is not None:
            result['UserNumber'] = self.user_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TranscodeTemplate') is not None:
            self.transcode_template = m.get('TranscodeTemplate')
        if m.get('UserNumber') is not None:
            self.user_number = m.get('UserNumber')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos(TeaModel):
    def __init__(
        self,
        info: List[DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo] = None,
    ):
        self.info = info

    def validate(self):
        if self.info:
            for k in self.info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Info'] = []
        if self.info is not None:
            for k in self.info:
                result['Info'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info = []
        if m.get('Info') is not None:
            for k in m.get('Info'):
                temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo()
                self.info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo(TeaModel):
    def __init__(
        self,
        infos: DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos = None,
        stream_name: str = None,
    ):
        self.infos = infos
        self.stream_name = stream_name

    def validate(self):
        if self.infos:
            self.infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.infos is not None:
            result['Infos'] = self.infos.to_map()
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Infos') is not None:
            temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfoInfos()
            self.infos = temp_model.from_map(m['Infos'])
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo(TeaModel):
    def __init__(
        self,
        live_stream_online_user_num_info: List[DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo] = None,
    ):
        self.live_stream_online_user_num_info = live_stream_online_user_num_info

    def validate(self):
        if self.live_stream_online_user_num_info:
            for k in self.live_stream_online_user_num_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamOnlineUserNumInfo'] = []
        if self.live_stream_online_user_num_info is not None:
            for k in self.live_stream_online_user_num_info:
                result['LiveStreamOnlineUserNumInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_online_user_num_info = []
        if m.get('LiveStreamOnlineUserNumInfo') is not None:
            for k in m.get('LiveStreamOnlineUserNumInfo'):
                temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfoLiveStreamOnlineUserNumInfo()
                self.live_stream_online_user_num_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainOnlineUserNumResponseBody(TeaModel):
    def __init__(
        self,
        online_user_info: DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo = None,
        request_id: str = None,
        stream_count: int = None,
        user_count: int = None,
    ):
        self.online_user_info = online_user_info
        self.request_id = request_id
        self.stream_count = stream_count
        self.user_count = user_count

    def validate(self):
        if self.online_user_info:
            self.online_user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_user_info is not None:
            result['OnlineUserInfo'] = self.online_user_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stream_count is not None:
            result['StreamCount'] = self.stream_count
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineUserInfo') is not None:
            temp_model = DescribeVsDomainOnlineUserNumResponseBodyOnlineUserInfo()
            self.online_user_info = temp_model.from_map(m['OnlineUserInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StreamCount') is not None:
            self.stream_count = m.get('StreamCount')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class DescribeVsDomainOnlineUserNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainOnlineUserNumResponseBody = None,
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
            temp_model = DescribeVsDomainOnlineUserNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainPvDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVsDomainPvDataResponseBodyPvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainPvDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        pv_data_interval: DescribeVsDomainPvDataResponseBodyPvDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.pv_data_interval = pv_data_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PvDataInterval') is not None:
            temp_model = DescribeVsDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m['PvDataInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainPvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainPvDataResponseBody = None,
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
            temp_model = DescribeVsDomainPvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainPvUvDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo(TeaModel):
    def __init__(
        self,
        pv: str = None,
        time_stamp: str = None,
        uv: str = None,
    ):
        self.pv = pv
        self.time_stamp = time_stamp
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pv is not None:
            result['PV'] = self.pv
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.uv is not None:
            result['UV'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PV') is not None:
            self.pv = m.get('PV')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        return self


class DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos(TeaModel):
    def __init__(
        self,
        pv_uv_data_info: List[DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo] = None,
    ):
        self.pv_uv_data_info = pv_uv_data_info

    def validate(self):
        if self.pv_uv_data_info:
            for k in self.pv_uv_data_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PvUvDataInfo'] = []
        if self.pv_uv_data_info is not None:
            for k in self.pv_uv_data_info:
                result['PvUvDataInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pv_uv_data_info = []
        if m.get('PvUvDataInfo') is not None:
            for k in m.get('PvUvDataInfo'):
                temp_model = DescribeVsDomainPvUvDataResponseBodyPvUvDataInfosPvUvDataInfo()
                self.pv_uv_data_info.append(temp_model.from_map(k))
        return self


class DescribeVsDomainPvUvDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        pv_uv_data_infos: DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.pv_uv_data_infos = pv_uv_data_infos
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.pv_uv_data_infos:
            self.pv_uv_data_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pv_uv_data_infos is not None:
            result['PvUvDataInfos'] = self.pv_uv_data_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PvUvDataInfos') is not None:
            temp_model = DescribeVsDomainPvUvDataResponseBodyPvUvDataInfos()
            self.pv_uv_data_infos = temp_model.from_map(m['PvUvDataInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainPvUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainPvUvDataResponseBody = None,
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
            temp_model = DescribeVsDomainPvUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainRecordDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.region = region
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        record_value: str = None,
        stream_count_value: str = None,
        time_stamp: str = None,
    ):
        self.record_value = record_value
        self.stream_count_value = stream_count_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_value is not None:
            result['RecordValue'] = self.record_value
        if self.stream_count_value is not None:
            result['StreamCountValue'] = self.stream_count_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')
        if m.get('StreamCountValue') is not None:
            self.stream_count_value = m.get('StreamCountValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainRecordDataResponseBody(TeaModel):
    def __init__(
        self,
        record_data_per_interval: DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval = None,
        request_id: str = None,
    ):
        self.record_data_per_interval = record_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.record_data_per_interval:
            self.record_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_data_per_interval is not None:
            result['RecordDataPerInterval'] = self.record_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordDataPerInterval') is not None:
            temp_model = DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval()
            self.record_data_per_interval = temp_model.from_map(m['RecordDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsDomainRecordDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainRecordDataResponseBody = None,
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
            temp_model = DescribeVsDomainRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainRegionDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainRegionDataResponseBodyValueRegionProportionData(TeaModel):
    def __init__(
        self,
        avg_object_size: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        bps: str = None,
        bytes_proportion: str = None,
        proportion: str = None,
        qps: str = None,
        region: str = None,
        region_ename: str = None,
        req_err_rate: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        self.avg_object_size = avg_object_size
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.bps = bps
        self.bytes_proportion = bytes_proportion
        self.proportion = proportion
        self.qps = qps
        self.region = region
        self.region_ename = region_ename
        self.req_err_rate = req_err_rate
        self.total_bytes = total_bytes
        self.total_query = total_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size
        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate
        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion
        if self.proportion is not None:
            result['Proportion'] = self.proportion
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename
        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate
        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes
        if self.total_query is not None:
            result['TotalQuery'] = self.total_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')
        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')
        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')
        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')
        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')
        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')
        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')
        return self


class DescribeVsDomainRegionDataResponseBodyValue(TeaModel):
    def __init__(
        self,
        region_proportion_data: List[DescribeVsDomainRegionDataResponseBodyValueRegionProportionData] = None,
    ):
        self.region_proportion_data = region_proportion_data

    def validate(self):
        if self.region_proportion_data:
            for k in self.region_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k in self.region_proportion_data:
                result['RegionProportionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k in m.get('RegionProportionData'):
                temp_model = DescribeVsDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainRegionDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: DescribeVsDomainRegionDataResponseBodyValue = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Value') is not None:
            temp_model = DescribeVsDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class DescribeVsDomainRegionDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainRegionDataResponseBody = None,
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
            temp_model = DescribeVsDomainRegionDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainReqBpsDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        req_bps_value: str = None,
        time_stamp: str = None,
    ):
        self.req_bps_value = req_bps_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_bps_value is not None:
            result['ReqBpsValue'] = self.req_bps_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqBpsValue') is not None:
            self.req_bps_value = m.get('ReqBpsValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainReqBpsDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        req_bps_data_per_interval: DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.req_bps_data_per_interval = req_bps_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.req_bps_data_per_interval:
            self.req_bps_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_bps_data_per_interval is not None:
            result['ReqBpsDataPerInterval'] = self.req_bps_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqBpsDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqBpsDataResponseBodyReqBpsDataPerInterval()
            self.req_bps_data_per_interval = temp_model.from_map(m['ReqBpsDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainReqBpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainReqBpsDataResponseBody = None,
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
            temp_model = DescribeVsDomainReqBpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainReqTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        req_traffic_value: str = None,
        time_stamp: str = None,
    ):
        self.req_traffic_value = req_traffic_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_traffic_value is not None:
            result['ReqTrafficValue'] = self.req_traffic_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqTrafficValue') is not None:
            self.req_traffic_value = m.get('ReqTrafficValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainReqTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        req_traffic_data_per_interval: DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.req_traffic_data_per_interval = req_traffic_data_per_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.req_traffic_data_per_interval:
            self.req_traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.req_traffic_data_per_interval is not None:
            result['ReqTrafficDataPerInterval'] = self.req_traffic_data_per_interval.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReqTrafficDataPerInterval') is not None:
            temp_model = DescribeVsDomainReqTrafficDataResponseBodyReqTrafficDataPerInterval()
            self.req_traffic_data_per_interval = temp_model.from_map(m['ReqTrafficDataPerInterval'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainReqTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainReqTrafficDataResponseBody = None,
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
            temp_model = DescribeVsDomainReqTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainSnapshotDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        snapshot_value: str = None,
        time_stamp: str = None,
    ):
        self.snapshot_value = snapshot_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_value is not None:
            result['SnapshotValue'] = self.snapshot_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotValue') is not None:
            self.snapshot_value = m.get('SnapshotValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainSnapshotDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_data_per_interval: DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval = None,
    ):
        self.request_id = request_id
        self.snapshot_data_per_interval = snapshot_data_per_interval

    def validate(self):
        if self.snapshot_data_per_interval:
            self.snapshot_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_data_per_interval is not None:
            result['SnapshotDataPerInterval'] = self.snapshot_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotDataPerInterval') is not None:
            temp_model = DescribeVsDomainSnapshotDataResponseBodySnapshotDataPerInterval()
            self.snapshot_data_per_interval = temp_model.from_map(m['SnapshotDataPerInterval'])
        return self


class DescribeVsDomainSnapshotDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainSnapshotDataResponseBody = None,
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
            temp_model = DescribeVsDomainSnapshotDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainTrafficDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.interval = interval
        self.isp_name_en = isp_name_en
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en
        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')
        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        traffic_value: str = None,
    ):
        self.time_stamp = time_stamp
        self.traffic_value = traffic_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        return self


class DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval(TeaModel):
    def __init__(
        self,
        data_module: List[DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k in m.get('DataModule'):
                temp_model = DescribeVsDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        return self


class DescribeVsDomainTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        traffic_data_per_interval: DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeVsDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m['TrafficDataPerInterval'])
        return self


class DescribeVsDomainTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainTrafficDataResponseBody = None,
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
            temp_model = DescribeVsDomainTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsDomainUvDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData(TeaModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeVsDomainUvDataResponseBodyUvDataInterval(TeaModel):
    def __init__(
        self,
        usage_data: List[DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k in m.get('UsageData'):
                temp_model = DescribeVsDomainUvDataResponseBodyUvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k))
        return self


class DescribeVsDomainUvDataResponseBody(TeaModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        uv_data_interval: DescribeVsDomainUvDataResponseBodyUvDataInterval = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.uv_data_interval = uv_data_interval

    def validate(self):
        if self.uv_data_interval:
            self.uv_data_interval.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uv_data_interval is not None:
            result['UvDataInterval'] = self.uv_data_interval.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UvDataInterval') is not None:
            temp_model = DescribeVsDomainUvDataResponseBodyUvDataInterval()
            self.uv_data_interval = temp_model.from_map(m['UvDataInterval'])
        return self


class DescribeVsDomainUvDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsDomainUvDataResponseBody = None,
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
            temp_model = DescribeVsDomainUvDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsPullStreamConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.source_url = source_url
        self.start_time = start_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DescribeVsPullStreamConfigResponseBodyLiveAppRecordList(TeaModel):
    def __init__(
        self,
        live_app_record: List[DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord] = None,
    ):
        self.live_app_record = live_app_record

    def validate(self):
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k in self.live_app_record:
                result['LiveAppRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_app_record = []
        if m.get('LiveAppRecord') is not None:
            for k in m.get('LiveAppRecord'):
                temp_model = DescribeVsPullStreamConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        return self


class DescribeVsPullStreamConfigResponseBody(TeaModel):
    def __init__(
        self,
        live_app_record_list: DescribeVsPullStreamConfigResponseBodyLiveAppRecordList = None,
        request_id: str = None,
    ):
        self.live_app_record_list = live_app_record_list
        self.request_id = request_id

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = DescribeVsPullStreamConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m['LiveAppRecordList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsPullStreamConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsPullStreamConfigResponseBody = None,
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
            temp_model = DescribeVsPullStreamConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.source_url = source_url
        self.start_time = start_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList(TeaModel):
    def __init__(
        self,
        live_app_record: List[DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord] = None,
    ):
        self.live_app_record = live_app_record

    def validate(self):
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k in self.live_app_record:
                result['LiveAppRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_app_record = []
        if m.get('LiveAppRecord') is not None:
            for k in m.get('LiveAppRecord'):
                temp_model = DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        return self


class DescribeVsPullStreamInfoConfigResponseBody(TeaModel):
    def __init__(
        self,
        live_app_record_list: DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList = None,
        request_id: str = None,
    ):
        self.live_app_record_list = live_app_record_list
        self.request_id = request_id

    def validate(self):
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAppRecordList') is not None:
            temp_model = DescribeVsPullStreamInfoConfigResponseBodyLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(m['LiveAppRecordList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsPullStreamInfoConfigResponseBody = None,
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
            temp_model = DescribeVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStorageTrafficUsageDataRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        split_by: str = None,
        start_time: str = None,
    ):
        self.bucket = bucket
        self.end_time = end_time
        self.interval = interval
        self.owner_id = owner_id
        self.split_by = split_by
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.split_by is not None:
            result['SplitBy'] = self.split_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        lan_bandwidth_in_data_value: float = None,
        lan_bandwidth_out_data_value: float = None,
        lan_traffic_in_data_value: int = None,
        lan_traffic_out_data_value: int = None,
        time_stamp: str = None,
        wan_bandwidth_in_data_value: float = None,
        wan_bandwidth_out_data_value: float = None,
        wan_traffic_in_data_value: int = None,
        wan_traffic_out_data_value: int = None,
    ):
        self.bucket = bucket
        self.lan_bandwidth_in_data_value = lan_bandwidth_in_data_value
        self.lan_bandwidth_out_data_value = lan_bandwidth_out_data_value
        self.lan_traffic_in_data_value = lan_traffic_in_data_value
        self.lan_traffic_out_data_value = lan_traffic_out_data_value
        self.time_stamp = time_stamp
        self.wan_bandwidth_in_data_value = wan_bandwidth_in_data_value
        self.wan_bandwidth_out_data_value = wan_bandwidth_out_data_value
        self.wan_traffic_in_data_value = wan_traffic_in_data_value
        self.wan_traffic_out_data_value = wan_traffic_out_data_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.lan_bandwidth_in_data_value is not None:
            result['LanBandwidthInDataValue'] = self.lan_bandwidth_in_data_value
        if self.lan_bandwidth_out_data_value is not None:
            result['LanBandwidthOutDataValue'] = self.lan_bandwidth_out_data_value
        if self.lan_traffic_in_data_value is not None:
            result['LanTrafficInDataValue'] = self.lan_traffic_in_data_value
        if self.lan_traffic_out_data_value is not None:
            result['LanTrafficOutDataValue'] = self.lan_traffic_out_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.wan_bandwidth_in_data_value is not None:
            result['WanBandwidthInDataValue'] = self.wan_bandwidth_in_data_value
        if self.wan_bandwidth_out_data_value is not None:
            result['WanBandwidthOutDataValue'] = self.wan_bandwidth_out_data_value
        if self.wan_traffic_in_data_value is not None:
            result['WanTrafficInDataValue'] = self.wan_traffic_in_data_value
        if self.wan_traffic_out_data_value is not None:
            result['WanTrafficOutDataValue'] = self.wan_traffic_out_data_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('LanBandwidthInDataValue') is not None:
            self.lan_bandwidth_in_data_value = m.get('LanBandwidthInDataValue')
        if m.get('LanBandwidthOutDataValue') is not None:
            self.lan_bandwidth_out_data_value = m.get('LanBandwidthOutDataValue')
        if m.get('LanTrafficInDataValue') is not None:
            self.lan_traffic_in_data_value = m.get('LanTrafficInDataValue')
        if m.get('LanTrafficOutDataValue') is not None:
            self.lan_traffic_out_data_value = m.get('LanTrafficOutDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('WanBandwidthInDataValue') is not None:
            self.wan_bandwidth_in_data_value = m.get('WanBandwidthInDataValue')
        if m.get('WanBandwidthOutDataValue') is not None:
            self.wan_bandwidth_out_data_value = m.get('WanBandwidthOutDataValue')
        if m.get('WanTrafficInDataValue') is not None:
            self.wan_traffic_in_data_value = m.get('WanTrafficInDataValue')
        if m.get('WanTrafficOutDataValue') is not None:
            self.wan_traffic_out_data_value = m.get('WanTrafficOutDataValue')
        return self


class DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage(TeaModel):
    def __init__(
        self,
        traffic_usage_data_module: List[DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule] = None,
    ):
        self.traffic_usage_data_module = traffic_usage_data_module

    def validate(self):
        if self.traffic_usage_data_module:
            for k in self.traffic_usage_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficUsageDataModule'] = []
        if self.traffic_usage_data_module is not None:
            for k in self.traffic_usage_data_module:
                result['TrafficUsageDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_usage_data_module = []
        if m.get('TrafficUsageDataModule') is not None:
            for k in m.get('TrafficUsageDataModule'):
                temp_model = DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsageTrafficUsageDataModule()
                self.traffic_usage_data_module.append(temp_model.from_map(k))
        return self


class DescribeVsStorageTrafficUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_usage: DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage = None,
    ):
        self.request_id = request_id
        self.traffic_usage = traffic_usage

    def validate(self):
        if self.traffic_usage:
            self.traffic_usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_usage is not None:
            result['TrafficUsage'] = self.traffic_usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficUsage') is not None:
            temp_model = DescribeVsStorageTrafficUsageDataResponseBodyTrafficUsage()
            self.traffic_usage = temp_model.from_map(m['TrafficUsage'])
        return self


class DescribeVsStorageTrafficUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsStorageTrafficUsageDataResponseBody = None,
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
            temp_model = DescribeVsStorageTrafficUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStorageUsageDataRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        split_by: str = None,
        start_time: str = None,
    ):
        self.bucket = bucket
        self.end_time = end_time
        self.interval = interval
        self.owner_id = owner_id
        self.split_by = split_by
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.split_by is not None:
            result['SplitBy'] = self.split_by
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        storage_data_value: int = None,
        time_stamp: str = None,
    ):
        self.bucket = bucket
        self.storage_data_value = storage_data_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.storage_data_value is not None:
            result['StorageDataValue'] = self.storage_data_value
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('StorageDataValue') is not None:
            self.storage_data_value = m.get('StorageDataValue')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeVsStorageUsageDataResponseBodyStorageUsage(TeaModel):
    def __init__(
        self,
        storage_usage_data_module: List[DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule] = None,
    ):
        self.storage_usage_data_module = storage_usage_data_module

    def validate(self):
        if self.storage_usage_data_module:
            for k in self.storage_usage_data_module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StorageUsageDataModule'] = []
        if self.storage_usage_data_module is not None:
            for k in self.storage_usage_data_module:
                result['StorageUsageDataModule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_usage_data_module = []
        if m.get('StorageUsageDataModule') is not None:
            for k in m.get('StorageUsageDataModule'):
                temp_model = DescribeVsStorageUsageDataResponseBodyStorageUsageStorageUsageDataModule()
                self.storage_usage_data_module.append(temp_model.from_map(k))
        return self


class DescribeVsStorageUsageDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        storage_usage: DescribeVsStorageUsageDataResponseBodyStorageUsage = None,
    ):
        self.request_id = request_id
        self.storage_usage = storage_usage

    def validate(self):
        if self.storage_usage:
            self.storage_usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageUsage') is not None:
            temp_model = DescribeVsStorageUsageDataResponseBodyStorageUsage()
            self.storage_usage = temp_model.from_map(m['StorageUsage'])
        return self


class DescribeVsStorageUsageDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsStorageUsageDataResponseBody = None,
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
            temp_model = DescribeVsStorageUsageDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
    ):
        self.domain_name = domain_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_type: str = None,
        domain_name: str = None,
        notify_url: str = None,
    ):
        self.auth_key = auth_key
        self.auth_type = auth_type
        self.domain_name = domain_name
        self.notify_url = notify_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        return self


class DescribeVsStreamsNotifyUrlConfigResponseBody(TeaModel):
    def __init__(
        self,
        live_streams_notify_config: DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig = None,
        request_id: str = None,
    ):
        self.live_streams_notify_config = live_streams_notify_config
        self.request_id = request_id

    def validate(self):
        if self.live_streams_notify_config:
            self.live_streams_notify_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_streams_notify_config is not None:
            result['LiveStreamsNotifyConfig'] = self.live_streams_notify_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamsNotifyConfig') is not None:
            temp_model = DescribeVsStreamsNotifyUrlConfigResponseBodyLiveStreamsNotifyConfig()
            self.live_streams_notify_config = temp_model.from_map(m['LiveStreamsNotifyConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsStreamsNotifyUrlConfigResponseBody = None,
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
            temp_model = DescribeVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsOnlineListRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        order_by: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        start_time: str = None,
        stream_name: str = None,
        stream_type: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.order_by = order_by
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.query_type = query_type
        self.start_time = start_time
        self.stream_name = stream_name
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        publish_domain: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publish_url: str = None,
        stream_name: str = None,
        transcode_id: str = None,
        transcoded: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.publish_domain = publish_domain
        self.publish_time = publish_time
        self.publish_type = publish_type
        self.publish_url = publish_url
        self.stream_name = stream_name
        self.transcode_id = transcode_id
        self.transcoded = transcoded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
        return self


class DescribeVsStreamsOnlineListResponseBodyOnlineInfo(TeaModel):
    def __init__(
        self,
        live_stream_online_info: List[DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo] = None,
    ):
        self.live_stream_online_info = live_stream_online_info

    def validate(self):
        if self.live_stream_online_info:
            for k in self.live_stream_online_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamOnlineInfo'] = []
        if self.live_stream_online_info is not None:
            for k in self.live_stream_online_info:
                result['LiveStreamOnlineInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_online_info = []
        if m.get('LiveStreamOnlineInfo') is not None:
            for k in m.get('LiveStreamOnlineInfo'):
                temp_model = DescribeVsStreamsOnlineListResponseBodyOnlineInfoLiveStreamOnlineInfo()
                self.live_stream_online_info.append(temp_model.from_map(k))
        return self


class DescribeVsStreamsOnlineListResponseBody(TeaModel):
    def __init__(
        self,
        online_info: DescribeVsStreamsOnlineListResponseBodyOnlineInfo = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.online_info = online_info
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.online_info:
            self.online_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_info is not None:
            result['OnlineInfo'] = self.online_info.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineInfo') is not None:
            temp_model = DescribeVsStreamsOnlineListResponseBodyOnlineInfo()
            self.online_info = temp_model.from_map(m['OnlineInfo'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeVsStreamsOnlineListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsStreamsOnlineListResponseBody = None,
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
            temp_model = DescribeVsStreamsOnlineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsStreamsPublishListRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        order_by: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        start_time: str = None,
        stream_name: str = None,
        stream_type: str = None,
    ):
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.order_by = order_by
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.query_type = query_type
        self.start_time = start_time
        self.stream_name = stream_name
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        client_addr: str = None,
        domain_name: str = None,
        edge_node_addr: str = None,
        publish_domain: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publish_url: str = None,
        stop_time: str = None,
        stream_name: str = None,
        stream_url: str = None,
        transcode_id: str = None,
        transcoded: str = None,
    ):
        self.app_name = app_name
        self.client_addr = client_addr
        self.domain_name = domain_name
        self.edge_node_addr = edge_node_addr
        self.publish_domain = publish_domain
        self.publish_time = publish_time
        self.publish_type = publish_type
        self.publish_url = publish_url
        self.stop_time = stop_time
        self.stream_name = stream_name
        self.stream_url = stream_url
        self.transcode_id = transcode_id
        self.transcoded = transcoded

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.edge_node_addr is not None:
            result['EdgeNodeAddr'] = self.edge_node_addr
        if self.publish_domain is not None:
            result['PublishDomain'] = self.publish_domain
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url
        if self.transcode_id is not None:
            result['TranscodeId'] = self.transcode_id
        if self.transcoded is not None:
            result['Transcoded'] = self.transcoded
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EdgeNodeAddr') is not None:
            self.edge_node_addr = m.get('EdgeNodeAddr')
        if m.get('PublishDomain') is not None:
            self.publish_domain = m.get('PublishDomain')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')
        if m.get('TranscodeId') is not None:
            self.transcode_id = m.get('TranscodeId')
        if m.get('Transcoded') is not None:
            self.transcoded = m.get('Transcoded')
        return self


class DescribeVsStreamsPublishListResponseBodyPublishInfo(TeaModel):
    def __init__(
        self,
        live_stream_publish_info: List[DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo] = None,
    ):
        self.live_stream_publish_info = live_stream_publish_info

    def validate(self):
        if self.live_stream_publish_info:
            for k in self.live_stream_publish_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveStreamPublishInfo'] = []
        if self.live_stream_publish_info is not None:
            for k in self.live_stream_publish_info:
                result['LiveStreamPublishInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_publish_info = []
        if m.get('LiveStreamPublishInfo') is not None:
            for k in m.get('LiveStreamPublishInfo'):
                temp_model = DescribeVsStreamsPublishListResponseBodyPublishInfoLiveStreamPublishInfo()
                self.live_stream_publish_info.append(temp_model.from_map(k))
        return self


class DescribeVsStreamsPublishListResponseBody(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        publish_info: DescribeVsStreamsPublishListResponseBodyPublishInfo = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.publish_info = publish_info
        self.request_id = request_id
        self.total_num = total_num
        self.total_page = total_page

    def validate(self):
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublishInfo') is not None:
            temp_model = DescribeVsStreamsPublishListResponseBodyPublishInfo()
            self.publish_info = temp_model.from_map(m['PublishInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class DescribeVsStreamsPublishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsStreamsPublishListResponseBody = None,
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
            temp_model = DescribeVsStreamsPublishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsTopDomainsByFlowRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.limit = limit
        self.owner_id = owner_id
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
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        max_bps: int = None,
        max_bps_time: str = None,
        rank: int = None,
        total_access: int = None,
        total_traffic: str = None,
        traffic_percent: str = None,
    ):
        self.domain_name = domain_name
        self.max_bps = max_bps
        self.max_bps_time = max_bps_time
        self.rank = rank
        self.total_access = total_access
        self.total_traffic = total_traffic
        self.traffic_percent = traffic_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps
        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.total_access is not None:
            result['TotalAccess'] = self.total_access
        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic
        if self.traffic_percent is not None:
            result['TrafficPercent'] = self.traffic_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')
        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')
        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')
        if m.get('TrafficPercent') is not None:
            self.traffic_percent = m.get('TrafficPercent')
        return self


class DescribeVsTopDomainsByFlowResponseBodyTopDomains(TeaModel):
    def __init__(
        self,
        top_domain: List[DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain] = None,
    ):
        self.top_domain = top_domain

    def validate(self):
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.top_domain = []
        if m.get('TopDomain') is not None:
            for k in m.get('TopDomain'):
                temp_model = DescribeVsTopDomainsByFlowResponseBodyTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        return self


class DescribeVsTopDomainsByFlowResponseBody(TeaModel):
    def __init__(
        self,
        domain_count: int = None,
        domain_online_count: int = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        top_domains: DescribeVsTopDomainsByFlowResponseBodyTopDomains = None,
    ):
        self.domain_count = domain_count
        self.domain_online_count = domain_online_count
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
        self.top_domains = top_domains

    def validate(self):
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count
        if self.domain_online_count is not None:
            result['DomainOnlineCount'] = self.domain_online_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')
        if m.get('DomainOnlineCount') is not None:
            self.domain_online_count = m.get('DomainOnlineCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TopDomains') is not None:
            temp_model = DescribeVsTopDomainsByFlowResponseBodyTopDomains()
            self.top_domains = temp_model.from_map(m['TopDomains'])
        return self


class DescribeVsTopDomainsByFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsTopDomainsByFlowResponseBody = None,
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
            temp_model = DescribeVsTopDomainsByFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsUpPeakPublishStreamDataRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_switch: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.domain_name = domain_name
        self.domain_switch = domain_switch
        self.end_time = end_time
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_switch is not None:
            result['DomainSwitch'] = self.domain_switch
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainSwitch') is not None:
            self.domain_switch = m.get('DomainSwitch')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData(TeaModel):
    def __init__(
        self,
        band_width: str = None,
        peak_time: str = None,
        publish_stream_num: int = None,
        query_time: str = None,
        stat_name: str = None,
    ):
        self.band_width = band_width
        self.peak_time = peak_time
        self.publish_stream_num = publish_stream_num
        self.query_time = query_time
        self.stat_name = stat_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time
        if self.publish_stream_num is not None:
            result['PublishStreamNum'] = self.publish_stream_num
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        if self.stat_name is not None:
            result['StatName'] = self.stat_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')
        if m.get('PublishStreamNum') is not None:
            self.publish_stream_num = m.get('PublishStreamNum')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')
        return self


class DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas(TeaModel):
    def __init__(
        self,
        describe_vs_up_peak_publish_stream_data: List[DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData] = None,
    ):
        self.describe_vs_up_peak_publish_stream_data = describe_vs_up_peak_publish_stream_data

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_data:
            for k in self.describe_vs_up_peak_publish_stream_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DescribeVsUpPeakPublishStreamData'] = []
        if self.describe_vs_up_peak_publish_stream_data is not None:
            for k in self.describe_vs_up_peak_publish_stream_data:
                result['DescribeVsUpPeakPublishStreamData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_vs_up_peak_publish_stream_data = []
        if m.get('DescribeVsUpPeakPublishStreamData') is not None:
            for k in m.get('DescribeVsUpPeakPublishStreamData'):
                temp_model = DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatasDescribeVsUpPeakPublishStreamData()
                self.describe_vs_up_peak_publish_stream_data.append(temp_model.from_map(k))
        return self


class DescribeVsUpPeakPublishStreamDataResponseBody(TeaModel):
    def __init__(
        self,
        describe_vs_up_peak_publish_stream_datas: DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas = None,
        request_id: str = None,
    ):
        self.describe_vs_up_peak_publish_stream_datas = describe_vs_up_peak_publish_stream_datas
        self.request_id = request_id

    def validate(self):
        if self.describe_vs_up_peak_publish_stream_datas:
            self.describe_vs_up_peak_publish_stream_datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.describe_vs_up_peak_publish_stream_datas is not None:
            result['DescribeVsUpPeakPublishStreamDatas'] = self.describe_vs_up_peak_publish_stream_datas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeVsUpPeakPublishStreamDatas') is not None:
            temp_model = DescribeVsUpPeakPublishStreamDataResponseBodyDescribeVsUpPeakPublishStreamDatas()
            self.describe_vs_up_peak_publish_stream_datas = temp_model.from_map(m['DescribeVsUpPeakPublishStreamDatas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVsUpPeakPublishStreamDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsUpPeakPublishStreamDataResponseBody = None,
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
            temp_model = DescribeVsUpPeakPublishStreamDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVsUserResourcePackageRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        curr_capacity: str = None,
        display_name: str = None,
        init_capacity: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.commodity_code = commodity_code
        self.curr_capacity = curr_capacity
        self.display_name = display_name
        self.init_capacity = init_capacity
        self.instance_id = instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVsUserResourcePackageResponseBodyResourcePackageInfos(TeaModel):
    def __init__(
        self,
        resource_package_info: List[DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
    ):
        self.resource_package_info = resource_package_info

    def validate(self):
        if self.resource_package_info:
            for k in self.resource_package_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k in self.resource_package_info:
                result['ResourcePackageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k in m.get('ResourcePackageInfo'):
                temp_model = DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k))
        return self


class DescribeVsUserResourcePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: DescribeVsUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
        self.request_id = request_id
        self.resource_package_infos = resource_package_infos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourcePackageInfos') is not None:
            temp_model = DescribeVsUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m['ResourcePackageInfos'])
        return self


class DescribeVsUserResourcePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVsUserResourcePackageResponseBody = None,
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
            temp_model = DescribeVsUserResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForbidVsStreamRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        oneshot: str = None,
        owner_id: int = None,
        resume_time: str = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.control_stream_action = control_stream_action
        self.domain_name = domain_name
        self.live_stream_type = live_stream_type
        self.oneshot = oneshot
        self.owner_id = owner_id
        self.resume_time = resume_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.oneshot is not None:
            result['Oneshot'] = self.oneshot
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resume_time is not None:
            result['ResumeTime'] = self.resume_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('Oneshot') is not None:
            self.oneshot = m.get('Oneshot')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResumeTime') is not None:
            self.resume_time = m.get('ResumeTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class ForbidVsStreamResponseBody(TeaModel):
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


class ForbidVsStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ForbidVsStreamResponseBody = None,
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
            temp_model = ForbidVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBucketInfoRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        owner_id: int = None,
    ):
        self.bucket_name = bucket_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetBucketInfoResponseBodyBucketInfo(TeaModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        create_time: str = None,
        data_redundancy_type: str = None,
        dispatcher_type: str = None,
        endpoint: str = None,
        modify_time: str = None,
        resource_type: str = None,
        storage_class: str = None,
    ):
        self.bucket_acl = bucket_acl
        self.bucket_name = bucket_name
        self.comment = comment
        self.create_time = create_time
        self.data_redundancy_type = data_redundancy_type
        self.dispatcher_type = dispatcher_type
        self.endpoint = endpoint
        self.modify_time = modify_time
        self.resource_type = resource_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class GetBucketInfoResponseBody(TeaModel):
    def __init__(
        self,
        bucket_info: GetBucketInfoResponseBodyBucketInfo = None,
        request_id: str = None,
    ):
        self.bucket_info = bucket_info
        self.request_id = request_id

    def validate(self):
        if self.bucket_info:
            self.bucket_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_info is not None:
            result['BucketInfo'] = self.bucket_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketInfo') is not None:
            temp_model = GetBucketInfoResponseBodyBucketInfo()
            self.bucket_info = temp_model.from_map(m['BucketInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBucketInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBucketInfoResponseBody = None,
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
            temp_model = GetBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetObjectTotalRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        owner_id: int = None,
    ):
        self.bucket_name = bucket_name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetObjectTotalResponseBody(TeaModel):
    def __init__(
        self,
        object_count: int = None,
        request_id: str = None,
    ):
        self.object_count = object_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_count is not None:
            result['ObjectCount'] = self.object_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetObjectTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetObjectTotalResponseBody = None,
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
            temp_model = GetObjectTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GotoPresetRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        preset_id: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.preset_id = preset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        return self


class GotoPresetResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GotoPresetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GotoPresetResponseBody = None,
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
            temp_model = GotoPresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBucketsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        marker: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        prefix: str = None,
    ):
        self.keyword = keyword
        self.marker = marker
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        return self


class ListBucketsResponseBodyBucketInfos(TeaModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        create_time: str = None,
        data_redundancy_type: str = None,
        dispatcher_type: str = None,
        endpoint: str = None,
        modify_time: str = None,
        resource_type: str = None,
        storage_class: str = None,
    ):
        self.bucket_acl = bucket_acl
        self.bucket_name = bucket_name
        self.comment = comment
        self.create_time = create_time
        self.data_redundancy_type = data_redundancy_type
        self.dispatcher_type = dispatcher_type
        self.endpoint = endpoint
        self.modify_time = modify_time
        self.resource_type = resource_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ListBucketsResponseBody(TeaModel):
    def __init__(
        self,
        bucket_infos: List[ListBucketsResponseBodyBucketInfos] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bucket_infos = bucket_infos
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bucket_infos:
            for k in self.bucket_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BucketInfos'] = []
        if self.bucket_infos is not None:
            for k in self.bucket_infos:
                result['BucketInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bucket_infos = []
        if m.get('BucketInfos') is not None:
            for k in m.get('BucketInfos'):
                temp_model = ListBucketsResponseBodyBucketInfos()
                self.bucket_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBucketsResponseBody = None,
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
            temp_model = ListBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceChannelsRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceChannelsResponseBodyChannels(TeaModel):
    def __init__(
        self,
        channel_id: int = None,
        device_id: str = None,
        device_status: str = None,
        name: str = None,
        params: str = None,
    ):
        self.channel_id = channel_id
        self.device_id = device_id
        self.device_status = device_status
        self.name = name
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class ListDeviceChannelsResponseBody(TeaModel):
    def __init__(
        self,
        channels: List[ListDeviceChannelsResponseBodyChannels] = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.channels = channels
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['Channels'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('Channels') is not None:
            for k in m.get('Channels'):
                temp_model = ListDeviceChannelsResponseBodyChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeviceChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceChannelsResponseBody = None,
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
            temp_model = ListDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceRecordsRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        search_criteria: str = None,
        stream_id: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.search_criteria = search_criteria
        self.stream_id = stream_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        return self


class ListDeviceRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        file_size: int = None,
        filename: str = None,
        record_type: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.file_size = file_size
        self.filename = filename
        self.record_type = record_type
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
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDeviceRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        records: List[ListDeviceRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListDeviceRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeviceRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceRecordsResponseBody = None,
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
            temp_model = ListDeviceRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectsRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        continuation_token: str = None,
        delimiter: str = None,
        encoding_type: str = None,
        marker: str = None,
        max_keys: int = None,
        owner_id: int = None,
        prefix: str = None,
        start_after: str = None,
    ):
        self.bucket_name = bucket_name
        self.continuation_token = continuation_token
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.marker = marker
        self.max_keys = max_keys
        self.owner_id = owner_id
        self.prefix = prefix
        self.start_after = start_after

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.start_after is not None:
            result['StartAfter'] = self.start_after
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('StartAfter') is not None:
            self.start_after = m.get('StartAfter')
        return self


class ListObjectsResponseBodyContents(TeaModel):
    def __init__(
        self,
        etag: str = None,
        key: str = None,
        last_modified: str = None,
        size: int = None,
        storage_class: str = None,
    ):
        self.etag = etag
        self.key = key
        self.last_modified = last_modified
        self.size = size
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.key is not None:
            result['Key'] = self.key
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.size is not None:
            result['Size'] = self.size
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class ListObjectsResponseBody(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        common_prefixes: List[str] = None,
        contents: List[ListObjectsResponseBodyContents] = None,
        continuation_token: str = None,
        delimiter: str = None,
        encoding_type: str = None,
        is_truncated: bool = None,
        key_count: int = None,
        marker: str = None,
        max_keys: int = None,
        next_continuation_token: str = None,
        next_marker: str = None,
        prefix: str = None,
        request_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.common_prefixes = common_prefixes
        self.contents = contents
        self.continuation_token = continuation_token
        self.delimiter = delimiter
        self.encoding_type = encoding_type
        self.is_truncated = is_truncated
        self.key_count = key_count
        self.marker = marker
        self.max_keys = max_keys
        self.next_continuation_token = next_continuation_token
        self.next_marker = next_marker
        self.prefix = prefix
        self.request_id = request_id

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.common_prefixes is not None:
            result['CommonPrefixes'] = self.common_prefixes
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.continuation_token is not None:
            result['ContinuationToken'] = self.continuation_token
        if self.delimiter is not None:
            result['Delimiter'] = self.delimiter
        if self.encoding_type is not None:
            result['EncodingType'] = self.encoding_type
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.key_count is not None:
            result['KeyCount'] = self.key_count
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.next_continuation_token is not None:
            result['NextContinuationToken'] = self.next_continuation_token
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CommonPrefixes') is not None:
            self.common_prefixes = m.get('CommonPrefixes')
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = ListObjectsResponseBodyContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('ContinuationToken') is not None:
            self.continuation_token = m.get('ContinuationToken')
        if m.get('Delimiter') is not None:
            self.delimiter = m.get('Delimiter')
        if m.get('EncodingType') is not None:
            self.encoding_type = m.get('EncodingType')
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('KeyCount') is not None:
            self.key_count = m.get('KeyCount')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('NextContinuationToken') is not None:
            self.next_continuation_token = m.get('NextContinuationToken')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListObjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListObjectsResponseBody = None,
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
            temp_model = ListObjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceRequest(TeaModel):
    def __init__(
        self,
        alarm_method: str = None,
        auto_pos: bool = None,
        auto_start: bool = None,
        description: str = None,
        directory_id: str = None,
        gb_id: str = None,
        group_id: str = None,
        id: str = None,
        ip: str = None,
        latitude: str = None,
        longitude: str = None,
        name: str = None,
        owner_id: int = None,
        params: str = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        pos_interval: int = None,
        type: str = None,
        url: str = None,
        username: str = None,
        vendor: str = None,
    ):
        self.alarm_method = alarm_method
        self.auto_pos = auto_pos
        self.auto_start = auto_start
        self.description = description
        self.directory_id = directory_id
        self.gb_id = gb_id
        self.group_id = group_id
        self.id = id
        self.ip = ip
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.owner_id = owner_id
        self.params = params
        self.parent_id = parent_id
        self.password = password
        self.port = port
        self.pos_interval = pos_interval
        self.type = type
        self.url = url
        self.username = username
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_method is not None:
            result['AlarmMethod'] = self.alarm_method
        if self.auto_pos is not None:
            result['AutoPos'] = self.auto_pos
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.description is not None:
            result['Description'] = self.description
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.params is not None:
            result['Params'] = self.params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.pos_interval is not None:
            result['PosInterval'] = self.pos_interval
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMethod') is not None:
            self.alarm_method = m.get('AlarmMethod')
        if m.get('AutoPos') is not None:
            self.auto_pos = m.get('AutoPos')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PosInterval') is not None:
            self.pos_interval = m.get('PosInterval')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ModifyDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeviceResponseBody = None,
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
            temp_model = ModifyDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        channel_id: int = None,
        id: str = None,
        owner_id: int = None,
        status: int = None,
    ):
        self.alarm_id = alarm_id
        self.channel_id = channel_id
        self.id = id
        self.owner_id = owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyDeviceAlarmResponseBody(TeaModel):
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


class ModifyDeviceAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeviceAlarmResponseBody = None,
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
            temp_model = ModifyDeviceAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceCaptureRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        image: int = None,
        owner_id: int = None,
        video: int = None,
    ):
        self.id = id
        self.image = image
        self.owner_id = owner_id
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class ModifyDeviceCaptureResponseBody(TeaModel):
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


class ModifyDeviceCaptureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeviceCaptureResponseBody = None,
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
            temp_model = ModifyDeviceCaptureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDeviceChannelsRequest(TeaModel):
    def __init__(
        self,
        channels: str = None,
        device_status: str = None,
        dsn: str = None,
        id: str = None,
        owner_id: int = None,
    ):
        self.channels = channels
        self.device_status = device_status
        self.dsn = dsn
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status
        if self.dsn is not None:
            result['Dsn'] = self.dsn
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')
        if m.get('Dsn') is not None:
            self.dsn = m.get('Dsn')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyDeviceChannelsResponseBody(TeaModel):
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


class ModifyDeviceChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDeviceChannelsResponseBody = None,
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
            temp_model = ModifyDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDirectoryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDirectoryResponseBody = None,
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
            temp_model = ModifyDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGroupRequest(TeaModel):
    def __init__(
        self,
        callback: str = None,
        description: str = None,
        enabled: bool = None,
        id: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
    ):
        self.callback = callback
        self.description = description
        self.enabled = enabled
        self.id = id
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        self.name = name
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.id is not None:
            result['Id'] = self.id
        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol
        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull
        if self.name is not None:
            result['Name'] = self.name
        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')
        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class ModifyGroupResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGroupResponseBody = None,
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
            temp_model = ModifyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParentPlatformRequest(TeaModel):
    def __init__(
        self,
        auto_start: bool = None,
        client_auth: bool = None,
        client_password: str = None,
        client_username: str = None,
        description: str = None,
        gb_id: str = None,
        id: str = None,
        ip: str = None,
        name: str = None,
        owner_id: int = None,
        port: int = None,
    ):
        self.auto_start = auto_start
        self.client_auth = client_auth
        self.client_password = client_password
        self.client_username = client_username
        self.description = description
        self.gb_id = gb_id
        self.id = id
        self.ip = ip
        self.name = name
        self.owner_id = owner_id
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.client_auth is not None:
            result['ClientAuth'] = self.client_auth
        if self.client_password is not None:
            result['ClientPassword'] = self.client_password
        if self.client_username is not None:
            result['ClientUsername'] = self.client_username
        if self.description is not None:
            result['Description'] = self.description
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('ClientAuth') is not None:
            self.client_auth = m.get('ClientAuth')
        if m.get('ClientPassword') is not None:
            self.client_password = m.get('ClientPassword')
        if m.get('ClientUsername') is not None:
            self.client_username = m.get('ClientUsername')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyParentPlatformResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyParentPlatformResponseBody = None,
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
            temp_model = ModifyParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPurchasedDeviceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        name: str = None,
        order_id: str = None,
        owner_id: int = None,
        register_code: str = None,
        sub_type: str = None,
        vendor: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.order_id = order_id
        self.owner_id = owner_id
        self.register_code = register_code
        self.sub_type = sub_type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ModifyPurchasedDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPurchasedDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPurchasedDeviceResponseBody = None,
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
            temp_model = ModifyPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateRequest(TeaModel):
    def __init__(
        self,
        callback: str = None,
        description: str = None,
        file_format: str = None,
        flv: str = None,
        hls_m3u_8: str = None,
        hls_ts: str = None,
        id: str = None,
        interval: int = None,
        jpg_on_demand: str = None,
        jpg_overwrite: str = None,
        jpg_sequence: str = None,
        mp_4: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        owner_id: int = None,
        region: str = None,
        retention: int = None,
        trans_configs_json: str = None,
        trigger: str = None,
    ):
        self.callback = callback
        self.description = description
        self.file_format = file_format
        self.flv = flv
        self.hls_m3u_8 = hls_m3u_8
        self.hls_ts = hls_ts
        self.id = id
        self.interval = interval
        self.jpg_on_demand = jpg_on_demand
        self.jpg_overwrite = jpg_overwrite
        self.jpg_sequence = jpg_sequence
        self.mp_4 = mp_4
        self.name = name
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_file_prefix = oss_file_prefix
        self.owner_id = owner_id
        self.region = region
        self.retention = retention
        self.trans_configs_json = trans_configs_json
        self.trigger = trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.file_format is not None:
            result['FileFormat'] = self.file_format
        if self.flv is not None:
            result['Flv'] = self.flv
        if self.hls_m3u_8 is not None:
            result['HlsM3u8'] = self.hls_m3u_8
        if self.hls_ts is not None:
            result['HlsTs'] = self.hls_ts
        if self.id is not None:
            result['Id'] = self.id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.jpg_on_demand is not None:
            result['JpgOnDemand'] = self.jpg_on_demand
        if self.jpg_overwrite is not None:
            result['JpgOverwrite'] = self.jpg_overwrite
        if self.jpg_sequence is not None:
            result['JpgSequence'] = self.jpg_sequence
        if self.mp_4 is not None:
            result['Mp4'] = self.mp_4
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.retention is not None:
            result['Retention'] = self.retention
        if self.trans_configs_json is not None:
            result['TransConfigsJSON'] = self.trans_configs_json
        if self.trigger is not None:
            result['Trigger'] = self.trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')
        if m.get('Flv') is not None:
            self.flv = m.get('Flv')
        if m.get('HlsM3u8') is not None:
            self.hls_m3u_8 = m.get('HlsM3u8')
        if m.get('HlsTs') is not None:
            self.hls_ts = m.get('HlsTs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('JpgOnDemand') is not None:
            self.jpg_on_demand = m.get('JpgOnDemand')
        if m.get('JpgOverwrite') is not None:
            self.jpg_overwrite = m.get('JpgOverwrite')
        if m.get('JpgSequence') is not None:
            self.jpg_sequence = m.get('JpgSequence')
        if m.get('Mp4') is not None:
            self.mp_4 = m.get('Mp4')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Retention') is not None:
            self.retention = m.get('Retention')
        if m.get('TransConfigsJSON') is not None:
            self.trans_configs_json = m.get('TransConfigsJSON')
        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')
        return self


class ModifyTemplateResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTemplateResponseBody = None,
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
            temp_model = ModifyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenVsServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenVsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenVsServiceResponseBody = None,
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
            temp_model = OpenVsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateRenderingDevicesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        operation: str = None,
        owner_id: int = None,
        pod_id: str = None,
    ):
        self.instance_ids = instance_ids
        self.operation = operation
        self.owner_id = owner_id
        self.pod_id = pod_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class OperateRenderingDevicesResponseBody(TeaModel):
    def __init__(
        self,
        failed_ids: List[str] = None,
        request_id: str = None,
    ):
        self.failed_ids = failed_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateRenderingDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperateRenderingDevicesResponseBody = None,
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
            temp_model = OperateRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PrepareUploadRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        client_ip: str = None,
        owner_id: int = None,
    ):
        self.bucket_name = bucket_name
        self.client_ip = client_ip
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class PrepareUploadResponseBody(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        request_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PrepareUploadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PrepareUploadResponseBody = None,
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
            temp_model = PrepareUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutBucketRequest(TeaModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        data_redundancy_type: str = None,
        dispatcher_type: str = None,
        endpoint: str = None,
        owner_id: int = None,
        resource_type: str = None,
        storage_class: str = None,
    ):
        self.bucket_acl = bucket_acl
        self.bucket_name = bucket_name
        self.comment = comment
        self.data_redundancy_type = data_redundancy_type
        self.dispatcher_type = dispatcher_type
        self.endpoint = endpoint
        self.owner_id = owner_id
        self.resource_type = resource_type
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.dispatcher_type is not None:
            result['DispatcherType'] = self.dispatcher_type
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('DispatcherType') is not None:
            self.dispatcher_type = m.get('DispatcherType')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        return self


class PutBucketResponseBody(TeaModel):
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


class PutBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutBucketResponseBody = None,
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
            temp_model = PutBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetRenderingDevicesRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_ids: str = None,
        owner_id: int = None,
        pod_id: str = None,
    ):
        self.image_id = image_id
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.pod_id = pod_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pod_id is not None:
            result['PodId'] = self.pod_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')
        return self


class ResetRenderingDevicesResponseBody(TeaModel):
    def __init__(
        self,
        failed_ids: List[str] = None,
        request_id: str = None,
    ):
        self.failed_ids = failed_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_ids is not None:
            result['FailedIds'] = self.failed_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedIds') is not None:
            self.failed_ids = m.get('FailedIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetRenderingDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetRenderingDevicesResponseBody = None,
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
            temp_model = ResetRenderingDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeVsStreamRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        control_stream_action: str = None,
        domain_name: str = None,
        live_stream_type: str = None,
        owner_id: int = None,
        stream_name: str = None,
    ):
        self.app_name = app_name
        self.control_stream_action = control_stream_action
        self.domain_name = domain_name
        self.live_stream_type = live_stream_type
        self.owner_id = owner_id
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.control_stream_action is not None:
            result['ControlStreamAction'] = self.control_stream_action
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.live_stream_type is not None:
            result['LiveStreamType'] = self.live_stream_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ControlStreamAction') is not None:
            self.control_stream_action = m.get('ControlStreamAction')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('LiveStreamType') is not None:
            self.live_stream_type = m.get('LiveStreamType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class ResumeVsStreamResponseBody(TeaModel):
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


class ResumeVsStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeVsStreamResponseBody = None,
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
            temp_model = ResumeVsStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPresetRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        preset_id: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.preset_id = preset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.preset_id is not None:
            result['PresetId'] = self.preset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')
        return self


class SetPresetResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetPresetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetPresetResponseBody = None,
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
            temp_model = SetPresetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVsDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_type: str = None,
        domain_name: str = None,
        force_set: str = None,
        owner_id: int = None,
        region: str = None,
        sslpri: str = None,
        sslprotocol: str = None,
        sslpub: str = None,
    ):
        self.cert_name = cert_name
        self.cert_type = cert_type
        self.domain_name = domain_name
        self.force_set = force_set
        self.owner_id = owner_id
        self.region = region
        self.sslpri = sslpri
        self.sslprotocol = sslprotocol
        self.sslpub = sslpub

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.force_set is not None:
            result['ForceSet'] = self.force_set
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        if self.sslpri is not None:
            result['SSLPri'] = self.sslpri
        if self.sslprotocol is not None:
            result['SSLProtocol'] = self.sslprotocol
        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ForceSet') is not None:
            self.force_set = m.get('ForceSet')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SSLPri') is not None:
            self.sslpri = m.get('SSLPri')
        if m.get('SSLProtocol') is not None:
            self.sslprotocol = m.get('SSLProtocol')
        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')
        return self


class SetVsDomainCertificateResponseBody(TeaModel):
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


class SetVsDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetVsDomainCertificateResponseBody = None,
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
            temp_model = SetVsDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVsStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_type: str = None,
        domain_name: str = None,
        notify_url: str = None,
        owner_id: int = None,
    ):
        self.auth_key = auth_key
        self.auth_type = auth_type
        self.domain_name = domain_name
        self.notify_url = notify_url
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SetVsStreamsNotifyUrlConfigResponseBody(TeaModel):
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


class SetVsStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetVsStreamsNotifyUrlConfigResponseBody = None,
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
            temp_model = SetVsStreamsNotifyUrlConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StartDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDeviceResponseBody = None,
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
            temp_model = StartDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartParentPlatformRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StartParentPlatformResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartParentPlatformResponseBody = None,
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
            temp_model = StartParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRecordStreamRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        play_domain: str = None,
    ):
        self.app = app
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.play_domain = play_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        return self


class StartRecordStreamResponseBody(TeaModel):
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


class StartRecordStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartRecordStreamResponseBody = None,
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
            temp_model = StartRecordStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartStreamRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        id: str = None,
        owner_id: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.id = id
        self.owner_id = owner_id
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
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StartStreamResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartStreamResponseBody = None,
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
            temp_model = StartStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTransferStreamRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        transcode: str = None,
        url: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.transcode = transcode
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class StartTransferStreamResponseBody(TeaModel):
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


class StartTransferStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartTransferStreamResponseBody = None,
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
            temp_model = StartTransferStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAdjustRequest(TeaModel):
    def __init__(
        self,
        focus: bool = None,
        id: str = None,
        iris: bool = None,
        owner_id: int = None,
    ):
        self.focus = focus
        self.id = id
        self.iris = iris
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.focus is not None:
            result['Focus'] = self.focus
        if self.id is not None:
            result['Id'] = self.id
        if self.iris is not None:
            result['Iris'] = self.iris
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Focus') is not None:
            self.focus = m.get('Focus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Iris') is not None:
            self.iris = m.get('Iris')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StopAdjustResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAdjustResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopAdjustResponseBody = None,
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
            temp_model = StopAdjustResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StopDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDeviceResponseBody = None,
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
            temp_model = StopDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMoveRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        pan: bool = None,
        tilt: bool = None,
        zoom: bool = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pan is not None:
            result['Pan'] = self.pan
        if self.tilt is not None:
            result['Tilt'] = self.tilt
        if self.zoom is not None:
            result['Zoom'] = self.zoom
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Pan') is not None:
            self.pan = m.get('Pan')
        if m.get('Tilt') is not None:
            self.tilt = m.get('Tilt')
        if m.get('Zoom') is not None:
            self.zoom = m.get('Zoom')
        return self


class StopMoveResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopMoveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMoveResponseBody = None,
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
            temp_model = StopMoveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopParentPlatformRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StopParentPlatformResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopParentPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopParentPlatformResponseBody = None,
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
            temp_model = StopParentPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRecordStreamRequest(TeaModel):
    def __init__(
        self,
        app: str = None,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        play_domain: str = None,
    ):
        self.app = app
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.play_domain = play_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')
        return self


class StopRecordStreamResponseBody(TeaModel):
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


class StopRecordStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopRecordStreamResponseBody = None,
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
            temp_model = StopRecordStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopStreamRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StopStreamResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopStreamResponseBody = None,
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
            temp_model = StopStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTransferStreamRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
        transcode: str = None,
    ):
        self.id = id
        self.owner_id = owner_id
        self.transcode = transcode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.transcode is not None:
            result['Transcode'] = self.transcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Transcode') is not None:
            self.transcode = m.get('Transcode')
        return self


class StopTransferStreamResponseBody(TeaModel):
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


class StopTransferStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopTransferStreamResponseBody = None,
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
            temp_model = StopTransferStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncCatalogsRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SyncCatalogsResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncCatalogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncCatalogsResponseBody = None,
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
            temp_model = SyncCatalogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDeviceChannelsRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SyncDeviceChannelsResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncDeviceChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncDeviceChannelsResponseBody = None,
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
            temp_model = SyncDeviceChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDirectoryRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UnbindDirectoryResponseBody(TeaModel):
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


class UnbindDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindDirectoryResponseBody = None,
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
            temp_model = UnbindDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindParentPlatformDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        parent_platform_id: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.parent_platform_id = parent_platform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parent_platform_id is not None:
            result['ParentPlatformId'] = self.parent_platform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ParentPlatformId') is not None:
            self.parent_platform_id = m.get('ParentPlatformId')
        return self


class UnbindParentPlatformDeviceResponseBody(TeaModel):
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


class UnbindParentPlatformDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindParentPlatformDeviceResponseBody = None,
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
            temp_model = UnbindParentPlatformDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPurchasedDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UnbindPurchasedDeviceResponseBody(TeaModel):
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


class UnbindPurchasedDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindPurchasedDeviceResponseBody = None,
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
            temp_model = UnbindPurchasedDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindTemplateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: int = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class UnbindTemplateResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        request_id: str = None,
        template_id: str = None,
        template_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.request_id = request_id
        self.template_id = template_id
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class UnbindTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindTemplateResponseBody = None,
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
            temp_model = UnbindTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockDeviceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        owner_id: int = None,
    ):
        self.id = id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UnlockDeviceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnlockDeviceResponseBody = None,
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
            temp_model = UnlockDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAIConfigRequest(TeaModel):
    def __init__(
        self,
        capture_interval: int = None,
        config_id: str = None,
        configs: str = None,
        description: str = None,
        end_time: int = None,
        features: str = None,
        owner_id: int = None,
        start_time: int = None,
        status: str = None,
    ):
        self.capture_interval = capture_interval
        self.config_id = config_id
        self.configs = configs
        self.description = description
        self.end_time = end_time
        self.features = features
        self.owner_id = owner_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_interval is not None:
            result['CaptureInterval'] = self.capture_interval
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.features is not None:
            result['Features'] = self.features
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureInterval') is not None:
            self.capture_interval = m.get('CaptureInterval')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAIConfigResponseBody(TeaModel):
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


class UpdateAIConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAIConfigResponseBody = None,
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
            temp_model = UpdateAIConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBucketInfoRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        comment: str = None,
        owner_id: int = None,
    ):
        self.bucket_name = bucket_name
        self.comment = comment
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpdateBucketInfoResponseBody(TeaModel):
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


class UpdateBucketInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateBucketInfoResponseBody = None,
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
            temp_model = UpdateBucketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        effective_time: str = None,
        internal_ports: str = None,
        maintain_time: str = None,
        name: str = None,
        owner_id: int = None,
        security_group_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.description = description
        self.effective_time = effective_time
        self.internal_ports = internal_ports
        self.maintain_time = maintain_time
        self.name = name
        self.owner_id = owner_id
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.description is not None:
            result['Description'] = self.description
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.internal_ports is not None:
            result['InternalPorts'] = self.internal_ports
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InternalPorts') is not None:
            self.internal_ports = m.get('InternalPorts')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateClusterResponseBody(TeaModel):
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


class UpdateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateClusterResponseBody = None,
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
            temp_model = UpdateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRenderingDeviceSpecRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        description: str = None,
        effective_time: bool = None,
        instance_ids: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        specification: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.description = description
        self.effective_time = effective_time
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.period = period
        self.period_unit = period_unit
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.description is not None:
            result['Description'] = self.description
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class UpdateRenderingDeviceSpecResponseBody(TeaModel):
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


class UpdateRenderingDeviceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRenderingDeviceSpecResponseBody = None,
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
            temp_model = UpdateRenderingDeviceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVsPullStreamInfoConfigRequest(TeaModel):
    def __init__(
        self,
        always: str = None,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.always = always
        self.app_name = app_name
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        self.source_url = source_url
        self.start_time = start_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.always is not None:
            result['Always'] = self.always
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.source_url is not None:
            result['SourceUrl'] = self.source_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Always') is not None:
            self.always = m.get('Always')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class UpdateVsPullStreamInfoConfigResponseBody(TeaModel):
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


class UpdateVsPullStreamInfoConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateVsPullStreamInfoConfigResponseBody = None,
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
            temp_model = UpdateVsPullStreamInfoConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeRenderingDevicesHostOSRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
        rom_name: str = None,
        rom_path: str = None,
        rom_version: str = None,
    ):
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        self.rom_name = rom_name
        self.rom_path = rom_path
        self.rom_version = rom_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rom_name is not None:
            result['RomName'] = self.rom_name
        if self.rom_path is not None:
            result['RomPath'] = self.rom_path
        if self.rom_version is not None:
            result['RomVersion'] = self.rom_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RomName') is not None:
            self.rom_name = m.get('RomName')
        if m.get('RomPath') is not None:
            self.rom_path = m.get('RomPath')
        if m.get('RomVersion') is not None:
            self.rom_version = m.get('RomVersion')
        return self


class UpgradeRenderingDevicesHostOSResponseBody(TeaModel):
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


class UpgradeRenderingDevicesHostOSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeRenderingDevicesHostOSResponseBody = None,
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
            temp_model = UpgradeRenderingDevicesHostOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeRenderingDevicesImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        instance_ids: str = None,
        owner_id: int = None,
    ):
        self.image_id = image_id
        self.instance_ids = instance_ids
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpgradeRenderingDevicesImageResponseBody(TeaModel):
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


class UpgradeRenderingDevicesImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeRenderingDevicesImageResponseBody = None,
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
            temp_model = UpgradeRenderingDevicesImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadDeviceRecordRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        owner_id: int = None,
        search_criteria: str = None,
        stream_id: str = None,
        upload_id: str = None,
        upload_mode: str = None,
        upload_params: str = None,
        upload_type: str = None,
    ):
        self.device_id = device_id
        self.owner_id = owner_id
        self.search_criteria = search_criteria
        self.stream_id = stream_id
        self.upload_id = upload_id
        self.upload_mode = upload_mode
        self.upload_params = upload_params
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.search_criteria is not None:
            result['SearchCriteria'] = self.search_criteria
        if self.stream_id is not None:
            result['StreamId'] = self.stream_id
        if self.upload_id is not None:
            result['UploadId'] = self.upload_id
        if self.upload_mode is not None:
            result['UploadMode'] = self.upload_mode
        if self.upload_params is not None:
            result['UploadParams'] = self.upload_params
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SearchCriteria') is not None:
            self.search_criteria = m.get('SearchCriteria')
        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')
        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')
        if m.get('UploadMode') is not None:
            self.upload_mode = m.get('UploadMode')
        if m.get('UploadParams') is not None:
            self.upload_params = m.get('UploadParams')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        return self


class UploadDeviceRecordResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadDeviceRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UploadDeviceRecordResponseBody = None,
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
            temp_model = UploadDeviceRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


