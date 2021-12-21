# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddAclAuthorizationRequest(TeaModel):
    def __init__(
        self,
        acl_operation: str = None,
        client_token: str = None,
        pattern_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.acl_operation = acl_operation
        self.client_token = client_token
        self.pattern_type = pattern_type
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation is not None:
            result['AclOperation'] = self.acl_operation
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperation') is not None:
            self.acl_operation = m.get('AclOperation')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AddAclAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAclAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAclAuthorizationResponseBody = None,
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
            temp_model = AddAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAuthenticatedUserRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        password: str = None,
        user_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AddAuthenticatedUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAuthenticatedUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAuthenticatedUserResponseBody = None,
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
            temp_model = AddAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
    ):
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class CheckClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckClusterNameResponseBody = None,
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
            temp_model = CheckClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckInventoryRequest(TeaModel):
    def __init__(
        self,
        cloud_disk_size: int = None,
        cu_num: int = None,
        enable_multi_available_zone: bool = None,
        instance_id: str = None,
        main_zone_id: str = None,
        region_id: str = None,
        zone_ids: str = None,
    ):
        self.cloud_disk_size = cloud_disk_size
        self.cu_num = cu_num
        self.enable_multi_available_zone = enable_multi_available_zone
        self.instance_id = instance_id
        self.main_zone_id = main_zone_id
        self.region_id = region_id
        self.zone_ids = zone_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_disk_size is not None:
            result['CloudDiskSize'] = self.cloud_disk_size
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.enable_multi_available_zone is not None:
            result['EnableMultiAvailableZone'] = self.enable_multi_available_zone
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.main_zone_id is not None:
            result['MainZoneId'] = self.main_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudDiskSize') is not None:
            self.cloud_disk_size = m.get('CloudDiskSize')
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('EnableMultiAvailableZone') is not None:
            self.enable_multi_available_zone = m.get('EnableMultiAvailableZone')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MainZoneId') is not None:
            self.main_zone_id = m.get('MainZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')
        return self


class CheckInventoryResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckInventoryResponseBody = None,
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
            temp_model = CheckInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLeftCuRequest(TeaModel):
    def __init__(
        self,
        cu_num: int = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.cu_num = cu_num
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckLeftCuResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckLeftCuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckLeftCuResponseBody = None,
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
            temp_model = CheckLeftCuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserAccountResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUserAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckUserAccountResponseBody = None,
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
            temp_model = CheckUserAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserResourceRequest(TeaModel):
    def __init__(
        self,
        enable_multi_available_zone: bool = None,
        main_zone_id: str = None,
        public_network_enabled: bool = None,
        region_id: str = None,
        type: str = None,
        zone_vswitch_list: str = None,
    ):
        self.enable_multi_available_zone = enable_multi_available_zone
        self.main_zone_id = main_zone_id
        self.public_network_enabled = public_network_enabled
        self.region_id = region_id
        self.type = type
        self.zone_vswitch_list = zone_vswitch_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_multi_available_zone is not None:
            result['EnableMultiAvailableZone'] = self.enable_multi_available_zone
        if self.main_zone_id is not None:
            result['MainZoneId'] = self.main_zone_id
        if self.public_network_enabled is not None:
            result['PublicNetworkEnabled'] = self.public_network_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_vswitch_list is not None:
            result['ZoneVswitchList'] = self.zone_vswitch_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMultiAvailableZone') is not None:
            self.enable_multi_available_zone = m.get('EnableMultiAvailableZone')
        if m.get('MainZoneId') is not None:
            self.main_zone_id = m.get('MainZoneId')
        if m.get('PublicNetworkEnabled') is not None:
            self.public_network_enabled = m.get('PublicNetworkEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneVswitchList') is not None:
            self.zone_vswitch_list = m.get('ZoneVswitchList')
        return self


class CheckUserResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUserResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckUserResourceResponseBody = None,
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
            temp_model = CheckUserResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVpcRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CheckVpcResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckVpcResponseBody = None,
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
            temp_model = CheckVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVswitchRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckVswitchResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckVswitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckVswitchResponseBody = None,
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
            temp_model = CheckVswitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmOrderRequest(TeaModel):
    def __init__(
        self,
        order_info: str = None,
    ):
        self.order_info = order_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        return self


class ConfirmOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmOrderResponseBody = None,
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
            temp_model = ConfirmOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cluster_info: str = None,
    ):
        self.client_token = client_token
        self.cluster_info = cluster_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class CreateClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        began_on: int = None,
        end_on: int = None,
        order_id: str = None,
    ):
        self.began_on = began_on
        self.end_on = end_on
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateClusterResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreateDefaultRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDefaultRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDefaultRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDefaultRoleResponseBody = None,
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
            temp_model = CreateDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        order_info: str = None,
    ):
        self.client_token = client_token
        self.order_info = order_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateOrderResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclAuthorizationRequest(TeaModel):
    def __init__(
        self,
        acl_operation: str = None,
        instance_id: str = None,
        pattern_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.acl_operation = acl_operation
        self.instance_id = instance_id
        self.pattern_type = pattern_type
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation is not None:
            result['AclOperation'] = self.acl_operation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperation') is not None:
            self.acl_operation = m.get('AclOperation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteAclAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAclAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAclAuthorizationResponseBody = None,
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
            temp_model = DeleteAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthenticatedUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteAuthenticatedUserResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAuthenticatedUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAuthenticatedUserResponseBody = None,
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
            temp_model = DeleteAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterDetailRequest(TeaModel):
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


class GetClusterDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        cluster_biz_id: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        cluster_status_value: int = None,
        control_center_url: str = None,
        duration: int = None,
        expire_time: bool = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        order_biz_id: str = None,
        package_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        running_time: int = None,
        server_cert: str = None,
        zone_id: str = None,
    ):
        self.begin_time = begin_time
        self.cluster_biz_id = cluster_biz_id
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_status_value = cluster_status_value
        self.control_center_url = control_center_url
        self.duration = duration
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.order_biz_id = order_biz_id
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.running_time = running_time
        self.server_cert = server_cert
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetClusterDetailResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetClusterDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetClusterDetailResponseBody = None,
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
            temp_model = GetClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigInfoResponseBodyDataPricingInfos(TeaModel):
    def __init__(
        self,
        duration: int = None,
        pricing_cycle: str = None,
    ):
        self.duration = duration
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class DataSpecVersionInfoMapValue(TeaModel):
    def __init__(
        self,
        spec_version: str = None,
        spec_version_en: str = None,
        multi_azpermission: bool = None,
    ):
        self.spec_version = spec_version
        self.spec_version_en = spec_version_en
        self.multi_azpermission = multi_azpermission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.spec_version_en is not None:
            result['SpecVersionEn'] = self.spec_version_en
        if self.multi_azpermission is not None:
            result['MultiAZPermission'] = self.multi_azpermission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('SpecVersionEn') is not None:
            self.spec_version_en = m.get('SpecVersionEn')
        if m.get('MultiAZPermission') is not None:
            self.multi_azpermission = m.get('MultiAZPermission')
        return self


class GetConfigInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        pricing_infos: List[GetConfigInfoResponseBodyDataPricingInfos] = None,
        spec_version_info_map: Dict[str, DataSpecVersionInfoMapValue] = None,
    ):
        self.pricing_infos = pricing_infos
        self.spec_version_info_map = spec_version_info_map

    def validate(self):
        if self.pricing_infos:
            for k in self.pricing_infos:
                if k:
                    k.validate()
        if self.spec_version_info_map:
            for v in self.spec_version_info_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PricingInfos'] = []
        if self.pricing_infos is not None:
            for k in self.pricing_infos:
                result['PricingInfos'].append(k.to_map() if k else None)
        result['SpecVersionInfoMap'] = {}
        if self.spec_version_info_map is not None:
            for k, v in self.spec_version_info_map.items():
                result['SpecVersionInfoMap'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pricing_infos = []
        if m.get('PricingInfos') is not None:
            for k in m.get('PricingInfos'):
                temp_model = GetConfigInfoResponseBodyDataPricingInfos()
                self.pricing_infos.append(temp_model.from_map(k))
        self.spec_version_info_map = {}
        if m.get('SpecVersionInfoMap') is not None:
            for k, v in m.get('SpecVersionInfoMap').items():
                temp_model = DataSpecVersionInfoMapValue()
                self.spec_version_info_map[k] = temp_model.from_map(v)
        return self


class GetConfigInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetConfigInfoResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetConfigInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConfigInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConfigInfoResponseBody = None,
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
            temp_model = GetConfigInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAclDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        pattern_type: str = None,
        permission_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.pattern_type = pattern_type
        self.permission_type = permission_type
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserAclDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_operation_list: List[str] = None,
        pattern_type: str = None,
        permission_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.acl_operation_list = acl_operation_list
        self.pattern_type = pattern_type
        self.permission_type = permission_type
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_list is not None:
            result['AclOperationList'] = self.acl_operation_list
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationList') is not None:
            self.acl_operation_list = m.get('AclOperationList')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetUserAclDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserAclDetailResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserAclDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserAclDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserAclDetailResponseBody = None,
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
            temp_model = GetUserAclDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasDefaultRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        has_auth: bool = None,
        role_auth_url: str = None,
    ):
        self.has_auth = has_auth
        self.role_auth_url = role_auth_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_auth is not None:
            result['HasAuth'] = self.has_auth
        if self.role_auth_url is not None:
            result['RoleAuthUrl'] = self.role_auth_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasAuth') is not None:
            self.has_auth = m.get('HasAuth')
        if m.get('RoleAuthUrl') is not None:
            self.role_auth_url = m.get('RoleAuthUrl')
        return self


class HasDefaultRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: HasDefaultRoleResponseBodyData = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = HasDefaultRoleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasDefaultRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HasDefaultRoleResponseBody = None,
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
            temp_model = HasDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclAuthorizationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        pattern_type: str = None,
        permission_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.pattern_type = pattern_type
        self.permission_type = permission_type
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListAclAuthorizationResponseBodyData(TeaModel):
    def __init__(
        self,
        acl_operation_list: List[str] = None,
        pattern_type: str = None,
        permission_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.acl_operation_list = acl_operation_list
        self.pattern_type = pattern_type
        self.permission_type = permission_type
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_list is not None:
            result['AclOperationList'] = self.acl_operation_list
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperationList') is not None:
            self.acl_operation_list = m.get('AclOperationList')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAclAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAclAuthorizationResponseBodyData] = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAclAuthorizationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAclAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAclAuthorizationResponseBody = None,
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
            temp_model = ListAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatedUserRequest(TeaModel):
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


class ListAuthenticatedUserResponseBodyData(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        user_name: str = None,
    ):
        self.creation_time = creation_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListAuthenticatedUserResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAuthenticatedUserResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAuthenticatedUserResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAuthenticatedUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAuthenticatedUserResponseBody = None,
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
            temp_model = ListAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssinfosRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOssinfosResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        oxs_endpoint: str = None,
        vpc_endpoint: str = None,
    ):
        self.bucket = bucket
        self.endpoint = endpoint
        self.oxs_endpoint = oxs_endpoint
        self.vpc_endpoint = vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.oxs_endpoint is not None:
            result['OxsEndpoint'] = self.oxs_endpoint
        if self.vpc_endpoint is not None:
            result['VpcEndpoint'] = self.vpc_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('OxsEndpoint') is not None:
            self.oxs_endpoint = m.get('OxsEndpoint')
        if m.get('VpcEndpoint') is not None:
            self.vpc_endpoint = m.get('VpcEndpoint')
        return self


class ListOssinfosResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListOssinfosResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOssinfosResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOssinfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOssinfosResponseBody = None,
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
            temp_model = ListOssinfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        self.description = description
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListRegionsResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListSecurityGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        vpc_id: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.security_group_id = security_group_id
        self.security_group_name = security_group_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListSecurityGroupsResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSecurityGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSecurityGroupsResponseBody = None,
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
            temp_model = ListSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcsResponseBodyData(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        region_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.description = description
        self.region_id = region_id
        self.status = status
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class ListVpcsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListVpcsResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpcsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVpcsResponseBody = None,
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
            temp_model = ListVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVswitchesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVswitchesResponseBodyData(TeaModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        is_default: bool = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.cidr_block = cidr_block
        self.creation_time = creation_time
        self.description = description
        self.is_default = is_default
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVswitchesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListVswitchesResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVswitchesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVswitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVswitchesResponseBody = None,
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
            temp_model = ListVswitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListZonesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListZonesResponseBody = None,
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAclAuthorizationRequest(TeaModel):
    def __init__(
        self,
        acl_operations: str = None,
        client_token: str = None,
        instance_id: str = None,
        pattern_type: str = None,
        permission_type: str = None,
        resource_name: str = None,
        resource_type: str = None,
        user_name: str = None,
    ):
        self.acl_operations = acl_operations
        self.client_token = client_token
        self.instance_id = instance_id
        self.pattern_type = pattern_type
        self.permission_type = permission_type
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operations is not None:
            result['AclOperations'] = self.acl_operations
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclOperations') is not None:
            self.acl_operations = m.get('AclOperations')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyAclAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAclAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAclAuthorizationResponseBody = None,
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
            temp_model = ModifyAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserPasswordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyUserPasswordResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserPasswordResponseBody = None,
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
            temp_model = ModifyUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryControlCenterLoginInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class QueryControlCenterLoginInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        control_center_login_name: str = None,
        control_center_password: str = None,
    ):
        self.control_center_login_name = control_center_login_name
        self.control_center_password = control_center_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_center_login_name is not None:
            result['ControlCenterLoginName'] = self.control_center_login_name
        if self.control_center_password is not None:
            result['ControlCenterPassword'] = self.control_center_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlCenterLoginName') is not None:
            self.control_center_login_name = m.get('ControlCenterLoginName')
        if m.get('ControlCenterPassword') is not None:
            self.control_center_password = m.get('ControlCenterPassword')
        return self


class QueryControlCenterLoginInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryControlCenterLoginInfoResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryControlCenterLoginInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryControlCenterLoginInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryControlCenterLoginInfoResponseBody = None,
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
            temp_model = QueryControlCenterLoginInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPriceRequest(TeaModel):
    def __init__(
        self,
        order_info: str = None,
    ):
        self.order_info = order_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        return self


class QueryPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPriceResponseBody = None,
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
            temp_model = QueryPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewPriceRequest(TeaModel):
    def __init__(
        self,
        duration: str = None,
        instance_id: str = None,
        pricing_cycle: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class QueryRenewPriceResponseBodyDataCspSoftPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        csp_soft_price_info: QueryRenewPriceResponseBodyDataCspSoftPriceInfo = None,
    ):
        self.csp_soft_price_info = csp_soft_price_info

    def validate(self):
        if self.csp_soft_price_info:
            self.csp_soft_price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csp_soft_price_info is not None:
            result['CspSoftPriceInfo'] = self.csp_soft_price_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CspSoftPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataCspSoftPriceInfo()
            self.csp_soft_price_info = temp_model.from_map(m['CspSoftPriceInfo'])
        return self


class QueryRenewPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryRenewPriceResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRenewPriceResponseBody = None,
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
            temp_model = QueryRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpPriceRequest(TeaModel):
    def __init__(
        self,
        broker_number: int = None,
        instance_id: str = None,
    ):
        self.broker_number = broker_number
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo(TeaModel):
    def __init__(
        self,
        currency: str = None,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.currency = currency
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyData(TeaModel):
    def __init__(
        self,
        csp_soft_price_info: QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo = None,
    ):
        self.csp_soft_price_info = csp_soft_price_info

    def validate(self):
        if self.csp_soft_price_info:
            self.csp_soft_price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csp_soft_price_info is not None:
            result['CspSoftPriceInfo'] = self.csp_soft_price_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CspSoftPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo()
            self.csp_soft_price_info = temp_model.from_map(m['CspSoftPriceInfo'])
        return self


class QueryScaleUpPriceResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryScaleUpPriceResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryScaleUpPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryScaleUpPriceResponseBody = None,
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
            temp_model = QueryScaleUpPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnpaidOrderRequest(TeaModel):
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


class QueryUnpaidOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUnpaidOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUnpaidOrderResponseBody = None,
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
            temp_model = QueryUnpaidOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: str = None,
        instance_id: str = None,
        pricing_cycle: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: RenewInstanceResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleUpClusterRequest(TeaModel):
    def __init__(
        self,
        broker_number: int = None,
        instance_id: str = None,
    ):
        self.broker_number = broker_number
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ScaleUpClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class ScaleUpClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: ScaleUpClusterResponseBodyData = None,
        err_code: int = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ScaleUpClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleUpClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScaleUpClusterResponseBody = None,
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
            temp_model = ScaleUpClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchClusterInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class SearchClusterInstancesResponseBodyDataClusterInstanceInfo(TeaModel):
    def __init__(
        self,
        control_center_login_name: str = None,
        duration: int = None,
        open_colddata_archiving: bool = None,
        oss_bucket_path: str = None,
        oss_endpoint: str = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        spec_version: str = None,
        vpc_id: str = None,
        vsw_ids: str = None,
    ):
        self.control_center_login_name = control_center_login_name
        self.duration = duration
        self.open_colddata_archiving = open_colddata_archiving
        self.oss_bucket_path = oss_bucket_path
        self.oss_endpoint = oss_endpoint
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.spec_version = spec_version
        self.vpc_id = vpc_id
        self.vsw_ids = vsw_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_center_login_name is not None:
            result['ControlCenterLoginName'] = self.control_center_login_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.open_colddata_archiving is not None:
            result['OpenColddataArchiving'] = self.open_colddata_archiving
        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_ids is not None:
            result['VswIds'] = self.vsw_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlCenterLoginName') is not None:
            self.control_center_login_name = m.get('ControlCenterLoginName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OpenColddataArchiving') is not None:
            self.open_colddata_archiving = m.get('OpenColddataArchiving')
        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswIds') is not None:
            self.vsw_ids = m.get('VswIds')
        return self


class SearchClusterInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        cku_conf: str = None,
        cluster_id: str = None,
        cluster_instance_info: SearchClusterInstancesResponseBodyDataClusterInstanceInfo = None,
        cluster_name: str = None,
        cluster_size: int = None,
        cluster_status: str = None,
        cluster_status_value: int = None,
        control_center_url: str = None,
        cu_num: int = None,
        expire_time: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        open_ksql: bool = None,
        order_biz_id: str = None,
        package_type: str = None,
        region_id: str = None,
        storage_size: int = None,
        unpaid_order_ids: List[int] = None,
        valid_broker_number: bool = None,
        version: str = None,
        zone_id: str = None,
    ):
        self.cku_conf = cku_conf
        self.cluster_id = cluster_id
        self.cluster_instance_info = cluster_instance_info
        self.cluster_name = cluster_name
        self.cluster_size = cluster_size
        self.cluster_status = cluster_status
        self.cluster_status_value = cluster_status_value
        self.control_center_url = control_center_url
        self.cu_num = cu_num
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.open_ksql = open_ksql
        self.order_biz_id = order_biz_id
        self.package_type = package_type
        self.region_id = region_id
        self.storage_size = storage_size
        self.unpaid_order_ids = unpaid_order_ids
        self.valid_broker_number = valid_broker_number
        self.version = version
        self.zone_id = zone_id

    def validate(self):
        if self.cluster_instance_info:
            self.cluster_instance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cku_conf is not None:
            result['CkuConf'] = self.cku_conf
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_info is not None:
            result['ClusterInstanceInfo'] = self.cluster_instance_info.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.open_ksql is not None:
            result['OpenKsql'] = self.open_ksql
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.unpaid_order_ids is not None:
            result['UnpaidOrderIds'] = self.unpaid_order_ids
        if self.valid_broker_number is not None:
            result['ValidBrokerNumber'] = self.valid_broker_number
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CkuConf') is not None:
            self.cku_conf = m.get('CkuConf')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceInfo') is not None:
            temp_model = SearchClusterInstancesResponseBodyDataClusterInstanceInfo()
            self.cluster_instance_info = temp_model.from_map(m['ClusterInstanceInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OpenKsql') is not None:
            self.open_ksql = m.get('OpenKsql')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('UnpaidOrderIds') is not None:
            self.unpaid_order_ids = m.get('UnpaidOrderIds')
        if m.get('ValidBrokerNumber') is not None:
            self.valid_broker_number = m.get('ValidBrokerNumber')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchClusterInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SearchClusterInstancesResponseBodyData] = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchClusterInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchClusterInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchClusterInstancesResponseBody = None,
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
            temp_model = SearchClusterInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleOrderRequest(TeaModel):
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


class SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList(TeaModel):
    def __init__(
        self,
        broker_number: int = None,
        cu_num_per_broker: int = None,
        storage_size_per_broker: int = None,
    ):
        self.broker_number = broker_number
        self.cu_num_per_broker = cu_num_per_broker
        self.storage_size_per_broker = storage_size_per_broker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.cu_num_per_broker is not None:
            result['CuNumPerBroker'] = self.cu_num_per_broker
        if self.storage_size_per_broker is not None:
            result['StorageSizePerBroker'] = self.storage_size_per_broker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('CuNumPerBroker') is not None:
            self.cu_num_per_broker = m.get('CuNumPerBroker')
        if m.get('StorageSizePerBroker') is not None:
            self.storage_size_per_broker = m.get('StorageSizePerBroker')
        return self


class SingleOrderResponseBodyDataCspResourceConfig(TeaModel):
    def __init__(
        self,
        broker_config_list: List[SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList] = None,
        multi_available_zone_permission: bool = None,
    ):
        self.broker_config_list = broker_config_list
        self.multi_available_zone_permission = multi_available_zone_permission

    def validate(self):
        if self.broker_config_list:
            for k in self.broker_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BrokerConfigList'] = []
        if self.broker_config_list is not None:
            for k in self.broker_config_list:
                result['BrokerConfigList'].append(k.to_map() if k else None)
        if self.multi_available_zone_permission is not None:
            result['MultiAvailableZonePermission'] = self.multi_available_zone_permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.broker_config_list = []
        if m.get('BrokerConfigList') is not None:
            for k in m.get('BrokerConfigList'):
                temp_model = SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList()
                self.broker_config_list.append(temp_model.from_map(k))
        if m.get('MultiAvailableZonePermission') is not None:
            self.multi_available_zone_permission = m.get('MultiAvailableZonePermission')
        return self


class SingleOrderResponseBodyDataEcsGroupList(TeaModel):
    def __init__(
        self,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        host_group_name: str = None,
        host_group_type: str = None,
        instance_type: str = None,
        node_count: int = None,
        sys_disk_capacity: int = None,
        sys_disk_type: str = None,
    ):
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.host_group_name = host_group_name
        self.host_group_type = host_group_type
        self.instance_type = instance_type
        self.node_count = node_count
        self.sys_disk_capacity = sys_disk_capacity
        self.sys_disk_type = sys_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.sys_disk_capacity is not None:
            result['SysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['SysDiskType'] = self.sys_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('SysDiskCapacity')
        if m.get('SysDiskType') is not None:
            self.sys_disk_type = m.get('SysDiskType')
        return self


class SingleOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cluster_id: str = None,
        cluster_size: int = None,
        cluster_status: int = None,
        csp_resource_config: SingleOrderResponseBodyDataCspResourceConfig = None,
        cu_num: int = None,
        duration: int = None,
        ecs_group_list: List[SingleOrderResponseBodyDataEcsGroupList] = None,
        instance_id: str = None,
        order_id: str = None,
        package_type: str = None,
        pricing_cycle: str = None,
        spec_version: str = None,
        storage_size: int = None,
    ):
        self.auto_renew = auto_renew
        self.cluster_id = cluster_id
        self.cluster_size = cluster_size
        self.cluster_status = cluster_status
        self.csp_resource_config = csp_resource_config
        self.cu_num = cu_num
        self.duration = duration
        self.ecs_group_list = ecs_group_list
        self.instance_id = instance_id
        self.order_id = order_id
        self.package_type = package_type
        self.pricing_cycle = pricing_cycle
        self.spec_version = spec_version
        self.storage_size = storage_size

    def validate(self):
        if self.csp_resource_config:
            self.csp_resource_config.validate()
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.csp_resource_config is not None:
            result['CspResourceConfig'] = self.csp_resource_config.to_map()
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('CspResourceConfig') is not None:
            temp_model = SingleOrderResponseBodyDataCspResourceConfig()
            self.csp_resource_config = temp_model.from_map(m['CspResourceConfig'])
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SingleOrderResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class SingleOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: SingleOrderResponseBodyData = None,
        err_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SingleOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SingleOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SingleOrderResponseBody = None,
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
            temp_model = SingleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        instance_id: str = None,
    ):
        self.cluster_name = cluster_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateClusterNameResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateClusterNameResponseBody = None,
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
            temp_model = UpdateClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


