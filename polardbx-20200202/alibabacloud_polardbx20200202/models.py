# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AlignStoragePrimaryAzoneRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        storage_instance_name: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.storage_instance_name = storage_instance_name
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_instance_name is not None:
            result['StorageInstanceName'] = self.storage_instance_name
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageInstanceName') is not None:
            self.storage_instance_name = m.get('StorageInstanceName')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class AlignStoragePrimaryAzoneResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AlignStoragePrimaryAzoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AlignStoragePrimaryAzoneResponseBody = None,
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
            temp_model = AlignStoragePrimaryAzoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateColdDataVolumeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AllocateColdDataVolumeResponseBody(TeaModel):
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


class AllocateColdDataVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateColdDataVolumeResponseBody = None,
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
            temp_model = AllocateColdDataVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.connection_string_prefix = connection_string_prefix
        self.dbinstance_name = dbinstance_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.port = port
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
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


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateInstancePublicConnectionResponseBody = None,
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
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelActiveOperationTasksRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        region_id: str = None,
    ):
        self.ids = ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelActiveOperationTasksResponseBody(TeaModel):
    def __init__(
        self,
        ids: str = None,
        request_id: str = None,
    ):
        self.ids = ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelActiveOperationTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelActiveOperationTasksResponseBody = None,
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
            temp_model = CancelActiveOperationTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        role_arn: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class CheckCloudResourceAuthorizedResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization_state: str = None,
        role_arn: str = None,
    ):
        self.authorization_state = authorization_state
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_state is not None:
            result['AuthorizationState'] = self.authorization_state
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationState') is not None:
            self.authorization_state = m.get('AuthorizationState')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        return self


