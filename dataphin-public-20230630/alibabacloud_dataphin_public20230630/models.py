# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DataSourceInfo(TeaModel):
    def __init__(
        self,
        configs: Dict[str, str] = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        scope: str = None,
        tenant_id: int = None,
        type: str = None,
    ):
        self.configs = configs
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.scope = scope
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.description is not None:
            result['Description'] = self.description
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DatasourceCreate(TeaModel):
    def __init__(
        self,
        check_activity: bool = None,
        configs: Dict[str, str] = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_activity = check_activity
        self.configs = configs
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_activity is not None:
            result['CheckActivity'] = self.check_activity
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckActivity') is not None:
            self.check_activity = m.get('CheckActivity')
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddTenantMembersRequestAddCommandUserList(TeaModel):
    def __init__(
        self,
        id: str = None,
        role_list: List[str] = None,
    ):
        self.id = id
        self.role_list = role_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.role_list is not None:
            result['RoleList'] = self.role_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')
        return self


class AddTenantMembersRequestAddCommand(TeaModel):
    def __init__(
        self,
        user_list: List[AddTenantMembersRequestAddCommandUserList] = None,
    ):
        # This parameter is required.
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = AddTenantMembersRequestAddCommandUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class AddTenantMembersRequest(TeaModel):
    def __init__(
        self,
        add_command: AddTenantMembersRequestAddCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.add_command = add_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.add_command:
            self.add_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command is not None:
            result['AddCommand'] = self.add_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            temp_model = AddTenantMembersRequestAddCommand()
            self.add_command = temp_model.from_map(m['AddCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddTenantMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        add_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.add_command_shrink = add_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command_shrink is not None:
            result['AddCommand'] = self.add_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            self.add_command_shrink = m.get('AddCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddTenantMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddTenantMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTenantMembersResponseBody = None,
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
            temp_model = AddTenantMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTenantMembersBySourceUserRequestAddCommandSourceUserList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        mail: str = None,
        mobile_phone: str = None,
        source_id: str = None,
    ):
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class AddTenantMembersBySourceUserRequestAddCommand(TeaModel):
    def __init__(
        self,
        source_user_list: List[AddTenantMembersBySourceUserRequestAddCommandSourceUserList] = None,
    ):
        self.source_user_list = source_user_list

    def validate(self):
        if self.source_user_list:
            for k in self.source_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceUserList'] = []
        if self.source_user_list is not None:
            for k in self.source_user_list:
                result['SourceUserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_user_list = []
        if m.get('SourceUserList') is not None:
            for k in m.get('SourceUserList'):
                temp_model = AddTenantMembersBySourceUserRequestAddCommandSourceUserList()
                self.source_user_list.append(temp_model.from_map(k))
        return self


class AddTenantMembersBySourceUserRequest(TeaModel):
    def __init__(
        self,
        add_command: AddTenantMembersBySourceUserRequestAddCommand = None,
        op_tenant_id: int = None,
    ):
        self.add_command = add_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.add_command:
            self.add_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command is not None:
            result['AddCommand'] = self.add_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            temp_model = AddTenantMembersBySourceUserRequestAddCommand()
            self.add_command = temp_model.from_map(m['AddCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddTenantMembersBySourceUserShrinkRequest(TeaModel):
    def __init__(
        self,
        add_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.add_command_shrink = add_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command_shrink is not None:
            result['AddCommand'] = self.add_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            self.add_command_shrink = m.get('AddCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddTenantMembersBySourceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddTenantMembersBySourceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTenantMembersBySourceUserResponseBody = None,
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
            temp_model = AddTenantMembersBySourceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserGroupMemberRequestAddCommand(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.user_group_id = user_group_id
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class AddUserGroupMemberRequest(TeaModel):
    def __init__(
        self,
        add_command: AddUserGroupMemberRequestAddCommand = None,
        op_tenant_id: int = None,
    ):
        self.add_command = add_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.add_command:
            self.add_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command is not None:
            result['AddCommand'] = self.add_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            temp_model = AddUserGroupMemberRequestAddCommand()
            self.add_command = temp_model.from_map(m['AddCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddUserGroupMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        add_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.add_command_shrink = add_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_command_shrink is not None:
            result['AddCommand'] = self.add_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            self.add_command_shrink = m.get('AddCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class AddUserGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserGroupMemberResponseBody = None,
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
            temp_model = AddUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDataSourceConnectivityRequestCheckCommandConfigItemList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
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


class CheckDataSourceConnectivityRequestCheckCommand(TeaModel):
    def __init__(
        self,
        config_item_list: List[CheckDataSourceConnectivityRequestCheckCommandConfigItemList] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.config_item_list = config_item_list
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = CheckDataSourceConnectivityRequestCheckCommandConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckDataSourceConnectivityRequest(TeaModel):
    def __init__(
        self,
        check_command: CheckDataSourceConnectivityRequestCheckCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command = check_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.check_command:
            self.check_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_command is not None:
            result['CheckCommand'] = self.check_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            temp_model = CheckDataSourceConnectivityRequestCheckCommand()
            self.check_command = temp_model.from_map(m['CheckCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CheckDataSourceConnectivityShrinkRequest(TeaModel):
    def __init__(
        self,
        check_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command_shrink = check_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_command_shrink is not None:
            result['CheckCommand'] = self.check_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            self.check_command_shrink = m.get('CheckCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CheckDataSourceConnectivityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckDataSourceConnectivityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDataSourceConnectivityResponseBody = None,
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
            temp_model = CheckDataSourceConnectivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDataSourceConnectivityByIdRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CheckDataSourceConnectivityByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckDataSourceConnectivityByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDataSourceConnectivityByIdResponseBody = None,
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
            temp_model = CheckDataSourceConnectivityByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResourcePermissionRequestCheckCommandResourceList(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CheckResourcePermissionRequestCheckCommand(TeaModel):
    def __init__(
        self,
        operate: str = None,
        resource_list: List[CheckResourcePermissionRequestCheckCommandResourceList] = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.operate = operate
        # This parameter is required.
        self.resource_list = resource_list
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate is not None:
            result['Operate'] = self.operate
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operate') is not None:
            self.operate = m.get('Operate')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = CheckResourcePermissionRequestCheckCommandResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CheckResourcePermissionRequest(TeaModel):
    def __init__(
        self,
        check_command: CheckResourcePermissionRequestCheckCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command = check_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.check_command:
            self.check_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_command is not None:
            result['CheckCommand'] = self.check_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            temp_model = CheckResourcePermissionRequestCheckCommand()
            self.check_command = temp_model.from_map(m['CheckCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CheckResourcePermissionShrinkRequest(TeaModel):
    def __init__(
        self,
        check_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.check_command_shrink = check_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_command_shrink is not None:
            result['CheckCommand'] = self.check_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCommand') is not None:
            self.check_command_shrink = m.get('CheckCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CheckResourcePermissionResponseBodyResourcePermissionList(TeaModel):
    def __init__(
        self,
        has_permission: bool = None,
        resource_id: str = None,
    ):
        self.has_permission = has_permission
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_permission is not None:
            result['HasPermission'] = self.has_permission
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPermission') is not None:
            self.has_permission = m.get('HasPermission')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CheckResourcePermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        resource_permission_list: List[CheckResourcePermissionResponseBodyResourcePermissionList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.resource_permission_list = resource_permission_list
        self.success = success

    def validate(self):
        if self.resource_permission_list:
            for k in self.resource_permission_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourcePermissionList'] = []
        if self.resource_permission_list is not None:
            for k in self.resource_permission_list:
                result['ResourcePermissionList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_permission_list = []
        if m.get('ResourcePermissionList') is not None:
            for k in m.get('ResourcePermissionList'):
                temp_model = CheckResourcePermissionResponseBodyResourcePermissionList()
                self.resource_permission_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckResourcePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckResourcePermissionResponseBody = None,
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
            temp_model = CheckResourcePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdHocFileRequestCreateCommand(TeaModel):
    def __init__(
        self,
        content: str = None,
        directory: str = None,
        name: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateAdHocFileRequest(TeaModel):
    def __init__(
        self,
        create_command: CreateAdHocFileRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = CreateAdHocFileRequestCreateCommand()
            self.create_command = temp_model.from_map(m['CreateCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateAdHocFileShrinkRequest(TeaModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command_shrink = create_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateAdHocFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_id: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_id = file_id
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAdHocFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAdHocFileResponseBody = None,
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
            temp_model = CreateAdHocFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
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


class CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate(TeaModel):
    def __init__(
        self,
        check_activity: bool = None,
        config_item_list: List[CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList] = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_activity = check_activity
        # This parameter is required.
        self.config_item_list = config_item_list
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_activity is not None:
            result['CheckActivity'] = self.check_activity
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckActivity') is not None:
            self.check_activity = m.get('CheckActivity')
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreateConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDataSourceRequestCreateCommandDevDataSourceCreate(TeaModel):
    def __init__(
        self,
        data_source_create: CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate = None,
        prod_data_source_id: int = None,
    ):
        # 数据源创建结构体
        self.data_source_create = data_source_create
        self.prod_data_source_id = prod_data_source_id

    def validate(self):
        if self.data_source_create:
            self.data_source_create.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_create is not None:
            result['DataSourceCreate'] = self.data_source_create.to_map()
        if self.prod_data_source_id is not None:
            result['ProdDataSourceId'] = self.prod_data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceCreate') is not None:
            temp_model = CreateDataSourceRequestCreateCommandDevDataSourceCreateDataSourceCreate()
            self.data_source_create = temp_model.from_map(m['DataSourceCreate'])
        if m.get('ProdDataSourceId') is not None:
            self.prod_data_source_id = m.get('ProdDataSourceId')
        return self


class CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
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


class CreateDataSourceRequestCreateCommandProdDataSourceCreate(TeaModel):
    def __init__(
        self,
        check_activity: bool = None,
        config_item_list: List[CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList] = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.check_activity = check_activity
        # This parameter is required.
        self.config_item_list = config_item_list
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_activity is not None:
            result['CheckActivity'] = self.check_activity
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckActivity') is not None:
            self.check_activity = m.get('CheckActivity')
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = CreateDataSourceRequestCreateCommandProdDataSourceCreateConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDataSourceRequestCreateCommand(TeaModel):
    def __init__(
        self,
        dev_data_source_create: CreateDataSourceRequestCreateCommandDevDataSourceCreate = None,
        prod_data_source_create: CreateDataSourceRequestCreateCommandProdDataSourceCreate = None,
    ):
        self.dev_data_source_create = dev_data_source_create
        # 数据源创建结构体
        self.prod_data_source_create = prod_data_source_create

    def validate(self):
        if self.dev_data_source_create:
            self.dev_data_source_create.validate()
        if self.prod_data_source_create:
            self.prod_data_source_create.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dev_data_source_create is not None:
            result['DevDataSourceCreate'] = self.dev_data_source_create.to_map()
        if self.prod_data_source_create is not None:
            result['ProdDataSourceCreate'] = self.prod_data_source_create.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceCreate') is not None:
            temp_model = CreateDataSourceRequestCreateCommandDevDataSourceCreate()
            self.dev_data_source_create = temp_model.from_map(m['DevDataSourceCreate'])
        if m.get('ProdDataSourceCreate') is not None:
            temp_model = CreateDataSourceRequestCreateCommandProdDataSourceCreate()
            self.prod_data_source_create = temp_model.from_map(m['ProdDataSourceCreate'])
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(
        self,
        create_command: CreateDataSourceRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = CreateDataSourceRequestCreateCommand()
            self.create_command = temp_model.from_map(m['CreateCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateDataSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.create_command_shrink = create_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateDataSourceResponseBodyCreateResult(TeaModel):
    def __init__(
        self,
        dev_data_source_id: int = None,
        prod_data_source_id: int = None,
    ):
        self.dev_data_source_id = dev_data_source_id
        self.prod_data_source_id = prod_data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dev_data_source_id is not None:
            result['DevDataSourceId'] = self.dev_data_source_id
        if self.prod_data_source_id is not None:
            result['ProdDataSourceId'] = self.prod_data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceId') is not None:
            self.dev_data_source_id = m.get('DevDataSourceId')
        if m.get('ProdDataSourceId') is not None:
            self.prod_data_source_id = m.get('ProdDataSourceId')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_result: CreateDataSourceResponseBodyCreateResult = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.create_result = create_result
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateResult') is not None:
            temp_model = CreateDataSourceResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m['CreateResult'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSourceResponseBody = None,
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
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDirectoryRequestCreateCommand(TeaModel):
    def __init__(
        self,
        category: str = None,
        directory: str = None,
        name: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateDirectoryRequest(TeaModel):
    def __init__(
        self,
        create_command: CreateDirectoryRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = CreateDirectoryRequestCreateCommand()
            self.create_command = temp_model.from_map(m['CreateCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateDirectoryShrinkRequest(TeaModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command_shrink = create_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_id: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_id = file_id
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDirectoryResponseBody = None,
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
            temp_model = CreateDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateNodeSupplementRequestCreateCommandFilterList(TeaModel):
    def __init__(
        self,
        exclude: bool = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        self.exclude = exclude
        self.key = key
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.key is not None:
            result['Key'] = self.key
        if self.value_list is not None:
            result['ValueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')
        return self


class CreateNodeSupplementRequestCreateCommandGlobalParamList(TeaModel):
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


class CreateNodeSupplementRequestCreateCommandNodeIdList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_id_list = field_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateNodeSupplementRequestCreateCommandNodeParamsListParamList(TeaModel):
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


class CreateNodeSupplementRequestCreateCommandNodeParamsList(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        param_list: List[CreateNodeSupplementRequestCreateCommandNodeParamsListParamList] = None,
    ):
        self.node_id = node_id
        self.param_list = param_list

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = CreateNodeSupplementRequestCreateCommandNodeParamsListParamList()
                self.param_list.append(temp_model.from_map(k))
        return self


class CreateNodeSupplementRequestCreateCommand(TeaModel):
    def __init__(
        self,
        contain_all_down_stream: bool = None,
        down_stream_node_id_list: List[CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList] = None,
        end_biz_date: str = None,
        filter_list: List[CreateNodeSupplementRequestCreateCommandFilterList] = None,
        global_param_list: List[CreateNodeSupplementRequestCreateCommandGlobalParamList] = None,
        max_due_time: str = None,
        min_due_time: str = None,
        name: str = None,
        node_id_list: List[CreateNodeSupplementRequestCreateCommandNodeIdList] = None,
        node_params_list: List[CreateNodeSupplementRequestCreateCommandNodeParamsList] = None,
        parallelism: int = None,
        project_id: int = None,
        start_biz_date: str = None,
    ):
        self.contain_all_down_stream = contain_all_down_stream
        self.down_stream_node_id_list = down_stream_node_id_list
        # This parameter is required.
        self.end_biz_date = end_biz_date
        self.filter_list = filter_list
        self.global_param_list = global_param_list
        self.max_due_time = max_due_time
        self.min_due_time = min_due_time
        self.name = name
        # This parameter is required.
        self.node_id_list = node_id_list
        self.node_params_list = node_params_list
        self.parallelism = parallelism
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.start_biz_date = start_biz_date

    def validate(self):
        if self.down_stream_node_id_list:
            for k in self.down_stream_node_id_list:
                if k:
                    k.validate()
        if self.filter_list:
            for k in self.filter_list:
                if k:
                    k.validate()
        if self.global_param_list:
            for k in self.global_param_list:
                if k:
                    k.validate()
        if self.node_id_list:
            for k in self.node_id_list:
                if k:
                    k.validate()
        if self.node_params_list:
            for k in self.node_params_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_all_down_stream is not None:
            result['ContainAllDownStream'] = self.contain_all_down_stream
        result['DownStreamNodeIdList'] = []
        if self.down_stream_node_id_list is not None:
            for k in self.down_stream_node_id_list:
                result['DownStreamNodeIdList'].append(k.to_map() if k else None)
        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date
        result['FilterList'] = []
        if self.filter_list is not None:
            for k in self.filter_list:
                result['FilterList'].append(k.to_map() if k else None)
        result['GlobalParamList'] = []
        if self.global_param_list is not None:
            for k in self.global_param_list:
                result['GlobalParamList'].append(k.to_map() if k else None)
        if self.max_due_time is not None:
            result['MaxDueTime'] = self.max_due_time
        if self.min_due_time is not None:
            result['MinDueTime'] = self.min_due_time
        if self.name is not None:
            result['Name'] = self.name
        result['NodeIdList'] = []
        if self.node_id_list is not None:
            for k in self.node_id_list:
                result['NodeIdList'].append(k.to_map() if k else None)
        result['NodeParamsList'] = []
        if self.node_params_list is not None:
            for k in self.node_params_list:
                result['NodeParamsList'].append(k.to_map() if k else None)
        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainAllDownStream') is not None:
            self.contain_all_down_stream = m.get('ContainAllDownStream')
        self.down_stream_node_id_list = []
        if m.get('DownStreamNodeIdList') is not None:
            for k in m.get('DownStreamNodeIdList'):
                temp_model = CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList()
                self.down_stream_node_id_list.append(temp_model.from_map(k))
        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')
        self.filter_list = []
        if m.get('FilterList') is not None:
            for k in m.get('FilterList'):
                temp_model = CreateNodeSupplementRequestCreateCommandFilterList()
                self.filter_list.append(temp_model.from_map(k))
        self.global_param_list = []
        if m.get('GlobalParamList') is not None:
            for k in m.get('GlobalParamList'):
                temp_model = CreateNodeSupplementRequestCreateCommandGlobalParamList()
                self.global_param_list.append(temp_model.from_map(k))
        if m.get('MaxDueTime') is not None:
            self.max_due_time = m.get('MaxDueTime')
        if m.get('MinDueTime') is not None:
            self.min_due_time = m.get('MinDueTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.node_id_list = []
        if m.get('NodeIdList') is not None:
            for k in m.get('NodeIdList'):
                temp_model = CreateNodeSupplementRequestCreateCommandNodeIdList()
                self.node_id_list.append(temp_model.from_map(k))
        self.node_params_list = []
        if m.get('NodeParamsList') is not None:
            for k in m.get('NodeParamsList'):
                temp_model = CreateNodeSupplementRequestCreateCommandNodeParamsList()
                self.node_params_list.append(temp_model.from_map(k))
        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')
        return self


class CreateNodeSupplementRequest(TeaModel):
    def __init__(
        self,
        create_command: CreateNodeSupplementRequestCreateCommand = None,
        env: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = CreateNodeSupplementRequestCreateCommand()
            self.create_command = temp_model.from_map(m['CreateCommand'])
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateNodeSupplementShrinkRequest(TeaModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        env: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command_shrink = create_command_shrink
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateNodeSupplementResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        submit_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.submit_id = submit_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNodeSupplementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNodeSupplementResponseBody = None,
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
            temp_model = CreateNodeSupplementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequestCreateCommand(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin_user_id_list: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        self.active = active
        self.admin_user_id_list = admin_user_id_list
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.admin_user_id_list is not None:
            result['AdminUserIdList'] = self.admin_user_id_list
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('AdminUserIdList') is not None:
            self.admin_user_id_list = m.get('AdminUserIdList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        create_command: CreateUserGroupRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = CreateUserGroupRequestCreateCommand()
            self.create_command = temp_model.from_map(m['CreateCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateUserGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        create_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.create_command_shrink = create_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_command_shrink is not None:
            result['CreateCommand'] = self.create_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            self.create_command_shrink = m.get('CreateCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_group_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserGroupResponseBody = None,
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
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAdHocFileRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteAdHocFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAdHocFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAdHocFileResponseBody = None,
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
            temp_model = DeleteAdHocFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequestDeleteCommand(TeaModel):
    def __init__(
        self,
        mode: str = None,
        prod_data_source_id: int = None,
    ):
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.prod_data_source_id = prod_data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.prod_data_source_id is not None:
            result['ProdDataSourceId'] = self.prod_data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ProdDataSourceId') is not None:
            self.prod_data_source_id = m.get('ProdDataSourceId')
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        delete_command: DeleteDataSourceRequestDeleteCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_command = delete_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.delete_command:
            self.delete_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_command is not None:
            result['DeleteCommand'] = self.delete_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteCommand') is not None:
            temp_model = DeleteDataSourceRequestDeleteCommand()
            self.delete_command = temp_model.from_map(m['DeleteCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class DeleteDataSourceShrinkRequest(TeaModel):
    def __init__(
        self,
        delete_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_command_shrink = delete_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_command_shrink is not None:
            result['DeleteCommand'] = self.delete_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteCommand') is not None:
            self.delete_command_shrink = m.get('DeleteCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceResponseBody = None,
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
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoryRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDirectoryResponseBody = None,
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
            temp_model = DeleteDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserGroupResponseBody = None,
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
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteManualNodeRequestExecuteCommandParamList(TeaModel):
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


class ExecuteManualNodeRequestExecuteCommand(TeaModel):
    def __init__(
        self,
        end_biz_date: str = None,
        flow_name: str = None,
        node_id: str = None,
        param_list: List[ExecuteManualNodeRequestExecuteCommandParamList] = None,
        project_id: int = None,
        start_biz_date: str = None,
    ):
        # This parameter is required.
        self.end_biz_date = end_biz_date
        self.flow_name = flow_name
        # This parameter is required.
        self.node_id = node_id
        self.param_list = param_list
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.start_biz_date = start_biz_date

    def validate(self):
        if self.param_list:
            for k in self.param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        result['ParamList'] = []
        if self.param_list is not None:
            for k in self.param_list:
                result['ParamList'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        self.param_list = []
        if m.get('ParamList') is not None:
            for k in m.get('ParamList'):
                temp_model = ExecuteManualNodeRequestExecuteCommandParamList()
                self.param_list.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')
        return self


class ExecuteManualNodeRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        execute_command: ExecuteManualNodeRequestExecuteCommand = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.execute_command = execute_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.execute_command:
            self.execute_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.execute_command is not None:
            result['ExecuteCommand'] = self.execute_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExecuteCommand') is not None:
            temp_model = ExecuteManualNodeRequestExecuteCommand()
            self.execute_command = temp_model.from_map(m['ExecuteCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ExecuteManualNodeShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        execute_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.execute_command_shrink = execute_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.execute_command_shrink is not None:
            result['ExecuteCommand'] = self.execute_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ExecuteCommand') is not None:
            self.execute_command_shrink = m.get('ExecuteCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ExecuteManualNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        flow_id: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.flow_id = flow_id
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteManualNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteManualNodeResponseBody = None,
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
            temp_model = ExecuteManualNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FixDataRequestFixDataCommandDownStreamInstanceIdList(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FixDataRequestFixDataCommandRootInstanceId(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class FixDataRequestFixDataCommand(TeaModel):
    def __init__(
        self,
        contain_root_instance: bool = None,
        down_stream_instance_id_list: List[FixDataRequestFixDataCommandDownStreamInstanceIdList] = None,
        downstream_range: str = None,
        force_rerun: bool = None,
        project_id: int = None,
        root_instance_id: FixDataRequestFixDataCommandRootInstanceId = None,
    ):
        self.contain_root_instance = contain_root_instance
        self.down_stream_instance_id_list = down_stream_instance_id_list
        self.downstream_range = downstream_range
        self.force_rerun = force_rerun
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.root_instance_id = root_instance_id

    def validate(self):
        if self.down_stream_instance_id_list:
            for k in self.down_stream_instance_id_list:
                if k:
                    k.validate()
        if self.root_instance_id:
            self.root_instance_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_root_instance is not None:
            result['ContainRootInstance'] = self.contain_root_instance
        result['DownStreamInstanceIdList'] = []
        if self.down_stream_instance_id_list is not None:
            for k in self.down_stream_instance_id_list:
                result['DownStreamInstanceIdList'].append(k.to_map() if k else None)
        if self.downstream_range is not None:
            result['DownstreamRange'] = self.downstream_range
        if self.force_rerun is not None:
            result['ForceRerun'] = self.force_rerun
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.root_instance_id is not None:
            result['RootInstanceId'] = self.root_instance_id.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainRootInstance') is not None:
            self.contain_root_instance = m.get('ContainRootInstance')
        self.down_stream_instance_id_list = []
        if m.get('DownStreamInstanceIdList') is not None:
            for k in m.get('DownStreamInstanceIdList'):
                temp_model = FixDataRequestFixDataCommandDownStreamInstanceIdList()
                self.down_stream_instance_id_list.append(temp_model.from_map(k))
        if m.get('DownstreamRange') is not None:
            self.downstream_range = m.get('DownstreamRange')
        if m.get('ForceRerun') is not None:
            self.force_rerun = m.get('ForceRerun')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RootInstanceId') is not None:
            temp_model = FixDataRequestFixDataCommandRootInstanceId()
            self.root_instance_id = temp_model.from_map(m['RootInstanceId'])
        return self


class FixDataRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        fix_data_command: FixDataRequestFixDataCommand = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.fix_data_command = fix_data_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.fix_data_command:
            self.fix_data_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.fix_data_command is not None:
            result['FixDataCommand'] = self.fix_data_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('FixDataCommand') is not None:
            temp_model = FixDataRequestFixDataCommand()
            self.fix_data_command = temp_model.from_map(m['FixDataCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class FixDataShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        fix_data_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.fix_data_command_shrink = fix_data_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.fix_data_command_shrink is not None:
            result['FixDataCommand'] = self.fix_data_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('FixDataCommand') is not None:
            self.fix_data_command_shrink = m.get('FixDataCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class FixDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        submit_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.submit_id = submit_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.submit_id is not None:
            result['SubmitId'] = self.submit_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubmitId') is not None:
            self.submit_id = m.get('SubmitId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FixDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FixDataResponseBody = None,
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
            temp_model = FixDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdHocFileRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetAdHocFileResponseBodyFileInfo(TeaModel):
    def __init__(
        self,
        content: str = None,
        creator: str = None,
        directory: str = None,
        id: int = None,
        last_modifier: str = None,
        name: str = None,
        project_id: int = None,
    ):
        self.content = content
        self.creator = creator
        self.directory = directory
        self.id = id
        self.last_modifier = last_modifier
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetAdHocFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_info: GetAdHocFileResponseBodyFileInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_info = file_info
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.file_info is not None:
            result['FileInfo'] = self.file_info.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FileInfo') is not None:
            temp_model = GetAdHocFileResponseBodyFileInfo()
            self.file_info = temp_model.from_map(m['FileInfo'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAdHocFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAdHocFileResponseBody = None,
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
            temp_model = GetAdHocFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevObjectDependencyRequest(TeaModel):
    def __init__(
        self,
        object_from: str = None,
        object_id: str = None,
        object_type: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.object_from = object_from
        # This parameter is required.
        self.object_id = object_id
        # This parameter is required.
        self.object_type = object_type
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_from is not None:
            result['ObjectFrom'] = self.object_from
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectFrom') is not None:
            self.object_from = m.get('ObjectFrom')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod(TeaModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        self.period_offset = period_offset
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_offset is not None:
            result['PeriodOffset'] = self.period_offset
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodOffset') is not None:
            self.period_offset = m.get('PeriodOffset')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        return self


class GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        key: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList(TeaModel):
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


class GetDevObjectDependencyResponseBodyDevObjectDependencyList(TeaModel):
    def __init__(
        self,
        auto_parse: bool = None,
        biz_type: str = None,
        biz_unit_id: str = None,
        biz_unit_name: str = None,
        cron_expression: str = None,
        custom_cron_expression: bool = None,
        depend_field_list: List[str] = None,
        dependency_period: GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod = None,
        dependency_strategy: str = None,
        dim_mid_node: bool = None,
        effect_field_list: List[str] = None,
        external_biz_info: str = None,
        manually_add: bool = None,
        node_id: str = None,
        node_name: str = None,
        node_output_name: str = None,
        node_output_table_name: str = None,
        node_type: str = None,
        output_context_param_list: List[GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList] = None,
        owner_list: List[GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList] = None,
        period_diff: int = None,
        project_id: int = None,
        project_name: str = None,
        schedule_type: str = None,
        self_depend: bool = None,
        sub_biz_type: str = None,
        valid: bool = None,
    ):
        self.auto_parse = auto_parse
        self.biz_type = biz_type
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.cron_expression = cron_expression
        self.custom_cron_expression = custom_cron_expression
        self.depend_field_list = depend_field_list
        self.dependency_period = dependency_period
        self.dependency_strategy = dependency_strategy
        self.dim_mid_node = dim_mid_node
        self.effect_field_list = effect_field_list
        self.external_biz_info = external_biz_info
        self.manually_add = manually_add
        self.node_id = node_id
        self.node_name = node_name
        self.node_output_name = node_output_name
        self.node_output_table_name = node_output_table_name
        self.node_type = node_type
        self.output_context_param_list = output_context_param_list
        self.owner_list = owner_list
        self.period_diff = period_diff
        self.project_id = project_id
        self.project_name = project_name
        self.schedule_type = schedule_type
        self.self_depend = self_depend
        self.sub_biz_type = sub_biz_type
        self.valid = valid

    def validate(self):
        if self.dependency_period:
            self.dependency_period.validate()
        if self.output_context_param_list:
            for k in self.output_context_param_list:
                if k:
                    k.validate()
        if self.owner_list:
            for k in self.owner_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_parse is not None:
            result['AutoParse'] = self.auto_parse
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.custom_cron_expression is not None:
            result['CustomCronExpression'] = self.custom_cron_expression
        if self.depend_field_list is not None:
            result['DependFieldList'] = self.depend_field_list
        if self.dependency_period is not None:
            result['DependencyPeriod'] = self.dependency_period.to_map()
        if self.dependency_strategy is not None:
            result['DependencyStrategy'] = self.dependency_strategy
        if self.dim_mid_node is not None:
            result['DimMidNode'] = self.dim_mid_node
        if self.effect_field_list is not None:
            result['EffectFieldList'] = self.effect_field_list
        if self.external_biz_info is not None:
            result['ExternalBizInfo'] = self.external_biz_info
        if self.manually_add is not None:
            result['ManuallyAdd'] = self.manually_add
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_output_name is not None:
            result['NodeOutputName'] = self.node_output_name
        if self.node_output_table_name is not None:
            result['NodeOutputTableName'] = self.node_output_table_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        result['OutputContextParamList'] = []
        if self.output_context_param_list is not None:
            for k in self.output_context_param_list:
                result['OutputContextParamList'].append(k.to_map() if k else None)
        result['OwnerList'] = []
        if self.owner_list is not None:
            for k in self.owner_list:
                result['OwnerList'].append(k.to_map() if k else None)
        if self.period_diff is not None:
            result['PeriodDiff'] = self.period_diff
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.self_depend is not None:
            result['SelfDepend'] = self.self_depend
        if self.sub_biz_type is not None:
            result['SubBizType'] = self.sub_biz_type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoParse') is not None:
            self.auto_parse = m.get('AutoParse')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('CustomCronExpression') is not None:
            self.custom_cron_expression = m.get('CustomCronExpression')
        if m.get('DependFieldList') is not None:
            self.depend_field_list = m.get('DependFieldList')
        if m.get('DependencyPeriod') is not None:
            temp_model = GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod()
            self.dependency_period = temp_model.from_map(m['DependencyPeriod'])
        if m.get('DependencyStrategy') is not None:
            self.dependency_strategy = m.get('DependencyStrategy')
        if m.get('DimMidNode') is not None:
            self.dim_mid_node = m.get('DimMidNode')
        if m.get('EffectFieldList') is not None:
            self.effect_field_list = m.get('EffectFieldList')
        if m.get('ExternalBizInfo') is not None:
            self.external_biz_info = m.get('ExternalBizInfo')
        if m.get('ManuallyAdd') is not None:
            self.manually_add = m.get('ManuallyAdd')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeOutputName') is not None:
            self.node_output_name = m.get('NodeOutputName')
        if m.get('NodeOutputTableName') is not None:
            self.node_output_table_name = m.get('NodeOutputTableName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        self.output_context_param_list = []
        if m.get('OutputContextParamList') is not None:
            for k in m.get('OutputContextParamList'):
                temp_model = GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList()
                self.output_context_param_list.append(temp_model.from_map(k))
        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k in m.get('OwnerList'):
                temp_model = GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList()
                self.owner_list.append(temp_model.from_map(k))
        if m.get('PeriodDiff') is not None:
            self.period_diff = m.get('PeriodDiff')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('SelfDepend') is not None:
            self.self_depend = m.get('SelfDepend')
        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetDevObjectDependencyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dev_object_dependency_list: List[GetDevObjectDependencyResponseBodyDevObjectDependencyList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dev_object_dependency_list = dev_object_dependency_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dev_object_dependency_list:
            for k in self.dev_object_dependency_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DevObjectDependencyList'] = []
        if self.dev_object_dependency_list is not None:
            for k in self.dev_object_dependency_list:
                result['DevObjectDependencyList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.dev_object_dependency_list = []
        if m.get('DevObjectDependencyList') is not None:
            for k in m.get('DevObjectDependencyList'):
                temp_model = GetDevObjectDependencyResponseBodyDevObjectDependencyList()
                self.dev_object_dependency_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDevObjectDependencyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDevObjectDependencyResponseBody = None,
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
            temp_model = GetDevObjectDependencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceDownStreamRequestInstanceGet(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_type: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class GetInstanceDownStreamRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_get: GetInstanceDownStreamRequestInstanceGet = None,
        op_tenant_id: int = None,
        run_status: str = None,
    ):
        # This parameter is required.
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_get = instance_get
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.run_status = run_status

    def validate(self):
        if self.instance_get:
            self.instance_get.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_get is not None:
            result['InstanceGet'] = self.instance_get.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.run_status is not None:
            result['RunStatus'] = self.run_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceGet') is not None:
            temp_model = GetInstanceDownStreamRequestInstanceGet()
            self.instance_get = temp_model.from_map(m['InstanceGet'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')
        return self


class GetInstanceDownStreamShrinkRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_get_shrink: str = None,
        op_tenant_id: int = None,
        run_status: str = None,
    ):
        # This parameter is required.
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_get_shrink = instance_get_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.run_status = run_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_get_shrink is not None:
            result['InstanceGet'] = self.instance_get_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.run_status is not None:
            result['RunStatus'] = self.run_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceGet') is not None:
            self.instance_get_shrink = m.get('InstanceGet')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')
        return self


class GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList(TeaModel):
    def __init__(
        self,
        field_instance_id: str = None,
        run_status: str = None,
        select_status: str = None,
    ):
        self.field_instance_id = field_instance_id
        self.run_status = run_status
        self.select_status = select_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id is not None:
            result['FieldInstanceId'] = self.field_instance_id
        if self.run_status is not None:
            result['RunStatus'] = self.run_status
        if self.select_status is not None:
            result['SelectStatus'] = self.select_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceId') is not None:
            self.field_instance_id = m.get('FieldInstanceId')
        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')
        if m.get('SelectStatus') is not None:
            self.select_status = m.get('SelectStatus')
        return self


class GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceDownStreamResponseBodyInstanceRelationList(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        extend_info: str = None,
        field_instance_list: List[GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList] = None,
        instance_info: GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo = None,
        run_status: str = None,
        select_status: str = None,
        select_status_cause: str = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.extend_info = extend_info
        self.field_instance_list = field_instance_list
        self.instance_info = instance_info
        self.run_status = run_status
        self.select_status = select_status
        self.select_status_cause = select_status_cause

    def validate(self):
        if self.field_instance_list:
            for k in self.field_instance_list:
                if k:
                    k.validate()
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        result['FieldInstanceList'] = []
        if self.field_instance_list is not None:
            for k in self.field_instance_list:
                result['FieldInstanceList'].append(k.to_map() if k else None)
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.run_status is not None:
            result['RunStatus'] = self.run_status
        if self.select_status is not None:
            result['SelectStatus'] = self.select_status
        if self.select_status_cause is not None:
            result['SelectStatusCause'] = self.select_status_cause
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        self.field_instance_list = []
        if m.get('FieldInstanceList') is not None:
            for k in m.get('FieldInstanceList'):
                temp_model = GetInstanceDownStreamResponseBodyInstanceRelationListFieldInstanceList()
                self.field_instance_list.append(temp_model.from_map(k))
        if m.get('InstanceInfo') is not None:
            temp_model = GetInstanceDownStreamResponseBodyInstanceRelationListInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')
        if m.get('SelectStatus') is not None:
            self.select_status = m.get('SelectStatus')
        if m.get('SelectStatusCause') is not None:
            self.select_status_cause = m.get('SelectStatusCause')
        return self


class GetInstanceDownStreamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_relation_list: List[GetInstanceDownStreamResponseBodyInstanceRelationList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_relation_list = instance_relation_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_relation_list:
            for k in self.instance_relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InstanceRelationList'] = []
        if self.instance_relation_list is not None:
            for k in self.instance_relation_list:
                result['InstanceRelationList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instance_relation_list = []
        if m.get('InstanceRelationList') is not None:
            for k in m.get('InstanceRelationList'):
                temp_model = GetInstanceDownStreamResponseBodyInstanceRelationList()
                self.instance_relation_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceDownStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceDownStreamResponseBody = None,
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
            temp_model = GetInstanceDownStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceUpDownStreamRequestInstanceId(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetInstanceUpDownStreamRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_id: GetInstanceUpDownStreamRequestInstanceId = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        self.up_stream_depth = up_stream_depth

    def validate(self):
        if self.instance_id:
            self.instance_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceId') is not None:
            temp_model = GetInstanceUpDownStreamRequestInstanceId()
            self.instance_id = temp_model.from_map(m['InstanceId'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')
        return self


class GetInstanceUpDownStreamShrinkRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        instance_id_shrink: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.instance_id_shrink = instance_id_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id
        self.up_stream_depth = up_stream_depth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_id_shrink is not None:
            result['InstanceId'] = self.instance_id_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceId') is not None:
            self.instance_id_shrink = m.get('InstanceId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')
        return self


class GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        self.id = id
        self.name = name
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class GetInstanceUpDownStreamResponseBodyInstanceDagInfo(TeaModel):
    def __init__(
        self,
        down_instance_list: List[GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList] = None,
        start_instance_list: List[GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList] = None,
        up_instance_list: List[GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList] = None,
    ):
        self.down_instance_list = down_instance_list
        self.start_instance_list = start_instance_list
        self.up_instance_list = up_instance_list

    def validate(self):
        if self.down_instance_list:
            for k in self.down_instance_list:
                if k:
                    k.validate()
        if self.start_instance_list:
            for k in self.start_instance_list:
                if k:
                    k.validate()
        if self.up_instance_list:
            for k in self.up_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownInstanceList'] = []
        if self.down_instance_list is not None:
            for k in self.down_instance_list:
                result['DownInstanceList'].append(k.to_map() if k else None)
        result['StartInstanceList'] = []
        if self.start_instance_list is not None:
            for k in self.start_instance_list:
                result['StartInstanceList'].append(k.to_map() if k else None)
        result['UpInstanceList'] = []
        if self.up_instance_list is not None:
            for k in self.up_instance_list:
                result['UpInstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.down_instance_list = []
        if m.get('DownInstanceList') is not None:
            for k in m.get('DownInstanceList'):
                temp_model = GetInstanceUpDownStreamResponseBodyInstanceDagInfoDownInstanceList()
                self.down_instance_list.append(temp_model.from_map(k))
        self.start_instance_list = []
        if m.get('StartInstanceList') is not None:
            for k in m.get('StartInstanceList'):
                temp_model = GetInstanceUpDownStreamResponseBodyInstanceDagInfoStartInstanceList()
                self.start_instance_list.append(temp_model.from_map(k))
        self.up_instance_list = []
        if m.get('UpInstanceList') is not None:
            for k in m.get('UpInstanceList'):
                temp_model = GetInstanceUpDownStreamResponseBodyInstanceDagInfoUpInstanceList()
                self.up_instance_list.append(temp_model.from_map(k))
        return self


class GetInstanceUpDownStreamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_dag_info: GetInstanceUpDownStreamResponseBodyInstanceDagInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_dag_info = instance_dag_info
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_dag_info:
            self.instance_dag_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance_dag_info is not None:
            result['InstanceDagInfo'] = self.instance_dag_info.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InstanceDagInfo') is not None:
            temp_model = GetInstanceUpDownStreamResponseBodyInstanceDagInfo()
            self.instance_dag_info = temp_model.from_map(m['InstanceDagInfo'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceUpDownStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceUpDownStreamResponseBody = None,
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
            temp_model = GetInstanceUpDownStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMyRolesRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetMyRolesResponseBodyRoleList(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        self.description = description
        self.id = id
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetMyRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        role_list: List[GetMyRolesResponseBodyRoleList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.role_list = role_list
        self.success = success

    def validate(self):
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['RoleList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_list = []
        if m.get('RoleList') is not None:
            for k in m.get('RoleList'):
                temp_model = GetMyRolesResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMyRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMyRolesResponseBody = None,
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
            temp_model = GetMyRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMyTenantsRequest(TeaModel):
    def __init__(
        self,
        feature_code_list: List[str] = None,
        op_tenant_id: int = None,
    ):
        self.feature_code_list = feature_code_list
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_code_list is not None:
            result['FeatureCodeList'] = self.feature_code_list
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureCodeList') is not None:
            self.feature_code_list = m.get('FeatureCodeList')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetMyTenantsShrinkRequest(TeaModel):
    def __init__(
        self,
        feature_code_list_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.feature_code_list_shrink = feature_code_list_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_code_list_shrink is not None:
            result['FeatureCodeList'] = self.feature_code_list_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureCodeList') is not None:
            self.feature_code_list_shrink = m.get('FeatureCodeList')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetMyTenantsResponseBodyTenantList(TeaModel):
    def __init__(
        self,
        delete_time: int = None,
        deleted: bool = None,
        description: str = None,
        id: int = None,
        name: str = None,
        ops_tenant: bool = None,
        owner_id: str = None,
        resource_limited: bool = None,
        tenant_type_list: List[str] = None,
        title_type: str = None,
        visible: bool = None,
    ):
        self.delete_time = delete_time
        self.deleted = deleted
        self.description = description
        self.id = id
        self.name = name
        self.ops_tenant = ops_tenant
        self.owner_id = owner_id
        self.resource_limited = resource_limited
        self.tenant_type_list = tenant_type_list
        self.title_type = title_type
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.ops_tenant is not None:
            result['OpsTenant'] = self.ops_tenant
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_limited is not None:
            result['ResourceLimited'] = self.resource_limited
        if self.tenant_type_list is not None:
            result['TenantTypeList'] = self.tenant_type_list
        if self.title_type is not None:
            result['TitleType'] = self.title_type
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OpsTenant') is not None:
            self.ops_tenant = m.get('OpsTenant')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceLimited') is not None:
            self.resource_limited = m.get('ResourceLimited')
        if m.get('TenantTypeList') is not None:
            self.tenant_type_list = m.get('TenantTypeList')
        if m.get('TitleType') is not None:
            self.title_type = m.get('TitleType')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetMyTenantsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant_list: List[GetMyTenantsResponseBodyTenantList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tenant_list = tenant_list

    def validate(self):
        if self.tenant_list:
            for k in self.tenant_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TenantList'] = []
        if self.tenant_list is not None:
            for k in self.tenant_list:
                result['TenantList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tenant_list = []
        if m.get('TenantList') is not None:
            for k in m.get('TenantList'):
                temp_model = GetMyTenantsResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k))
        return self


class GetMyTenantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMyTenantsResponseBody = None,
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
            temp_model = GetMyTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeUpDownStreamRequestNodeId(TeaModel):
    def __init__(
        self,
        field_id_list: str = None,
        id: str = None,
    ):
        self.field_id_list = field_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetNodeUpDownStreamRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        node_id: GetNodeUpDownStreamRequestNodeId = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.node_id = node_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.project_id = project_id
        self.up_stream_depth = up_stream_depth

    def validate(self):
        if self.node_id:
            self.node_id.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.node_id is not None:
            result['NodeId'] = self.node_id.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NodeId') is not None:
            temp_model = GetNodeUpDownStreamRequestNodeId()
            self.node_id = temp_model.from_map(m['NodeId'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')
        return self


class GetNodeUpDownStreamShrinkRequest(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        env: str = None,
        node_id_shrink: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
        up_stream_depth: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.env = env
        # This parameter is required.
        self.node_id_shrink = node_id_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.project_id = project_id
        self.up_stream_depth = up_stream_depth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        if self.env is not None:
            result['Env'] = self.env
        if self.node_id_shrink is not None:
            result['NodeId'] = self.node_id_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.up_stream_depth is not None:
            result['UpStreamDepth'] = self.up_stream_depth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NodeId') is not None:
            self.node_id_shrink = m.get('NodeId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('UpStreamDepth') is not None:
            self.up_stream_depth = m.get('UpStreamDepth')
        return self


class GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetNodeUpDownStreamResponseBodyNodeDagInfo(TeaModel):
    def __init__(
        self,
        down_stream_node_list: List[GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList] = None,
        start_node_list: List[GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList] = None,
        up_stream_node_list: List[GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList] = None,
    ):
        self.down_stream_node_list = down_stream_node_list
        self.start_node_list = start_node_list
        self.up_stream_node_list = up_stream_node_list

    def validate(self):
        if self.down_stream_node_list:
            for k in self.down_stream_node_list:
                if k:
                    k.validate()
        if self.start_node_list:
            for k in self.start_node_list:
                if k:
                    k.validate()
        if self.up_stream_node_list:
            for k in self.up_stream_node_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownStreamNodeList'] = []
        if self.down_stream_node_list is not None:
            for k in self.down_stream_node_list:
                result['DownStreamNodeList'].append(k.to_map() if k else None)
        result['StartNodeList'] = []
        if self.start_node_list is not None:
            for k in self.start_node_list:
                result['StartNodeList'].append(k.to_map() if k else None)
        result['UpStreamNodeList'] = []
        if self.up_stream_node_list is not None:
            for k in self.up_stream_node_list:
                result['UpStreamNodeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.down_stream_node_list = []
        if m.get('DownStreamNodeList') is not None:
            for k in m.get('DownStreamNodeList'):
                temp_model = GetNodeUpDownStreamResponseBodyNodeDagInfoDownStreamNodeList()
                self.down_stream_node_list.append(temp_model.from_map(k))
        self.start_node_list = []
        if m.get('StartNodeList') is not None:
            for k in m.get('StartNodeList'):
                temp_model = GetNodeUpDownStreamResponseBodyNodeDagInfoStartNodeList()
                self.start_node_list.append(temp_model.from_map(k))
        self.up_stream_node_list = []
        if m.get('UpStreamNodeList') is not None:
            for k in m.get('UpStreamNodeList'):
                temp_model = GetNodeUpDownStreamResponseBodyNodeDagInfoUpStreamNodeList()
                self.up_stream_node_list.append(temp_model.from_map(k))
        return self


class GetNodeUpDownStreamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_dag_info: GetNodeUpDownStreamResponseBodyNodeDagInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_dag_info = node_dag_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_dag_info:
            self.node_dag_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.node_dag_info is not None:
            result['NodeDagInfo'] = self.node_dag_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeDagInfo') is not None:
            temp_model = GetNodeUpDownStreamResponseBodyNodeDagInfo()
            self.node_dag_info = temp_model.from_map(m['NodeDagInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNodeUpDownStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeUpDownStreamResponseBody = None,
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
            temp_model = GetNodeUpDownStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationSubmitStatusRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        job_id: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetOperationSubmitStatusResponseBodyOperationSubmitJob(TeaModel):
    def __init__(
        self,
        external_biz_id: str = None,
        job_id: str = None,
        operation: str = None,
        operation_status: str = None,
        operator: str = None,
        progress: str = None,
    ):
        self.external_biz_id = external_biz_id
        self.job_id = job_id
        self.operation = operation
        self.operation_status = operation_status
        self.operator = operator
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_biz_id is not None:
            result['ExternalBizId'] = self.external_biz_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalBizId') is not None:
            self.external_biz_id = m.get('ExternalBizId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class GetOperationSubmitStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_submit_job: GetOperationSubmitStatusResponseBodyOperationSubmitJob = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.operation_submit_job = operation_submit_job
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.operation_submit_job:
            self.operation_submit_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.operation_submit_job is not None:
            result['OperationSubmitJob'] = self.operation_submit_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperationSubmitJob') is not None:
            temp_model = GetOperationSubmitStatusResponseBodyOperationSubmitJob()
            self.operation_submit_job = temp_model.from_map(m['OperationSubmitJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOperationSubmitStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOperationSubmitStatusResponseBody = None,
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
            temp_model = GetOperationSubmitStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalInstanceRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        instance_id: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetPhysicalInstanceResponseBodyInstanceNodeInfoCreator(TeaModel):
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


class GetPhysicalInstanceResponseBodyInstanceNodeInfoModifier(TeaModel):
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


class GetPhysicalInstanceResponseBodyInstanceNodeInfoOwnerList(TeaModel):
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


class GetPhysicalInstanceResponseBodyInstanceNodeInfo(TeaModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: GetPhysicalInstanceResponseBodyInstanceNodeInfoCreator = None,
        description: str = None,
        dry_run: bool = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: GetPhysicalInstanceResponseBodyInstanceNodeInfoModifier = None,
        name: str = None,
        owner_list: List[GetPhysicalInstanceResponseBodyInstanceNodeInfoOwnerList] = None,
        priority_list: List[str] = None,
        resource_group_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        sub_detail_type: str = None,
        type: str = None,
    ):
        self.biz_unit_name = biz_unit_name
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.dry_run = dry_run
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.resource_group_list = resource_group_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.sub_detail_type = sub_detail_type
        self.type = type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner_list:
            for k in self.owner_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.from_ is not None:
            result['From'] = self.from_
        if self.has_dev is not None:
            result['HasDev'] = self.has_dev
        if self.has_prod is not None:
            result['HasProd'] = self.has_prod
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['OwnerList'] = []
        if self.owner_list is not None:
            for k in self.owner_list:
                result['OwnerList'].append(k.to_map() if k else None)
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.resource_group_list is not None:
            result['ResourceGroupList'] = self.resource_group_list
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.sub_detail_type is not None:
            result['SubDetailType'] = self.sub_detail_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = GetPhysicalInstanceResponseBodyInstanceNodeInfoCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('HasDev') is not None:
            self.has_dev = m.get('HasDev')
        if m.get('HasProd') is not None:
            self.has_prod = m.get('HasProd')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = GetPhysicalInstanceResponseBodyInstanceNodeInfoModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k in m.get('OwnerList'):
                temp_model = GetPhysicalInstanceResponseBodyInstanceNodeInfoOwnerList()
                self.owner_list.append(temp_model.from_map(k))
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ResourceGroupList') is not None:
            self.resource_group_list = m.get('ResourceGroupList')
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPhysicalInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        due_time: str = None,
        duration: str = None,
        end_execute_time: int = None,
        extend_info: str = None,
        id: str = None,
        index: int = None,
        node_info: GetPhysicalInstanceResponseBodyInstanceNodeInfo = None,
        start_execute_time: int = None,
        status_list: List[str] = None,
    ):
        self.biz_date = biz_date
        self.due_time = due_time
        self.duration = duration
        self.end_execute_time = end_execute_time
        self.extend_info = extend_info
        self.id = id
        self.index = index
        self.node_info = node_info
        self.start_execute_time = start_execute_time
        self.status_list = status_list

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.id is not None:
            result['Id'] = self.id
        if self.index is not None:
            result['Index'] = self.index
        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()
        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NodeInfo') is not None:
            temp_model = GetPhysicalInstanceResponseBodyInstanceNodeInfo()
            self.node_info = temp_model.from_map(m['NodeInfo'])
        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class GetPhysicalInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance: GetPhysicalInstanceResponseBodyInstance = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance = instance
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Instance') is not None:
            temp_model = GetPhysicalInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalInstanceResponseBody = None,
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
            temp_model = GetPhysicalInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalInstanceLogRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        instance_id: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetPhysicalInstanceLogResponseBodyTaskrunLogList(TeaModel):
    def __init__(
        self,
        duration: str = None,
        end_time: str = None,
        log_content: str = None,
        start_time: str = None,
        status: str = None,
        taskrun_id: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.log_content = log_content
        self.start_time = start_time
        self.status = status
        self.taskrun_id = taskrun_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.taskrun_id is not None:
            result['TaskrunId'] = self.taskrun_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskrunId') is not None:
            self.taskrun_id = m.get('TaskrunId')
        return self


class GetPhysicalInstanceLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        taskrun_log_list: List[GetPhysicalInstanceLogResponseBodyTaskrunLogList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.taskrun_log_list = taskrun_log_list

    def validate(self):
        if self.taskrun_log_list:
            for k in self.taskrun_log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TaskrunLogList'] = []
        if self.taskrun_log_list is not None:
            for k in self.taskrun_log_list:
                result['TaskrunLogList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.taskrun_log_list = []
        if m.get('TaskrunLogList') is not None:
            for k in m.get('TaskrunLogList'):
                temp_model = GetPhysicalInstanceLogResponseBodyTaskrunLogList()
                self.taskrun_log_list.append(temp_model.from_map(k))
        return self


class GetPhysicalInstanceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalInstanceLogResponseBody = None,
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
            temp_model = GetPhysicalInstanceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalNodeRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        node_id: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.node_id = node_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetPhysicalNodeResponseBodyNodeInfoCreator(TeaModel):
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


class GetPhysicalNodeResponseBodyNodeInfoModifier(TeaModel):
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


class GetPhysicalNodeResponseBodyNodeInfoOwner(TeaModel):
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


class GetPhysicalNodeResponseBodyNodeInfoProjectInfo(TeaModel):
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


class GetPhysicalNodeResponseBodyNodeInfo(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        creator: GetPhysicalNodeResponseBodyNodeInfoCreator = None,
        cron_expression: str = None,
        data_source_id: int = None,
        data_source_schema: str = None,
        description: str = None,
        from_: str = None,
        id: str = None,
        last_modified_time: int = None,
        modifier: GetPhysicalNodeResponseBodyNodeInfoModifier = None,
        name: str = None,
        operator_type: str = None,
        output_name_list: List[str] = None,
        owner: GetPhysicalNodeResponseBodyNodeInfoOwner = None,
        priority: str = None,
        project_info: GetPhysicalNodeResponseBodyNodeInfoProjectInfo = None,
        schedule_type: str = None,
        status: str = None,
        trigger_config: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.cron_expression = cron_expression
        self.data_source_id = data_source_id
        self.data_source_schema = data_source_schema
        self.description = description
        self.from_ = from_
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.operator_type = operator_type
        self.output_name_list = output_name_list
        self.owner = owner
        self.priority = priority
        self.project_info = project_info
        self.schedule_type = schedule_type
        self.status = status
        self.trigger_config = trigger_config

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner:
            self.owner.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema
        if self.description is not None:
            result['Description'] = self.description
        if self.from_ is not None:
            result['From'] = self.from_
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.output_name_list is not None:
            result['OutputNameList'] = self.output_name_list
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = GetPhysicalNodeResponseBodyNodeInfoCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = GetPhysicalNodeResponseBodyNodeInfoModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OutputNameList') is not None:
            self.output_name_list = m.get('OutputNameList')
        if m.get('Owner') is not None:
            temp_model = GetPhysicalNodeResponseBodyNodeInfoOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProjectInfo') is not None:
            temp_model = GetPhysicalNodeResponseBodyNodeInfoProjectInfo()
            self.project_info = temp_model.from_map(m['ProjectInfo'])
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        return self


class GetPhysicalNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_info: GetPhysicalNodeResponseBodyNodeInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_info = node_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeInfo') is not None:
            temp_model = GetPhysicalNodeResponseBodyNodeInfo()
            self.node_info = temp_model.from_map(m['NodeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalNodeResponseBody = None,
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
            temp_model = GetPhysicalNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalNodeByOutputNameRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        output_name: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.output_name = output_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.output_name is not None:
            result['OutputName'] = self.output_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('OutputName') is not None:
            self.output_name = m.get('OutputName')
        return self


class GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator(TeaModel):
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


class GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier(TeaModel):
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


class GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner(TeaModel):
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


class GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo(TeaModel):
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


class GetPhysicalNodeByOutputNameResponseBodyNodeInfo(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        creator: GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator = None,
        description: str = None,
        from_: str = None,
        id: str = None,
        last_modified_time: int = None,
        modifier: GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier = None,
        name: str = None,
        operator_type: str = None,
        owner: GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner = None,
        priority: str = None,
        project_info: GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo = None,
        schedule_type: str = None,
        status: str = None,
        trigger_config: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.from_ = from_
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.operator_type = operator_type
        self.owner = owner
        self.priority = priority
        self.project_info = project_info
        self.schedule_type = schedule_type
        self.status = status
        self.trigger_config = trigger_config

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner:
            self.owner.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.from_ is not None:
            result['From'] = self.from_
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Owner') is not None:
            temp_model = GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProjectInfo') is not None:
            temp_model = GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo()
            self.project_info = temp_model.from_map(m['ProjectInfo'])
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')
        return self


class GetPhysicalNodeByOutputNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_info: GetPhysicalNodeByOutputNameResponseBodyNodeInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_info = node_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeInfo') is not None:
            temp_model = GetPhysicalNodeByOutputNameResponseBodyNodeInfo()
            self.node_info = temp_model.from_map(m['NodeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalNodeByOutputNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalNodeByOutputNameResponseBody = None,
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
            temp_model = GetPhysicalNodeByOutputNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalNodeContentRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        node_id: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.node_id = node_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetPhysicalNodeContentResponseBodyData(TeaModel):
    def __init__(
        self,
        code_content: str = None,
        node_id: str = None,
        node_name: str = None,
    ):
        self.code_content = code_content
        self.node_id = node_id
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_content is not None:
            result['CodeContent'] = self.code_content
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeContent') is not None:
            self.code_content = m.get('CodeContent')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetPhysicalNodeContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhysicalNodeContentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhysicalNodeContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalNodeContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalNodeContentResponseBody = None,
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
            temp_model = GetPhysicalNodeContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalNodeOperationLogRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        node_id: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.node_id = node_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetPhysicalNodeOperationLogResponseBodyOperationLogList(TeaModel):
    def __init__(
        self,
        context: str = None,
        operation_time: str = None,
        operation_type: str = None,
        operator: str = None,
        operator_name: str = None,
    ):
        self.context = context
        self.operation_time = operation_time
        self.operation_type = operation_type
        self.operator = operator
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['Context'] = self.context
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            self.context = m.get('Context')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        return self


class GetPhysicalNodeOperationLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        operation_log_list: List[GetPhysicalNodeOperationLogResponseBodyOperationLogList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.operation_log_list = operation_log_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.operation_log_list:
            for k in self.operation_log_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['OperationLogList'] = []
        if self.operation_log_list is not None:
            for k in self.operation_log_list:
                result['OperationLogList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.operation_log_list = []
        if m.get('OperationLogList') is not None:
            for k in m.get('OperationLogList'):
                temp_model = GetPhysicalNodeOperationLogResponseBodyOperationLogList()
                self.operation_log_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalNodeOperationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhysicalNodeOperationLogResponseBody = None,
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
            temp_model = GetPhysicalNodeOperationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectProduceUserRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectProduceUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectProduceUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user: GetProjectProduceUserResponseBodyUser = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = GetProjectProduceUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetProjectProduceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectProduceUserResponseBody = None,
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
            temp_model = GetProjectProduceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupplementDagrunRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        supplement_id: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.supplement_id = supplement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        return self


class GetSupplementDagrunResponseBodyDagrunList(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        duration: str = None,
        end_execute_time: int = None,
        id: str = None,
        start_execute_time: int = None,
        status: str = None,
        supplement_id: str = None,
    ):
        self.biz_date = biz_date
        self.duration = duration
        self.end_execute_time = end_execute_time
        # Dagrun ID
        self.id = id
        self.start_execute_time = start_execute_time
        self.status = status
        self.supplement_id = supplement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time
        if self.id is not None:
            result['Id'] = self.id
        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time
        if self.status is not None:
            result['Status'] = self.status
        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')
        return self


class GetSupplementDagrunResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dagrun_list: List[GetSupplementDagrunResponseBodyDagrunList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dagrun_list = dagrun_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dagrun_list:
            for k in self.dagrun_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DagrunList'] = []
        if self.dagrun_list is not None:
            for k in self.dagrun_list:
                result['DagrunList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.dagrun_list = []
        if m.get('DagrunList') is not None:
            for k in m.get('DagrunList'):
                temp_model = GetSupplementDagrunResponseBodyDagrunList()
                self.dagrun_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSupplementDagrunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSupplementDagrunResponseBody = None,
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
            temp_model = GetSupplementDagrunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupplementDagrunInstanceRequest(TeaModel):
    def __init__(
        self,
        dagrun_id: str = None,
        env: str = None,
        op_tenant_id: int = None,
    ):
        # Dagrun ID
        # 
        # This parameter is required.
        self.dagrun_id = dagrun_id
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dagrun_id is not None:
            result['DagrunId'] = self.dagrun_id
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagrunId') is not None:
            self.dagrun_id = m.get('DagrunId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoCreator(TeaModel):
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


class GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoModifier(TeaModel):
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


class GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoOwnerList(TeaModel):
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


class GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfo(TeaModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoCreator = None,
        description: str = None,
        dry_run: bool = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoModifier = None,
        name: str = None,
        owner_list: List[GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoOwnerList] = None,
        priority_list: List[str] = None,
        resource_group_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        sub_detail_type: str = None,
        type: str = None,
    ):
        self.biz_unit_name = biz_unit_name
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.dry_run = dry_run
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.resource_group_list = resource_group_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.sub_detail_type = sub_detail_type
        self.type = type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner_list:
            for k in self.owner_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.from_ is not None:
            result['From'] = self.from_
        if self.has_dev is not None:
            result['HasDev'] = self.has_dev
        if self.has_prod is not None:
            result['HasProd'] = self.has_prod
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['OwnerList'] = []
        if self.owner_list is not None:
            for k in self.owner_list:
                result['OwnerList'].append(k.to_map() if k else None)
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.resource_group_list is not None:
            result['ResourceGroupList'] = self.resource_group_list
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.sub_detail_type is not None:
            result['SubDetailType'] = self.sub_detail_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('HasDev') is not None:
            self.has_dev = m.get('HasDev')
        if m.get('HasProd') is not None:
            self.has_prod = m.get('HasProd')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k in m.get('OwnerList'):
                temp_model = GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfoOwnerList()
                self.owner_list.append(temp_model.from_map(k))
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ResourceGroupList') is not None:
            self.resource_group_list = m.get('ResourceGroupList')
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSupplementDagrunInstanceResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        biz_date: int = None,
        due_time: int = None,
        duration: str = None,
        end_execute_time: int = None,
        extend_info: str = None,
        id: str = None,
        index: int = None,
        node_info: GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfo = None,
        start_execute_time: int = None,
        status_list: List[str] = None,
        type: str = None,
    ):
        self.biz_date = biz_date
        self.due_time = due_time
        self.duration = duration
        self.end_execute_time = end_execute_time
        self.extend_info = extend_info
        self.id = id
        self.index = index
        self.node_info = node_info
        self.start_execute_time = start_execute_time
        self.status_list = status_list
        self.type = type

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.id is not None:
            result['Id'] = self.id
        if self.index is not None:
            result['Index'] = self.index
        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()
        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NodeInfo') is not None:
            temp_model = GetSupplementDagrunInstanceResponseBodyInstanceListNodeInfo()
            self.node_info = temp_model.from_map(m['NodeInfo'])
        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSupplementDagrunInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_list: List[GetSupplementDagrunInstanceResponseBodyInstanceList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_list = instance_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetSupplementDagrunInstanceResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSupplementDagrunInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSupplementDagrunInstanceResponseBody = None,
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
            temp_model = GetSupplementDagrunInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserBySourceIdRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        source_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class GetUserBySourceIdResponseBodyUser(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
    ):
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserBySourceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user: GetUserBySourceIdResponseBodyUser = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = GetUserBySourceIdResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserBySourceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserBySourceIdResponseBody = None,
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
            temp_model = GetUserBySourceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBodyUserGroupInfoAdminList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetUserGroupResponseBodyUserGroupInfo(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin_list: List[GetUserGroupResponseBodyUserGroupInfoAdminList] = None,
        description: str = None,
        id: str = None,
        my_role: str = None,
        name: str = None,
    ):
        self.active = active
        self.admin_list = admin_list
        self.description = description
        self.id = id
        self.my_role = my_role
        self.name = name

    def validate(self):
        if self.admin_list:
            for k in self.admin_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        result['AdminList'] = []
        if self.admin_list is not None:
            for k in self.admin_list:
                result['AdminList'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.my_role is not None:
            result['MyRole'] = self.my_role
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        self.admin_list = []
        if m.get('AdminList') is not None:
            for k in m.get('AdminList'):
                temp_model = GetUserGroupResponseBodyUserGroupInfoAdminList()
                self.admin_list.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MyRole') is not None:
            self.my_role = m.get('MyRole')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_group_info: GetUserGroupResponseBodyUserGroupInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_group_info = user_group_info

    def validate(self):
        if self.user_group_info:
            self.user_group_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_group_info is not None:
            result['UserGroupInfo'] = self.user_group_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserGroupInfo') is not None:
            temp_model = GetUserGroupResponseBodyUserGroupInfo()
            self.user_group_info = temp_model.from_map(m['UserGroupInfo'])
        return self


class GetUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserGroupResponseBody = None,
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
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUsersRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class GetUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        user_id_list_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_id_list_shrink = user_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.user_id_list_shrink is not None:
            result['UserIdList'] = self.user_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UserIdList') is not None:
            self.user_id_list_shrink = m.get('UserIdList')
        return self


class GetUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        display_name_without_status: str = None,
        enable_white_ip: str = None,
        fei_shu_robot: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        mail: str = None,
        mobile_phone: str = None,
        name: str = None,
        nick_name: str = None,
        parent_id: str = None,
        real_name: str = None,
        source_id: str = None,
        source_type: str = None,
        we_chat_robot: str = None,
        white_ip: str = None,
    ):
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.display_name_without_status = display_name_without_status
        self.enable_white_ip = enable_white_ip
        self.fei_shu_robot = fei_shu_robot
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.name = name
        self.nick_name = nick_name
        self.parent_id = parent_id
        self.real_name = real_name
        self.source_id = source_id
        self.source_type = source_type
        self.we_chat_robot = we_chat_robot
        self.white_ip = white_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.display_name_without_status is not None:
            result['DisplayNameWithoutStatus'] = self.display_name_without_status
        if self.enable_white_ip is not None:
            result['EnableWhiteIp'] = self.enable_white_ip
        if self.fei_shu_robot is not None:
            result['FeiShuRobot'] = self.fei_shu_robot
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.name is not None:
            result['Name'] = self.name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.we_chat_robot is not None:
            result['WeChatRobot'] = self.we_chat_robot
        if self.white_ip is not None:
            result['WhiteIp'] = self.white_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DisplayNameWithoutStatus') is not None:
            self.display_name_without_status = m.get('DisplayNameWithoutStatus')
        if m.get('EnableWhiteIp') is not None:
            self.enable_white_ip = m.get('EnableWhiteIp')
        if m.get('FeiShuRobot') is not None:
            self.fei_shu_robot = m.get('FeiShuRobot')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('WeChatRobot') is not None:
            self.we_chat_robot = m.get('WeChatRobot')
        if m.get('WhiteIp') is not None:
            self.white_ip = m.get('WhiteIp')
        return self


class GetUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_list: List[GetUsersResponseBodyUserList] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = GetUsersResponseBodyUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class GetUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUsersResponseBody = None,
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
            temp_model = GetUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantResourcePermissionRequestGrantCommandResourceList(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GrantResourcePermissionRequestGrantCommand(TeaModel):
    def __init__(
        self,
        effective_end: str = None,
        operate_list: List[str] = None,
        reason: str = None,
        resource_list: List[GrantResourcePermissionRequestGrantCommandResourceList] = None,
        resource_type: str = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.effective_end = effective_end
        # This parameter is required.
        self.operate_list = operate_list
        self.reason = reason
        # This parameter is required.
        self.resource_list = resource_list
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.user_id_list = user_id_list

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_end is not None:
            result['EffectiveEnd'] = self.effective_end
        if self.operate_list is not None:
            result['OperateList'] = self.operate_list
        if self.reason is not None:
            result['Reason'] = self.reason
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveEnd') is not None:
            self.effective_end = m.get('EffectiveEnd')
        if m.get('OperateList') is not None:
            self.operate_list = m.get('OperateList')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = GrantResourcePermissionRequestGrantCommandResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class GrantResourcePermissionRequest(TeaModel):
    def __init__(
        self,
        grant_command: GrantResourcePermissionRequestGrantCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.grant_command = grant_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.grant_command:
            self.grant_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_command is not None:
            result['GrantCommand'] = self.grant_command.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantCommand') is not None:
            temp_model = GrantResourcePermissionRequestGrantCommand()
            self.grant_command = temp_model.from_map(m['GrantCommand'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GrantResourcePermissionShrinkRequest(TeaModel):
    def __init__(
        self,
        grant_command_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.grant_command_shrink = grant_command_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_command_shrink is not None:
            result['GrantCommand'] = self.grant_command_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantCommand') is not None:
            self.grant_command_shrink = m.get('GrantCommand')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class GrantResourcePermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantResourcePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantResourcePermissionResponseBody = None,
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
            temp_model = GrantResourcePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddableRolesRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListAddableRolesResponseBodyRoleList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListAddableRolesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        role_list: List[ListAddableRolesResponseBodyRoleList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.role_list = role_list
        self.success = success

    def validate(self):
        if self.role_list:
            for k in self.role_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleList'] = []
        if self.role_list is not None:
            for k in self.role_list:
                result['RoleList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_list = []
        if m.get('RoleList') is not None:
            for k in m.get('RoleList'):
                temp_model = ListAddableRolesResponseBodyRoleList()
                self.role_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAddableRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddableRolesResponseBody = None,
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
            temp_model = ListAddableRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddableUsersRequestListQuery(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        search_text: str = None,
    ):
        self.page = page
        self.page_size = page_size
        self.search_text = search_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        return self


class ListAddableUsersRequest(TeaModel):
    def __init__(
        self,
        list_query: ListAddableUsersRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListAddableUsersRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListAddableUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListAddableUsersResponseBodyPageResultUserList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        display_name_without_status: str = None,
        enable_white_ip: str = None,
        fei_shu_robot: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        mail: str = None,
        mobile_phone: str = None,
        name: str = None,
        nick_name: str = None,
        parent_id: str = None,
        real_name: str = None,
        source_id: str = None,
        source_type: str = None,
        we_chat_robot: str = None,
        white_ip: str = None,
    ):
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.display_name_without_status = display_name_without_status
        self.enable_white_ip = enable_white_ip
        self.fei_shu_robot = fei_shu_robot
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.name = name
        self.nick_name = nick_name
        self.parent_id = parent_id
        self.real_name = real_name
        self.source_id = source_id
        self.source_type = source_type
        self.we_chat_robot = we_chat_robot
        self.white_ip = white_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.display_name_without_status is not None:
            result['DisplayNameWithoutStatus'] = self.display_name_without_status
        if self.enable_white_ip is not None:
            result['EnableWhiteIp'] = self.enable_white_ip
        if self.fei_shu_robot is not None:
            result['FeiShuRobot'] = self.fei_shu_robot
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.name is not None:
            result['Name'] = self.name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.we_chat_robot is not None:
            result['WeChatRobot'] = self.we_chat_robot
        if self.white_ip is not None:
            result['WhiteIp'] = self.white_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DisplayNameWithoutStatus') is not None:
            self.display_name_without_status = m.get('DisplayNameWithoutStatus')
        if m.get('EnableWhiteIp') is not None:
            self.enable_white_ip = m.get('EnableWhiteIp')
        if m.get('FeiShuRobot') is not None:
            self.fei_shu_robot = m.get('FeiShuRobot')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('WeChatRobot') is not None:
            self.we_chat_robot = m.get('WeChatRobot')
        if m.get('WhiteIp') is not None:
            self.white_ip = m.get('WhiteIp')
        return self


class ListAddableUsersResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        user_list: List[ListAddableUsersResponseBodyPageResultUserList] = None,
    ):
        self.total_count = total_count
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = ListAddableUsersResponseBodyPageResultUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListAddableUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListAddableUsersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListAddableUsersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAddableUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddableUsersResponseBody = None,
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
            temp_model = ListAddableUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceWithConfigRequestListQuery(TeaModel):
    def __init__(
        self,
        name: str = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        scope_list: List[str] = None,
        tag: str = None,
        type_list: List[str] = None,
    ):
        self.name = name
        self.owner_list = owner_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.scope_list = scope_list
        self.tag = tag
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type_list is not None:
            result['TypeList'] = self.type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')
        return self


class ListDataSourceWithConfigRequest(TeaModel):
    def __init__(
        self,
        list_query: ListDataSourceWithConfigRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListDataSourceWithConfigRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListDataSourceWithConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList(TeaModel):
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


class ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo(TeaModel):
    def __init__(
        self,
        config_item_list: List[ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList] = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.config_item_list = config_item_list
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.scope = scope
        self.type = type

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.description is not None:
            result['Description'] = self.description
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfoConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList(TeaModel):
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


class ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo(TeaModel):
    def __init__(
        self,
        config_item_list: List[ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList] = None,
        create_time: int = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.config_item_list = config_item_list
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.env = env
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.scope = scope
        self.type = type

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.description is not None:
            result['Description'] = self.description
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfoConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDataSourceWithConfigResponseBodyPageResultDataSourceList(TeaModel):
    def __init__(
        self,
        dev_data_source_info: ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo = None,
        prod_data_source_info: ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo = None,
    ):
        # 开发环境数据源信息
        self.dev_data_source_info = dev_data_source_info
        # 生产环境数据源
        self.prod_data_source_info = prod_data_source_info

    def validate(self):
        if self.dev_data_source_info:
            self.dev_data_source_info.validate()
        if self.prod_data_source_info:
            self.prod_data_source_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dev_data_source_info is not None:
            result['DevDataSourceInfo'] = self.dev_data_source_info.to_map()
        if self.prod_data_source_info is not None:
            result['ProdDataSourceInfo'] = self.prod_data_source_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevDataSourceInfo') is not None:
            temp_model = ListDataSourceWithConfigResponseBodyPageResultDataSourceListDevDataSourceInfo()
            self.dev_data_source_info = temp_model.from_map(m['DevDataSourceInfo'])
        if m.get('ProdDataSourceInfo') is not None:
            temp_model = ListDataSourceWithConfigResponseBodyPageResultDataSourceListProdDataSourceInfo()
            self.prod_data_source_info = temp_model.from_map(m['ProdDataSourceInfo'])
        return self


class ListDataSourceWithConfigResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        data_source_list: List[ListDataSourceWithConfigResponseBodyPageResultDataSourceList] = None,
        total_count: int = None,
    ):
        self.data_source_list = data_source_list
        self.total_count = total_count

    def validate(self):
        if self.data_source_list:
            for k in self.data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSourceList'] = []
        if self.data_source_list is not None:
            for k in self.data_source_list:
                result['DataSourceList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_list = []
        if m.get('DataSourceList') is not None:
            for k in m.get('DataSourceList'):
                temp_model = ListDataSourceWithConfigResponseBodyPageResultDataSourceList()
                self.data_source_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataSourceWithConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListDataSourceWithConfigResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListDataSourceWithConfigResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSourceWithConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceWithConfigResponseBody = None,
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
            temp_model = ListDataSourceWithConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFilesRequestListQuery(TeaModel):
    def __init__(
        self,
        category: str = None,
        directory: str = None,
        env: str = None,
        project_id: int = None,
        recursive: bool = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.recursive = recursive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.env is not None:
            result['Env'] = self.env
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        return self


class ListFilesRequest(TeaModel):
    def __init__(
        self,
        list_query: ListFilesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListFilesRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListFilesResponseBodyFileList(TeaModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        creator: str = None,
        directory: str = None,
        file_type: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        last_modifier: str = None,
        name: str = None,
        project_id: int = None,
    ):
        self.category = category
        self.content = content
        self.creator = creator
        self.directory = directory
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.last_modifier = last_modifier
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifier') is not None:
            self.last_modifier = m.get('LastModifier')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListFilesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        file_list: List[ListFilesResponseBodyFileList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.file_list = file_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = ListFilesResponseBodyFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFilesResponseBody = None,
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
            temp_model = ListFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequestListQuery(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_unit_id: int = None,
        max_biz_date: str = None,
        max_run_date: str = None,
        min_biz_date: str = None,
        min_run_date: str = None,
        node_id: str = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        priority_list: List[str] = None,
        project_id: int = None,
        run_status_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        schedule_type: str = None,
        search_text: str = None,
        sub_biz_type_list: List[str] = None,
    ):
        self.biz_type = biz_type
        self.biz_unit_id = biz_unit_id
        self.max_biz_date = max_biz_date
        self.max_run_date = max_run_date
        self.min_biz_date = min_biz_date
        self.min_run_date = min_run_date
        self.node_id = node_id
        self.owner_list = owner_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.priority_list = priority_list
        # This parameter is required.
        self.project_id = project_id
        self.run_status_list = run_status_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        # This parameter is required.
        self.schedule_type = schedule_type
        self.search_text = search_text
        self.sub_biz_type_list = sub_biz_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id
        if self.max_biz_date is not None:
            result['MaxBizDate'] = self.max_biz_date
        if self.max_run_date is not None:
            result['MaxRunDate'] = self.max_run_date
        if self.min_biz_date is not None:
            result['MinBizDate'] = self.min_biz_date
        if self.min_run_date is not None:
            result['MinRunDate'] = self.min_run_date
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.run_status_list is not None:
            result['RunStatusList'] = self.run_status_list
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.sub_biz_type_list is not None:
            result['SubBizTypeList'] = self.sub_biz_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')
        if m.get('MaxBizDate') is not None:
            self.max_biz_date = m.get('MaxBizDate')
        if m.get('MaxRunDate') is not None:
            self.max_run_date = m.get('MaxRunDate')
        if m.get('MinBizDate') is not None:
            self.min_biz_date = m.get('MinBizDate')
        if m.get('MinRunDate') is not None:
            self.min_run_date = m.get('MinRunDate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RunStatusList') is not None:
            self.run_status_list = m.get('RunStatusList')
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('SubBizTypeList') is not None:
            self.sub_biz_type_list = m.get('SubBizTypeList')
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query: ListInstancesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            temp_model = ListInstancesRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListInstancesResponseBodyPageResultDataNodeInfoCreator(TeaModel):
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


class ListInstancesResponseBodyPageResultDataNodeInfoModifier(TeaModel):
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


class ListInstancesResponseBodyPageResultDataNodeInfoOwnerList(TeaModel):
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


class ListInstancesResponseBodyPageResultDataNodeInfo(TeaModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: ListInstancesResponseBodyPageResultDataNodeInfoCreator = None,
        description: str = None,
        dry_run: bool = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: ListInstancesResponseBodyPageResultDataNodeInfoModifier = None,
        name: str = None,
        owner_list: List[ListInstancesResponseBodyPageResultDataNodeInfoOwnerList] = None,
        priority_list: List[str] = None,
        resource_group_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        sub_detail_type: str = None,
        type: str = None,
    ):
        self.biz_unit_name = biz_unit_name
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.dry_run = dry_run
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.resource_group_list = resource_group_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.sub_detail_type = sub_detail_type
        self.type = type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner_list:
            for k in self.owner_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.from_ is not None:
            result['From'] = self.from_
        if self.has_dev is not None:
            result['HasDev'] = self.has_dev
        if self.has_prod is not None:
            result['HasProd'] = self.has_prod
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['OwnerList'] = []
        if self.owner_list is not None:
            for k in self.owner_list:
                result['OwnerList'].append(k.to_map() if k else None)
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.resource_group_list is not None:
            result['ResourceGroupList'] = self.resource_group_list
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.sub_detail_type is not None:
            result['SubDetailType'] = self.sub_detail_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = ListInstancesResponseBodyPageResultDataNodeInfoCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('HasDev') is not None:
            self.has_dev = m.get('HasDev')
        if m.get('HasProd') is not None:
            self.has_prod = m.get('HasProd')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = ListInstancesResponseBodyPageResultDataNodeInfoModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k in m.get('OwnerList'):
                temp_model = ListInstancesResponseBodyPageResultDataNodeInfoOwnerList()
                self.owner_list.append(temp_model.from_map(k))
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ResourceGroupList') is not None:
            self.resource_group_list = m.get('ResourceGroupList')
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyPageResultData(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        due_time: str = None,
        duration: str = None,
        end_execute_time: int = None,
        extend_info: str = None,
        id: str = None,
        index: int = None,
        node_info: ListInstancesResponseBodyPageResultDataNodeInfo = None,
        start_execute_time: int = None,
        status_list: List[str] = None,
    ):
        self.biz_date = biz_date
        self.due_time = due_time
        self.duration = duration
        self.end_execute_time = end_execute_time
        self.extend_info = extend_info
        self.id = id
        self.index = index
        self.node_info = node_info
        self.start_execute_time = start_execute_time
        self.status_list = status_list

    def validate(self):
        if self.node_info:
            self.node_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.due_time is not None:
            result['DueTime'] = self.due_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.id is not None:
            result['Id'] = self.id
        if self.index is not None:
            result['Index'] = self.index
        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()
        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('DueTime') is not None:
            self.due_time = m.get('DueTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NodeInfo') is not None:
            temp_model = ListInstancesResponseBodyPageResultDataNodeInfo()
            self.node_info = temp_model.from_map(m['NodeInfo'])
        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class ListInstancesResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        data: List[ListInstancesResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListInstancesResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListInstancesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListInstancesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeDownStreamRequestListQueryFilterList(TeaModel):
    def __init__(
        self,
        exclude: bool = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        self.exclude = exclude
        self.key = key
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude is not None:
            result['Exclude'] = self.exclude
        if self.key is not None:
            result['Key'] = self.key
        if self.value_list is not None:
            result['ValueList'] = self.value_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')
        return self


class ListNodeDownStreamRequestListQueryNodeIdList(TeaModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_id_list = field_id_list
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListNodeDownStreamRequestListQuery(TeaModel):
    def __init__(
        self,
        down_stream_depth: int = None,
        filter_list: List[ListNodeDownStreamRequestListQueryFilterList] = None,
        node_id_list: List[ListNodeDownStreamRequestListQueryNodeIdList] = None,
        project_id: int = None,
    ):
        self.down_stream_depth = down_stream_depth
        self.filter_list = filter_list
        # This parameter is required.
        self.node_id_list = node_id_list
        self.project_id = project_id

    def validate(self):
        if self.filter_list:
            for k in self.filter_list:
                if k:
                    k.validate()
        if self.node_id_list:
            for k in self.node_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_stream_depth is not None:
            result['DownStreamDepth'] = self.down_stream_depth
        result['FilterList'] = []
        if self.filter_list is not None:
            for k in self.filter_list:
                result['FilterList'].append(k.to_map() if k else None)
        result['NodeIdList'] = []
        if self.node_id_list is not None:
            for k in self.node_id_list:
                result['NodeIdList'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownStreamDepth') is not None:
            self.down_stream_depth = m.get('DownStreamDepth')
        self.filter_list = []
        if m.get('FilterList') is not None:
            for k in m.get('FilterList'):
                temp_model = ListNodeDownStreamRequestListQueryFilterList()
                self.filter_list.append(temp_model.from_map(k))
        self.node_id_list = []
        if m.get('NodeIdList') is not None:
            for k in m.get('NodeIdList'):
                temp_model = ListNodeDownStreamRequestListQueryNodeIdList()
                self.node_id_list.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListNodeDownStreamRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query: ListNodeDownStreamRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            temp_model = ListNodeDownStreamRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListNodeDownStreamShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListNodeDownStreamResponseBodyNodeInfoList(TeaModel):
    def __init__(
        self,
        depth: int = None,
        field_id_list: List[str] = None,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.depth = depth
        self.field_id_list = field_id_list
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodeDownStreamResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_info_list: List[ListNodeDownStreamResponseBodyNodeInfoList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_info_list = node_info_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_info_list:
            for k in self.node_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['NodeInfoList'] = []
        if self.node_info_list is not None:
            for k in self.node_info_list:
                result['NodeInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.node_info_list = []
        if m.get('NodeInfoList') is not None:
            for k in m.get('NodeInfoList'):
                temp_model = ListNodeDownStreamResponseBodyNodeInfoList()
                self.node_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodeDownStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeDownStreamResponseBody = None,
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
            temp_model = ListNodeDownStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequestListQuery(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
        node_biz_type: str = None,
        node_sub_biz_type_list: List[str] = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        priority_list: List[str] = None,
        project_id: int = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        schedule_type: str = None,
        search_text: str = None,
    ):
        self.dry_run = dry_run
        # This parameter is required.
        self.node_biz_type = node_biz_type
        # This parameter is required.
        self.node_sub_biz_type_list = node_sub_biz_type_list
        self.owner_list = owner_list
        self.page = page
        self.page_size = page_size
        self.priority_list = priority_list
        # This parameter is required.
        self.project_id = project_id
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.schedule_type = schedule_type
        self.search_text = search_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.node_biz_type is not None:
            result['NodeBizType'] = self.node_biz_type
        if self.node_sub_biz_type_list is not None:
            result['NodeSubBizTypeList'] = self.node_sub_biz_type_list
        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NodeBizType') is not None:
            self.node_biz_type = m.get('NodeBizType')
        if m.get('NodeSubBizTypeList') is not None:
            self.node_sub_biz_type_list = m.get('NodeSubBizTypeList')
        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query: ListNodesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            temp_model = ListNodesRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        self.env = env
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListNodesResponseBodyPageResultNodeListCreator(TeaModel):
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


class ListNodesResponseBodyPageResultNodeListModifier(TeaModel):
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


class ListNodesResponseBodyPageResultNodeListOwnerList(TeaModel):
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


class ListNodesResponseBodyPageResultNodeListProjectInfo(TeaModel):
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


class ListNodesResponseBodyPageResultNodeList(TeaModel):
    def __init__(
        self,
        biz_unit_name: str = None,
        create_time: str = None,
        creator: ListNodesResponseBodyPageResultNodeListCreator = None,
        description: str = None,
        dry_run: bool = None,
        extend_info: str = None,
        from_: str = None,
        has_dev: bool = None,
        has_prod: bool = None,
        id: str = None,
        last_modified_time: str = None,
        modifier: ListNodesResponseBodyPageResultNodeListModifier = None,
        name: str = None,
        owner_list: List[ListNodesResponseBodyPageResultNodeListOwnerList] = None,
        priority_list: List[str] = None,
        project_info: ListNodesResponseBodyPageResultNodeListProjectInfo = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        sub_detail_type: str = None,
        type: str = None,
    ):
        self.biz_unit_name = biz_unit_name
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.dry_run = dry_run
        self.extend_info = extend_info
        self.from_ = from_
        self.has_dev = has_dev
        self.has_prod = has_prod
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.owner_list = owner_list
        self.priority_list = priority_list
        self.project_info = project_info
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.sub_detail_type = sub_detail_type
        self.type = type

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner_list:
            for k in self.owner_list:
                if k:
                    k.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.from_ is not None:
            result['From'] = self.from_
        if self.has_dev is not None:
            result['HasDev'] = self.has_dev
        if self.has_prod is not None:
            result['HasProd'] = self.has_prod
        if self.id is not None:
            result['Id'] = self.id
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['OwnerList'] = []
        if self.owner_list is not None:
            for k in self.owner_list:
                result['OwnerList'].append(k.to_map() if k else None)
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()
        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused
        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list
        if self.sub_detail_type is not None:
            result['SubDetailType'] = self.sub_detail_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            temp_model = ListNodesResponseBodyPageResultNodeListCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('From') is not None:
            self.from_ = m.get('From')
        if m.get('HasDev') is not None:
            self.has_dev = m.get('HasDev')
        if m.get('HasProd') is not None:
            self.has_prod = m.get('HasProd')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = ListNodesResponseBodyPageResultNodeListModifier()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k in m.get('OwnerList'):
                temp_model = ListNodesResponseBodyPageResultNodeListOwnerList()
                self.owner_list.append(temp_model.from_map(k))
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('ProjectInfo') is not None:
            temp_model = ListNodesResponseBodyPageResultNodeListProjectInfo()
            self.project_info = temp_model.from_map(m['ProjectInfo'])
        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')
        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')
        if m.get('SubDetailType') is not None:
            self.sub_detail_type = m.get('SubDetailType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodesResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        node_list: List[ListNodesResponseBodyPageResultNodeList] = None,
        total_count: int = None,
    ):
        self.node_list = node_list
        self.total_count = total_count

    def validate(self):
        if self.node_list:
            for k in self.node_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeList'] = []
        if self.node_list is not None:
            for k in self.node_list:
                result['NodeList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_list = []
        if m.get('NodeList') is not None:
            for k in m.get('NodeList'):
                temp_model = ListNodesResponseBodyPageResultNodeList()
                self.node_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListNodesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListNodesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
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
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcePermissionOperationLogRequestListQuery(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        search_text: str = None,
        tab_type: str = None,
    ):
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.search_text = search_text
        # This parameter is required.
        self.tab_type = tab_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.tab_type is not None:
            result['TabType'] = self.tab_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('TabType') is not None:
            self.tab_type = m.get('TabType')
        return self


class ListResourcePermissionOperationLogRequest(TeaModel):
    def __init__(
        self,
        list_query: ListResourcePermissionOperationLogRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListResourcePermissionOperationLogRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListResourcePermissionOperationLogShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataAccount(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        # Id
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: int = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo(TeaModel):
    def __init__(
        self,
        biz_unit_info: ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo = None,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
        project_info: ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo = None,
        type: str = None,
    ):
        self.biz_unit_info = biz_unit_info
        self.display_name = display_name
        self.env = env
        self.id = id
        self.name = name
        self.project_info = project_info
        self.type = type

    def validate(self):
        if self.biz_unit_info:
            self.biz_unit_info.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_info is not None:
            result['BizUnitInfo'] = self.biz_unit_info.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitInfo') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoBizUnitInfo()
            self.biz_unit_info = temp_model.from_map(m['BizUnitInfo'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectInfo') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfoProjectInfo()
            self.project_info = temp_model.from_map(m['ProjectInfo'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionOperationLogResponseBodyPageResultData(TeaModel):
    def __init__(
        self,
        account: ListResourcePermissionOperationLogResponseBodyPageResultDataAccount = None,
        auth_scope: str = None,
        operate_id: int = None,
        operate_time: int = None,
        operate_type: str = None,
        period: ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod = None,
        reason: str = None,
        resource_info: ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo = None,
        target_account: ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount = None,
    ):
        self.account = account
        self.auth_scope = auth_scope
        self.operate_id = operate_id
        self.operate_time = operate_time
        self.operate_type = operate_type
        self.period = period
        self.reason = reason
        self.resource_info = resource_info
        self.target_account = target_account

    def validate(self):
        if self.account:
            self.account.validate()
        if self.period:
            self.period.validate()
        if self.resource_info:
            self.resource_info.validate()
        if self.target_account:
            self.target_account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account.to_map()
        if self.auth_scope is not None:
            result['AuthScope'] = self.auth_scope
        if self.operate_id is not None:
            result['OperateId'] = self.operate_id
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()
        if self.target_account is not None:
            result['TargetAccount'] = self.target_account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataAccount()
            self.account = temp_model.from_map(m['Account'])
        if m.get('AuthScope') is not None:
            self.auth_scope = m.get('AuthScope')
        if m.get('OperateId') is not None:
            self.operate_id = m.get('OperateId')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Period') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ResourceInfo') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataResourceInfo()
            self.resource_info = temp_model.from_map(m['ResourceInfo'])
        if m.get('TargetAccount') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResultDataTargetAccount()
            self.target_account = temp_model.from_map(m['TargetAccount'])
        return self


class ListResourcePermissionOperationLogResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        data: List[ListResourcePermissionOperationLogResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListResourcePermissionOperationLogResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcePermissionOperationLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListResourcePermissionOperationLogResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListResourcePermissionOperationLogResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListResourcePermissionOperationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcePermissionOperationLogResponseBody = None,
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
            temp_model = ListResourcePermissionOperationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcePermissionsRequestListQuery(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        search_text: str = None,
        tab_type: str = None,
    ):
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.search_text = search_text
        # This parameter is required.
        self.tab_type = tab_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.tab_type is not None:
            result['TabType'] = self.tab_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('TabType') is not None:
            self.tab_type = m.get('TabType')
        return self


class ListResourcePermissionsRequest(TeaModel):
    def __init__(
        self,
        list_query: ListResourcePermissionsRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListResourcePermissionsRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListResourcePermissionsShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListResourcePermissionsResponseBodyPageResultDataPeriod(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList(TeaModel):
    def __init__(
        self,
        period: ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod = None,
        permission_type: str = None,
    ):
        self.period = period
        self.permission_type = permission_type

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodListPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        return self


class ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        # Id
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        env: str = None,
        id: int = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.env = env
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListResourcePermissionsResponseBodyPageResultDataResourceInfo(TeaModel):
    def __init__(
        self,
        biz_unit_info: ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo = None,
        display_name: str = None,
        env: str = None,
        id: str = None,
        name: str = None,
        project_info: ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo = None,
        type: str = None,
    ):
        self.biz_unit_info = biz_unit_info
        self.display_name = display_name
        self.env = env
        self.id = id
        self.name = name
        self.project_info = project_info
        self.type = type

    def validate(self):
        if self.biz_unit_info:
            self.biz_unit_info.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_unit_info is not None:
            result['BizUnitInfo'] = self.biz_unit_info.to_map()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.env is not None:
            result['Env'] = self.env
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitInfo') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataResourceInfoBizUnitInfo()
            self.biz_unit_info = temp_model.from_map(m['BizUnitInfo'])
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectInfo') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataResourceInfoProjectInfo()
            self.project_info = temp_model.from_map(m['ProjectInfo'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionsResponseBodyPageResultDataTargetAccount(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcePermissionsResponseBodyPageResultData(TeaModel):
    def __init__(
        self,
        auth_scope: str = None,
        period: ListResourcePermissionsResponseBodyPageResultDataPeriod = None,
        permission_period_list: List[ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList] = None,
        record_id: str = None,
        resource_info: ListResourcePermissionsResponseBodyPageResultDataResourceInfo = None,
        target_account: ListResourcePermissionsResponseBodyPageResultDataTargetAccount = None,
    ):
        self.auth_scope = auth_scope
        self.period = period
        self.permission_period_list = permission_period_list
        self.record_id = record_id
        self.resource_info = resource_info
        self.target_account = target_account

    def validate(self):
        if self.period:
            self.period.validate()
        if self.permission_period_list:
            for k in self.permission_period_list:
                if k:
                    k.validate()
        if self.resource_info:
            self.resource_info.validate()
        if self.target_account:
            self.target_account.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_scope is not None:
            result['AuthScope'] = self.auth_scope
        if self.period is not None:
            result['Period'] = self.period.to_map()
        result['PermissionPeriodList'] = []
        if self.permission_period_list is not None:
            for k in self.permission_period_list:
                result['PermissionPeriodList'].append(k.to_map() if k else None)
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info.to_map()
        if self.target_account is not None:
            result['TargetAccount'] = self.target_account.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthScope') is not None:
            self.auth_scope = m.get('AuthScope')
        if m.get('Period') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataPeriod()
            self.period = temp_model.from_map(m['Period'])
        self.permission_period_list = []
        if m.get('PermissionPeriodList') is not None:
            for k in m.get('PermissionPeriodList'):
                temp_model = ListResourcePermissionsResponseBodyPageResultDataPermissionPeriodList()
                self.permission_period_list.append(temp_model.from_map(k))
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceInfo') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataResourceInfo()
            self.resource_info = temp_model.from_map(m['ResourceInfo'])
        if m.get('TargetAccount') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResultDataTargetAccount()
            self.target_account = temp_model.from_map(m['TargetAccount'])
        return self


class ListResourcePermissionsResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        data: List[ListResourcePermissionsResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListResourcePermissionsResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListResourcePermissionsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListResourcePermissionsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListResourcePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcePermissionsResponseBody = None,
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
            temp_model = ListResourcePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantMembersRequestListQuery(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        role_list: List[str] = None,
        search_text: str = None,
        user_group_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.role_list = role_list
        self.search_text = search_text
        self.user_group_id_list = user_group_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_list is not None:
            result['RoleList'] = self.role_list
        if self.search_text is not None:
            result['SearchText'] = self.search_text
        if self.user_group_id_list is not None:
            result['UserGroupIdList'] = self.user_group_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')
        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')
        if m.get('UserGroupIdList') is not None:
            self.user_group_id_list = m.get('UserGroupIdList')
        return self


class ListTenantMembersRequest(TeaModel):
    def __init__(
        self,
        list_query: ListTenantMembersRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListTenantMembersRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListTenantMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListTenantMembersResponseBodyPageResultUserListUserGroupList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        id: str = None,
        name: str = None,
    ):
        self.active = active
        self.description = description
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTenantMembersResponseBodyPageResultUserList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        display_name_without_status: str = None,
        enable_white_ip: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        mail: str = None,
        mobile_phone: str = None,
        name: str = None,
        nick_name: str = None,
        real_name: str = None,
        role_list: List[str] = None,
        source_id: str = None,
        source_type: str = None,
        user_group_list: List[ListTenantMembersResponseBodyPageResultUserListUserGroupList] = None,
        white_ip: str = None,
    ):
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.display_name_without_status = display_name_without_status
        self.enable_white_ip = enable_white_ip
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.name = name
        self.nick_name = nick_name
        self.real_name = real_name
        self.role_list = role_list
        self.source_id = source_id
        self.source_type = source_type
        self.user_group_list = user_group_list
        self.white_ip = white_ip

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.display_name_without_status is not None:
            result['DisplayNameWithoutStatus'] = self.display_name_without_status
        if self.enable_white_ip is not None:
            result['EnableWhiteIp'] = self.enable_white_ip
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.name is not None:
            result['Name'] = self.name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.role_list is not None:
            result['RoleList'] = self.role_list
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        if self.white_ip is not None:
            result['WhiteIp'] = self.white_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DisplayNameWithoutStatus') is not None:
            self.display_name_without_status = m.get('DisplayNameWithoutStatus')
        if m.get('EnableWhiteIp') is not None:
            self.enable_white_ip = m.get('EnableWhiteIp')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = ListTenantMembersResponseBodyPageResultUserListUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        if m.get('WhiteIp') is not None:
            self.white_ip = m.get('WhiteIp')
        return self


class ListTenantMembersResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        user_list: List[ListTenantMembersResponseBodyPageResultUserList] = None,
    ):
        self.total_count = total_count
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_list = []
        if m.get('UserList') is not None:
            for k in m.get('UserList'):
                temp_model = ListTenantMembersResponseBodyPageResultUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class ListTenantMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListTenantMembersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListTenantMembersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTenantMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantMembersResponseBody = None,
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
            temp_model = ListTenantMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupMembersRequestListQuery(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        user_group_id: str = None,
        user_id_list: List[str] = None,
    ):
        self.keyword = keyword
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.user_group_id = user_group_id
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class ListUserGroupMembersRequest(TeaModel):
    def __init__(
        self,
        list_query: ListUserGroupMembersRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListUserGroupMembersRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListUserGroupMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListUserGroupMembersResponseBodyPageResultMemberListCreator(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserGroupMembersResponseBodyPageResultMemberListUserInfo(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserGroupMembersResponseBodyPageResultMemberList(TeaModel):
    def __init__(
        self,
        creator: ListUserGroupMembersResponseBodyPageResultMemberListCreator = None,
        gmt_create: int = None,
        id: str = None,
        user_group_id: str = None,
        user_info: ListUserGroupMembersResponseBodyPageResultMemberListUserInfo = None,
        user_role: str = None,
    ):
        self.creator = creator
        self.gmt_create = gmt_create
        self.id = id
        self.user_group_id = user_group_id
        self.user_info = user_info
        self.user_role = user_role

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = ListUserGroupMembersResponseBodyPageResultMemberListCreator()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserInfo') is not None:
            temp_model = ListUserGroupMembersResponseBodyPageResultMemberListUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        return self


class ListUserGroupMembersResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        member_list: List[ListUserGroupMembersResponseBodyPageResultMemberList] = None,
        total_count: int = None,
    ):
        self.member_list = member_list
        self.total_count = total_count

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = ListUserGroupMembersResponseBodyPageResultMemberList()
                self.member_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListUserGroupMembersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListUserGroupMembersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupMembersResponseBody = None,
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
            temp_model = ListUserGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequestListQuery(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin_id_list: List[str] = None,
        filter_mine: bool = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.active = active
        self.admin_id_list = admin_id_list
        self.filter_mine = filter_mine
        self.keyword = keyword
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.admin_id_list is not None:
            result['AdminIdList'] = self.admin_id_list
        if self.filter_mine is not None:
            result['FilterMine'] = self.filter_mine
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('AdminIdList') is not None:
            self.admin_id_list = m.get('AdminIdList')
        if m.get('FilterMine') is not None:
            self.filter_mine = m.get('FilterMine')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(
        self,
        list_query: ListUserGroupsRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = ListUserGroupsRequestListQuery()
            self.list_query = temp_model.from_map(m['ListQuery'])
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListUserGroupsShrinkRequest(TeaModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        return self


class ListUserGroupsResponseBodyPageResultUserGroupListAdminList(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListUserGroupsResponseBodyPageResultUserGroupList(TeaModel):
    def __init__(
        self,
        active: bool = None,
        admin_list: List[ListUserGroupsResponseBodyPageResultUserGroupListAdminList] = None,
        description: str = None,
        id: str = None,
        my_role: str = None,
        name: str = None,
    ):
        self.active = active
        self.admin_list = admin_list
        self.description = description
        self.id = id
        self.my_role = my_role
        self.name = name

    def validate(self):
        if self.admin_list:
            for k in self.admin_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        result['AdminList'] = []
        if self.admin_list is not None:
            for k in self.admin_list:
                result['AdminList'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.my_role is not None:
            result['MyRole'] = self.my_role
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        self.admin_list = []
        if m.get('AdminList') is not None:
            for k in m.get('AdminList'):
                temp_model = ListUserGroupsResponseBodyPageResultUserGroupListAdminList()
                self.admin_list.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MyRole') is not None:
            self.my_role = m.get('MyRole')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListUserGroupsResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        user_group_list: List[ListUserGroupsResponseBodyPageResultUserGroupList] = None,
    ):
        self.total_count = total_count
        self.user_group_list = user_group_list

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = ListUserGroupsResponseBodyPageResultUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: ListUserGroupsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageResult') is not None:
            temp_model = ListUserGroupsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupsResponseBody = None,
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
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateInstanceRequestOperateCommandInstanceIdList(TeaModel):
    def __init__(
        self,
        field_instance_id_list: List[str] = None,
        id: str = None,
    ):
        self.field_instance_id_list = field_instance_id_list
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_instance_id_list is not None:
            result['FieldInstanceIdList'] = self.field_instance_id_list
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldInstanceIdList') is not None:
            self.field_instance_id_list = m.get('FieldInstanceIdList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class OperateInstanceRequestOperateCommand(TeaModel):
    def __init__(
        self,
        instance_id_list: List[OperateInstanceRequestOperateCommandInstanceIdList] = None,
        operation: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.instance_id_list = instance_id_list
        # This parameter is required.
        self.operation = operation
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.instance_id_list:
            for k in self.instance_id_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceIdList'] = []
        if self.instance_id_list is not None:
            for k in self.instance_id_list:
                result['InstanceIdList'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_id_list = []
        if m.get('InstanceIdList') is not None:
            for k in m.get('InstanceIdList'):
                temp_model = OperateInstanceRequestOperateCommandInstanceIdList()
                self.instance_id_list.append(temp_model.from_map(k))
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class OperateInstanceRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        operate_command: OperateInstanceRequestOperateCommand = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.operate_command = operate_command

    def validate(self):
        if self.operate_command:
            self.operate_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.operate_command is not None:
            result['OperateCommand'] = self.operate_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('OperateCommand') is not None:
            temp_model = OperateInstanceRequestOperateCommand()
            self.operate_command = temp_model.from_map(m['OperateCommand'])
        return self


class OperateInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        operate_command_shrink: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.operate_command_shrink = operate_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.operate_command_shrink is not None:
            result['OperateCommand'] = self.operate_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('OperateCommand') is not None:
            self.operate_command_shrink = m.get('OperateCommand')
        return self


class OperateInstanceResponseBodyInstanceStatusList(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        error_message: str = None,
        id: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        status: str = None,
    ):
        self.display_name = display_name
        self.error_message = error_message
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class OperateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_status_list: List[OperateInstanceResponseBodyInstanceStatusList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.instance_status_list = instance_status_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instance_status_list:
            for k in self.instance_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k in self.instance_status_list:
                result['InstanceStatusList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k in m.get('InstanceStatusList'):
                temp_model = OperateInstanceResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateInstanceResponseBody = None,
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
            temp_model = OperateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PausePhysicalNodeRequestPauseCommand(TeaModel):
    def __init__(
        self,
        node_id_list: List[str] = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.node_id_list = node_id_list
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PausePhysicalNodeRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        pause_command: PausePhysicalNodeRequestPauseCommand = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.pause_command = pause_command

    def validate(self):
        if self.pause_command:
            self.pause_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.pause_command is not None:
            result['PauseCommand'] = self.pause_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('PauseCommand') is not None:
            temp_model = PausePhysicalNodeRequestPauseCommand()
            self.pause_command = temp_model.from_map(m['PauseCommand'])
        return self


class PausePhysicalNodeShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        pause_command_shrink: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.pause_command_shrink = pause_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.pause_command_shrink is not None:
            result['PauseCommand'] = self.pause_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('PauseCommand') is not None:
            self.pause_command_shrink = m.get('PauseCommand')
        return self


class PausePhysicalNodeResponseBodyNodeOperateResultList(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        node_id: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.node_id = node_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PausePhysicalNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_operate_result_list: List[PausePhysicalNodeResponseBodyNodeOperateResultList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_operate_result_list = node_operate_result_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_operate_result_list:
            for k in self.node_operate_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['NodeOperateResultList'] = []
        if self.node_operate_result_list is not None:
            for k in self.node_operate_result_list:
                result['NodeOperateResultList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.node_operate_result_list = []
        if m.get('NodeOperateResultList') is not None:
            for k in m.get('NodeOperateResultList'):
                temp_model = PausePhysicalNodeResponseBodyNodeOperateResultList()
                self.node_operate_result_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PausePhysicalNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PausePhysicalNodeResponseBody = None,
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
            temp_model = PausePhysicalNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTenantMemberRequestRemoveCommand(TeaModel):
    def __init__(
        self,
        source_id: str = None,
    ):
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class RemoveTenantMemberRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command: RemoveTenantMemberRequestRemoveCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command = remove_command

    def validate(self):
        if self.remove_command:
            self.remove_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.remove_command is not None:
            result['RemoveCommand'] = self.remove_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RemoveCommand') is not None:
            temp_model = RemoveTenantMemberRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m['RemoveCommand'])
        return self


class RemoveTenantMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command_shrink = remove_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.remove_command_shrink is not None:
            result['RemoveCommand'] = self.remove_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RemoveCommand') is not None:
            self.remove_command_shrink = m.get('RemoveCommand')
        return self


class RemoveTenantMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveTenantMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveTenantMemberResponseBody = None,
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
            temp_model = RemoveTenantMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserGroupMemberRequestRemoveCommand(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.user_group_id = user_group_id
        # This parameter is required.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class RemoveUserGroupMemberRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command: RemoveUserGroupMemberRequestRemoveCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command = remove_command

    def validate(self):
        if self.remove_command:
            self.remove_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.remove_command is not None:
            result['RemoveCommand'] = self.remove_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RemoveCommand') is not None:
            temp_model = RemoveUserGroupMemberRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m['RemoveCommand'])
        return self


class RemoveUserGroupMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command_shrink = remove_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.remove_command_shrink is not None:
            result['RemoveCommand'] = self.remove_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RemoveCommand') is not None:
            self.remove_command_shrink = m.get('RemoveCommand')
        return self


class RemoveUserGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveUserGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserGroupMemberResponseBody = None,
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
            temp_model = RemoveUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumePhysicalNodeRequestResumeCommand(TeaModel):
    def __init__(
        self,
        node_id_list: List[str] = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.node_id_list = node_id_list
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ResumePhysicalNodeRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        resume_command: ResumePhysicalNodeRequestResumeCommand = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.resume_command = resume_command

    def validate(self):
        if self.resume_command:
            self.resume_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.resume_command is not None:
            result['ResumeCommand'] = self.resume_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ResumeCommand') is not None:
            temp_model = ResumePhysicalNodeRequestResumeCommand()
            self.resume_command = temp_model.from_map(m['ResumeCommand'])
        return self


class ResumePhysicalNodeShrinkRequest(TeaModel):
    def __init__(
        self,
        env: str = None,
        op_tenant_id: int = None,
        resume_command_shrink: str = None,
    ):
        self.env = env
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.resume_command_shrink = resume_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.resume_command_shrink is not None:
            result['ResumeCommand'] = self.resume_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ResumeCommand') is not None:
            self.resume_command_shrink = m.get('ResumeCommand')
        return self


class ResumePhysicalNodeResponseBodyNodeOperateResultList(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        node_id: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.node_id = node_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResumePhysicalNodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_operate_result_list: List[ResumePhysicalNodeResponseBodyNodeOperateResultList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_operate_result_list = node_operate_result_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_operate_result_list:
            for k in self.node_operate_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['NodeOperateResultList'] = []
        if self.node_operate_result_list is not None:
            for k in self.node_operate_result_list:
                result['NodeOperateResultList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.node_operate_result_list = []
        if m.get('NodeOperateResultList') is not None:
            for k in m.get('NodeOperateResultList'):
                temp_model = ResumePhysicalNodeResponseBodyNodeOperateResultList()
                self.node_operate_result_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumePhysicalNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumePhysicalNodeResponseBody = None,
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
            temp_model = ResumePhysicalNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeResourcePermissionRequestRevokeCommandResourceList(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class RevokeResourcePermissionRequestRevokeCommand(TeaModel):
    def __init__(
        self,
        operate_list: List[str] = None,
        reason: str = None,
        resource_list: List[RevokeResourcePermissionRequestRevokeCommandResourceList] = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        self.operate_list = operate_list
        self.reason = reason
        # This parameter is required.
        self.resource_list = resource_list
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_list is not None:
            result['OperateList'] = self.operate_list
        if self.reason is not None:
            result['Reason'] = self.reason
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateList') is not None:
            self.operate_list = m.get('OperateList')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = RevokeResourcePermissionRequestRevokeCommandResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RevokeResourcePermissionRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        revoke_command: RevokeResourcePermissionRequestRevokeCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.revoke_command = revoke_command

    def validate(self):
        if self.revoke_command:
            self.revoke_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.revoke_command is not None:
            result['RevokeCommand'] = self.revoke_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RevokeCommand') is not None:
            temp_model = RevokeResourcePermissionRequestRevokeCommand()
            self.revoke_command = temp_model.from_map(m['RevokeCommand'])
        return self


class RevokeResourcePermissionShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        revoke_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.revoke_command_shrink = revoke_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.revoke_command_shrink is not None:
            result['RevokeCommand'] = self.revoke_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('RevokeCommand') is not None:
            self.revoke_command_shrink = m.get('RevokeCommand')
        return self


class RevokeResourcePermissionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeResourcePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeResourcePermissionResponseBody = None,
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
            temp_model = RevokeResourcePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAdHocFileRequestUpdateCommand(TeaModel):
    def __init__(
        self,
        content: str = None,
        file_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateAdHocFileRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: UpdateAdHocFileRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            temp_model = UpdateAdHocFileRequestUpdateCommand()
            self.update_command = temp_model.from_map(m['UpdateCommand'])
        return self


class UpdateAdHocFileShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command_shrink = update_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command_shrink is not None:
            result['UpdateCommand'] = self.update_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            self.update_command_shrink = m.get('UpdateCommand')
        return self


class UpdateAdHocFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAdHocFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAdHocFileResponseBody = None,
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
            temp_model = UpdateAdHocFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSourceBasicInfoRequestUpdateCommand(TeaModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateDataSourceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: UpdateDataSourceBasicInfoRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            temp_model = UpdateDataSourceBasicInfoRequestUpdateCommand()
            self.update_command = temp_model.from_map(m['UpdateCommand'])
        return self


class UpdateDataSourceBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command_shrink = update_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command_shrink is not None:
            result['UpdateCommand'] = self.update_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            self.update_command_shrink = m.get('UpdateCommand')
        return self


class UpdateDataSourceBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataSourceBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSourceBasicInfoResponseBody = None,
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
            temp_model = UpdateDataSourceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSourceConfigRequestUpdateCommandConfigItemList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
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


class UpdateDataSourceConfigRequestUpdateCommand(TeaModel):
    def __init__(
        self,
        config_item_list: List[UpdateDataSourceConfigRequestUpdateCommandConfigItemList] = None,
        id: int = None,
    ):
        # This parameter is required.
        self.config_item_list = config_item_list
        # This parameter is required.
        self.id = id

    def validate(self):
        if self.config_item_list:
            for k in self.config_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigItemList'] = []
        if self.config_item_list is not None:
            for k in self.config_item_list:
                result['ConfigItemList'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_item_list = []
        if m.get('ConfigItemList') is not None:
            for k in m.get('ConfigItemList'):
                temp_model = UpdateDataSourceConfigRequestUpdateCommandConfigItemList()
                self.config_item_list.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateDataSourceConfigRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: UpdateDataSourceConfigRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            temp_model = UpdateDataSourceConfigRequestUpdateCommand()
            self.update_command = temp_model.from_map(m['UpdateCommand'])
        return self


class UpdateDataSourceConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command_shrink = update_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command_shrink is not None:
            result['UpdateCommand'] = self.update_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            self.update_command_shrink = m.get('UpdateCommand')
        return self


class UpdateDataSourceConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataSourceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSourceConfigResponseBody = None,
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
            temp_model = UpdateDataSourceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileDirectoryRequest(TeaModel):
    def __init__(
        self,
        directory: str = None,
        file_id: int = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory is not None:
            result['Directory'] = self.directory
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateFileDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFileDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFileDirectoryResponseBody = None,
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
            temp_model = UpdateFileDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileNameRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        name: str = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.name is not None:
            result['Name'] = self.name
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateFileNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFileNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFileNameResponseBody = None,
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
            temp_model = UpdateFileNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTenantMemberRequestUpdateCommandMemberList(TeaModel):
    def __init__(
        self,
        ding_number: str = None,
        mail: str = None,
        mobile_phone: str = None,
        role_list: List[str] = None,
        user_id: str = None,
    ):
        self.ding_number = ding_number
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.role_list = role_list
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone
        if self.role_list is not None:
            result['RoleList'] = self.role_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')
        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateTenantMemberRequestUpdateCommand(TeaModel):
    def __init__(
        self,
        member_list: List[UpdateTenantMemberRequestUpdateCommandMemberList] = None,
    ):
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MemberList'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['MemberList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k in m.get('MemberList'):
                temp_model = UpdateTenantMemberRequestUpdateCommandMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class UpdateTenantMemberRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: UpdateTenantMemberRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            temp_model = UpdateTenantMemberRequestUpdateCommand()
            self.update_command = temp_model.from_map(m['UpdateCommand'])
        return self


class UpdateTenantMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command_shrink = update_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command_shrink is not None:
            result['UpdateCommand'] = self.update_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            self.update_command_shrink = m.get('UpdateCommand')
        return self


class UpdateTenantMemberResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTenantMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTenantMemberResponseBody = None,
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
            temp_model = UpdateTenantMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequestUpdateCommand(TeaModel):
    def __init__(
        self,
        admin_user_id_list: List[str] = None,
        description: str = None,
        id: str = None,
        name: str = None,
    ):
        self.admin_user_id_list = admin_user_id_list
        self.description = description
        # This parameter is required.
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_user_id_list is not None:
            result['AdminUserIdList'] = self.admin_user_id_list
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUserIdList') is not None:
            self.admin_user_id_list = m.get('AdminUserIdList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: UpdateUserGroupRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            temp_model = UpdateUserGroupRequestUpdateCommand()
            self.update_command = temp_model.from_map(m['UpdateCommand'])
        return self


class UpdateUserGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.update_command_shrink = update_command_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.update_command_shrink is not None:
            result['UpdateCommand'] = self.update_command_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UpdateCommand') is not None:
            self.update_command_shrink = m.get('UpdateCommand')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserGroupResponseBody = None,
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
            temp_model = UpdateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupSwitchRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        op_tenant_id: int = None,
        user_group_id: str = None,
    ):
        # This parameter is required.
        self.active = active
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class UpdateUserGroupSwitchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserGroupSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserGroupSwitchResponseBody = None,
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
            temp_model = UpdateUserGroupSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