class CheckCloudResourceAuthorizedResponseBody(TeaModel):
    def __init__(
        self,
        data: CheckCloudResourceAuthorizedResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CheckCloudResourceAuthorizedResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCloudResourceAuthorizedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckCloudResourceAuthorizedResponseBody = None,
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
            temp_model = CheckCloudResourceAuthorizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        account_privilege: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_password = account_password
        self.account_privilege = account_privilege
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
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
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupRequest(TeaModel):
    def __init__(
        self,
        backup_type: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.backup_type = backup_type
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBackupResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_set_id: int = None,
    ):
        self.backup_set_id = backup_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        return self


class CreateBackupResponseBody(TeaModel):
    def __init__(
        self,
        data: List[CreateBackupResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = CreateBackupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackupResponseBody = None,
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
            temp_model = CreateBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        charset: str = None,
        dbinstance_name: str = None,
        db_description: str = None,
        db_name: str = None,
        mode: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.account_name = account_name
        self.account_privilege = account_privilege
        self.charset = charset
        self.dbinstance_name = dbinstance_name
        self.db_description = db_description
        self.db_name = db_name
        self.mode = mode
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class CreateDBResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBResponseBody = None,
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
            temp_model = CreateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cnnode_count: str = None,
        client_token: str = None,
        cn_class: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dnnode_count: str = None,
        dn_class: str = None,
        engine_version: str = None,
        is_read_dbinstance: bool = None,
        network_type: str = None,
        pay_type: str = None,
        period: str = None,
        primary_dbinstance_name: str = None,
        primary_zone: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_zone: str = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        used_time: int = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.cnnode_count = cnnode_count
        self.client_token = client_token
        self.cn_class = cn_class
        self.dbnode_class = dbnode_class
        self.dbnode_count = dbnode_count
        self.dnnode_count = dnnode_count
        self.dn_class = dn_class
        self.engine_version = engine_version
        self.is_read_dbinstance = is_read_dbinstance
        self.network_type = network_type
        self.pay_type = pay_type
        self.period = period
        self.primary_dbinstance_name = primary_dbinstance_name
        self.primary_zone = primary_zone
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.secondary_zone = secondary_zone
        self.tertiary_zone = tertiary_zone
        self.topology_type = topology_type
        self.used_time = used_time
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cnnode_count is not None:
            result['CNNodeCount'] = self.cnnode_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cn_class is not None:
            result['CnClass'] = self.cn_class
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        if self.dnnode_count is not None:
            result['DNNodeCount'] = self.dnnode_count
        if self.dn_class is not None:
            result['DnClass'] = self.dn_class
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.is_read_dbinstance is not None:
            result['IsReadDBInstance'] = self.is_read_dbinstance
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.primary_dbinstance_name is not None:
            result['PrimaryDBInstanceName'] = self.primary_dbinstance_name
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone
        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone
        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CNNodeCount') is not None:
            self.cnnode_count = m.get('CNNodeCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CnClass') is not None:
            self.cn_class = m.get('CnClass')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        if m.get('DNNodeCount') is not None:
            self.dnnode_count = m.get('DNNodeCount')
        if m.get('DnClass') is not None:
            self.dn_class = m.get('DnClass')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('IsReadDBInstance') is not None:
            self.is_read_dbinstance = m.get('IsReadDBInstance')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PrimaryDBInstanceName') is not None:
            self.primary_dbinstance_name = m.get('PrimaryDBInstanceName')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')
        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')
        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBInstanceResponseBody = None,
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
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSuperAccountRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_password = account_password
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateSuperAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSuperAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSuperAccountResponseBody = None,
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
            temp_model = CreateSuperAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.account_name = account_name
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
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
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        db_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDBResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBResponseBody = None,
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
            temp_model = DeleteDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
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


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBInstanceResponseBody = None,
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
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountListRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccountListResponseBodyData(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_privilege: str = None,
        account_type: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
        gmt_created: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_privilege = account_privilege
        self.account_type = account_type
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.gmt_created = gmt_created

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        return self


class DescribeAccountListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeAccountListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = DescribeAccountListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAccountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccountListResponseBody = None,
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
            temp_model = DescribeAccountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationMaintainConfRequest(TeaModel):
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


class DescribeActiveOperationMaintainConfResponseBodyConfig(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        cycle_time: str = None,
        cycle_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        modified_time: str = None,
        status: int = None,
    ):
        self.created_time = created_time
        self.cycle_time = cycle_time
        self.cycle_type = cycle_type
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.modified_time = modified_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cycle_time is not None:
            result['CycleTime'] = self.cycle_time
        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CycleTime') is not None:
            self.cycle_time = m.get('CycleTime')
        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeActiveOperationMaintainConfResponseBody(TeaModel):
    def __init__(
        self,
        config: DescribeActiveOperationMaintainConfResponseBodyConfig = None,
        has_config: int = None,
        request_id: str = None,
    ):
        self.config = config
        self.has_config = has_config
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.has_config is not None:
            result['HasConfig'] = self.has_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribeActiveOperationMaintainConfResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('HasConfig') is not None:
            self.has_config = m.get('HasConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeActiveOperationMaintainConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeActiveOperationMaintainConfResponseBody = None,
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
            temp_model = DescribeActiveOperationMaintainConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationTaskCountRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        product: str = None,
        region_id: str = None,
    ):
        self.category = category
        self.product = product
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeActiveOperationTaskCountResponseBody(TeaModel):
    def __init__(
        self,
        need_pop: int = None,
        request_id: str = None,
        task_count: int = None,
    ):
        self.need_pop = need_pop
        self.request_id = request_id
        self.task_count = task_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_pop is not None:
            result['NeedPop'] = self.need_pop
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_count is not None:
            result['TaskCount'] = self.task_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedPop') is not None:
            self.need_pop = m.get('NeedPop')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskCount') is not None:
            self.task_count = m.get('TaskCount')
        return self


class DescribeActiveOperationTaskCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeActiveOperationTaskCountResponseBody = None,
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
            temp_model = DescribeActiveOperationTaskCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeActiveOperationTasksRequest(TeaModel):
    def __init__(
        self,
        allow_cancel: int = None,
        allow_change: int = None,
        change_level: str = None,
        db_type: str = None,
        ins_name: str = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region: str = None,
        region_id: str = None,
        status: int = None,
        task_type: str = None,
    ):
        self.allow_cancel = allow_cancel
        self.allow_change = allow_change
        self.change_level = change_level
        self.db_type = db_type
        self.ins_name = ins_name
        self.page_number = page_number
        self.page_size = page_size
        self.product_id = product_id
        self.region = region
        self.region_id = region_id
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.allow_change is not None:
            result['AllowChange'] = self.allow_change
        if self.change_level is not None:
            result['ChangeLevel'] = self.change_level
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.region is not None:
            result['Region'] = self.region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('AllowChange') is not None:
            self.allow_change = m.get('AllowChange')
        if m.get('ChangeLevel') is not None:
            self.change_level = m.get('ChangeLevel')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeActiveOperationTasksResponseBodyItems(TeaModel):
    def __init__(
        self,
        allow_cancel: str = None,
        allow_change: str = None,
        change_level: str = None,
        change_level_en: str = None,
        change_level_zh: str = None,
        created_time: str = None,
        current_avz: str = None,
        db_type: str = None,
        db_version: str = None,
        deadline: str = None,
        id: int = None,
        impact: str = None,
        impact_en: str = None,
        impact_zh: str = None,
        ins_comment: str = None,
        ins_name: str = None,
        modified_time: str = None,
        prepare_interval: str = None,
        region: str = None,
        result_info: str = None,
        start_time: str = None,
        status: int = None,
        sub_ins_names: List[str] = None,
        switch_time: str = None,
        task_type: str = None,
        task_type_en: str = None,
        task_type_zh: str = None,
    ):
        self.allow_cancel = allow_cancel
        self.allow_change = allow_change
        self.change_level = change_level
        self.change_level_en = change_level_en
        self.change_level_zh = change_level_zh
        self.created_time = created_time
        self.current_avz = current_avz
        self.db_type = db_type
        self.db_version = db_version
        self.deadline = deadline
        self.id = id
        self.impact = impact
        self.impact_en = impact_en
        self.impact_zh = impact_zh
        self.ins_comment = ins_comment
        self.ins_name = ins_name
        self.modified_time = modified_time
        self.prepare_interval = prepare_interval
        self.region = region
        self.result_info = result_info
        self.start_time = start_time
        self.status = status
        self.sub_ins_names = sub_ins_names
        self.switch_time = switch_time
        self.task_type = task_type
        self.task_type_en = task_type_en
        self.task_type_zh = task_type_zh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_cancel is not None:
            result['AllowCancel'] = self.allow_cancel
        if self.allow_change is not None:
            result['AllowChange'] = self.allow_change
        if self.change_level is not None:
            result['ChangeLevel'] = self.change_level
        if self.change_level_en is not None:
            result['ChangeLevelEn'] = self.change_level_en
        if self.change_level_zh is not None:
            result['ChangeLevelZh'] = self.change_level_zh
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.current_avz is not None:
            result['CurrentAVZ'] = self.current_avz
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.deadline is not None:
            result['Deadline'] = self.deadline
        if self.id is not None:
            result['Id'] = self.id
        if self.impact is not None:
            result['Impact'] = self.impact
        if self.impact_en is not None:
            result['ImpactEn'] = self.impact_en
        if self.impact_zh is not None:
            result['ImpactZh'] = self.impact_zh
        if self.ins_comment is not None:
            result['InsComment'] = self.ins_comment
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.prepare_interval is not None:
            result['PrepareInterval'] = self.prepare_interval
        if self.region is not None:
            result['Region'] = self.region
        if self.result_info is not None:
            result['ResultInfo'] = self.result_info
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_ins_names is not None:
            result['SubInsNames'] = self.sub_ins_names
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_en is not None:
            result['TaskTypeEn'] = self.task_type_en
        if self.task_type_zh is not None:
            result['TaskTypeZh'] = self.task_type_zh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCancel') is not None:
            self.allow_cancel = m.get('AllowCancel')
        if m.get('AllowChange') is not None:
            self.allow_change = m.get('AllowChange')
        if m.get('ChangeLevel') is not None:
            self.change_level = m.get('ChangeLevel')
        if m.get('ChangeLevelEn') is not None:
            self.change_level_en = m.get('ChangeLevelEn')
        if m.get('ChangeLevelZh') is not None:
            self.change_level_zh = m.get('ChangeLevelZh')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CurrentAVZ') is not None:
            self.current_avz = m.get('CurrentAVZ')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('Deadline') is not None:
            self.deadline = m.get('Deadline')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Impact') is not None:
            self.impact = m.get('Impact')
        if m.get('ImpactEn') is not None:
            self.impact_en = m.get('ImpactEn')
        if m.get('ImpactZh') is not None:
            self.impact_zh = m.get('ImpactZh')
        if m.get('InsComment') is not None:
            self.ins_comment = m.get('InsComment')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PrepareInterval') is not None:
            self.prepare_interval = m.get('PrepareInterval')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResultInfo') is not None:
            self.result_info = m.get('ResultInfo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubInsNames') is not None:
            self.sub_ins_names = m.get('SubInsNames')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeEn') is not None:
            self.task_type_en = m.get('TaskTypeEn')
        if m.get('TaskTypeZh') is not None:
            self.task_type_zh = m.get('TaskTypeZh')
        return self


class DescribeActiveOperationTasksResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeActiveOperationTasksResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
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
            for k in m.get('Items'):
                temp_model = DescribeActiveOperationTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeActiveOperationTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeActiveOperationTasksResponseBody = None,
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
            temp_model = DescribeActiveOperationTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeArchiveTableListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        page_index: int = None,
        page_size: int = None,
        region_id: str = None,
        schema_name: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.page_index = page_index
        self.page_size = page_size
        self.region_id = region_id
        self.schema_name = schema_name
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeArchiveTableListResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        archive_status: str = None,
        created_date: int = None,
        file_count: int = None,
        last_success_archive_time: int = None,
        schema_name: str = None,
        space_size: float = None,
        table_name: str = None,
    ):
        self.archive_status = archive_status
        self.created_date = created_date
        self.file_count = file_count
        self.last_success_archive_time = last_success_archive_time
        self.schema_name = schema_name
        self.space_size = space_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.file_count is not None:
            result['FileCount'] = self.file_count
        if self.last_success_archive_time is not None:
            result['LastSuccessArchiveTime'] = self.last_success_archive_time
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.space_size is not None:
            result['SpaceSize'] = self.space_size
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')
        if m.get('LastSuccessArchiveTime') is not None:
            self.last_success_archive_time = m.get('LastSuccessArchiveTime')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SpaceSize') is not None:
            self.space_size = m.get('SpaceSize')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeArchiveTableListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        paused_count: int = None,
        running_count: int = None,
        success_count: int = None,
        tables: List[DescribeArchiveTableListResponseBodyDataTables] = None,
        tobe_archived_conut: int = None,
        total: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.paused_count = paused_count
        self.running_count = running_count
        self.success_count = success_count
        self.tables = tables
        self.tobe_archived_conut = tobe_archived_conut
        self.total = total

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.paused_count is not None:
            result['PausedCount'] = self.paused_count
        if self.running_count is not None:
            result['RunningCount'] = self.running_count
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tobe_archived_conut is not None:
            result['TobeArchivedConut'] = self.tobe_archived_conut
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PausedCount') is not None:
            self.paused_count = m.get('PausedCount')
        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeArchiveTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TobeArchivedConut') is not None:
            self.tobe_archived_conut = m.get('TobeArchivedConut')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeArchiveTableListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeArchiveTableListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeArchiveTableListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeArchiveTableListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeArchiveTableListResponseBody = None,
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
            temp_model = DescribeArchiveTableListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBackupPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_period: str = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        backup_type: str = None,
        backup_way: str = None,
        cold_data_backup_interval: int = None,
        cold_data_backup_retention: int = None,
        cross_region_data_backup_retention: int = None,
        cross_region_log_backup_retention: int = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        force_clean_on_high_space_usage: int = None,
        is_cross_region_data_backup_enabled: bool = None,
        is_cross_region_log_backup_enabled: bool = None,
        is_enabled: int = None,
        local_log_retention: int = None,
        local_log_retention_number: int = None,
        log_local_retention_space: int = None,
        remove_log_retention: int = None,
    ):
        self.backup_period = backup_period
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.backup_type = backup_type
        self.backup_way = backup_way
        self.cold_data_backup_interval = cold_data_backup_interval
        self.cold_data_backup_retention = cold_data_backup_retention
        self.cross_region_data_backup_retention = cross_region_data_backup_retention
        self.cross_region_log_backup_retention = cross_region_log_backup_retention
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.is_cross_region_data_backup_enabled = is_cross_region_data_backup_enabled
        self.is_cross_region_log_backup_enabled = is_cross_region_log_backup_enabled
        self.is_enabled = is_enabled
        self.local_log_retention = local_log_retention
        self.local_log_retention_number = local_log_retention_number
        self.log_local_retention_space = log_local_retention_space
        self.remove_log_retention = remove_log_retention

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.cold_data_backup_interval is not None:
            result['ColdDataBackupInterval'] = self.cold_data_backup_interval
        if self.cold_data_backup_retention is not None:
            result['ColdDataBackupRetention'] = self.cold_data_backup_retention
        if self.cross_region_data_backup_retention is not None:
            result['CrossRegionDataBackupRetention'] = self.cross_region_data_backup_retention
        if self.cross_region_log_backup_retention is not None:
            result['CrossRegionLogBackupRetention'] = self.cross_region_log_backup_retention
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_cross_region_data_backup_enabled is not None:
            result['IsCrossRegionDataBackupEnabled'] = self.is_cross_region_data_backup_enabled
        if self.is_cross_region_log_backup_enabled is not None:
            result['IsCrossRegionLogBackupEnabled'] = self.is_cross_region_log_backup_enabled
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.local_log_retention_number is not None:
            result['LocalLogRetentionNumber'] = self.local_log_retention_number
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('ColdDataBackupInterval') is not None:
            self.cold_data_backup_interval = m.get('ColdDataBackupInterval')
        if m.get('ColdDataBackupRetention') is not None:
            self.cold_data_backup_retention = m.get('ColdDataBackupRetention')
        if m.get('CrossRegionDataBackupRetention') is not None:
            self.cross_region_data_backup_retention = m.get('CrossRegionDataBackupRetention')
        if m.get('CrossRegionLogBackupRetention') is not None:
            self.cross_region_log_backup_retention = m.get('CrossRegionLogBackupRetention')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsCrossRegionDataBackupEnabled') is not None:
            self.is_cross_region_data_backup_enabled = m.get('IsCrossRegionDataBackupEnabled')
        if m.get('IsCrossRegionLogBackupEnabled') is not None:
            self.is_cross_region_log_backup_enabled = m.get('IsCrossRegionLogBackupEnabled')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LocalLogRetentionNumber') is not None:
            self.local_log_retention_number = m.get('LocalLogRetentionNumber')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeBackupPolicyResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = DescribeBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        region_id: str = None,
    ):
        self.backup_set_id = backup_set_id
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBackupSetResponseBodyDataOSSList(TeaModel):
    def __init__(
        self,
        backup_set_file: str = None,
        download_link: str = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
    ):
        self.backup_set_file = backup_set_file
        self.download_link = download_link
        self.intranet_download_link = intranet_download_link
        self.link_expired_time = link_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_file is not None:
            result['BackupSetFile'] = self.backup_set_file
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link
        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetFile') is not None:
            self.backup_set_file = m.get('BackupSetFile')
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')
        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')
        return self


class DescribeBackupSetResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_model: int = None,
        backup_set_id: int = None,
        backup_set_size: int = None,
        backup_type: int = None,
        begin_time: int = None,
        end_time: int = None,
        osslist: List[DescribeBackupSetResponseBodyDataOSSList] = None,
        status: int = None,
    ):
        self.backup_model = backup_model
        self.backup_set_id = backup_set_id
        self.backup_set_size = backup_set_size
        self.backup_type = backup_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.osslist = osslist
        self.status = status

    def validate(self):
        if self.osslist:
            for k in self.osslist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_model is not None:
            result['BackupModel'] = self.backup_model
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['OSSList'] = []
        if self.osslist is not None:
            for k in self.osslist:
                result['OSSList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupModel') is not None:
            self.backup_model = m.get('BackupModel')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.osslist = []
        if m.get('OSSList') is not None:
            for k in m.get('OSSList'):
                temp_model = DescribeBackupSetResponseBodyDataOSSList()
                self.osslist.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupSetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeBackupSetResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = DescribeBackupSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupSetResponseBody = None,
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
            temp_model = DescribeBackupSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSetListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBackupSetListResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_model: int = None,
        backup_set_id: int = None,
        backup_set_size: int = None,
        backup_type: int = None,
        begin_time: int = None,
        end_time: int = None,
        status: int = None,
    ):
        self.backup_model = backup_model
        self.backup_set_id = backup_set_id
        self.backup_set_size = backup_set_size
        self.backup_type = backup_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_model is not None:
            result['BackupModel'] = self.backup_model
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupModel') is not None:
            self.backup_model = m.get('BackupModel')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeBackupSetListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeBackupSetListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = DescribeBackupSetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeBackupSetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackupSetListResponseBody = None,
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
            temp_model = DescribeBackupSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBinaryLogListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        end_time: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.end_time = end_time
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeBinaryLogListResponseBodyLogList(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        created_time: str = None,
        download_link: str = None,
        end_time: str = None,
        file_name: str = None,
        id: int = None,
        log_size: int = None,
        modified_time: str = None,
        purge_status: int = None,
        upload_host: str = None,
        upload_status: int = None,
    ):
        self.begin_time = begin_time
        self.created_time = created_time
        self.download_link = download_link
        self.end_time = end_time
        self.file_name = file_name
        self.id = id
        self.log_size = log_size
        self.modified_time = modified_time
        self.purge_status = purge_status
        self.upload_host = upload_host
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.purge_status is not None:
            result['PurgeStatus'] = self.purge_status
        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host
        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PurgeStatus') is not None:
            self.purge_status = m.get('PurgeStatus')
        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')
        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')
        return self


class DescribeBinaryLogListResponseBody(TeaModel):
    def __init__(
        self,
        log_list: List[DescribeBinaryLogListResponseBodyLogList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_number: int = None,
    ):
        self.log_list = log_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_number = total_number

    def validate(self):
        if self.log_list:
            for k in self.log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogList'] = []
        if self.log_list is not None:
            for k in self.log_list:
                result['LogList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k in m.get('LogList'):
                temp_model = DescribeBinaryLogListResponseBodyLogList()
                self.log_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class DescribeBinaryLogListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBinaryLogListResponseBody = None,
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
            temp_model = DescribeBinaryLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCharacterSetRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCharacterSetResponseBodyData(TeaModel):
    def __init__(
        self,
        character_set: List[str] = None,
        engine: str = None,
    ):
        self.character_set = character_set
        self.engine = engine

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_set is not None:
            result['CharacterSet'] = self.character_set
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterSet') is not None:
            self.character_set = m.get('CharacterSet')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeCharacterSetResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeCharacterSetResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeCharacterSetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCharacterSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCharacterSetResponseBody = None,
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
            temp_model = DescribeCharacterSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColdDataBasicInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeColdDataBasicInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_set_count: int = None,
        backup_set_space_size: float = None,
        cloud_product: str = None,
        current_space_size: float = None,
        data_redundancy_type: str = None,
        enable_status: bool = None,
        read_access_num: int = None,
        region_id: str = None,
        volume_name: str = None,
        write_access_num: float = None,
    ):
        self.backup_set_count = backup_set_count
        self.backup_set_space_size = backup_set_space_size
        self.cloud_product = cloud_product
        self.current_space_size = current_space_size
        self.data_redundancy_type = data_redundancy_type
        self.enable_status = enable_status
        self.read_access_num = read_access_num
        self.region_id = region_id
        self.volume_name = volume_name
        self.write_access_num = write_access_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_count is not None:
            result['BackupSetCount'] = self.backup_set_count
        if self.backup_set_space_size is not None:
            result['BackupSetSpaceSize'] = self.backup_set_space_size
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product
        if self.current_space_size is not None:
            result['CurrentSpaceSize'] = self.current_space_size
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.read_access_num is not None:
            result['ReadAccessNum'] = self.read_access_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.volume_name is not None:
            result['VolumeName'] = self.volume_name
        if self.write_access_num is not None:
            result['WriteAccessNum'] = self.write_access_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetCount') is not None:
            self.backup_set_count = m.get('BackupSetCount')
        if m.get('BackupSetSpaceSize') is not None:
            self.backup_set_space_size = m.get('BackupSetSpaceSize')
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')
        if m.get('CurrentSpaceSize') is not None:
            self.current_space_size = m.get('CurrentSpaceSize')
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ReadAccessNum') is not None:
            self.read_access_num = m.get('ReadAccessNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VolumeName') is not None:
            self.volume_name = m.get('VolumeName')
        if m.get('WriteAccessNum') is not None:
            self.write_access_num = m.get('WriteAccessNum')
        return self


class DescribeColdDataBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeColdDataBasicInfoResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeColdDataBasicInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeColdDataBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeColdDataBasicInfoResponseBody = None,
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
            temp_model = DescribeColdDataBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        self.connection_string = connection_string
        self.port = port
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(
        self,
        compute_node_id: str = None,
        data_node_id: str = None,
        id: str = None,
        node_class: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.compute_node_id = compute_node_id
        self.data_node_id = data_node_id
        self.id = id
        self.node_class = node_class
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_node_id is not None:
            result['ComputeNodeId'] = self.compute_node_id
        if self.data_node_id is not None:
            result['DataNodeId'] = self.data_node_id
        if self.id is not None:
            result['Id'] = self.id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeNodeId') is not None:
            self.compute_node_id = m.get('ComputeNodeId')
        if m.get('DataNodeId') is not None:
            self.data_node_id = m.get('DataNodeId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceAttributeResponseBodyDBInstance(TeaModel):
    def __init__(
        self,
        can_not_create_columnar: bool = None,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        columnar_instance_name: str = None,
        columnar_read_dbinstances: List[str] = None,
        commodity_code: str = None,
        conn_addrs: List[DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs] = None,
        connection_string: str = None,
        create_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnodes: List[DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        different_dnspec: bool = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        engine: str = None,
        expire_date: str = None,
        expired: str = None,
        id: str = None,
        kind_code: int = None,
        ltsversions: List[str] = None,
        latest_minor_version: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        minor_version: str = None,
        network: str = None,
        pay_type: str = None,
        port: str = None,
        primary_zone: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        rights_separation_enabled: bool = None,
        rights_separation_status: str = None,
        secondary_zone: str = None,
        series: str = None,
        status: str = None,
        storage_used: int = None,
        tag_set: List[DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet] = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.can_not_create_columnar = can_not_create_columnar
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.columnar_instance_name = columnar_instance_name
        self.columnar_read_dbinstances = columnar_read_dbinstances
        self.commodity_code = commodity_code
        self.conn_addrs = conn_addrs
        self.connection_string = connection_string
        self.create_time = create_time
        self.dbinstance_type = dbinstance_type
        self.dbnode_class = dbnode_class
        self.dbnode_count = dbnode_count
        self.dbnodes = dbnodes
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.description = description
        self.different_dnspec = different_dnspec
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.engine = engine
        self.expire_date = expire_date
        self.expired = expired
        self.id = id
        self.kind_code = kind_code
        self.ltsversions = ltsversions
        self.latest_minor_version = latest_minor_version
        self.lock_mode = lock_mode
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.minor_version = minor_version
        self.network = network
        self.pay_type = pay_type
        self.port = port
        # 主可用区。
        self.primary_zone = primary_zone
        self.read_dbinstances = read_dbinstances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.rights_separation_enabled = rights_separation_enabled
        self.rights_separation_status = rights_separation_status
        # 次可用区。
        self.secondary_zone = secondary_zone
        self.series = series
        self.status = status
        self.storage_used = storage_used
        self.tag_set = tag_set
        # 第三可用区。
        self.tertiary_zone = tertiary_zone
        # 拓扑类型：
        # 
        # - **3azones**：三可用区；
        # - **1azone**：单可用区。
        self.topology_type = topology_type
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()
        if self.tag_set:
            for k in self.tag_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_not_create_columnar is not None:
            result['CanNotCreateColumnar'] = self.can_not_create_columnar
        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code
        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count
        if self.columnar_instance_name is not None:
            result['ColumnarInstanceName'] = self.columnar_instance_name
        if self.columnar_read_dbinstances is not None:
            result['ColumnarReadDBInstances'] = self.columnar_read_dbinstances
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.different_dnspec is not None:
            result['DifferentDNSpec'] = self.different_dnspec
        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code
        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.ltsversions is not None:
            result['LTSVersions'] = self.ltsversions
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rights_separation_enabled is not None:
            result['RightsSeparationEnabled'] = self.rights_separation_enabled
        if self.rights_separation_status is not None:
            result['RightsSeparationStatus'] = self.rights_separation_status
        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        result['TagSet'] = []
        if self.tag_set is not None:
            for k in self.tag_set:
                result['TagSet'].append(k.to_map() if k else None)
        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone
        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanNotCreateColumnar') is not None:
            self.can_not_create_columnar = m.get('CanNotCreateColumnar')
        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')
        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')
        if m.get('ColumnarInstanceName') is not None:
            self.columnar_instance_name = m.get('ColumnarInstanceName')
        if m.get('ColumnarReadDBInstances') is not None:
            self.columnar_read_dbinstances = m.get('ColumnarReadDBInstances')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DifferentDNSpec') is not None:
            self.different_dnspec = m.get('DifferentDNSpec')
        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')
        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LTSVersions') is not None:
            self.ltsversions = m.get('LTSVersions')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RightsSeparationEnabled') is not None:
            self.rights_separation_enabled = m.get('RightsSeparationEnabled')
        if m.get('RightsSeparationStatus') is not None:
            self.rights_separation_status = m.get('RightsSeparationStatus')
        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        self.tag_set = []
        if m.get('TagSet') is not None:
            for k in m.get('TagSet'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBInstanceTagSet()
                self.tag_set.append(temp_model.from_map(k))
        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')
        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance: DescribeDBInstanceAttributeResponseBodyDBInstance = None,
        request_id: str = None,
    ):
        self.dbinstance = dbinstance
        self.request_id = request_id

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstance') is not None:
            temp_model = DescribeDBInstanceAttributeResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
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
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.config_name = config_name
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        config_value: str = None,
        db_instance_name: str = None,
    ):
        self.config_name = config_name
        self.config_value = config_value
        self.db_instance_name = db_instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        return self


class DescribeDBInstanceConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceConfigResponseBody = None,
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
            temp_model = DescribeDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceHARequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceHAResponseBodyData(TeaModel):
    def __init__(
        self,
        primary_azone_id: str = None,
        primary_region_id: str = None,
        secondary_azone_id: str = None,
        secondary_region_id: str = None,
        topology_type: str = None,
    ):
        self.primary_azone_id = primary_azone_id
        self.primary_region_id = primary_region_id
        self.secondary_azone_id = secondary_azone_id
        self.secondary_region_id = secondary_region_id
        self.topology_type = topology_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary_azone_id is not None:
            result['PrimaryAzoneId'] = self.primary_azone_id
        if self.primary_region_id is not None:
            result['PrimaryRegionId'] = self.primary_region_id
        if self.secondary_azone_id is not None:
            result['SecondaryAzoneId'] = self.secondary_azone_id
        if self.secondary_region_id is not None:
            result['SecondaryRegionId'] = self.secondary_region_id
        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryAzoneId') is not None:
            self.primary_azone_id = m.get('PrimaryAzoneId')
        if m.get('PrimaryRegionId') is not None:
            self.primary_region_id = m.get('PrimaryRegionId')
        if m.get('SecondaryAzoneId') is not None:
            self.secondary_azone_id = m.get('SecondaryAzoneId')
        if m.get('SecondaryRegionId') is not None:
            self.secondary_region_id = m.get('SecondaryRegionId')
        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')
        return self


class DescribeDBInstanceHAResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceHAResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceHAResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDBInstanceHAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceHAResponseBody = None,
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
            temp_model = DescribeDBInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceSSLResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_common_name: str = None,
        sslenabled: bool = None,
        sslexpired_time: str = None,
    ):
        self.cert_common_name = cert_common_name
        self.sslenabled = sslenabled
        self.sslexpired_time = sslexpired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled
        if self.sslexpired_time is not None:
            result['SSLExpiredTime'] = self.sslexpired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')
        if m.get('SSLExpiredTime') is not None:
            self.sslexpired_time = m.get('SSLExpiredTime')
        return self


class DescribeDBInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceSSLResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceSSLResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceSSLResponseBody = None,
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
            temp_model = DescribeDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceTDERequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceTDEResponseBodyData(TeaModel):
    def __init__(
        self,
        tdestatus: str = None,
    ):
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class DescribeDBInstanceTDEResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceTDEResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceTDEResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceTDEResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceTDEResponseBody = None,
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
            temp_model = DescribeDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceTopologyRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        end_time: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.end_time = end_time
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems(TeaModel):
    def __init__(
        self,
        activated: bool = None,
        azone: str = None,
        character_type: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        phy_instance_name: str = None,
        region: str = None,
        role: str = None,
    ):
        self.activated = activated
        self.azone = azone
        self.character_type = character_type
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.phy_instance_name = phy_instance_name
        self.region = region
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activated is not None:
            result['Activated'] = self.activated
        if self.azone is not None:
            result['Azone'] = self.azone
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.phy_instance_name is not None:
            result['PhyInstanceName'] = self.phy_instance_name
        if self.region is not None:
            result['Region'] = self.region
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('PhyInstanceName') is not None:
            self.phy_instance_name = m.get('PhyInstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList(TeaModel):
    def __init__(
        self,
        azone: str = None,
        role: str = None,
    ):
        self.azone = azone
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.azone is not None:
            result['Azone'] = self.azone
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_net_type: int = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.dbinstance_net_type = dbinstance_net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems(TeaModel):
    def __init__(
        self,
        activated: bool = None,
        azone: str = None,
        azone_role_list: List[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList] = None,
        character_type: str = None,
        connection_ip: List[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp] = None,
        dbinstance_conn_type: int = None,
        dbinstance_create_time: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        dbinstance_status: int = None,
        dbinstance_status_description: str = None,
        disk_size: int = None,
        engine: str = None,
        engine_version: str = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        max_connections: int = None,
        max_iops: int = None,
        node_class: str = None,
        phy_instance_name: str = None,
        region: str = None,
        role: str = None,
        status: str = None,
        version: str = None,
    ):
        self.activated = activated
        self.azone = azone
        self.azone_role_list = azone_role_list
        self.character_type = character_type
        self.connection_ip = connection_ip
        self.dbinstance_conn_type = dbinstance_conn_type
        self.dbinstance_create_time = dbinstance_create_time
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.dbinstance_status = dbinstance_status
        self.dbinstance_status_description = dbinstance_status_description
        self.disk_size = disk_size
        self.engine = engine
        self.engine_version = engine_version
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.max_connections = max_connections
        self.max_iops = max_iops
        self.node_class = node_class
        self.phy_instance_name = phy_instance_name
        self.region = region
        self.role = role
        self.status = status
        self.version = version

    def validate(self):
        if self.azone_role_list:
            for k in self.azone_role_list:
                if k:
                    k.validate()
        if self.connection_ip:
            for k in self.connection_ip:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activated is not None:
            result['Activated'] = self.activated
        if self.azone is not None:
            result['Azone'] = self.azone
        result['AzoneRoleList'] = []
        if self.azone_role_list is not None:
            for k in self.azone_role_list:
                result['AzoneRoleList'].append(k.to_map() if k else None)
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        result['ConnectionIp'] = []
        if self.connection_ip is not None:
            for k in self.connection_ip:
                result['ConnectionIp'].append(k.to_map() if k else None)
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type
        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections
        if self.max_iops is not None:
            result['MaxIops'] = self.max_iops
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.phy_instance_name is not None:
            result['PhyInstanceName'] = self.phy_instance_name
        if self.region is not None:
            result['Region'] = self.region
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')
        self.azone_role_list = []
        if m.get('AzoneRoleList') is not None:
            for k in m.get('AzoneRoleList'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsAzoneRoleList()
                self.azone_role_list.append(temp_model.from_map(k))
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        self.connection_ip = []
        if m.get('ConnectionIp') is not None:
            for k in m.get('ConnectionIp'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItemsConnectionIp()
                self.connection_ip.append(temp_model.from_map(k))
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')
        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')
        if m.get('MaxIops') is not None:
            self.max_iops = m.get('MaxIops')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('PhyInstanceName') is not None:
            self.phy_instance_name = m.get('PhyInstanceName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology(TeaModel):
    def __init__(
        self,
        dbinstance_conn_type: str = None,
        dbinstance_create_time: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_name: str = None,
        dbinstance_status: int = None,
        dbinstance_status_description: str = None,
        dbinstance_storage: int = None,
        engine: str = None,
        engine_version: str = None,
        history_items: List[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems] = None,
        items: List[DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems] = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
    ):
        self.dbinstance_conn_type = dbinstance_conn_type
        self.dbinstance_create_time = dbinstance_create_time
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_name = dbinstance_name
        self.dbinstance_status = dbinstance_status
        self.dbinstance_status_description = dbinstance_status_description
        self.dbinstance_storage = dbinstance_storage
        self.engine = engine
        self.engine_version = engine_version
        self.history_items = history_items
        self.items = items
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time

    def validate(self):
        if self.history_items:
            for k in self.history_items:
                if k:
                    k.validate()
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_conn_type is not None:
            result['DBInstanceConnType'] = self.dbinstance_conn_type
        if self.dbinstance_create_time is not None:
            result['DBInstanceCreateTime'] = self.dbinstance_create_time
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.dbinstance_status_description is not None:
            result['DBInstanceStatusDescription'] = self.dbinstance_status_description
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        result['HistoryItems'] = []
        if self.history_items is not None:
            for k in self.history_items:
                result['HistoryItems'].append(k.to_map() if k else None)
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceConnType') is not None:
            self.dbinstance_conn_type = m.get('DBInstanceConnType')
        if m.get('DBInstanceCreateTime') is not None:
            self.dbinstance_create_time = m.get('DBInstanceCreateTime')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('DBInstanceStatusDescription') is not None:
            self.dbinstance_status_description = m.get('DBInstanceStatusDescription')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k in m.get('HistoryItems'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyHistoryItems()
                self.history_items.append(temp_model.from_map(k))
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopologyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        return self


class DescribeDBInstanceTopologyResponseBodyData(TeaModel):
    def __init__(
        self,
        logic_instance_topology: DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology = None,
    ):
        self.logic_instance_topology = logic_instance_topology

    def validate(self):
        if self.logic_instance_topology:
            self.logic_instance_topology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic_instance_topology is not None:
            result['LogicInstanceTopology'] = self.logic_instance_topology.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicInstanceTopology') is not None:
            temp_model = DescribeDBInstanceTopologyResponseBodyDataLogicInstanceTopology()
            self.logic_instance_topology = temp_model.from_map(m['LogicInstanceTopology'])
        return self


class DescribeDBInstanceTopologyResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDBInstanceTopologyResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDBInstanceTopologyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceTopologyResponseBody = None,
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
            temp_model = DescribeDBInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceViaEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        port: int = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        vpc_instance_id: str = None,
    ):
        self.connection_string = connection_string
        self.port = port
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes(TeaModel):
    def __init__(
        self,
        compute_node_id: str = None,
        data_node_id: str = None,
        id: str = None,
        node_class: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.compute_node_id = compute_node_id
        self.data_node_id = data_node_id
        self.id = id
        self.node_class = node_class
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_node_id is not None:
            result['ComputeNodeId'] = self.compute_node_id
        if self.data_node_id is not None:
            result['DataNodeId'] = self.data_node_id
        if self.id is not None:
            result['Id'] = self.id
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeNodeId') is not None:
            self.compute_node_id = m.get('ComputeNodeId')
        if m.get('DataNodeId') is not None:
            self.data_node_id = m.get('DataNodeId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstanceViaEndpointResponseBodyDBInstance(TeaModel):
    def __init__(
        self,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        commodity_code: str = None,
        conn_addrs: List[DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs] = None,
        connection_string: str = None,
        create_time: str = None,
        dbinstance_type: str = None,
        dbnode_class: str = None,
        dbnode_count: int = None,
        dbnodes: List[DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes] = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        engine: str = None,
        expire_date: str = None,
        expired: str = None,
        id: str = None,
        kind_code: int = None,
        ltsversions: List[str] = None,
        latest_minor_version: str = None,
        lock_mode: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        minor_version: str = None,
        network: str = None,
        pay_type: str = None,
        port: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        rights_separation_enabled: bool = None,
        rights_separation_status: str = None,
        series: str = None,
        status: str = None,
        storage_used: int = None,
        tag_set: List[DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet] = None,
        type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.commodity_code = commodity_code
        self.conn_addrs = conn_addrs
        self.connection_string = connection_string
        self.create_time = create_time
        self.dbinstance_type = dbinstance_type
        self.dbnode_class = dbnode_class
        self.dbnode_count = dbnode_count
        self.dbnodes = dbnodes
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.description = description
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.engine = engine
        self.expire_date = expire_date
        self.expired = expired
        self.id = id
        self.kind_code = kind_code
        self.ltsversions = ltsversions
        self.latest_minor_version = latest_minor_version
        self.lock_mode = lock_mode
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.minor_version = minor_version
        self.network = network
        self.pay_type = pay_type
        self.port = port
        self.read_dbinstances = read_dbinstances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.rights_separation_enabled = rights_separation_enabled
        self.rights_separation_status = rights_separation_status
        self.series = series
        self.status = status
        self.storage_used = storage_used
        self.tag_set = tag_set
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.conn_addrs:
            for k in self.conn_addrs:
                if k:
                    k.validate()
        if self.dbnodes:
            for k in self.dbnodes:
                if k:
                    k.validate()
        if self.tag_set:
            for k in self.tag_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code
        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        result['ConnAddrs'] = []
        if self.conn_addrs is not None:
            for k in self.conn_addrs:
                result['ConnAddrs'].append(k.to_map() if k else None)
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class
        if self.dbnode_count is not None:
            result['DBNodeCount'] = self.dbnode_count
        result['DBNodes'] = []
        if self.dbnodes is not None:
            for k in self.dbnodes:
                result['DBNodes'].append(k.to_map() if k else None)
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code
        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.kind_code is not None:
            result['KindCode'] = self.kind_code
        if self.ltsversions is not None:
            result['LTSVersions'] = self.ltsversions
        if self.latest_minor_version is not None:
            result['LatestMinorVersion'] = self.latest_minor_version
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.port is not None:
            result['Port'] = self.port
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rights_separation_enabled is not None:
            result['RightsSeparationEnabled'] = self.rights_separation_enabled
        if self.rights_separation_status is not None:
            result['RightsSeparationStatus'] = self.rights_separation_status
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        result['TagSet'] = []
        if self.tag_set is not None:
            for k in self.tag_set:
                result['TagSet'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')
        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        self.conn_addrs = []
        if m.get('ConnAddrs') is not None:
            for k in m.get('ConnAddrs'):
                temp_model = DescribeDBInstanceViaEndpointResponseBodyDBInstanceConnAddrs()
                self.conn_addrs.append(temp_model.from_map(k))
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')
        if m.get('DBNodeCount') is not None:
            self.dbnode_count = m.get('DBNodeCount')
        self.dbnodes = []
        if m.get('DBNodes') is not None:
            for k in m.get('DBNodes'):
                temp_model = DescribeDBInstanceViaEndpointResponseBodyDBInstanceDBNodes()
                self.dbnodes.append(temp_model.from_map(k))
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')
        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KindCode') is not None:
            self.kind_code = m.get('KindCode')
        if m.get('LTSVersions') is not None:
            self.ltsversions = m.get('LTSVersions')
        if m.get('LatestMinorVersion') is not None:
            self.latest_minor_version = m.get('LatestMinorVersion')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RightsSeparationEnabled') is not None:
            self.rights_separation_enabled = m.get('RightsSeparationEnabled')
        if m.get('RightsSeparationStatus') is not None:
            self.rights_separation_status = m.get('RightsSeparationStatus')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        self.tag_set = []
        if m.get('TagSet') is not None:
            for k in m.get('TagSet'):
                temp_model = DescribeDBInstanceViaEndpointResponseBodyDBInstanceTagSet()
                self.tag_set.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceViaEndpointResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance: DescribeDBInstanceViaEndpointResponseBodyDBInstance = None,
        request_id: str = None,
    ):
        self.dbinstance = dbinstance
        self.request_id = request_id

    def validate(self):
        if self.dbinstance:
            self.dbinstance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance is not None:
            result['DBInstance'] = self.dbinstance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstance') is not None:
            temp_model = DescribeDBInstanceViaEndpointResponseBodyDBInstance()
            self.dbinstance = temp_model.from_map(m['DBInstance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceViaEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceViaEndpointResponseBody = None,
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
            temp_model = DescribeDBInstanceViaEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        must_has_cdc: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        series: str = None,
        tags: str = None,
    ):
        self.instance_id = instance_id
        self.must_has_cdc = must_has_cdc
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.series = series
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.must_has_cdc is not None:
            result['MustHasCdc'] = self.must_has_cdc
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.series is not None:
            result['Series'] = self.series
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MustHasCdc') is not None:
            self.must_has_cdc = m.get('MustHasCdc')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeDBInstancesResponseBodyDBInstancesNodes(TeaModel):
    def __init__(
        self,
        class_code: str = None,
        id: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.class_code = class_code
        self.id = id
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBodyDBInstancesTagSet(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesResponseBodyDBInstances(TeaModel):
    def __init__(
        self,
        cdc_instance_name: str = None,
        cn_node_class_code: str = None,
        cn_node_count: int = None,
        columnar_instance_name: str = None,
        columnar_read_dbinstances: List[str] = None,
        commodity_code: str = None,
        contain_binlog_x: bool = None,
        create_time: str = None,
        dbinstance_name: str = None,
        dbtype: str = None,
        dbversion: str = None,
        description: str = None,
        dn_node_class_code: str = None,
        dn_node_count: int = None,
        engine: str = None,
        expire_time: str = None,
        expired: bool = None,
        id: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        minor_version: str = None,
        network: str = None,
        node_class: str = None,
        node_count: int = None,
        nodes: List[DescribeDBInstancesResponseBodyDBInstancesNodes] = None,
        pay_type: str = None,
        primary_zone: str = None,
        read_dbinstances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        secondary_zone: str = None,
        series: str = None,
        status: str = None,
        storage_used: int = None,
        support_binlog_x: bool = None,
        tag_set: List[DescribeDBInstancesResponseBodyDBInstancesTagSet] = None,
        tertiary_zone: str = None,
        topology_type: str = None,
        type: str = None,
        vpcid: str = None,
        zone_id: str = None,
    ):
        self.cdc_instance_name = cdc_instance_name
        self.cn_node_class_code = cn_node_class_code
        self.cn_node_count = cn_node_count
        self.columnar_instance_name = columnar_instance_name
        self.columnar_read_dbinstances = columnar_read_dbinstances
        self.commodity_code = commodity_code
        self.contain_binlog_x = contain_binlog_x
        self.create_time = create_time
        self.dbinstance_name = dbinstance_name
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.description = description
        self.dn_node_class_code = dn_node_class_code
        self.dn_node_count = dn_node_count
        self.engine = engine
        self.expire_time = expire_time
        self.expired = expired
        self.id = id
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.minor_version = minor_version
        self.network = network
        self.node_class = node_class
        self.node_count = node_count
        self.nodes = nodes
        self.pay_type = pay_type
        # 主可用区。
        self.primary_zone = primary_zone
        self.read_dbinstances = read_dbinstances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # 次可用区。
        self.secondary_zone = secondary_zone
        self.series = series
        self.status = status
        self.storage_used = storage_used
        self.support_binlog_x = support_binlog_x
        self.tag_set = tag_set
        # 第三可用区。
        self.tertiary_zone = tertiary_zone
        # 拓扑类型：
        # 
        # - **3azones**：三可用区；
        # - **1azone**：单可用区。
        self.topology_type = topology_type
        self.type = type
        # VPC ID。
        self.vpcid = vpcid
        self.zone_id = zone_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.tag_set:
            for k in self.tag_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdc_instance_name is not None:
            result['CdcInstanceName'] = self.cdc_instance_name
        if self.cn_node_class_code is not None:
            result['CnNodeClassCode'] = self.cn_node_class_code
        if self.cn_node_count is not None:
            result['CnNodeCount'] = self.cn_node_count
        if self.columnar_instance_name is not None:
            result['ColumnarInstanceName'] = self.columnar_instance_name
        if self.columnar_read_dbinstances is not None:
            result['ColumnarReadDBInstances'] = self.columnar_read_dbinstances
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.contain_binlog_x is not None:
            result['ContainBinlogX'] = self.contain_binlog_x
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.description is not None:
            result['Description'] = self.description
        if self.dn_node_class_code is not None:
            result['DnNodeClassCode'] = self.dn_node_class_code
        if self.dn_node_count is not None:
            result['DnNodeCount'] = self.dn_node_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.id is not None:
            result['Id'] = self.id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.network is not None:
            result['Network'] = self.network
        if self.node_class is not None:
            result['NodeClass'] = self.node_class
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.read_dbinstances is not None:
            result['ReadDBInstances'] = self.read_dbinstances
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.secondary_zone is not None:
            result['SecondaryZone'] = self.secondary_zone
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.support_binlog_x is not None:
            result['SupportBinlogX'] = self.support_binlog_x
        result['TagSet'] = []
        if self.tag_set is not None:
            for k in self.tag_set:
                result['TagSet'].append(k.to_map() if k else None)
        if self.tertiary_zone is not None:
            result['TertiaryZone'] = self.tertiary_zone
        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type
        if self.type is not None:
            result['Type'] = self.type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdcInstanceName') is not None:
            self.cdc_instance_name = m.get('CdcInstanceName')
        if m.get('CnNodeClassCode') is not None:
            self.cn_node_class_code = m.get('CnNodeClassCode')
        if m.get('CnNodeCount') is not None:
            self.cn_node_count = m.get('CnNodeCount')
        if m.get('ColumnarInstanceName') is not None:
            self.columnar_instance_name = m.get('ColumnarInstanceName')
        if m.get('ColumnarReadDBInstances') is not None:
            self.columnar_read_dbinstances = m.get('ColumnarReadDBInstances')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ContainBinlogX') is not None:
            self.contain_binlog_x = m.get('ContainBinlogX')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnNodeClassCode') is not None:
            self.dn_node_class_code = m.get('DnNodeClassCode')
        if m.get('DnNodeCount') is not None:
            self.dn_node_count = m.get('DnNodeCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NodeClass') is not None:
            self.node_class = m.get('NodeClass')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('ReadDBInstances') is not None:
            self.read_dbinstances = m.get('ReadDBInstances')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondaryZone') is not None:
            self.secondary_zone = m.get('SecondaryZone')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('SupportBinlogX') is not None:
            self.support_binlog_x = m.get('SupportBinlogX')
        self.tag_set = []
        if m.get('TagSet') is not None:
            for k in m.get('TagSet'):
                temp_model = DescribeDBInstancesResponseBodyDBInstancesTagSet()
                self.tag_set.append(temp_model.from_map(k))
        if m.get('TertiaryZone') is not None:
            self.tertiary_zone = m.get('TertiaryZone')
        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        dbinstances: List[DescribeDBInstancesResponseBodyDBInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_number: int = None,
    ):
        self.dbinstances = dbinstances
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_number = total_number

    def validate(self):
        if self.dbinstances:
            for k in self.dbinstances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k in self.dbinstances:
                result['DBInstances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_number is not None:
            result['TotalNumber'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k in m.get('DBInstances'):
                temp_model = DescribeDBInstancesResponseBodyDBInstances()
                self.dbinstances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancesResponseBody = None,
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
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBNodePerformanceRequest(TeaModel):
    def __init__(
        self,
        character_type: str = None,
        dbinstance_name: str = None,
        dbnode_ids: str = None,
        dbnode_role: str = None,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.character_type = character_type
        self.dbinstance_name = dbinstance_name
        self.dbnode_ids = dbnode_ids
        self.dbnode_role = dbnode_role
        self.end_time = end_time
        self.key = key
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.character_type is not None:
            result['CharacterType'] = self.character_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbnode_ids is not None:
            result['DBNodeIds'] = self.dbnode_ids
        if self.dbnode_role is not None:
            result['DBNodeRole'] = self.dbnode_role
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key is not None:
            result['Key'] = self.key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBNodeIds') is not None:
            self.dbnode_ids = m.get('DBNodeIds')
        if m.get('DBNodeRole') is not None:
            self.dbnode_role = m.get('DBNodeRole')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
    ):
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints(TeaModel):
    def __init__(
        self,
        performance_item_value: List[DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue] = None,
    ):
        self.performance_item_value = performance_item_value

    def validate(self):
        if self.performance_item_value:
            for k in self.performance_item_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItemValue'] = []
        if self.performance_item_value is not None:
            for k in self.performance_item_value:
                result['PerformanceItemValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_item_value = []
        if m.get('PerformanceItemValue') is not None:
            for k in m.get('PerformanceItemValue'):
                temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPointsPerformanceItemValue()
                self.performance_item_value.append(temp_model.from_map(k))
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem(TeaModel):
    def __init__(
        self,
        dbnode_id: str = None,
        measurement: str = None,
        metric_name: str = None,
        points: DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints = None,
    ):
        self.dbnode_id = dbnode_id
        self.measurement = measurement
        self.metric_name = metric_name
        self.points = points

    def validate(self):
        if self.points:
            self.points.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id
        if self.measurement is not None:
            result['Measurement'] = self.measurement
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.points is not None:
            result['Points'] = self.points.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')
        if m.get('Measurement') is not None:
            self.measurement = m.get('Measurement')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Points') is not None:
            temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItemPoints()
            self.points = temp_model.from_map(m['Points'])
        return self


class DescribeDBNodePerformanceResponseBodyPerformanceKeys(TeaModel):
    def __init__(
        self,
        performance_item: List[DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem] = None,
    ):
        self.performance_item = performance_item

    def validate(self):
        if self.performance_item:
            for k in self.performance_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PerformanceItem'] = []
        if self.performance_item is not None:
            for k in self.performance_item:
                result['PerformanceItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_item = []
        if m.get('PerformanceItem') is not None:
            for k in m.get('PerformanceItem'):
                temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeysPerformanceItem()
                self.performance_item.append(temp_model.from_map(k))
        return self


class DescribeDBNodePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        end_time: str = None,
        performance_keys: DescribeDBNodePerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.end_time = end_time
        self.performance_keys = performance_keys
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PerformanceKeys') is not None:
            temp_model = DescribeDBNodePerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m['PerformanceKeys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBNodePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBNodePerformanceResponseBody = None,
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
            temp_model = DescribeDBNodePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDbListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbname: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDbListResponseBodyDataAccounts(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
    ):
        self.account_name = account_name
        self.account_privilege = account_privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        return self


class DescribeDbListResponseBodyData(TeaModel):
    def __init__(
        self,
        accounts: List[DescribeDbListResponseBodyDataAccounts] = None,
        character_set_name: str = None,
        dbdescription: str = None,
        dbinstance_name: str = None,
        dbname: str = None,
    ):
        self.accounts = accounts
        self.character_set_name = character_set_name
        self.dbdescription = dbdescription
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname

    def validate(self):
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name
        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbname is not None:
            result['DBName'] = self.dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k in m.get('Accounts'):
                temp_model = DescribeDbListResponseBodyDataAccounts()
                self.accounts.append(temp_model.from_map(k))
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')
        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        return self


class DescribeDbListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeDbListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = DescribeDbListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDbListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDbListResponseBody = None,
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
            temp_model = DescribeDbListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDistributeTableListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        db_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDistributeTableListResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        db_key: str = None,
        table_name: str = None,
        table_type: str = None,
        tb_key: str = None,
    ):
        self.db_key = db_key
        self.table_name = table_name
        self.table_type = table_type
        self.tb_key = tb_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_key is not None:
            result['DbKey'] = self.db_key
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.tb_key is not None:
            result['TbKey'] = self.tb_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbKey') is not None:
            self.db_key = m.get('DbKey')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TbKey') is not None:
            self.tb_key = m.get('TbKey')
        return self


class DescribeDistributeTableListResponseBodyData(TeaModel):
    def __init__(
        self,
        tables: List[DescribeDistributeTableListResponseBodyDataTables] = None,
    ):
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeDistributeTableListResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class DescribeDistributeTableListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeDistributeTableListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeDistributeTableListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDistributeTableListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDistributeTableListResponseBody = None,
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
            temp_model = DescribeDistributeTableListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeEventsResponseBodyEventItems(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        event_name: str = None,
        event_payload: str = None,
        event_reason: str = None,
        event_record_time: str = None,
        event_time: str = None,
        event_type: str = None,
        event_user_type: str = None,
        region_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.event_id = event_id
        self.event_name = event_name
        self.event_payload = event_payload
        self.event_reason = event_reason
        self.event_record_time = event_record_time
        self.event_time = event_time
        self.event_type = event_type
        self.event_user_type = event_user_type
        self.region_id = region_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_payload is not None:
            result['EventPayload'] = self.event_payload
        if self.event_reason is not None:
            result['EventReason'] = self.event_reason
        if self.event_record_time is not None:
            result['EventRecordTime'] = self.event_record_time
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.event_user_type is not None:
            result['EventUserType'] = self.event_user_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventPayload') is not None:
            self.event_payload = m.get('EventPayload')
        if m.get('EventReason') is not None:
            self.event_reason = m.get('EventReason')
        if m.get('EventRecordTime') is not None:
            self.event_record_time = m.get('EventRecordTime')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EventUserType') is not None:
            self.event_user_type = m.get('EventUserType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(
        self,
        event_items: List[DescribeEventsResponseBodyEventItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.event_items = event_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.event_items:
            for k in self.event_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventItems'] = []
        if self.event_items is not None:
            for k in self.event_items:
                result['EventItems'].append(k.to_map() if k else None)
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
        self.event_items = []
        if m.get('EventItems') is not None:
            for k in m.get('EventItems'):
                temp_model = DescribeEventsResponseBodyEventItems()
                self.event_items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventsResponseBody = None,
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
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        param_level: str = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.param_level = param_level
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeParameterTemplatesResponseBodyDataParameters(TeaModel):
    def __init__(
        self,
        checking_code: str = None,
        dynamic: int = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        revisable: int = None,
    ):
        self.checking_code = checking_code
        self.dynamic = dynamic
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.revisable = revisable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        if self.revisable is not None:
            result['Revisable'] = self.revisable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        if m.get('Revisable') is not None:
            self.revisable = m.get('Revisable')
        return self


class DescribeParameterTemplatesResponseBodyData(TeaModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        parameter_count: int = None,
        parameters: List[DescribeParameterTemplatesResponseBodyDataParameters] = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.parameter_count = parameter_count
        self.parameters = parameters

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParameterTemplatesResponseBodyDataParameters()
                self.parameters.append(temp_model.from_map(k))
        return self


class DescribeParameterTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeParameterTemplatesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeParameterTemplatesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParameterTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeParameterTemplatesResponseBody = None,
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
            temp_model = DescribeParameterTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        param_level: str = None,
        region_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.param_level = param_level
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeParametersResponseBodyDataConfigParameters(TeaModel):
    def __init__(
        self,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyDataRunningParameters(TeaModel):
    def __init__(
        self,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeParametersResponseBodyData(TeaModel):
    def __init__(
        self,
        config_parameters: List[DescribeParametersResponseBodyDataConfigParameters] = None,
        engine: str = None,
        engine_version: str = None,
        running_parameters: List[DescribeParametersResponseBodyDataRunningParameters] = None,
    ):
        self.config_parameters = config_parameters
        self.engine = engine
        self.engine_version = engine_version
        self.running_parameters = running_parameters

    def validate(self):
        if self.config_parameters:
            for k in self.config_parameters:
                if k:
                    k.validate()
        if self.running_parameters:
            for k in self.running_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigParameters'] = []
        if self.config_parameters is not None:
            for k in self.config_parameters:
                result['ConfigParameters'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k in self.running_parameters:
                result['RunningParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_parameters = []
        if m.get('ConfigParameters') is not None:
            for k in m.get('ConfigParameters'):
                temp_model = DescribeParametersResponseBodyDataConfigParameters()
                self.config_parameters.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k in m.get('RunningParameters'):
                temp_model = DescribeParametersResponseBodyDataRunningParameters()
                self.running_parameters.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeParametersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeParametersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeParametersResponseBody = None,
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
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        self.vpc_enabled = vpc_enabled
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        support_polarx_10: bool = None,
        support_polarx_20: bool = None,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        self.region_id = region_id
        self.support_polarx_10 = support_polarx_10
        self.support_polarx_20 = support_polarx_20
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.support_polarx_10 is not None:
            result['SupportPolarx10'] = self.support_polarx_10
        if self.support_polarx_20 is not None:
            result['SupportPolarx20'] = self.support_polarx_20
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportPolarx10') is not None:
            self.support_polarx_10 = m.get('SupportPolarx10')
        if m.get('SupportPolarx20') is not None:
            self.support_polarx_20 = m.get('SupportPolarx20')
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        error_code: int = None,
        message: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScaleOutMigrateTaskListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeScaleOutMigrateTaskListResponseBody(TeaModel):
    def __init__(
        self,
        progress: int = None,
        request_id: str = None,
    ):
        self.progress = progress
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeScaleOutMigrateTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScaleOutMigrateTaskListResponseBody = None,
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
            temp_model = DescribeScaleOutMigrateTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSecurityIpsResponseBodyDataGroupItems(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        security_iplist: str = None,
    ):
        self.group_name = group_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class DescribeSecurityIpsResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_items: List[DescribeSecurityIpsResponseBodyDataGroupItems] = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.group_items = group_items

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIpsResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k))
        return self


class DescribeSecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeSecurityIpsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeSecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityIpsResponseBody = None,
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
            temp_model = DescribeSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        tag_key: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeTagsResponseBodyTagInfos(TeaModel):
    def __init__(
        self,
        dbinstance_ids: List[str] = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.dbinstance_ids = dbinstance_ids
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_infos: List[DescribeTagsResponseBodyTagInfos] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.tag_infos = tag_infos

    def validate(self):
        if self.tag_infos:
            for k in self.tag_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagInfos'] = []
        if self.tag_infos is not None:
            for k in self.tag_infos:
                result['TagInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_infos = []
        if m.get('TagInfos') is not None:
            for k in m.get('TagInfos'):
                temp_model = DescribeTagsResponseBodyTagInfos()
                self.tag_infos.append(temp_model.from_map(k))
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTagsResponseBody = None,
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
            temp_model = DescribeTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTasksResponseBodyItems(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        dbname: str = None,
        finish_time: str = None,
        progress: str = None,
        progress_info: str = None,
        scale_out_token: str = None,
        status: str = None,
        task_action: str = None,
        task_error_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
    ):
        self.begin_time = begin_time
        self.dbname = dbname
        self.finish_time = finish_time
        self.progress = progress
        self.progress_info = progress_info
        self.scale_out_token = scale_out_token
        self.status = status
        self.task_action = task_action
        self.task_error_code = task_error_code
        self.task_error_message = task_error_message
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.progress_info is not None:
            result['ProgressInfo'] = self.progress_info
        if self.scale_out_token is not None:
            result['ScaleOutToken'] = self.scale_out_token
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_error_code is not None:
            result['TaskErrorCode'] = self.task_error_code
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProgressInfo') is not None:
            self.progress_info = m.get('ProgressInfo')
        if m.get('ScaleOutToken') is not None:
            self.scale_out_token = m.get('ScaleOutToken')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeTasksResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserEncryptionKeyListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserEncryptionKeyListResponseBodyData(TeaModel):
    def __init__(
        self,
        key_ids: List[str] = None,
    ):
        self.key_ids = key_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')
        return self


class DescribeUserEncryptionKeyListResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeUserEncryptionKeyListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeUserEncryptionKeyListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserEncryptionKeyListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserEncryptionKeyListResponseBody = None,
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
            temp_model = DescribeUserEncryptionKeyListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRightsSeparationRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dba_account_name: str = None,
        dba_account_password: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.dba_account_name = dba_account_name
        self.dba_account_password = dba_account_password
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dba_account_name is not None:
            result['DbaAccountName'] = self.dba_account_name
        if self.dba_account_password is not None:
            result['DbaAccountPassword'] = self.dba_account_password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbaAccountName') is not None:
            self.dba_account_name = m.get('DbaAccountName')
        if m.get('DbaAccountPassword') is not None:
            self.dba_account_password = m.get('DbaAccountPassword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableRightsSeparationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableRightsSeparationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableRightsSeparationResponseBody = None,
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
            temp_model = DisableRightsSeparationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableRightsSeparationRequest(TeaModel):
    def __init__(
        self,
        audit_account_description: str = None,
        audit_account_name: str = None,
        audit_account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_description: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.audit_account_description = audit_account_description
        self.audit_account_name = audit_account_name
        self.audit_account_password = audit_account_password
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.security_account_description = security_account_description
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_account_description is not None:
            result['AuditAccountDescription'] = self.audit_account_description
        if self.audit_account_name is not None:
            result['AuditAccountName'] = self.audit_account_name
        if self.audit_account_password is not None:
            result['AuditAccountPassword'] = self.audit_account_password
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_description is not None:
            result['SecurityAccountDescription'] = self.security_account_description
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAccountDescription') is not None:
            self.audit_account_description = m.get('AuditAccountDescription')
        if m.get('AuditAccountName') is not None:
            self.audit_account_name = m.get('AuditAccountName')
        if m.get('AuditAccountPassword') is not None:
            self.audit_account_password = m.get('AuditAccountPassword')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountDescription') is not None:
            self.security_account_description = m.get('SecurityAccountDescription')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class EnableRightsSeparationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableRightsSeparationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableRightsSeparationResponseBody = None,
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
            temp_model = EnableRightsSeparationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyAccountDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountDescriptionResponseBody = None,
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
            temp_model = ModifyAccountDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccountPrivilegeRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        dbinstance_name: str = None,
        db_name: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.account_name = account_name
        self.account_privilege = account_privilege
        self.dbinstance_name = dbinstance_name
        self.db_name = db_name
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class ModifyAccountPrivilegeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAccountPrivilegeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccountPrivilegeResponseBody = None,
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
            temp_model = ModifyAccountPrivilegeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyActiveOperationMaintainConfRequest(TeaModel):
    def __init__(
        self,
        cycle_time: str = None,
        cycle_type: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        region_id: str = None,
        status: int = None,
    ):
        self.cycle_time = cycle_time
        self.cycle_type = cycle_type
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_time is not None:
            result['CycleTime'] = self.cycle_time
        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleTime') is not None:
            self.cycle_time = m.get('CycleTime')
        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyActiveOperationMaintainConfResponseBody(TeaModel):
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


class ModifyActiveOperationMaintainConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyActiveOperationMaintainConfResponseBody = None,
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
            temp_model = ModifyActiveOperationMaintainConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyActiveOperationTasksRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        immediate_start: int = None,
        region_id: str = None,
        switch_time: str = None,
    ):
        self.ids = ids
        self.immediate_start = immediate_start
        self.region_id = region_id
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.immediate_start is not None:
            result['ImmediateStart'] = self.immediate_start
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ImmediateStart') is not None:
            self.immediate_start = m.get('ImmediateStart')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class ModifyActiveOperationTasksResponseBody(TeaModel):
    def __init__(
        self,
        ids: str = None,
        request_id: str = None,
    ):
        self.ids = ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyActiveOperationTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyActiveOperationTasksResponseBody = None,
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
            temp_model = ModifyActiveOperationTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cn_class: str = None,
        dbinstance_name: str = None,
        dn_class: str = None,
        region_id: str = None,
        target_dbinstance_class: str = None,
    ):
        self.client_token = client_token
        self.cn_class = cn_class
        self.dbinstance_name = dbinstance_name
        self.dn_class = dn_class
        self.region_id = region_id
        self.target_dbinstance_class = target_dbinstance_class

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cn_class is not None:
            result['CnClass'] = self.cn_class
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dn_class is not None:
            result['DnClass'] = self.dn_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CnClass') is not None:
            self.cn_class = m.get('CnClass')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DnClass') is not None:
            self.dn_class = m.get('DnClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')
        return self


class ModifyDBInstanceClassResponseBody(TeaModel):
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


class ModifyDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceClassResponseBody = None,
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
            temp_model = ModifyDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConfigRequest(TeaModel):
    def __init__(
        self,
        config_name: str = None,
        config_value: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.config_name = config_name
        self.config_value = config_value
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceConfigResponseBody(TeaModel):
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


class ModifyDBInstanceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConfigResponseBody = None,
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
            temp_model = ModifyDBInstanceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_name: str = None,
        new_port: str = None,
        new_prefix: str = None,
        region_id: str = None,
    ):
        self.connection_string = connection_string
        self.dbinstance_name = dbinstance_name
        self.new_port = new_port
        self.new_prefix = new_prefix
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.new_port is not None:
            result['NewPort'] = self.new_port
        if self.new_prefix is not None:
            result['NewPrefix'] = self.new_prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('NewPort') is not None:
            self.new_port = m.get('NewPort')
        if m.get('NewPrefix') is not None:
            self.new_prefix = m.get('NewPrefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceConnectionStringResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_name: str = None,
        dbinstance_net_type: str = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.dbinstance_name = dbinstance_name
        self.dbinstance_net_type = dbinstance_net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyDBInstanceConnectionStringResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ModifyDBInstanceConnectionStringResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ModifyDBInstanceConnectionStringResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceConnectionStringResponseBody = None,
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
            temp_model = ModifyDBInstanceConnectionStringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_description = dbinstance_description
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDBInstanceDescriptionResponseBody(TeaModel):
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


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceDescriptionResponseBody = None,
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
            temp_model = ModifyDBInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseDescriptionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        db_description: str = None,
        db_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.db_description = db_description
        self.db_name = db_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDatabaseDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDatabaseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseDescriptionResponseBody = None,
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
            temp_model = ModifyDatabaseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        param_level: str = None,
        parameters: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dbinstance_id = dbinstance_id
        self.param_level = param_level
        self.parameters = parameters
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.param_level is not None:
            result['ParamLevel'] = self.param_level
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyParameterResponseBody(TeaModel):
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


class ModifyParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyParameterResponseBody = None,
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
            temp_model = ModifyParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_name: str = None,
        modify_mode: str = None,
        region_id: str = None,
        security_iplist: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.group_name = group_name
        self.modify_mode = modify_mode
        self.region_id = region_id
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecurityIpsResponseBody = None,
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
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseColdDataVolumeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleaseColdDataVolumeResponseBody(TeaModel):
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


class ReleaseColdDataVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseColdDataVolumeResponseBody = None,
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
            temp_model = ReleaseColdDataVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        current_connection_string: str = None,
        dbinstance_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.current_connection_string = current_connection_string
        self.dbinstance_name = dbinstance_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
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


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstancePublicConnectionResponseBody = None,
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
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.account_name = account_name
        self.account_password = account_password
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name
        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')
        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestartDBInstanceResponseBody(TeaModel):
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


class RestartDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDBInstanceResponseBody = None,
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
            temp_model = RestartDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchDBInstanceHARequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_primary_azone_id: str = None,
        target_primary_region_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode
        self.target_primary_azone_id = target_primary_azone_id
        self.target_primary_region_id = target_primary_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.target_primary_azone_id is not None:
            result['TargetPrimaryAzoneId'] = self.target_primary_azone_id
        if self.target_primary_region_id is not None:
            result['TargetPrimaryRegionId'] = self.target_primary_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('TargetPrimaryAzoneId') is not None:
            self.target_primary_azone_id = m.get('TargetPrimaryAzoneId')
        if m.get('TargetPrimaryRegionId') is not None:
            self.target_primary_region_id = m.get('TargetPrimaryRegionId')
        return self


class SwitchDBInstanceHAResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SwitchDBInstanceHAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchDBInstanceHAResponseBody = None,
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
            temp_model = SwitchDBInstanceHAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # requestId
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # RequestId
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        backup_period: str = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        backup_type: str = None,
        backup_way: str = None,
        cold_data_backup_interval: int = None,
        cold_data_backup_retention: int = None,
        cross_region_data_backup_retention: int = None,
        cross_region_log_backup_retention: int = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        force_clean_on_high_space_usage: int = None,
        is_cross_region_data_backup_enabled: bool = None,
        is_cross_region_log_backup_enabled: bool = None,
        is_enabled: int = None,
        local_log_retention: int = None,
        local_log_retention_number: int = None,
        log_local_retention_space: int = None,
        region_id: str = None,
        remove_log_retention: int = None,
    ):
        self.backup_period = backup_period
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.backup_type = backup_type
        self.backup_way = backup_way
        self.cold_data_backup_interval = cold_data_backup_interval
        self.cold_data_backup_retention = cold_data_backup_retention
        self.cross_region_data_backup_retention = cross_region_data_backup_retention
        self.cross_region_log_backup_retention = cross_region_log_backup_retention
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.is_cross_region_data_backup_enabled = is_cross_region_data_backup_enabled
        self.is_cross_region_log_backup_enabled = is_cross_region_log_backup_enabled
        self.is_enabled = is_enabled
        self.local_log_retention = local_log_retention
        self.local_log_retention_number = local_log_retention_number
        self.log_local_retention_space = log_local_retention_space
        self.region_id = region_id
        self.remove_log_retention = remove_log_retention

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.cold_data_backup_interval is not None:
            result['ColdDataBackupInterval'] = self.cold_data_backup_interval
        if self.cold_data_backup_retention is not None:
            result['ColdDataBackupRetention'] = self.cold_data_backup_retention
        if self.cross_region_data_backup_retention is not None:
            result['CrossRegionDataBackupRetention'] = self.cross_region_data_backup_retention
        if self.cross_region_log_backup_retention is not None:
            result['CrossRegionLogBackupRetention'] = self.cross_region_log_backup_retention
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_cross_region_data_backup_enabled is not None:
            result['IsCrossRegionDataBackupEnabled'] = self.is_cross_region_data_backup_enabled
        if self.is_cross_region_log_backup_enabled is not None:
            result['IsCrossRegionLogBackupEnabled'] = self.is_cross_region_log_backup_enabled
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.local_log_retention_number is not None:
            result['LocalLogRetentionNumber'] = self.local_log_retention_number
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('ColdDataBackupInterval') is not None:
            self.cold_data_backup_interval = m.get('ColdDataBackupInterval')
        if m.get('ColdDataBackupRetention') is not None:
            self.cold_data_backup_retention = m.get('ColdDataBackupRetention')
        if m.get('CrossRegionDataBackupRetention') is not None:
            self.cross_region_data_backup_retention = m.get('CrossRegionDataBackupRetention')
        if m.get('CrossRegionLogBackupRetention') is not None:
            self.cross_region_log_backup_retention = m.get('CrossRegionLogBackupRetention')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsCrossRegionDataBackupEnabled') is not None:
            self.is_cross_region_data_backup_enabled = m.get('IsCrossRegionDataBackupEnabled')
        if m.get('IsCrossRegionLogBackupEnabled') is not None:
            self.is_cross_region_log_backup_enabled = m.get('IsCrossRegionLogBackupEnabled')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LocalLogRetentionNumber') is not None:
            self.local_log_retention_number = m.get('LocalLogRetentionNumber')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class UpdateBackupPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        backup_period: str = None,
        backup_plan_begin: str = None,
        backup_set_retention: int = None,
        backup_type: str = None,
        backup_way: str = None,
        cold_data_backup_interval: int = None,
        cold_data_backup_retention: int = None,
        cross_region_data_backup_retention: int = None,
        cross_region_log_backup_retention: int = None,
        dbinstance_name: str = None,
        dest_cross_region: str = None,
        force_clean_on_high_space_usage: int = None,
        is_cross_region_data_backup_enabled: bool = None,
        is_cross_region_log_backup_enabled: bool = None,
        is_enabled: int = None,
        local_log_retention: int = None,
        local_log_retention_number: int = None,
        log_local_retention_space: int = None,
        remove_log_retention: int = None,
    ):
        self.backup_period = backup_period
        self.backup_plan_begin = backup_plan_begin
        self.backup_set_retention = backup_set_retention
        self.backup_type = backup_type
        self.backup_way = backup_way
        self.cold_data_backup_interval = cold_data_backup_interval
        self.cold_data_backup_retention = cold_data_backup_retention
        self.cross_region_data_backup_retention = cross_region_data_backup_retention
        self.cross_region_log_backup_retention = cross_region_log_backup_retention
        self.dbinstance_name = dbinstance_name
        self.dest_cross_region = dest_cross_region
        self.force_clean_on_high_space_usage = force_clean_on_high_space_usage
        self.is_cross_region_data_backup_enabled = is_cross_region_data_backup_enabled
        self.is_cross_region_log_backup_enabled = is_cross_region_log_backup_enabled
        self.is_enabled = is_enabled
        self.local_log_retention = local_log_retention
        self.local_log_retention_number = local_log_retention_number
        self.log_local_retention_space = log_local_retention_space
        self.remove_log_retention = remove_log_retention

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.backup_plan_begin is not None:
            result['BackupPlanBegin'] = self.backup_plan_begin
        if self.backup_set_retention is not None:
            result['BackupSetRetention'] = self.backup_set_retention
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_way is not None:
            result['BackupWay'] = self.backup_way
        if self.cold_data_backup_interval is not None:
            result['ColdDataBackupInterval'] = self.cold_data_backup_interval
        if self.cold_data_backup_retention is not None:
            result['ColdDataBackupRetention'] = self.cold_data_backup_retention
        if self.cross_region_data_backup_retention is not None:
            result['CrossRegionDataBackupRetention'] = self.cross_region_data_backup_retention
        if self.cross_region_log_backup_retention is not None:
            result['CrossRegionLogBackupRetention'] = self.cross_region_log_backup_retention
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dest_cross_region is not None:
            result['DestCrossRegion'] = self.dest_cross_region
        if self.force_clean_on_high_space_usage is not None:
            result['ForceCleanOnHighSpaceUsage'] = self.force_clean_on_high_space_usage
        if self.is_cross_region_data_backup_enabled is not None:
            result['IsCrossRegionDataBackupEnabled'] = self.is_cross_region_data_backup_enabled
        if self.is_cross_region_log_backup_enabled is not None:
            result['IsCrossRegionLogBackupEnabled'] = self.is_cross_region_log_backup_enabled
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.local_log_retention is not None:
            result['LocalLogRetention'] = self.local_log_retention
        if self.local_log_retention_number is not None:
            result['LocalLogRetentionNumber'] = self.local_log_retention_number
        if self.log_local_retention_space is not None:
            result['LogLocalRetentionSpace'] = self.log_local_retention_space
        if self.remove_log_retention is not None:
            result['RemoveLogRetention'] = self.remove_log_retention
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('BackupPlanBegin') is not None:
            self.backup_plan_begin = m.get('BackupPlanBegin')
        if m.get('BackupSetRetention') is not None:
            self.backup_set_retention = m.get('BackupSetRetention')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupWay') is not None:
            self.backup_way = m.get('BackupWay')
        if m.get('ColdDataBackupInterval') is not None:
            self.cold_data_backup_interval = m.get('ColdDataBackupInterval')
        if m.get('ColdDataBackupRetention') is not None:
            self.cold_data_backup_retention = m.get('ColdDataBackupRetention')
        if m.get('CrossRegionDataBackupRetention') is not None:
            self.cross_region_data_backup_retention = m.get('CrossRegionDataBackupRetention')
        if m.get('CrossRegionLogBackupRetention') is not None:
            self.cross_region_log_backup_retention = m.get('CrossRegionLogBackupRetention')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DestCrossRegion') is not None:
            self.dest_cross_region = m.get('DestCrossRegion')
        if m.get('ForceCleanOnHighSpaceUsage') is not None:
            self.force_clean_on_high_space_usage = m.get('ForceCleanOnHighSpaceUsage')
        if m.get('IsCrossRegionDataBackupEnabled') is not None:
            self.is_cross_region_data_backup_enabled = m.get('IsCrossRegionDataBackupEnabled')
        if m.get('IsCrossRegionLogBackupEnabled') is not None:
            self.is_cross_region_log_backup_enabled = m.get('IsCrossRegionLogBackupEnabled')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('LocalLogRetention') is not None:
            self.local_log_retention = m.get('LocalLogRetention')
        if m.get('LocalLogRetentionNumber') is not None:
            self.local_log_retention_number = m.get('LocalLogRetentionNumber')
        if m.get('LogLocalRetentionSpace') is not None:
            self.log_local_retention_space = m.get('LogLocalRetentionSpace')
        if m.get('RemoveLogRetention') is not None:
            self.remove_log_retention = m.get('RemoveLogRetention')
        return self


class UpdateBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: List[UpdateBackupPolicyResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
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
                temp_model = UpdateBackupPolicyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBackupPolicyResponseBody = None,
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
            temp_model = UpdateBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstanceSSLRequest(TeaModel):
    def __init__(
        self,
        cert_common_name: str = None,
        dbinstance_name: str = None,
        enable_ssl: bool = None,
        region_id: str = None,
    ):
        self.cert_common_name = cert_common_name
        self.dbinstance_name = dbinstance_name
        self.enable_ssl = enable_ssl
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_common_name is not None:
            result['CertCommonName'] = self.cert_common_name
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertCommonName') is not None:
            self.cert_common_name = m.get('CertCommonName')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateDBInstanceSSLResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDBInstanceSSLResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateDBInstanceSSLResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateDBInstanceSSLResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDBInstanceSSLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDBInstanceSSLResponseBody = None,
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
            temp_model = UpdateDBInstanceSSLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDBInstanceTDERequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        encryption_key: str = None,
        region_id: str = None,
        role_arn: str = None,
        tdestatus: int = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.encryption_key = encryption_key
        self.region_id = region_id
        self.role_arn = role_arn
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')
        return self


class UpdateDBInstanceTDEResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateDBInstanceTDEResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateDBInstanceTDEResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateDBInstanceTDEResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDBInstanceTDEResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDBInstanceTDEResponseBody = None,
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
            temp_model = UpdateDBInstanceTDEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolarDBXInstanceNodeRequest(TeaModel):
    def __init__(
        self,
        cnnode_count: str = None,
        client_token: str = None,
        dbinstance_name: str = None,
        dnnode_count: str = None,
        db_instance_node_count: str = None,
        region_id: str = None,
    ):
        self.cnnode_count = cnnode_count
        self.client_token = client_token
        self.dbinstance_name = dbinstance_name
        self.dnnode_count = dnnode_count
        self.db_instance_node_count = db_instance_node_count
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cnnode_count is not None:
            result['CNNodeCount'] = self.cnnode_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dnnode_count is not None:
            result['DNNodeCount'] = self.dnnode_count
        if self.db_instance_node_count is not None:
            result['DbInstanceNodeCount'] = self.db_instance_node_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CNNodeCount') is not None:
            self.cnnode_count = m.get('CNNodeCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DNNodeCount') is not None:
            self.dnnode_count = m.get('DNNodeCount')
        if m.get('DbInstanceNodeCount') is not None:
            self.db_instance_node_count = m.get('DbInstanceNodeCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdatePolarDBXInstanceNodeResponseBody(TeaModel):
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


class UpdatePolarDBXInstanceNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePolarDBXInstanceNodeResponseBody = None,
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
            temp_model = UpdatePolarDBXInstanceNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        minor_version: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.minor_version = minor_version
        self.region_id = region_id
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')
        return self


class UpgradeDBInstanceKernelVersionResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        request_id: str = None,
        target_minor_version: str = None,
        task_id: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.request_id = request_id
        self.target_minor_version = target_minor_version
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_minor_version is not None:
            result['TargetMinorVersion'] = self.target_minor_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetMinorVersion') is not None:
            self.target_minor_version = m.get('TargetMinorVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpgradeDBInstanceKernelVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeDBInstanceKernelVersionResponseBody = None,
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
            temp_model = UpgradeDBInstanceKernelVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


