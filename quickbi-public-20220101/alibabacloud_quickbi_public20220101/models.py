# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddDataLevelPermissionRuleUsersRequest(TeaModel):
    def __init__(
        self,
        add_user_model: str = None,
    ):
        # This parameter is required.
        self.add_user_model = add_user_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_user_model is not None:
            result['AddUserModel'] = self.add_user_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddUserModel') is not None:
            self.add_user_model = m.get('AddUserModel')
        return self


class AddDataLevelPermissionRuleUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface. Valid values:\\n\\n*   true: The request was successful.\\n*   false: The request failed.\\n
        self.result = result
        # Indicates whether the request is successful. Valid values:\\n\\n*   true: The request was successful.\\n*   false: The request failed.\\n
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDataLevelPermissionRuleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDataLevelPermissionRuleUsersResponseBody = None,
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
            temp_model = AddDataLevelPermissionRuleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        operate_type: str = None,
        rule_type: str = None,
        target_ids: str = None,
        target_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # Operation Type: You can set this parameter to one of the following values.
        # 
        # *   ADD: Add a whitelist
        # *   DELETE: deletes a whitelist.
        self.operate_type = operate_type
        # The type of row-level permissions.
        # 
        # *   ROW_LEVEL: row-level permissions,
        # *   COLUMN_LEVEL: column-level permissions
        self.rule_type = rule_type
        self.target_ids = target_ids
        # Modify the type of the whitelist:
        # 
        # *   1: user
        # *   2: user group
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AddDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDataLevelPermissionWhiteListResponseBody = None,
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
            temp_model = AddDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddShareReportRequest(TeaModel):
    def __init__(
        self,
        auth_point: int = None,
        expire_date: int = None,
        share_to_id: str = None,
        share_to_type: int = None,
        works_id: str = None,
    ):
        # The scope of authorization. Valid values:
        # 
        # *   1: view only
        # *   3: View and export
        # 
        # This parameter is required.
        self.auth_point = auth_point
        # The validity period of the share. The value is a timestamp in milliseconds.
        # 
        # This parameter is required.
        self.expire_date = expire_date
        # The ID of the person to be shared, which may be the user ID of the Quick BI or the user group ID.
        # 
        # *   If ShareToType is 0 (user), ShareTo is the user ID.
        # *   When ShareToType is set to 1 (user group), ShareTo is the user group ID.
        # *   When ShareToType=2 (organization), ShareTo is the ID of the organization.
        self.share_to_id = share_to_id
        # The share type of the template. Valid values:
        # 
        # *   0: user
        # *   1: user group
        # *   2: organization
        # 
        # This parameter is required.
        self.share_to_type = share_to_type
        # The ID of the shared work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class AddShareReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddShareReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddShareReportResponseBody = None,
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
            temp_model = AddShareReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        nick_name: str = None,
        role_ids: str = None,
        user_type: int = None,
    ):
        # Aliyun account ID.
        # >Warning: For versions of Quick BI released after December 31, 2024, AccountId will be a required parameter. Please modify your API before this date.
        # 
        # <props="china">Published only on the China site
        self.account_id = account_id
        # Aliyun account name.
        # 
        # - Note: If it is a sub-account, the format should be \\"primary account: sub-account\\". For example: master_test@aliyun.com:subaccount
        # - Format check: Maximum length of 50 characters.
        self.account_name = account_name
        # Whether to assign the organization administrator role. Value range: 
        # 
        # - true: Yes 
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIds is provided.</notice>
        self.admin_user = admin_user
        # Whether to assign the organization permission administrator role. Value range: 
        # 
        # - true: Yes 
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIds is provided.</notice>
        self.auth_admin_user = auth_admin_user
        # Aliyun account nickname.
        # 
        # - Format check: Maximum length of 50 characters.
        # - Special format validation: Chinese and English characters, numbers, _ \\ / | () ] [
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # Preset or custom organization role IDs bound to the user, separated by commas, with a maximum of 3. Value range:
        # - Organization Administrator (preset role): 111111111
        # - Permission Administrator (preset role): 111111112
        # - Regular User (preset role): 111111113
        self.role_ids = role_ids
        # The user type of the organization member. Value range:
        # - 1: Developer
        # - 2: Visitor
        # - 3: Analyst
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AddUserResponseBodyResult(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        nick_name: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # Aliyun account.
        self.account_name = account_name
        # Whether the organization administrator role is assigned. Value range: 
        # 
        # - true: Yes
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIdList is provided.</notice>
        self.admin_user = admin_user
        # Whether the permission administrator role is assigned. Value range: 
        # 
        # - true: Yes
        # - false: No
        # 
        # <notice>This parameter is deprecated and not recommended for use. It is invalid when RoleIdList is provided.</notice>
        self.auth_admin_user = auth_admin_user
        # Aliyun account nickname.
        self.nick_name = nick_name
        # List of organization role IDs bound to the user.
        self.role_id_list = role_id_list
        # UserID in Quick BI.
        self.user_id = user_id
        # User type of the organization member. Value range: 
        # - 1: Developer 
        # - 2: Visitor 
        # - 3: Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: AddUserResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns detailed information about the newly added Aliyun user.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddUserResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserResponseBody = None,
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
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserGroupMemberRequest(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id_list: str = None,
    ):
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The ID of the Quick BI user. Separate multiple IDs with commas (,). Example: abc,efg. You can enter a maximum of 1000 entries.
        # 
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


class AddUserGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of adding members to a user group is returned. Valid values:
        # 
        # *   true: The task is added.
        # *   false: The tag failed to be added.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class AddUserGroupMembersRequest(TeaModel):
    def __init__(
        self,
        user_group_ids: str = None,
        user_id: str = None,
    ):
        # The IDs of the user groups. Separate the IDs with commas (,). Example: aGroupId,bGroupId,cGroupIds
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids
        # The user ID of the Quick BI.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserGroupMembersResponseBody = None,
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
            temp_model = AddUserGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserTagMetaRequest(TeaModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_name: str = None,
    ):
        # Tag description. Format check: maximum length of 255 characters.
        self.tag_description = tag_description
        # Tag name. Format check:
        # - Maximum length of 50 characters.
        # - Only Chinese, English, numbers, and /\\|[]() symbols are allowed.
        # 
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class AddUserTagMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the ID of the successfully added tag.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request succeeded 
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserTagMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserTagMetaResponseBody = None,
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
            temp_model = AddUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToWorkspaceRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The preset space role ID. Value range:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # The ID of the Quick BI user to be added.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddUserToWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Returns the result of the interface execution. Value range:
        # 
        # - true: Execution successful
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Value range:
        # 
        # - true: Request successful
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserToWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserToWorkspaceResponseBody = None,
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
            temp_model = AddUserToWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddWorkspaceUsersRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        user_ids: str = None,
        workspace_id: str = None,
    ):
        # Preset space role ID. Value range:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # User ID. This is the UserID for Quick BI, not the Alibaba Cloud UID.
        # 
        # - Supports batch parameters, with user IDs separated by commas (,).
        # 
        # This parameter is required.
        self.user_ids = user_ids
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddWorkspaceUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        failure: int = None,
        failure_detail: Dict[str, Any] = None,
        success: int = None,
        total: int = None,
    ):
        # Number of users that failed to be added.
        self.failure = failure
        # Reasons for the failures.
        self.failure_detail = failure_detail
        # Number of users that were added successfully.
        self.success = success
        # Total number of users being added.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['Failure'] = self.failure
        if self.failure_detail is not None:
            result['FailureDetail'] = self.failure_detail
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failure') is not None:
            self.failure = m.get('Failure')
        if m.get('FailureDetail') is not None:
            self.failure_detail = m.get('FailureDetail')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class AddWorkspaceUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: AddWorkspaceUsersResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the API execution.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request was successful. There may be cases where some members are added successfully and others fail. For the reasons of failure, refer to the FailureDetail in the response.
        # - false: The request failed, and no data will be persisted.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AddWorkspaceUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWorkspaceUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddWorkspaceUsersResponseBody = None,
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
            temp_model = AddWorkspaceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllotDatasetAccelerationTaskRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
    ):
        # The dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        return self


class AllotDatasetAccelerationTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the IP address whitelist is updated. Valid values:
        # 
        # *   true: The task is triggered.
        # *   false: The task fails to be triggered.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AllotDatasetAccelerationTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllotDatasetAccelerationTaskResponseBody = None,
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
            temp_model = AllotDatasetAccelerationTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeMenuRequest(TeaModel):
    def __init__(
        self,
        auth_points_value: int = None,
        data_portal_id: str = None,
        menu_ids: str = None,
        user_group_ids: str = None,
        user_ids: str = None,
    ):
        # Authorizes the permissions of the menu. Valid values:
        # 
        # *   1: view
        # *   3: View + Export (default)
        self.auth_points_value = auth_points_value
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The menu ID of the BI portal leaf node.
        # 
        # *   The directory menu cannot be authorized.
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 100.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # The IDs of the user groups.
        # 
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 200.
        # *   UserGroupIds and UserIds cannot be empty at the same time
        self.user_group_ids = user_group_ids
        # The IDs of the end users. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        # 
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 200.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_points_value is not None:
            result['AuthPointsValue'] = self.auth_points_value
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPointsValue') is not None:
            self.auth_points_value = m.get('AuthPointsValue')
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AuthorizeMenuResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of authorized menus.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeMenuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeMenuResponseBody = None,
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
            temp_model = AuthorizeMenuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAddFeishuUsersRequest(TeaModel):
    def __init__(
        self,
        feishu_users: str = None,
        is_admin: bool = None,
        is_auth_admin: bool = None,
        user_group_ids: str = None,
        user_type: int = None,
    ):
        self.feishu_users = feishu_users
        self.is_admin = is_admin
        self.is_auth_admin = is_auth_admin
        self.user_group_ids = user_group_ids
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feishu_users is not None:
            result['FeishuUsers'] = self.feishu_users
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.is_auth_admin is not None:
            result['IsAuthAdmin'] = self.is_auth_admin
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeishuUsers') is not None:
            self.feishu_users = m.get('FeishuUsers')
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('IsAuthAdmin') is not None:
            self.is_auth_admin = m.get('IsAuthAdmin')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_desc: str = None,
        input: str = None,
    ):
        self.code = code
        self.code_desc = code_desc
        self.input = input

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_desc is not None:
            result['CodeDesc'] = self.code_desc
        if self.input is not None:
            result['Input'] = self.input
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeDesc') is not None:
            self.code_desc = m.get('CodeDesc')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        return self


class BatchAddFeishuUsersResponseBodyResultFailResults(TeaModel):
    def __init__(
        self,
        fail_infos: List[BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos] = None,
    ):
        self.fail_infos = fail_infos

    def validate(self):
        if self.fail_infos:
            for k in self.fail_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailInfos'] = []
        if self.fail_infos is not None:
            for k in self.fail_infos:
                result['FailInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_infos = []
        if m.get('FailInfos') is not None:
            for k in m.get('FailInfos'):
                temp_model = BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos()
                self.fail_infos.append(temp_model.from_map(k))
        return self


class BatchAddFeishuUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        fail_count: int = None,
        fail_results: List[BatchAddFeishuUsersResponseBodyResultFailResults] = None,
        ok_count: int = None,
    ):
        self.fail_count = fail_count
        self.fail_results = fail_results
        self.ok_count = ok_count

    def validate(self):
        if self.fail_results:
            for k in self.fail_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        result['FailResults'] = []
        if self.fail_results is not None:
            for k in self.fail_results:
                result['FailResults'].append(k.to_map() if k else None)
        if self.ok_count is not None:
            result['OkCount'] = self.ok_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        self.fail_results = []
        if m.get('FailResults') is not None:
            for k in m.get('FailResults'):
                temp_model = BatchAddFeishuUsersResponseBodyResultFailResults()
                self.fail_results.append(temp_model.from_map(k))
        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')
        return self


class BatchAddFeishuUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: BatchAddFeishuUsersResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = BatchAddFeishuUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchAddFeishuUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAddFeishuUsersResponseBody = None,
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
            temp_model = BatchAddFeishuUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAuthorizationMenuRequest(TeaModel):
    def __init__(
        self,
        data_portal_id: str = None,
        menu_ids: str = None,
        user_group_ids: str = None,
        user_ids: str = None,
    ):
        # The ID of the data portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The leaf node menu IDs of the data portal.
        # 
        # - Supports batch parameters, with IDs separated by commas (,). The maximum number for batch modification is 100.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # List of user group IDs.
        # 
        # - Supports batch parameters, with IDs separated by commas (,). The maximum number for batch modification is 200.
        # - UserGroupIds and UserIds cannot both be empty.
        self.user_group_ids = user_group_ids
        # List of user IDs. These are Quick BI UserIDs, not Alibaba Cloud UIDs.
        # 
        # - Supports batch parameters, with IDs separated by commas (,). The maximum number for batch modification is 200.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class CancelAuthorizationMenuResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Number of menus successfully unauthorized.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelAuthorizationMenuResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelAuthorizationMenuResponseBody = None,
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
            temp_model = CancelAuthorizationMenuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCollectionRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        works_id: str = None,
    ):
        # The ID of the favorite user. The user ID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the work to cancel the collection.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CancelCollectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCollectionResponseBody = None,
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
            temp_model = CancelCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelReportShareRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        share_to_ids: str = None,
        share_to_type: int = None,
    ):
        # The ID of the work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The ID of the person to be shared, which may be the user ID of the Quick BI or the user group ID.
        # 
        # *   If ShareToType is 0 (user), ShareTo is the user ID.
        # *   When ShareToType is set to 1 (user group), ShareTo is the user group ID.
        # *   When ShareToType=2 (organization), ShareTo is the ID of the organization.
        # 
        # This parameter is required.
        self.share_to_ids = share_to_ids
        # The deletion method. Valid values:
        # 
        # *   0: Delete by user
        # *   1: Delete by user group
        # *   2: Delete by organization
        # 
        # This parameter is required.
        self.share_to_type = share_to_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.share_to_ids is not None:
            result['ShareToIds'] = self.share_to_ids
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ShareToIds') is not None:
            self.share_to_ids = m.get('ShareToIds')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        return self


class CancelReportShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelReportShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelReportShareResponseBody = None,
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
            temp_model = CancelReportShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeVisibilityModelRequest(TeaModel):
    def __init__(
        self,
        data_portal_id: str = None,
        menu_ids: str = None,
        show_only_with_access: bool = None,
    ):
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The menu ID of the BI portal leaf node.
        # 
        # *   The directory menu cannot be authorized.
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 100.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # Whether only authorization is visible. Valid values:
        # 
        # *   true: Only the authorization is visible.
        # *   false: Both are visible.
        # 
        # This parameter is required.
        self.show_only_with_access = show_only_with_access

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids
        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')
        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')
        return self


class ChangeVisibilityModelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of menus that are successfully modified.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeVisibilityModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeVisibilityModelResponseBody = None,
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
            temp_model = ChangeVisibilityModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckReadableRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        works_id: str = None,
    ):
        # The user ID of the Quick BI to be checked.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the work. Resources here include BI portal, dashboards, spreadsheets, and self-service access.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CheckReadableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckReadableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckReadableResponseBody = None,
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
            temp_model = CheckReadableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        cmpt_id: str = None,
        expire_time: int = None,
        global_param: str = None,
        ticket_num: int = None,
        user_id: str = None,
        watermark_param: str = None,
        works_id: str = None,
    ):
        # The user\\"s account name.
        # 
        # - If the user is an Alibaba Cloud primary account **wangwu**, the format is **[Primary Account]**, for example, **wangwu**.
        # - If the user is a RAM account **zhangsan**@aliyun.cn**, the format is **[Primary Account: Sub-Account]**, for example, **wangwu:zhangsan**.
        # 
        # > Only one of UserId and AccountName needs to be filled in. If neither is filled in, it will default to binding the report\\"s Owner, and the report will be accessed with that user\\"s identity. If you need to configure row-level permissions, please refer to [Row-Level Permissions](https://help.aliyun.com/document_detail/322783.html).
        self.account_name = account_name
        # The type of the user\\"s account.
        # - 1: Alibaba Cloud account
        # - 3: Quick BI self-built account
        # - 4: DingTalk
        # - 5: RAM sub-account
        # - 9: WeCom
        # - 10: Feishu
        # > If AccountName is not empty, then AccountType must also not be empty.
        self.account_type = account_type
        # Component ID. This is the ID of a component within the above-mentioned dashboard; other types of works do not support this.
        # Refer to [QueryWorksBloodRelationship](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryWorksBloodRelationship?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&lang=JAVA&tab=DOC&sdkStyle=old) for the API to get the component ID.
        self.cmpt_id = cmpt_id
        # Expiration time
        # - Unit: minutes
        # - Default: 240
        self.expire_time = expire_time
        # Global parameters for the report filter conditions.
        # - A string in JsonArray format.
        # 
        # > If you need to use global parameter capabilities, please contact the [Quick BI Operations Manager](https://h5-alimebot.dingtalk.com/intl/index.htm?spm=a2c4g.11186623.0.0.3da14f6chrDv9e&sourceType=ding_talk&from=DEFFB9G5KBByQkwq23wneFIOmaJ).
        self.global_param = global_param
        # The number of tickets. Each time a ticket is used, the number of tickets decreases by 1.
        # - Default value: 1
        # - Recommended value: 1
        # - Maximum value: 99999
        self.ticket_num = ticket_num
        # Quick BI\\"s UserId, which is not your Alibaba Cloud account ID.
        # You can call the [QueryUserInfoByAccount](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryUserInfoByAccount?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&tab=DOC&sdkStyle=old) interface to obtain the UserId. An example of a UserId is fe67f61a35a94b7da1a34ba174a7****.
        # 
        # > Only one of UserId and AccountName needs to be filled in. If neither is filled in, it will default to binding the report\\"s Owner, and the report will be accessed with that user\\"s identity. If you need to configure row-level permissions, please refer to [Row-Level Permissions](https://help.aliyun.com/document_detail/322783.html).
        self.user_id = user_id
        # Watermark parameters for the report.
        # - Must not exceed 50 characters.
        # - When the report type is a large screen, watermark parameter passing is not supported.
        self.watermark_param = watermark_param
        # The ID of the report to be embedded. Currently supports dashboards, spreadsheets, data screens, self-service data retrieval, ad-hoc analysis, and data entry.
        # 
        # This parameter is required.
        self.works_id = works_id

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
        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.global_param is not None:
            result['GlobalParam'] = self.global_param
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The generated ticket value.
        self.result = result
        # Indicates whether the request was successful. Value range: 
        # - true: Request succeeded 
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTicketResponseBody = None,
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicket4CopilotRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        copilot_id: str = None,
        expire_time: int = None,
        ticket_num: int = None,
        user_id: str = None,
    ):
        # User\\"s account name.
        # <notice>Note: Only one of userId and accountName needs to be filled in. If neither is provided, it will default to the report owner, and the report will be accessed with that user\\"s identity.</notice>
        self.account_name = account_name
        # User\\"s account type:
        # 
        # - 1: Alibaba Cloud Primary Account
        # 
        # - 3: Quick BI Self-built Account
        # 
        # - 4: DingTalk
        # 
        # - 5: Alibaba Cloud RAM Account
        # 
        # - 6: Third-party Account (SAML, OAuth, etc.)
        # 
        # - 9: WeCom
        # 
        # - 10: Feishu
        # 
        # <notice>Note: If accountName is not empty, then accountType must also be provided.</notice>
        self.account_type = account_type
        # ID of the Smart Q module to be embedded.
        # 
        # This parameter is required.
        self.copilot_id = copilot_id
        # Expiration time.
        # 
        # - Unit: minutes, maximum 240 (4 hours).
        # 
        # - Default: 240.
        self.expire_time = expire_time
        # Range of ticket quantity:
        # 
        # - Default value is 1.
        # 
        # - Recommended value is 1.
        # 
        # - Maximum value is 99999.
        # 
        # Each time a ticket is used, the ticket count decreases by 1.
        self.ticket_num = ticket_num
        # Quick BI\\"s UserId.
        # 
        # - You can obtain this by calling [3.1.7 Get User Details Based on Third-Party Account] or other relevant APIs.
        # 
        # <notice>Note: Only one of userId and accountName needs to be filled in. If neither is provided, it will default to the report owner, and the report will be accessed with that user\\"s identity.</notice>
        self.user_id = user_id

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
        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateTicket4CopilotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # ID of the Smart Q module to be embedded.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request succeeded
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTicket4CopilotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTicket4CopilotResponseBody = None,
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
            temp_model = CreateTicket4CopilotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(
        self,
        parent_user_group_id: str = None,
        user_group_description: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The ID of the parent user group. You can add new user groups to this group:
        # 
        # *   If you enter the ID of a parent user group, the new user group is added to the user group with the ID.
        # *   If you enter -1, the new user group is added to the root directory.
        # 
        # This parameter is required.
        self.parent_user_group_id = parent_user_group_id
        # The description of the user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.user_group_description = user_group_description
        # The unique ID of the user group.
        # 
        # *   If you specify the UserGroupId parameter, the system automatically generates the UserGroupId parameter. If you specify the UserGroupId parameter, the user ID is used as the user group ID. You must ensure that the user ID is unique within the organization.
        # *   Format verification: Maximum length 64, cannot be -1,
        self.user_group_id = user_group_id
        # The name of the RAM user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        # 
        # This parameter is required.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the added user group is returned. An empty string \\"\\" is returned if the add fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class DataInterpretationRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        model_code: str = None,
        prompt_force_override: bool = None,
        user_prompt: str = None,
        user_question: str = None,
    ):
        # This parameter is required.
        self.data = data
        self.model_code = model_code
        self.prompt_force_override = prompt_force_override
        self.user_prompt = user_prompt
        self.user_question = user_question

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.model_code is not None:
            result['ModelCode'] = self.model_code
        if self.prompt_force_override is not None:
            result['PromptForceOverride'] = self.prompt_force_override
        if self.user_prompt is not None:
            result['UserPrompt'] = self.user_prompt
        if self.user_question is not None:
            result['UserQuestion'] = self.user_question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')
        if m.get('PromptForceOverride') is not None:
            self.prompt_force_override = m.get('PromptForceOverride')
        if m.get('UserPrompt') is not None:
            self.user_prompt = m.get('UserPrompt')
        if m.get('UserQuestion') is not None:
            self.user_question = m.get('UserQuestion')
        return self


class DataInterpretationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DataInterpretationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DataInterpretationResponseBody = None,
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
            temp_model = DataInterpretationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DataSetBloodRequest(TeaModel):
    def __init__(
        self,
        data_set_ids: str = None,
        user_id: str = None,
        works_type: str = None,
    ):
        # List of dataset IDs, separated by English commas.
        # 
        # This parameter is required.
        self.data_set_ids = data_set_ids
        # Specify the owner of the report, which is the userId.
        self.user_id = user_id
        # Specify the type of report:
        # - REPORT: Workbooks
        # - dashboardOfflineQuery: Downloads
        # - DASHBOARD: Dashboard
        # - ANALYSIS: Ad Hoc Analysis
        # - SCREEN: Visualization Screen
        # - PAGE: Old dashboard
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_ids is not None:
            result['DataSetIds'] = self.data_set_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetIds') is not None:
            self.data_set_ids = m.get('DataSetIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        return self


class DataSetBloodResponseBodyResult(TeaModel):
    def __init__(
        self,
        works_id: str = None,
        works_type: str = None,
    ):
        # Work ID.
        self.works_id = works_id
        # Work types: - REPORT: 
        # - REPORT: Workbooks
        # - dashboardOfflineQuery: Downloads
        # - DASHBOARD: Dashboard
        # - ANALYSIS: Ad Hoc Analysis
        # - SCREEN: Visualization Screen
        # - PAGE: Old dashboard
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        return self


class DataSetBloodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DataSetBloodResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of works.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DataSetBloodResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DataSetBloodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DataSetBloodResponseBody = None,
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
            temp_model = DataSetBloodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DataSourceBloodRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
    ):
        # Data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        return self


class DataSourceBloodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[str] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of dataset IDs.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DataSourceBloodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DataSourceBloodResponseBody = None,
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
            temp_model = DataSourceBloodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelayTicketExpireTimeRequest(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        ticket: str = None,
    ):
        # The time to postpone.
        # 
        # *   Unit: minutes. Valid values: 0 to 240. Unit: minutes. Valid values: 4 hours.
        # *   Expired bills cannot be extended.
        # 
        # This parameter is required.
        self.expire_time = expire_time
        # The value of the third-party embedded ticket, that is, the accessTicket value in the URL.
        # 
        # This parameter is required.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class DelayTicketExpireTimeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Whether the extension is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DelayTicketExpireTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelayTicketExpireTimeResponseBody = None,
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
            temp_model = DelayTicketExpireTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLevelPermissionRuleUsersRequest(TeaModel):
    def __init__(
        self,
        delete_user_model: str = None,
    ):
        # This parameter is required.
        self.delete_user_model = delete_user_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_user_model is not None:
            result['DeleteUserModel'] = self.delete_user_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteUserModel') is not None:
            self.delete_user_model = m.get('DeleteUserModel')
        return self


class DeleteDataLevelPermissionRuleUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLevelPermissionRuleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLevelPermissionRuleUsersResponseBody = None,
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
            temp_model = DeleteDataLevelPermissionRuleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataLevelRuleConfigRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_id: str = None,
    ):
        # This parameter is required.
        self.cube_id = cube_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteDataLevelRuleConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataLevelRuleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataLevelRuleConfigResponseBody = None,
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
            temp_model = DeleteDataLevelRuleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTicketRequest(TeaModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        # The value of the third-party embedded ticket, which is the `accessTicket` in the URL.
        # 
        # This parameter is required.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class DeleteTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Indicates whether the deletion was successful. Possible values:
        # - true: The request was successful
        # - false: The request failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTicketResponseBody = None,
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
            temp_model = DeleteTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        transfer_user_id: str = None,
        user_id: str = None,
    ):
        # The ID of the successor. If not empty, the report resources in the workspace of the deleted user will be transferred to the successor; otherwise, they will be transferred to the space owner.
        # - The successor cannot be an organization visitor
        # - The permissions of the successor in the workspace must not be less than those of the deleted user, with management permissions > development permissions > sharing permissions > viewing permissions
        # - If the successor is not in the workspace, they will be automatically added to the workspace
        self.transfer_user_id = transfer_user_id
        # The ID of the user to be deleted. This user ID is the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.transfer_user_id is not None:
            result['TransferUserId'] = self.transfer_user_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransferUserId') is not None:
            self.transfer_user_id = m.get('TransferUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the execution result of the interface. Possible values:
        # 
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserFromWorkspaceRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # The ID of the user to be deleted. Note that this UserID is for Quick BI, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteUserFromWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Returns the result of the API execution. Possible values:
        # 
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request succeeded - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserFromWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserFromWorkspaceResponseBody = None,
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
            temp_model = DeleteUserFromWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
    ):
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class DeleteUserGroupMemberRequest(TeaModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id: str = None,
    ):
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The user ID of the Quick BI.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Returns the result of deleting a user group member. Valid values:
        # 
        # *   true: The task is deleted.
        # *   false: The deletion failed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserGroupMemberResponseBody = None,
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
            temp_model = DeleteUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupMembersRequest(TeaModel):
    def __init__(
        self,
        user_group_ids: str = None,
        user_id: str = None,
    ):
        # The ID of the user group(s) to exit.
        # 
        # - Supports batch parameters, separate IDs with a comma (,).
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids
        # The UserID of the user to be removed from the user group. Note that this UserID refers to the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution. Possible values:
        # 
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserGroupMembersResponseBody = None,
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
            temp_model = DeleteUserGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserTagMetaRequest(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
    ):
        # The ID of the tag to be deleted.
        # 
        # This parameter is required.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class DeleteUserTagMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the deleted tag is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserTagMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserTagMetaResponseBody = None,
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
            temp_model = DeleteUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceConnectionInfoRequest(TeaModel):
    def __init__(
        self,
        ds_id: str = None,
    ):
        # Data source ID.
        # 
        # This parameter is required.
        self.ds_id = ds_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        return self


class GetDataSourceConnectionInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        address: str = None,
        auth_level: str = None,
        creator_id: str = None,
        ds_id: str = None,
        ds_type: str = None,
        ds_version: str = None,
        instance: str = None,
        instance_id: str = None,
        modify_user: str = None,
        no_sasl: bool = None,
        parent_ds_type: str = None,
        port: str = None,
        project: str = None,
        schema: str = None,
        show_name: str = None,
        workspace_id: str = None,
    ):
        # Database connection string address (domain or IP).
        self.address = address
        # Permission level:
        # 
        # - 0 -- Private
        # - 1 -- Collaborative Editing (old)
        # - 11 -- Collaborative Editing - Space Members
        # - 12 -- Collaborative Editing - Specified to Individuals
        self.auth_level = auth_level
        # Quick BI user ID of the creator.
        self.creator_id = creator_id
        # Data source ID.
        self.ds_id = ds_id
        # Data source type.
        self.ds_type = ds_type
        # Version of the data source.
        self.ds_version = ds_version
        # Database instance, corresponding to the database name, and for ODPS, it is the project.
        self.instance = instance
        # Instance ID.
        self.instance_id = instance_id
        # Quick BI user ID of the modifier.
        self.modify_user = modify_user
        # Whether the impala data source requires authentication to log in:
        # 
        # - true - Requires account and password login  
        # - false - No authentication required (default)
        self.no_sasl = no_sasl
        # Primary data source type for multi-engine data sources.
        self.parent_ds_type = parent_ds_type
        # Port.
        self.port = port
        # Used for front-end display when obtaining connection details for ODPS.
        self.project = project
        # Database schema, only needs to be set for databases that support schemas.
        self.schema = schema
        # Display name of the data source on the front end.
        self.show_name = show_name
        # Workspace ID to which the data source belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.auth_level is not None:
            result['AuthLevel'] = self.auth_level
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.ds_version is not None:
            result['DsVersion'] = self.ds_version
        if self.instance is not None:
            result['Instance'] = self.instance
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.no_sasl is not None:
            result['NoSasl'] = self.no_sasl
        if self.parent_ds_type is not None:
            result['ParentDsType'] = self.parent_ds_type
        if self.port is not None:
            result['Port'] = self.port
        if self.project is not None:
            result['Project'] = self.project
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AuthLevel') is not None:
            self.auth_level = m.get('AuthLevel')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('DsVersion') is not None:
            self.ds_version = m.get('DsVersion')
        if m.get('Instance') is not None:
            self.instance = m.get('Instance')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('NoSasl') is not None:
            self.no_sasl = m.get('NoSasl')
        if m.get('ParentDsType') is not None:
            self.parent_ds_type = m.get('ParentDsType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetDataSourceConnectionInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDataSourceConnectionInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Data source information.
        self.result = result
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDataSourceConnectionInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataSourceConnectionInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSourceConnectionInfoResponseBody = None,
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
            temp_model = GetDataSourceConnectionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMailTaskStatusRequest(TeaModel):
    def __init__(
        self,
        mail_id: str = None,
        task_id: int = None,
    ):
        # Mail ID
        # 
        # This parameter is required.
        self.mail_id = mail_id
        # Task ID
        # 
        # > - If the task ID is not provided, the latest task status will be returned by default;
        # > - If the task ID is provided, the status of the specified task will be returned.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_id is not None:
            result['MailId'] = self.mail_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailId') is not None:
            self.mail_id = m.get('MailId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetMailTaskStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        exec_time: str = None,
        mail_id: str = None,
        status: str = None,
        task_id: int = None,
    ):
        # Execution time, in the format yyyy-MM-dd HH:mm:ss
        self.exec_time = exec_time
        # Mail ID
        self.mail_id = mail_id
        # Mail status. Possible values:
        # 
        # - Success: SENT
        # - Failure: FAILED 
        # - In Progress: PROCESSING
        self.status = status
        # Task ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_time is not None:
            result['execTime'] = self.exec_time
        if self.mail_id is not None:
            result['mailId'] = self.mail_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('execTime') is not None:
            self.exec_time = m.get('execTime')
        if m.get('mailId') is not None:
            self.mail_id = m.get('mailId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetMailTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetMailTaskStatusResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful. 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetMailTaskStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMailTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMailTaskStatusResponseBody = None,
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
            temp_model = GetMailTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupInfoRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
    ):
        # Keyword of the user group name.
        # 
        # This parameter is required.
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class GetUserGroupInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        identified_path: str = None,
        modified_time: str = None,
        modify_user: str = None,
        parent_usergroup_id: str = None,
        usergroup_desc: str = None,
        usergroup_id: str = None,
        usergroup_name: str = None,
    ):
        # Creation time of the user group.
        self.create_time = create_time
        # Creator of the sub-user group. This is the UserID in Quick BI, not the UID in Alibaba Cloud.
        self.create_user = create_user
        # Directory level of the user group.
        self.identified_path = identified_path
        # Last modified time of the user group.
        self.modified_time = modified_time
        # Modifier of the user group. This is the UserID in Quick BI, not the UID in Alibaba Cloud.
        self.modify_user = modify_user
        # Parent user group ID.
        self.parent_usergroup_id = parent_usergroup_id
        # Description of the user group.
        self.usergroup_desc = usergroup_desc
        # User group ID.
        self.usergroup_id = usergroup_id
        # Name of the user group.
        self.usergroup_name = usergroup_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class GetUserGroupInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[GetUserGroupInfoResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # User group information.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetUserGroupInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserGroupInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserGroupInfoResponseBody = None,
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
            temp_model = GetUserGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorksEmbedListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        works_type: str = None,
        ws_id: str = None,
    ):
        # Report name (fuzzy match)
        self.keyword = keyword
        # Page number (defaults to 1 if empty)
        self.page_no = page_no
        # Number of items per page (defaults to 10 if empty)
        self.page_size = page_size
        # Report type
        # 
        # - page, Dashboard
        # - screen, Data Screen
        # - report, Spreadsheet
        # - ANALYSIS, Ad-hoc Analysis
        # - dashboardOfflineQuery, Self-service Data Retrieval
        # - dataForm, Data Entry Form
        self.works_type = works_type
        # Workspace ID
        self.ws_id = ws_id

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
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.ws_id is not None:
            result['WsId'] = self.ws_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WsId') is not None:
            self.ws_id = m.get('WsId')
        return self


class GetWorksEmbedListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        embed_time: str = None,
        works_id: str = None,
        works_name: str = None,
        works_type: str = None,
        workspace_id: str = None,
    ):
        # Embed time
        self.embed_time = embed_time
        # Report ID
        self.works_id = works_id
        # Report name
        self.works_name = works_name
        # Report type
        self.works_type = works_type
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.embed_time is not None:
            result['EmbedTime'] = self.embed_time
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.works_name is not None:
            result['WorksName'] = self.works_name
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbedTime') is not None:
            self.embed_time = m.get('EmbedTime')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorksName') is not None:
            self.works_name = m.get('WorksName')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetWorksEmbedListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[GetWorksEmbedListResponseBodyResultData] = None,
        page_no: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Array of reports
        self.data = data
        # Page number
        self.page_no = page_no
        # Number of items per page
        self.page_size = page_size
        # Total number of items
        self.total_num = total_num
        # Total number of pages
        self.total_pages = total_pages

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetWorksEmbedListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class GetWorksEmbedListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetWorksEmbedListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID
        self.request_id = request_id
        # Array of report objects
        self.result = result
        # Whether the request was successful
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetWorksEmbedListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWorksEmbedListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorksEmbedListResponseBody = None,
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
            temp_model = GetWorksEmbedListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApiDatasourceRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        page_num: int = None,
        page_size: int = None,
        workspace_id: str = None,
    ):
        # The keyword of the API data source name.
        self.key_word = key_word
        # Current page number for API data source list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Valid values: 1 to 100.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListApiDatasourceResponseBodyResultData(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        body: str = None,
        data_size: float = None,
        date_update_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        job_id: str = None,
        parameters: str = None,
        show_name: str = None,
        status_type: int = None,
    ):
        # The ID of the API data source.
        self.api_id = api_id
        # The parameter configuration of the query statement in JSON format. You can customize the parameter configuration.
        self.body = body
        # The data volume of the API data source.
        # 
        # *   Unit: Kbit/s
        self.data_size = data_size
        # The last synchronization time of the API data source.
        self.date_update_time = date_update_time
        # The time when the quota plan was created.
        self.gmt_create = gmt_create
        # The time when the optimization job was modified.
        self.gmt_modified = gmt_modified
        # The job ID.
        self.job_id = job_id
        # The parameter configurations in the JSONArray format.
        # 
        # *   name: parameter name
        # *   value: the parameter value
        self.parameters = parameters
        # The name of the API data source.
        self.show_name = show_name
        # The status of the API data source synchronization task.
        # 
        # Valid values:
        # 
        # *   0: the to be run.
        # *   1: The is running.
        # *   2: The is successfully.
        # *   3: failed.
        self.status_type = status_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.body is not None:
            result['Body'] = self.body
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.date_update_time is not None:
            result['DateUpdateTime'] = self.date_update_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.status_type is not None:
            result['StatusType'] = self.status_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DateUpdateTime') is not None:
            self.date_update_time = m.get('DateUpdateTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('StatusType') is not None:
            self.status_type = m.get('StatusType')
        return self


class ListApiDatasourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[ListApiDatasourceResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
    ):
        # The list of API data sources that were queried.
        self.data = data
        # The page number.
        self.page_num = page_num
        # The number of rows per page set when the interface is requested.
        self.page_size = page_size
        # The total number of rows.
        self.total_num = total_num

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListApiDatasourceResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class ListApiDatasourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListApiDatasourceResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The query results are returned.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListApiDatasourceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListApiDatasourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApiDatasourceResponseBody = None,
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
            temp_model = ListApiDatasourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListByUserGroupIdRequest(TeaModel):
    def __init__(
        self,
        user_group_ids: str = None,
    ):
        # The ID of the user group that you want to query. Separate multiple user groups with commas (,).
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')
        return self


class ListByUserGroupIdResponseBodyResultUserGroupModels(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        identified_path: str = None,
        modified_time: str = None,
        modify_user: str = None,
        parent_usergroup_id: str = None,
        usergroup_desc: str = None,
        usergroup_id: str = None,
        usergroup_name: str = None,
    ):
        # The time when the Secret was created.
        self.create_time = create_time
        # The UserID of the creator in the Quick BI.
        self.create_user = create_user
        # The path of the user group.
        self.identified_path = identified_path
        # The time when the protection policy was last modified.
        self.modified_time = modified_time
        # The UserID of the modifier in the Quick BI.
        self.modify_user = modify_user
        # The ID of the parent user group.
        self.parent_usergroup_id = parent_usergroup_id
        # The description of the user group.
        self.usergroup_desc = usergroup_desc
        # The ID of the user group.
        self.usergroup_id = usergroup_id
        # The name of the user group.
        self.usergroup_name = usergroup_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class ListByUserGroupIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        failed_user_group_ids: List[str] = None,
        user_group_models: List[ListByUserGroupIdResponseBodyResultUserGroupModels] = None,
    ):
        # List of failed user groups.
        self.failed_user_group_ids = failed_user_group_ids
        # The details of the user group that was queried.
        self.user_group_models = user_group_models

    def validate(self):
        if self.user_group_models:
            for k in self.user_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_user_group_ids is not None:
            result['FailedUserGroupIds'] = self.failed_user_group_ids
        result['UserGroupModels'] = []
        if self.user_group_models is not None:
            for k in self.user_group_models:
                result['UserGroupModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedUserGroupIds') is not None:
            self.failed_user_group_ids = m.get('FailedUserGroupIds')
        self.user_group_models = []
        if m.get('UserGroupModels') is not None:
            for k in m.get('UserGroupModels'):
                temp_model = ListByUserGroupIdResponseBodyResultUserGroupModels()
                self.user_group_models.append(temp_model.from_map(k))
        return self


class ListByUserGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListByUserGroupIdResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The user group query result is returned.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListByUserGroupIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListByUserGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListByUserGroupIdResponseBody = None,
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
            temp_model = ListByUserGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCollectionsRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the user. The user ID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListCollectionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        favorite_id: int = None,
        owner_id: str = None,
        works_id: str = None,
        works_name: str = None,
        works_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.favorite_id = favorite_id
        self.owner_id = owner_id
        self.works_id = works_id
        self.works_name = works_name
        self.works_type = works_type
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite_id is not None:
            result['FavoriteId'] = self.favorite_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.works_name is not None:
            result['WorksName'] = self.works_name
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FavoriteId') is not None:
            self.favorite_id = m.get('FavoriteId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorksName') is not None:
            self.works_name = m.get('WorksName')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListCollectionsResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.result = result
        # The primary key ID of the favorite record.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCollectionsResponseBody = None,
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
            temp_model = ListCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCubeDataLevelPermissionConfigRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # The type of the dataset row and column permission. Valid values:
        # 
        # *   ROW_LEVEL: row-level permissions
        # *   COLUMN_LEVEL: column-level permissions
        # 
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListCubeDataLevelPermissionConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # { "isOpen": 1, "extraConfigModel": { // Additional configuration information "ruleType": "ROW_LEVEL", // The row-level permission type. "missHitPolicy": "NONE", // The hit rule policy: NONE has no permissions, and ALL has permissions. "cubeId": "7c7223 ae-31d1-4d2f-b11f-3c744528014b" // The ID of the dataset. }, "ruleType": "ROW_LEVEL", // Row-column permission type\\
        # "ruleModels": [ { "ruleUsersModel": { // The target population. "userGroups": [ "0d5fb19b- ****-1248 fc27ca51", // The ID of the user group. "4aa3f089-****-85f0-0e8ac7c2dee9" ], "users": [ "HuangJia ***2e3fa822", // The ID of the user. "4334***84358" ] }, "ruleContentModel": { "ruleContentType": "ROW_FIELD", // The row-column permission type. "ruleContentJson": "{"conditionNode":{"caption": " Period ","isMeasure":false,"pathId":"7d3b073bc6","relationOperator":"not-null","name":"7d3b073bc6","value":{"value":[""}UM]," ENueType "} // The JSON string of the row-column permission rule. "ruleOriginConfigJson": "{"operator":"and","operands":[{"labelName": " Period ","isValid":true,"uniqueId":"5","fieldId":"7d3b073bc6","error":false,"fieldType":"string",": default "" value":{"conditionOp":"not-null","conditionValue":""},"valueType":"ENUM"}}],"isRelation":true}" }, // The fixed-format JSON string required by the frontend "isOpen": 1, // The status of the row-column permission configuration. 1. On. 0. Off. "hitTakeEffect": 1, // Specifies whether the rule takes effect after a column-level permission is hit. 1 takes effect and 0 takes effect. "ruleName": "Test row-level permission_Do not delete", // The name of the row-column permission rule. "ruleLevelType": "ROW_LEVEL", // The row-column permission type. "ruleId": "a5bb24 da-772f-45e8-a43c-a891683e14da", // The ID of the row-column permission rule. "cubeId": "7c7223 ae-31d1-4d2f-b11f-3c744528014b", // The ID of the dataset. "ruleTargetScope": "OTHERS" rule takes effect: ALL owner and OTHERS designated owner. } ], "cubeId": "7c7223 ae-31d1-4d2f-b11f-3c744528014b" // The ID of the dataset. }
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCubeDataLevelPermissionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCubeDataLevelPermissionConfigResponseBody = None,
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
            temp_model = ListCubeDataLevelPermissionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_type: str = None,
    ):
        # Dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # Type of row and column permission that the whitelist belongs to:
        # 
        # - ROW_LEVEL: Row-level permission
        # - COLUMN_LEVEL: Column-level permission
        # 
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListDataLevelPermissionWhiteListResponseBodyResultUsersModel(TeaModel):
    def __init__(
        self,
        user_groups: List[str] = None,
        users: List[str] = None,
    ):
        # UserGroups.
        self.user_groups = user_groups
        # Users.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_groups is not None:
            result['UserGroups'] = self.user_groups
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroups') is not None:
            self.user_groups = m.get('UserGroups')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ListDataLevelPermissionWhiteListResponseBodyResult(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_type: str = None,
        users_model: ListDataLevelPermissionWhiteListResponseBodyResultUsersModel = None,
    ):
        # Dataset ID.
        self.cube_id = cube_id
        # Type of dataset row and column permissions. Possible values:
        # 
        # - ROW_LEVEL: Row-level permission
        # - COLUMN_LEVEL: Column-level permission
        self.rule_type = rule_type
        # Whitelist information.
        self.users_model = users_model

    def validate(self):
        if self.users_model:
            self.users_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.users_model is not None:
            result['UsersModel'] = self.users_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('UsersModel') is not None:
            temp_model = ListDataLevelPermissionWhiteListResponseBodyResultUsersModel()
            self.users_model = temp_model.from_map(m['UsersModel'])
        return self


class ListDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListDataLevelPermissionWhiteListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Whitelist for the specified row-level permission type.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListDataLevelPermissionWhiteListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataLevelPermissionWhiteListResponseBody = None,
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
            temp_model = ListDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceRequest(TeaModel):
    def __init__(
        self,
        ds_type: str = None,
        workspace_id: str = None,
    ):
        # Data source type.
        self.ds_type = ds_type
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListDataSourceResponseBodyResult(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_name: str = None,
        datasource_id: str = None,
        ds_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        parent_ds_type: str = None,
        show_name: str = None,
    ):
        # Quick BI user ID of the creator.
        self.creator_id = creator_id
        # Owner\\"s nickname.
        self.creator_name = creator_name
        # Data source ID.
        self.datasource_id = datasource_id
        # Data source type.
        self.ds_type = ds_type
        # Creation time of the data source, in yyyy-MM-dd HH:mm:ss format.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Primary data source type for multi-engine data sources.
        self.parent_ds_type = parent_ds_type
        # Display name of the data source.
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.parent_ds_type is not None:
            result['ParentDsType'] = self.parent_ds_type
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ParentDsType') is not None:
            self.parent_ds_type = m.get('ParentDsType')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class ListDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataSourceResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of data source information.
        self.result = result
        # Whether the request was successful.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDataSourceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceResponseBody = None,
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
            temp_model = ListDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFavoriteReportsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_size: int = None,
        tree_type: str = None,
        user_id: str = None,
    ):
        # Keyword of the work name.
        self.keyword = keyword
        # Number of rows in the work list to be queried:
        # Default value: 10
        # Maximum value: 9999
        self.page_size = page_size
        # Type of the work to be queried (leave blank to query all types). Value range:
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        self.tree_type = tree_type
        # The UserID of the user in Quick BI to be queried.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListFavoriteReportsResponseBodyResultData(TeaModel):
    def __init__(
        self,
        favorite: bool = None,
        favorite_date: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_edit_auth: bool = None,
        has_view_auth: bool = None,
        name: str = None,
        owner_name: str = None,
        owner_num: str = None,
        publish_status: int = None,
        tree_id: str = None,
        type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Indicates whether the user has favorited the work.
        self.favorite = favorite
        # The timestamp when the work was favorited.
        self.favorite_date = favorite_date
        # Timestamp of the work creation.
        self.gmt_create = gmt_create
        # Timestamp of the work modification.
        self.gmt_modified = gmt_modified
        # Indicates whether the user has edit permission for the work.
        self.has_edit_auth = has_edit_auth
        # Check if the user has the permission to view the work.
        self.has_view_auth = has_view_auth
        # Name of the work.
        self.name = name
        # Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # UserID of the work owner.
        self.owner_num = owner_num
        # Publication status of the work. Value range:
        # - 0: Not published
        # - 1: Published
        # - 2: Saved with modifications, not published
        # - 3: Offline
        self.publish_status = publish_status
        # Work ID.
        self.tree_id = tree_id
        # Type of the work. Value range:
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        self.type = type
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.favorite_date is not None:
            result['FavoriteDate'] = self.favorite_date
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('FavoriteDate') is not None:
            self.favorite_date = m.get('FavoriteDate')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListFavoriteReportsResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[ListFavoriteReportsResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # List of works queried.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page set when requesting the interface.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFavoriteReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListFavoriteReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListFavoriteReportsResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the query result.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListFavoriteReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListFavoriteReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFavoriteReportsResponseBody = None,
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
            temp_model = ListFavoriteReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationRoleUsersRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        role_id: int = None,
    ):
        # Keyword for the nickname of the organization member.
        self.keyword = keyword
        # Page number.
        # 
        # - Default value is 1.
        self.page_num = page_num
        # Number of items per page.
        # - Default value is 10.
        self.page_size = page_size
        # Organization role ID, including predefined roles and custom roles:
        # 
        # - Organization Administrator (predefined role): 111111111
        # - Permission Administrator (predefined role): 111111112
        # - Regular User (predefined role): 111111113
        # - Custom Role: The corresponding role ID for a custom role
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class ListOrganizationRoleUsersResponseBodyResultData(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        user_id: str = None,
    ):
        # Nickname of the organization member.
        self.nick_name = nick_name
        # UserID of the organization member in Quick BI.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListOrganizationRoleUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[ListOrganizationRoleUsersResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # User list.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of items per page as set in the request.
        self.page_size = page_size
        # Total number of items.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOrganizationRoleUsersResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListOrganizationRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListOrganizationRoleUsersResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the list of users under the organization role.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListOrganizationRoleUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrganizationRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrganizationRoleUsersResponseBody = None,
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
            temp_model = ListOrganizationRoleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationRolesResponseBodyResultAuthConfigList(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
    ):
        # Permission type:
        # - quick_monitor: Metric monitoring
        # - subscription: Subscription management
        # - offline_download: Self-service data retrieval
        # - resource_package: Resource package management
        # - organization_ask: Organization identification code (AK/SK)
        # - developer_openapi: OpenAPI
        # - data_service: Data service
        # - admin_authorize3rd: Embedded analysis
        # - component_manage: Custom component
        # - template_open: Custom template
        # - custom_driver: Custom driver (supported only in standalone deployment)
        # - open_platform_custom_plugin: Custom plugin (supported only in standalone deployment)
        # - enterprise_safety: Enterprise security
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class ListOrganizationRolesResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_config_list: List[ListOrganizationRolesResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role permission configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Possible values:
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Role ID.
        self.role_id = role_id
        # Role name.
        self.role_name = role_name

    def validate(self):
        if self.auth_config_list:
            for k in self.auth_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthConfigList'] = []
        if self.auth_config_list is not None:
            for k in self.auth_config_list:
                result['AuthConfigList'].append(k.to_map() if k else None)
        if self.is_system_role is not None:
            result['IsSystemRole'] = self.is_system_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_config_list = []
        if m.get('AuthConfigList') is not None:
            for k in m.get('AuthConfigList'):
                temp_model = ListOrganizationRolesResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k))
        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListOrganizationRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListOrganizationRolesResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the list of organization roles.
        self.result = result
        # 是否请求成功。取值范围：
        # - true：请求成功
        # - false：请求失败
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListOrganizationRolesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrganizationRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrganizationRolesResponseBody = None,
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
            temp_model = ListOrganizationRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortalMenuAuthorizationRequest(TeaModel):
    def __init__(
        self,
        data_portal_id: str = None,
    ):
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        return self


class ListPortalMenuAuthorizationResponseBodyResultReceivers(TeaModel):
    def __init__(
        self,
        receiver_id: str = None,
        receiver_type: int = None,
    ):
        # The ID of the authorization object.
        self.receiver_id = receiver_id
        # The type of the authorization object. Valid values:
        # 
        # *   0: user
        # *   1: user group
        self.receiver_type = receiver_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        return self


class ListPortalMenuAuthorizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        menu_id: str = None,
        receivers: List[ListPortalMenuAuthorizationResponseBodyResultReceivers] = None,
        show_only_with_access: bool = None,
    ):
        # The menu ID of the BI portal leaf node.
        self.menu_id = menu_id
        # The details of the object to which the menu is authorized.
        self.receivers = receivers
        # Whether only authorization is visible. Valid values:
        # 
        # *   true: Only the authorization is visible.
        # *   false: Both are visible.
        self.show_only_with_access = show_only_with_access

    def validate(self):
        if self.receivers:
            for k in self.receivers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.menu_id is not None:
            result['MenuId'] = self.menu_id
        result['Receivers'] = []
        if self.receivers is not None:
            for k in self.receivers:
                result['Receivers'].append(k.to_map() if k else None)
        if self.show_only_with_access is not None:
            result['ShowOnlyWithAccess'] = self.show_only_with_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MenuId') is not None:
            self.menu_id = m.get('MenuId')
        self.receivers = []
        if m.get('Receivers') is not None:
            for k in m.get('Receivers'):
                temp_model = ListPortalMenuAuthorizationResponseBodyResultReceivers()
                self.receivers.append(temp_model.from_map(k))
        if m.get('ShowOnlyWithAccess') is not None:
            self.show_only_with_access = m.get('ShowOnlyWithAccess')
        return self


class ListPortalMenuAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListPortalMenuAuthorizationResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of authorization details of the portal menu.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPortalMenuAuthorizationResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPortalMenuAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPortalMenuAuthorizationResponseBody = None,
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
            temp_model = ListPortalMenuAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortalMenusRequest(TeaModel):
    def __init__(
        self,
        data_portal_id: str = None,
        user_id: str = None,
    ):
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The user ID in the Quick BI. When passed in, the list displays only the menus that the user has permissions on.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListPortalMenusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # A JSON string that levels the details of the portal menu list. Valid values:
        # 
        # *   menuType: the type of the menu.
        # 
        #     *   0: dashboard
        #     *   1: outer chain
        #     *   2: workbook
        #     *   4: directory folder
        #     *   5: form filling
        #     *   6: self-service data retrieval
        # 
        # *   menuId: menu ID
        # 
        # *   uri: ID or URL of the resource associated with the menu
        # 
        # *   showOnlyWithAccess: Authorized Only Visible
        # 
        # *   menuName: menu display name
        # 
        # *   dependentPermisson: whether the report resource associated with the menu has permissions
        # 
        # *   children: submenu
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPortalMenusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPortalMenusResponseBody = None,
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
            temp_model = ListPortalMenusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecentViewReportsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        offset_day: int = None,
        page_size: int = None,
        query_mode: str = None,
        tree_type: str = None,
        user_id: str = None,
    ):
        # Keyword of the name of the work.
        self.keyword = keyword
        # The number of days to query data in the last few days. Default value: 10.
        self.offset_day = offset_day
        # Query the number of rows in the work list:
        # 
        # *   Default value: 10.
        # *   Maximum value: 9999
        self.page_size = page_size
        # The query mode. Valid values:
        # 
        # *   1: Sort by number of visits
        # *   2: Sort by Last Access Time
        self.query_mode = query_mode
        # Query the type of the work (fill in the blank to query all types). Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   REPORT: workbook
        self.tree_type = tree_type
        # The UserID of the user in the Quick BI.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.offset_day is not None:
            result['OffsetDay'] = self.offset_day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OffsetDay') is not None:
            self.offset_day = m.get('OffsetDay')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRecentViewReportsResponseBodyResultData(TeaModel):
    def __init__(
        self,
        favorite: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_edit_auth: bool = None,
        has_view_auth: bool = None,
        latest_view_time: str = None,
        name: str = None,
        owner_name: str = None,
        owner_num: str = None,
        publish_status: int = None,
        tree_id: str = None,
        type: str = None,
        view_count: int = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Queries whether the user has collected the work.
        self.favorite = favorite
        # The timestamp when the work was created.
        self.gmt_create = gmt_create
        # The timestamp when the work was modified.
        self.gmt_modified = gmt_modified
        # The query user has the editing rights of the work.
        self.has_edit_auth = has_edit_auth
        # The query user has the permission to view the work.
        self.has_view_auth = has_view_auth
        # The timestamp when the work was last accessed.
        self.latest_view_time = latest_view_time
        # The name of the work.
        self.name = name
        # The Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # The UserID of the work owner.
        self.owner_num = owner_num
        # The publication status of the work. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified and saved but not published.
        # *   3: unpublished
        self.publish_status = publish_status
        # The ID of the work.
        self.tree_id = tree_id
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   REPORT: workbook
        self.type = type
        # The number of times the work was accessed.
        self.view_count = view_count
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.latest_view_time is not None:
            result['LatestViewTime'] = self.latest_view_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.view_count is not None:
            result['ViewCount'] = self.view_count
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('LatestViewTime') is not None:
            self.latest_view_time = m.get('LatestViewTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListRecentViewReportsResponseBodyResult(TeaModel):
    def __init__(
        self,
        attention: str = None,
        data: List[ListRecentViewReportsResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Attention
        self.attention = attention
        # The list of queried works.
        self.data = data
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        # 
        # *   Default value: 10.
        # *   Maximum of 100 articles
        self.page_size = page_size
        # The total number of rows in the table.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_pages = total_pages

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
        if self.attention is not None:
            result['Attention'] = self.attention
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attention') is not None:
            self.attention = m.get('Attention')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRecentViewReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListRecentViewReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRecentViewReportsResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The query results are returned.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRecentViewReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRecentViewReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecentViewReportsResponseBody = None,
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
            temp_model = ListRecentViewReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedReportsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_size: int = None,
        tree_type: str = None,
        user_id: str = None,
    ):
        # Keyword of the name of the work.
        self.keyword = keyword
        # Query the number of rows in the work list:
        # 
        # *   Default value: 10.
        # *   Maximum value: 9999
        self.page_size = page_size
        # Query the type of the work (fill in the blank to query all types). Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   REPORT: workbook
        self.tree_type = tree_type
        # The UserID of the user to be queried in the Quick BI.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tree_type is not None:
            result['TreeType'] = self.tree_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TreeType') is not None:
            self.tree_type = m.get('TreeType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSharedReportsResponseBodyResultData(TeaModel):
    def __init__(
        self,
        favorite: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_edit_auth: bool = None,
        has_view_auth: bool = None,
        name: str = None,
        owner_name: str = None,
        owner_num: str = None,
        publish_status: int = None,
        tree_id: str = None,
        type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Queries whether the user has collected the work.
        self.favorite = favorite
        # The timestamp when the work was created.
        self.gmt_create = gmt_create
        # The timestamp when the work was modified.
        self.gmt_modified = gmt_modified
        # The query user has the editing rights of the work.
        self.has_edit_auth = has_edit_auth
        # The query user has the permission to view the work.
        self.has_view_auth = has_view_auth
        # The name of the work.
        self.name = name
        # The Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # The UserID of the work owner.
        self.owner_num = owner_num
        # The publication status of the work. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified and saved but not published.
        # *   3: unpublished
        self.publish_status = publish_status
        # The ID of the work.
        self.tree_id = tree_id
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   REPORT: workbook
        self.type = type
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite is not None:
            result['Favorite'] = self.favorite
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth
        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.tree_id is not None:
            result['TreeId'] = self.tree_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')
        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListSharedReportsResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[ListSharedReportsResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # The list of queried works.
        self.data = data
        # The page number of the returned page.
        self.page_num = page_num
        # The number of rows per page set when the interface is requested.
        self.page_size = page_size
        # The total number of rows in the table.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSharedReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListSharedReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListSharedReportsResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The query results are returned.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListSharedReportsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSharedReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSharedReportsResponseBody = None,
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
            temp_model = ListSharedReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the user. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserGroupsByUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        identified_path: str = None,
        modified_time: str = None,
        modify_user: str = None,
        parent_usergroup_id: str = None,
        usergroup_desc: str = None,
        usergroup_id: str = None,
        usergroup_name: str = None,
    ):
        # The time when the user group was created.
        self.create_time = create_time
        # The user group creator. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        self.create_user = create_user
        # Directory level of the user group.
        self.identified_path = identified_path
        # The time when the user group was last modified.
        self.modified_time = modified_time
        # The user group modifier. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        self.modify_user = modify_user
        # The ID of the user group.
        self.parent_usergroup_id = parent_usergroup_id
        # The description of the user group.
        self.usergroup_desc = usergroup_desc
        # The ID of the user group.
        self.usergroup_id = usergroup_id
        # The name of the user group.
        self.usergroup_name = usergroup_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_usergroup_id is not None:
            result['ParentUsergroupId'] = self.parent_usergroup_id
        if self.usergroup_desc is not None:
            result['UsergroupDesc'] = self.usergroup_desc
        if self.usergroup_id is not None:
            result['UsergroupId'] = self.usergroup_id
        if self.usergroup_name is not None:
            result['UsergroupName'] = self.usergroup_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUsergroupId') is not None:
            self.parent_usergroup_id = m.get('ParentUsergroupId')
        if m.get('UsergroupDesc') is not None:
            self.usergroup_desc = m.get('UsergroupDesc')
        if m.get('UsergroupId') is not None:
            self.usergroup_id = m.get('UsergroupId')
        if m.get('UsergroupName') is not None:
            self.usergroup_name = m.get('UsergroupName')
        return self


class ListUserGroupsByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListUserGroupsByUserIdResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the group.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListUserGroupsByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserGroupsByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserGroupsByUserIdResponseBody = None,
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
            temp_model = ListUserGroupsByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspaceRoleUsersRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        role_id: int = None,
        workspace_id: str = None,
    ):
        # Keyword for the user\\"s nickname.
        self.keyword = keyword
        # Current page number for pagination:
        # 
        # - Starting value: 1
        # - Default value: 1
        self.page_num = page_num
        # Number of items per page for pagination:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom roles: The corresponding role ID for custom roles
        # 
        # This parameter is required.
        self.role_id = role_id
        # The ID of the workspace. This parameter is optional. If you do not set this parameter, the roles of all workspaces are returned.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListWorkspaceRoleUsersResponseBodyResultData(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        user_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Nickname of the organization member.
        self.nick_name = nick_name
        # UserID of the organization member in Quick BI.
        self.user_id = user_id
        # Workspace ID.
        self.workspace_id = workspace_id
        # Workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class ListWorkspaceRoleUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[ListWorkspaceRoleUsersResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # User list.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of items per page as set in the request.
        self.page_size = page_size
        # Total number of items.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWorkspaceRoleUsersResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListWorkspaceRoleUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListWorkspaceRoleUsersResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the list of users under the specified workspace role.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful. 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListWorkspaceRoleUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWorkspaceRoleUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspaceRoleUsersResponseBody = None,
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
            temp_model = ListWorkspaceRoleUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspaceRolesRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListWorkspaceRolesResponseBodyResultAuthConfigList(TeaModel):
    def __init__(
        self,
        action_auth_keys: List[str] = None,
        auth_key: str = None,
    ):
        # Authorization scope.
        self.action_auth_keys = action_auth_keys
        # Authorization type:
        # - portal_create: Data Portal
        # - dashboard_create: Dashboard
        # - report_create: Spreadsheet
        # - screen_create: Data Screen
        # - analysis: Ad-hoc Analysis
        # - offline_download: Self-service Data Retrieval
        # - data_form: Data Entry
        # - quick_etl: Data Preparation
        # - cube: Dataset
        # - datasource: Data Source
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_auth_keys is not None:
            result['ActionAuthKeys'] = self.action_auth_keys
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionAuthKeys') is not None:
            self.action_auth_keys = m.get('ActionAuthKeys')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class ListWorkspaceRolesResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_config_list: List[ListWorkspaceRolesResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role authorization configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Value range:
        # 
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Workspace role ID, including predefined and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom role: The corresponding role ID for a custom role
        self.role_id = role_id
        # Role name.
        self.role_name = role_name

    def validate(self):
        if self.auth_config_list:
            for k in self.auth_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthConfigList'] = []
        if self.auth_config_list is not None:
            for k in self.auth_config_list:
                result['AuthConfigList'].append(k.to_map() if k else None)
        if self.is_system_role is not None:
            result['IsSystemRole'] = self.is_system_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_config_list = []
        if m.get('AuthConfigList') is not None:
            for k in m.get('AuthConfigList'):
                temp_model = ListWorkspaceRolesResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k))
        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class ListWorkspaceRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListWorkspaceRolesResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of workspace roles.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful. 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListWorkspaceRolesResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWorkspaceRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspaceRolesResponseBody = None,
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
            temp_model = ListWorkspaceRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManualRunMailTaskRequest(TeaModel):
    def __init__(
        self,
        mail_id: str = None,
    ):
        # The ID of the email task in the subscription management interface.
        # 
        # This parameter is required.
        self.mail_id = mail_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mail_id is not None:
            result['MailId'] = self.mail_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailId') is not None:
            self.mail_id = m.get('MailId')
        return self


class ManualRunMailTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Indicates whether the execution was successful.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request succeeded 
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ManualRunMailTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManualRunMailTaskResponseBody = None,
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
            temp_model = ManualRunMailTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiDatasourceParametersRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        parameters: str = None,
        workspace_id: str = None,
    ):
        # The ID of the API data source.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The configuration of API data parameters in the JSONArray format. You can modify a maximum of 10 parameters.
        # 
        # *   name: the name of a common parameter or a parameter in a query statement
        # *   value: the value of a common parameter or a parameter in a query statement.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ModifyApiDatasourceParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The execution result of the interface. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyApiDatasourceParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiDatasourceParametersResponseBody = None,
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
            temp_model = ModifyApiDatasourceParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCopilotEmbedConfigRequest(TeaModel):
    def __init__(
        self,
        agent_name: str = None,
        copilot_id: str = None,
        data_range: str = None,
        module_name: str = None,
    ):
        # Agent nickname.
        self.agent_name = agent_name
        # Embedding ID.
        # 
        # This parameter is required.
        self.copilot_id = copilot_id
        # Data range.
        # >Notice: The parameter type is jsonString, and only one switch between analysis themes and query resources can be effective. When the all-select switch is true, it takes precedence. It is recommended to pass only one parameter, with other notes
        self.data_range = data_range
        # Module name.
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id
        if self.data_range is not None:
            result['DataRange'] = self.data_range
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')
        if m.get('DataRange') is not None:
            self.data_range = m.get('DataRange')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class ModifyCopilotEmbedConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the API execution. Possible values:
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful
        # - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyCopilotEmbedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCopilotEmbedConfigResponseBody = None,
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
            temp_model = ModifyCopilotEmbedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryApprovalInfoRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        status: int = None,
        user_id: str = None,
    ):
        # Page number, default is 1.
        self.page = page
        # Number of rows per page, default is 1000.
        self.page_size = page_size
        # Approval status:
        # - 0: Pending
        # - 1: Processed
        # 
        # This parameter is required.
        self.status = status
        # Current approver user ID, qbi user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

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
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryApprovalInfoResponseBodyResultData(TeaModel):
    def __init__(
        self,
        applicant_id: str = None,
        applicant_name: str = None,
        application_id: str = None,
        apply_reason: str = None,
        approver_id: str = None,
        approver_name: str = None,
        delete_flag: bool = None,
        expire_date: int = None,
        flag_status: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        handle_reason: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        workspace_name: str = None,
    ):
        # Applicant\\"s user ID, qbi user ID.
        self.applicant_id = applicant_id
        # Applicant\\"s nickname.
        self.applicant_name = applicant_name
        # Application ID.
        self.application_id = application_id
        # Application reason.
        self.apply_reason = apply_reason
        # Approver\\"s user ID, qbi user ID.
        self.approver_id = approver_id
        # Approver\\"s nickname.
        self.approver_name = approver_name
        # Whether the resource has been deleted:
        # - true: Deleted
        # - false: Not deleted
        self.delete_flag = delete_flag
        # Permission expiration date, timestamp.
        self.expire_date = expire_date
        # Permission approval status:
        # - 0: Under review, corresponding to 0 in the request parameters
        # - 1: Approved, corresponding to 1 in the request parameters
        # - 2: Rejected, corresponding to 1 in the request parameters
        self.flag_status = flag_status
        # Application creation time, timestamp.
        self.gmt_create = gmt_create
        # Application modification time, timestamp.
        self.gmt_modified = gmt_modified
        # Handling reason.
        self.handle_reason = handle_reason
        # The ID of the resource for which permission is requested.
        self.resource_id = resource_id
        # The name of the resource for which permission is requested (e.g., report name, space name...).
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicant_id is not None:
            result['ApplicantId'] = self.applicant_id
        if self.applicant_name is not None:
            result['ApplicantName'] = self.applicant_name
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_reason is not None:
            result['ApplyReason'] = self.apply_reason
        if self.approver_id is not None:
            result['ApproverId'] = self.approver_id
        if self.approver_name is not None:
            result['ApproverName'] = self.approver_name
        if self.delete_flag is not None:
            result['DeleteFlag'] = self.delete_flag
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.flag_status is not None:
            result['FlagStatus'] = self.flag_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.handle_reason is not None:
            result['HandleReason'] = self.handle_reason
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicantId') is not None:
            self.applicant_id = m.get('ApplicantId')
        if m.get('ApplicantName') is not None:
            self.applicant_name = m.get('ApplicantName')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyReason') is not None:
            self.apply_reason = m.get('ApplyReason')
        if m.get('ApproverId') is not None:
            self.approver_id = m.get('ApproverId')
        if m.get('ApproverName') is not None:
            self.approver_name = m.get('ApproverName')
        if m.get('DeleteFlag') is not None:
            self.delete_flag = m.get('DeleteFlag')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('FlagStatus') is not None:
            self.flag_status = m.get('FlagStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HandleReason') is not None:
            self.handle_reason = m.get('HandleReason')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryApprovalInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryApprovalInfoResponseBodyResultData] = None,
        page: int = None,
        page_size: int = None,
        start: int = None,
        total: int = None,
        total_pages: int = None,
    ):
        # Array of approval flow information.
        self.data = data
        # The current page number.
        self.page = page
        # The number of records requested per page.
        self.page_size = page_size
        # The starting position of the current page.
        self.start = start
        # The total number of items.
        self.total = total
        # The total number of pages.
        self.total_pages = total_pages

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
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start is not None:
            result['Start'] = self.start
        if self.total is not None:
            result['Total'] = self.total
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryApprovalInfoResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryApprovalInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryApprovalInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return the result of the interface execution.
        self.result = result
        # Indicates whether the API call was successful. Possible values are:
        # - true: success
        # - false: failure
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryApprovalInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryApprovalInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryApprovalInfoResponseBody = None,
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
            temp_model = QueryApprovalInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAuditLogRequest(TeaModel):
    def __init__(
        self,
        access_source_flag: str = None,
        end_date: str = None,
        log_type: str = None,
        operator_id: str = None,
        operator_types: str = None,
        resource_type: str = None,
        start_date: str = None,
        user_access_device: str = None,
        workspace_id: str = None,
    ):
        self.access_source_flag = access_source_flag
        # End date of the query, format ("yyyyMMdd").
        # 
        # This parameter is required.
        self.end_date = end_date
        # Log type:
        # - dataView - Access
        # - function - Operation
        # - permission - Permission
        # 
        # This parameter is required.
        self.log_type = log_type
        # Operator\\"s user ID.
        self.operator_id = operator_id
        # Permission/Access/Operation type, empty - default all;
        # 
        # Refer to the audit log code values, send multiple values separated by English commas.
        self.operator_types = operator_types
        # Resource type, refer to the work type.
        self.resource_type = resource_type
        # Start date of the query, format ("yyyyMMdd"), cannot be earlier than 90 days from the current time.
        # 
        # This parameter is required.
        self.start_date = start_date
        self.user_access_device = user_access_device
        # Workspace ID, the ID of the workspace to which the logs to be queried belong.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_source_flag is not None:
            result['AccessSourceFlag'] = self.access_source_flag
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_types is not None:
            result['OperatorTypes'] = self.operator_types
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.user_access_device is not None:
            result['UserAccessDevice'] = self.user_access_device
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessSourceFlag') is not None:
            self.access_source_flag = m.get('AccessSourceFlag')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorTypes') is not None:
            self.operator_types = m.get('OperatorTypes')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('UserAccessDevice') is not None:
            self.user_access_device = m.get('UserAccessDevice')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryAuditLogResponseBodyResult(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        operator_account_name: str = None,
        operator_name: str = None,
        operator_type: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        workspace_id: str = None,
    ):
        # Log time.
        self.gmt_create = gmt_create
        # Operator account.
        self.operator_account_name = operator_account_name
        # Operator\\"s nickname.
        self.operator_name = operator_name
        # Operation type.
        self.operator_type = operator_type
        # Target ID.
        self.target_id = target_id
        # Target name.
        self.target_name = target_name
        # Target type.
        self.target_type = target_type
        # Workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.operator_account_name is not None:
            result['OperatorAccountName'] = self.operator_account_name
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OperatorAccountName') is not None:
            self.operator_account_name = m.get('OperatorAccountName')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryAuditLogResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of logs.
        self.result = result
        # Indicates whether the request was successful. Possible values: 
        # - true: The request succeeded 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryAuditLogResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAuditLogResponseBody = None,
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
            temp_model = QueryAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryComponentPerformanceRequest(TeaModel):
    def __init__(
        self,
        cost_time_avg_min: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        report_id: str = None,
        resource_type: str = None,
        workspace_id: str = None,
    ):
        # The average duration (minutes).
        self.cost_time_avg_min = cost_time_avg_min
        # The current page number of the workspace member list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_size = page_size
        # The query type. Valid values:
        # 
        # *   **lastDay**: Yesterday
        # *   **sevenDays**: Within seven days
        # *   **thirtyDays**: Within 30 days
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        self.report_id = report_id
        # The resource types.
        self.resource_type = resource_type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time_avg_min is not None:
            result['CostTimeAvgMin'] = self.cost_time_avg_min
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTimeAvgMin') is not None:
            self.cost_time_avg_min = m.get('CostTimeAvgMin')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryComponentPerformanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        cache_cost_time_avg: float = None,
        cache_query_count: int = None,
        component_id: str = None,
        component_name: str = None,
        cost_time_avg: float = None,
        query_count: int = None,
        query_count_avg: float = None,
        query_over_five_percent_num: float = None,
        query_over_five_sec_percent: str = None,
        query_over_ten_sec_percent: str = None,
        query_over_ten_sec_percent_num: float = None,
        query_timeout_count: int = None,
        query_timeout_count_percent: float = None,
        quick_index_cost_time_avg: float = None,
        quick_index_query_count: int = None,
        repeat_query_percent: str = None,
        repeat_query_percent_num: float = None,
        repeat_sql_query_count: int = None,
        repeat_sql_query_percent: str = None,
        report_id: str = None,
        report_name: str = None,
        report_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The average duration of cache hits.
        self.cache_cost_time_avg = cache_cost_time_avg
        # The number of cache hits.
        self.cache_query_count = cache_query_count
        # The component ID.
        self.component_id = component_id
        # The name of the add-on.
        self.component_name = component_name
        # The average query duration associated with the SQL pattern.
        self.cost_time_avg = cost_time_avg
        # The number of queries.
        self.query_count = query_count
        # The average number of queries.
        self.query_count_avg = query_count_avg
        # The query exceeds the 5S number of queries.
        self.query_over_five_percent_num = query_over_five_percent_num
        # Query the proportion of more than 5S.
        self.query_over_five_sec_percent = query_over_five_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent = query_over_ten_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent_num = query_over_ten_sec_percent_num
        # The number of times that the chart query times out.
        self.query_timeout_count = query_timeout_count
        # The percentage of timeout times for chart queries.
        self.query_timeout_count_percent = query_timeout_count_percent
        # The average time consumed by the Quick engine query.
        self.quick_index_cost_time_avg = quick_index_cost_time_avg
        # The number of times that the Quick engine is hit.
        self.quick_index_query_count = quick_index_query_count
        # The proportion of duplicate queries.
        self.repeat_query_percent = repeat_query_percent
        # The number of duplicate queries.
        self.repeat_query_percent_num = repeat_query_percent_num
        # The number of times the query is repeated.
        self.repeat_sql_query_count = repeat_sql_query_count
        # The proportion of duplicate queries.
        self.repeat_sql_query_percent = repeat_sql_query_percent
        # The ID of the work.
        self.report_id = report_id
        # The name of the report.
        self.report_name = report_name
        # The format of the report.
        self.report_type = report_type
        # The unique ID of the space.
        self.workspace_id = workspace_id
        # The name of the group.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_cost_time_avg is not None:
            result['CacheCostTimeAvg'] = self.cache_cost_time_avg
        if self.cache_query_count is not None:
            result['CacheQueryCount'] = self.cache_query_count
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.cost_time_avg is not None:
            result['CostTimeAvg'] = self.cost_time_avg
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.query_count_avg is not None:
            result['QueryCountAvg'] = self.query_count_avg
        if self.query_over_five_percent_num is not None:
            result['QueryOverFivePercentNum'] = self.query_over_five_percent_num
        if self.query_over_five_sec_percent is not None:
            result['QueryOverFiveSecPercent'] = self.query_over_five_sec_percent
        if self.query_over_ten_sec_percent is not None:
            result['QueryOverTenSecPercent'] = self.query_over_ten_sec_percent
        if self.query_over_ten_sec_percent_num is not None:
            result['QueryOverTenSecPercentNum'] = self.query_over_ten_sec_percent_num
        if self.query_timeout_count is not None:
            result['QueryTimeoutCount'] = self.query_timeout_count
        if self.query_timeout_count_percent is not None:
            result['QueryTimeoutCountPercent'] = self.query_timeout_count_percent
        if self.quick_index_cost_time_avg is not None:
            result['QuickIndexCostTimeAvg'] = self.quick_index_cost_time_avg
        if self.quick_index_query_count is not None:
            result['QuickIndexQueryCount'] = self.quick_index_query_count
        if self.repeat_query_percent is not None:
            result['RepeatQueryPercent'] = self.repeat_query_percent
        if self.repeat_query_percent_num is not None:
            result['RepeatQueryPercentNum'] = self.repeat_query_percent_num
        if self.repeat_sql_query_count is not None:
            result['RepeatSqlQueryCount'] = self.repeat_sql_query_count
        if self.repeat_sql_query_percent is not None:
            result['RepeatSqlQueryPercent'] = self.repeat_sql_query_percent
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_name is not None:
            result['ReportName'] = self.report_name
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostTimeAvg') is not None:
            self.cache_cost_time_avg = m.get('CacheCostTimeAvg')
        if m.get('CacheQueryCount') is not None:
            self.cache_query_count = m.get('CacheQueryCount')
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('CostTimeAvg') is not None:
            self.cost_time_avg = m.get('CostTimeAvg')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('QueryCountAvg') is not None:
            self.query_count_avg = m.get('QueryCountAvg')
        if m.get('QueryOverFivePercentNum') is not None:
            self.query_over_five_percent_num = m.get('QueryOverFivePercentNum')
        if m.get('QueryOverFiveSecPercent') is not None:
            self.query_over_five_sec_percent = m.get('QueryOverFiveSecPercent')
        if m.get('QueryOverTenSecPercent') is not None:
            self.query_over_ten_sec_percent = m.get('QueryOverTenSecPercent')
        if m.get('QueryOverTenSecPercentNum') is not None:
            self.query_over_ten_sec_percent_num = m.get('QueryOverTenSecPercentNum')
        if m.get('QueryTimeoutCount') is not None:
            self.query_timeout_count = m.get('QueryTimeoutCount')
        if m.get('QueryTimeoutCountPercent') is not None:
            self.query_timeout_count_percent = m.get('QueryTimeoutCountPercent')
        if m.get('QuickIndexCostTimeAvg') is not None:
            self.quick_index_cost_time_avg = m.get('QuickIndexCostTimeAvg')
        if m.get('QuickIndexQueryCount') is not None:
            self.quick_index_query_count = m.get('QuickIndexQueryCount')
        if m.get('RepeatQueryPercent') is not None:
            self.repeat_query_percent = m.get('RepeatQueryPercent')
        if m.get('RepeatQueryPercentNum') is not None:
            self.repeat_query_percent_num = m.get('RepeatQueryPercentNum')
        if m.get('RepeatSqlQueryCount') is not None:
            self.repeat_sql_query_count = m.get('RepeatSqlQueryCount')
        if m.get('RepeatSqlQueryPercent') is not None:
            self.repeat_sql_query_percent = m.get('RepeatSqlQueryPercent')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportName') is not None:
            self.report_name = m.get('ReportName')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryComponentPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryComponentPerformanceResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result returned.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryComponentPerformanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryComponentPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryComponentPerformanceResponseBody = None,
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
            temp_model = QueryComponentPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCopilotEmbedConfigRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
    ):
        # Name of the embedded configuration module, supports fuzzy search.
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class QueryCopilotEmbedConfigResponseBodyResultDataRange(TeaModel):
    def __init__(
        self,
        all_cube: bool = None,
        all_theme: bool = None,
        llm_cubes: List[str] = None,
        themes: List[str] = None,
    ):
        # Whether all question resources are selected.
        self.all_cube = all_cube
        # Whether all analysis themes are selected.
        self.all_theme = all_theme
        # Collection of question resource IDs.
        self.llm_cubes = llm_cubes
        # Collection of analysis theme IDs.
        self.themes = themes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_cube is not None:
            result['AllCube'] = self.all_cube
        if self.all_theme is not None:
            result['AllTheme'] = self.all_theme
        if self.llm_cubes is not None:
            result['LlmCubes'] = self.llm_cubes
        if self.themes is not None:
            result['Themes'] = self.themes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCube') is not None:
            self.all_cube = m.get('AllCube')
        if m.get('AllTheme') is not None:
            self.all_theme = m.get('AllTheme')
        if m.get('LlmCubes') is not None:
            self.llm_cubes = m.get('LlmCubes')
        if m.get('Themes') is not None:
            self.themes = m.get('Themes')
        return self


class QueryCopilotEmbedConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        agent_name: str = None,
        copilot_id: str = None,
        create_user: str = None,
        create_user_name: str = None,
        data_range: QueryCopilotEmbedConfigResponseBodyResultDataRange = None,
        modify_user: str = None,
        module_name: str = None,
        show_name: str = None,
    ):
        # Robot\\"s nickname.
        self.agent_name = agent_name
        # Embedding ID.
        self.copilot_id = copilot_id
        # ID of the creator.
        self.create_user = create_user
        # Nickname of the creator.
        self.create_user_name = create_user_name
        # Data range (analysis themes and question resources).
        self.data_range = data_range
        # ID of the modifier.
        self.modify_user = modify_user
        # Module name.
        self.module_name = module_name
        # Name of the embedded module.
        self.show_name = show_name

    def validate(self):
        if self.data_range:
            self.data_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name
        if self.copilot_id is not None:
            result['CopilotId'] = self.copilot_id
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.data_range is not None:
            result['DataRange'] = self.data_range.to_map()
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')
        if m.get('CopilotId') is not None:
            self.copilot_id = m.get('CopilotId')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DataRange') is not None:
            temp_model = QueryCopilotEmbedConfigResponseBodyResultDataRange()
            self.data_range = temp_model.from_map(m['DataRange'])
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        return self


class QueryCopilotEmbedConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryCopilotEmbedConfigResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of embedded configurations.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryCopilotEmbedConfigResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCopilotEmbedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCopilotEmbedConfigResponseBody = None,
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
            temp_model = QueryCopilotEmbedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCubeOptimizationRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryCubeOptimizationResponseBodyResultCubePerformanceDiagnoseModel(TeaModel):
    def __init__(
        self,
        cache_cost_time_avg: float = None,
        cache_query_count: int = None,
        cost_time_avg: float = None,
        cube_id: str = None,
        cube_name: str = None,
        query_count: int = None,
        query_count_avg: float = None,
        query_over_five_percent_num: float = None,
        query_over_five_sec_percent: str = None,
        query_over_ten_sec_percent: str = None,
        query_over_ten_sec_percent_num: float = None,
        query_timeout_count: int = None,
        query_timeout_count_percent: float = None,
        quick_index_cost_time_avg: float = None,
        quick_index_query_count: int = None,
        repeat_query_percent: str = None,
        repeat_query_percent_num: float = None,
        repeat_sql_query_count: int = None,
        repeat_sql_query_percent: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The average duration of cache hits.
        self.cache_cost_time_avg = cache_cost_time_avg
        # The number of cache hits.
        self.cache_query_count = cache_query_count
        # The average query duration associated with the SQL pattern.
        self.cost_time_avg = cost_time_avg
        # The dataset ID.
        self.cube_id = cube_id
        # The name of the dataset.
        self.cube_name = cube_name
        # The number of queries.
        self.query_count = query_count
        # The average number of queries.
        self.query_count_avg = query_count_avg
        # The percentage of the number of queries that exceed the 5S.
        self.query_over_five_percent_num = query_over_five_percent_num
        # Query the proportion of more than 5S.
        self.query_over_five_sec_percent = query_over_five_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent = query_over_ten_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent_num = query_over_ten_sec_percent_num
        # The number of times that the chart query times out.
        self.query_timeout_count = query_timeout_count
        # The percentage of timeout times for chart queries.
        self.query_timeout_count_percent = query_timeout_count_percent
        # The average time consumed by the Quick engine query.
        self.quick_index_cost_time_avg = quick_index_cost_time_avg
        # The number of times that the Quick engine is hit.
        self.quick_index_query_count = quick_index_query_count
        # The proportion of duplicate queries.
        self.repeat_query_percent = repeat_query_percent
        # The number of duplicate queries.
        self.repeat_query_percent_num = repeat_query_percent_num
        # The number of times the query is repeated.
        self.repeat_sql_query_count = repeat_sql_query_count
        # The proportion of duplicate queries.
        self.repeat_sql_query_percent = repeat_sql_query_percent
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_cost_time_avg is not None:
            result['CacheCostTimeAvg'] = self.cache_cost_time_avg
        if self.cache_query_count is not None:
            result['CacheQueryCount'] = self.cache_query_count
        if self.cost_time_avg is not None:
            result['CostTimeAvg'] = self.cost_time_avg
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.cube_name is not None:
            result['CubeName'] = self.cube_name
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.query_count_avg is not None:
            result['QueryCountAvg'] = self.query_count_avg
        if self.query_over_five_percent_num is not None:
            result['QueryOverFivePercentNum'] = self.query_over_five_percent_num
        if self.query_over_five_sec_percent is not None:
            result['QueryOverFiveSecPercent'] = self.query_over_five_sec_percent
        if self.query_over_ten_sec_percent is not None:
            result['QueryOverTenSecPercent'] = self.query_over_ten_sec_percent
        if self.query_over_ten_sec_percent_num is not None:
            result['QueryOverTenSecPercentNum'] = self.query_over_ten_sec_percent_num
        if self.query_timeout_count is not None:
            result['QueryTimeoutCount'] = self.query_timeout_count
        if self.query_timeout_count_percent is not None:
            result['QueryTimeoutCountPercent'] = self.query_timeout_count_percent
        if self.quick_index_cost_time_avg is not None:
            result['QuickIndexCostTimeAvg'] = self.quick_index_cost_time_avg
        if self.quick_index_query_count is not None:
            result['QuickIndexQueryCount'] = self.quick_index_query_count
        if self.repeat_query_percent is not None:
            result['RepeatQueryPercent'] = self.repeat_query_percent
        if self.repeat_query_percent_num is not None:
            result['RepeatQueryPercentNum'] = self.repeat_query_percent_num
        if self.repeat_sql_query_count is not None:
            result['RepeatSqlQueryCount'] = self.repeat_sql_query_count
        if self.repeat_sql_query_percent is not None:
            result['RepeatSqlQueryPercent'] = self.repeat_sql_query_percent
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostTimeAvg') is not None:
            self.cache_cost_time_avg = m.get('CacheCostTimeAvg')
        if m.get('CacheQueryCount') is not None:
            self.cache_query_count = m.get('CacheQueryCount')
        if m.get('CostTimeAvg') is not None:
            self.cost_time_avg = m.get('CostTimeAvg')
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('QueryCountAvg') is not None:
            self.query_count_avg = m.get('QueryCountAvg')
        if m.get('QueryOverFivePercentNum') is not None:
            self.query_over_five_percent_num = m.get('QueryOverFivePercentNum')
        if m.get('QueryOverFiveSecPercent') is not None:
            self.query_over_five_sec_percent = m.get('QueryOverFiveSecPercent')
        if m.get('QueryOverTenSecPercent') is not None:
            self.query_over_ten_sec_percent = m.get('QueryOverTenSecPercent')
        if m.get('QueryOverTenSecPercentNum') is not None:
            self.query_over_ten_sec_percent_num = m.get('QueryOverTenSecPercentNum')
        if m.get('QueryTimeoutCount') is not None:
            self.query_timeout_count = m.get('QueryTimeoutCount')
        if m.get('QueryTimeoutCountPercent') is not None:
            self.query_timeout_count_percent = m.get('QueryTimeoutCountPercent')
        if m.get('QuickIndexCostTimeAvg') is not None:
            self.quick_index_cost_time_avg = m.get('QuickIndexCostTimeAvg')
        if m.get('QuickIndexQueryCount') is not None:
            self.quick_index_query_count = m.get('QuickIndexQueryCount')
        if m.get('RepeatQueryPercent') is not None:
            self.repeat_query_percent = m.get('RepeatQueryPercent')
        if m.get('RepeatQueryPercentNum') is not None:
            self.repeat_query_percent_num = m.get('RepeatQueryPercentNum')
        if m.get('RepeatSqlQueryCount') is not None:
            self.repeat_sql_query_count = m.get('RepeatSqlQueryCount')
        if m.get('RepeatSqlQueryPercent') is not None:
            self.repeat_sql_query_percent = m.get('RepeatSqlQueryPercent')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryCubeOptimizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        advice_type: str = None,
        cube_performance_diagnose_model: QueryCubeOptimizationResponseBodyResultCubePerformanceDiagnoseModel = None,
    ):
        # The type of the suggestion. Valid values:
        # 
        # *   **OPEN_CACHE**: Open cache.
        # *   **OPEN_QUICK_ENGINE**: Open FAST Cache.
        # *   **INCREASE_CACHE_TIME**: Increase the cache time.
        self.advice_type = advice_type
        # The diagnostic information about the dataset.
        self.cube_performance_diagnose_model = cube_performance_diagnose_model

    def validate(self):
        if self.cube_performance_diagnose_model:
            self.cube_performance_diagnose_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice_type is not None:
            result['AdviceType'] = self.advice_type
        if self.cube_performance_diagnose_model is not None:
            result['CubePerformanceDiagnoseModel'] = self.cube_performance_diagnose_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdviceType') is not None:
            self.advice_type = m.get('AdviceType')
        if m.get('CubePerformanceDiagnoseModel') is not None:
            temp_model = QueryCubeOptimizationResponseBodyResultCubePerformanceDiagnoseModel()
            self.cube_performance_diagnose_model = temp_model.from_map(m['CubePerformanceDiagnoseModel'])
        return self


class QueryCubeOptimizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryCubeOptimizationResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The query results are returned.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryCubeOptimizationResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCubeOptimizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCubeOptimizationResponseBody = None,
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
            temp_model = QueryCubeOptimizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCubePerformanceRequest(TeaModel):
    def __init__(
        self,
        cost_time_avg_min: int = None,
        cube_id: str = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        workspace_id: str = None,
    ):
        # The average duration (minutes).
        self.cost_time_avg_min = cost_time_avg_min
        # The dataset ID.
        self.cube_id = cube_id
        # The current page number of the workspace member list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_size = page_size
        # The query type. Valid values:
        # 
        # *   **lastDay**: Yesterday
        # *   **sevenDays**: Within seven days
        # *   **thirtyDays**: Within 30 days
        # 
        # This parameter is required.
        self.query_type = query_type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time_avg_min is not None:
            result['CostTimeAvgMin'] = self.cost_time_avg_min
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTimeAvgMin') is not None:
            self.cost_time_avg_min = m.get('CostTimeAvgMin')
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryCubePerformanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        cache_cost_time_avg: float = None,
        cache_query_count: int = None,
        cost_time_avg: float = None,
        cube_id: str = None,
        cube_name: str = None,
        query_count: int = None,
        query_count_avg: float = None,
        query_over_five_percent_num: float = None,
        query_over_five_sec_percent: str = None,
        query_over_ten_sec_percent: str = None,
        query_over_ten_sec_percent_num: float = None,
        query_timeout_count: int = None,
        query_timeout_count_percent: float = None,
        quick_index_cost_time_avg: float = None,
        quick_index_query_count: int = None,
        repeat_query_percent: str = None,
        repeat_query_percent_num: float = None,
        repeat_sql_query_count: int = None,
        repeat_sql_query_percent: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The average duration of cache hits.
        self.cache_cost_time_avg = cache_cost_time_avg
        # The number of cache hits.
        self.cache_query_count = cache_query_count
        # The average query duration associated with the SQL pattern.
        self.cost_time_avg = cost_time_avg
        # The dataset ID.
        self.cube_id = cube_id
        # The name of the dataset.
        self.cube_name = cube_name
        # The number of queries.
        self.query_count = query_count
        # The average number of queries.
        self.query_count_avg = query_count_avg
        # The percentage of the number of queries that exceed the 5S.
        self.query_over_five_percent_num = query_over_five_percent_num
        # Query the proportion of more than 5S.
        self.query_over_five_sec_percent = query_over_five_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent = query_over_ten_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent_num = query_over_ten_sec_percent_num
        # The number of times that the chart query times out.
        self.query_timeout_count = query_timeout_count
        # The percentage of timeout times for chart queries.
        self.query_timeout_count_percent = query_timeout_count_percent
        # The average time consumed by the Quick engine query.
        self.quick_index_cost_time_avg = quick_index_cost_time_avg
        # The number of times that the Quick engine is hit.
        self.quick_index_query_count = quick_index_query_count
        # The proportion of duplicate queries.
        self.repeat_query_percent = repeat_query_percent
        # The number of duplicate queries.
        self.repeat_query_percent_num = repeat_query_percent_num
        # The number of times the query is repeated.
        self.repeat_sql_query_count = repeat_sql_query_count
        # The proportion of duplicate queries.
        self.repeat_sql_query_percent = repeat_sql_query_percent
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the group.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_cost_time_avg is not None:
            result['CacheCostTimeAvg'] = self.cache_cost_time_avg
        if self.cache_query_count is not None:
            result['CacheQueryCount'] = self.cache_query_count
        if self.cost_time_avg is not None:
            result['CostTimeAvg'] = self.cost_time_avg
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.cube_name is not None:
            result['CubeName'] = self.cube_name
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.query_count_avg is not None:
            result['QueryCountAvg'] = self.query_count_avg
        if self.query_over_five_percent_num is not None:
            result['QueryOverFivePercentNum'] = self.query_over_five_percent_num
        if self.query_over_five_sec_percent is not None:
            result['QueryOverFiveSecPercent'] = self.query_over_five_sec_percent
        if self.query_over_ten_sec_percent is not None:
            result['QueryOverTenSecPercent'] = self.query_over_ten_sec_percent
        if self.query_over_ten_sec_percent_num is not None:
            result['QueryOverTenSecPercentNum'] = self.query_over_ten_sec_percent_num
        if self.query_timeout_count is not None:
            result['QueryTimeoutCount'] = self.query_timeout_count
        if self.query_timeout_count_percent is not None:
            result['QueryTimeoutCountPercent'] = self.query_timeout_count_percent
        if self.quick_index_cost_time_avg is not None:
            result['QuickIndexCostTimeAvg'] = self.quick_index_cost_time_avg
        if self.quick_index_query_count is not None:
            result['QuickIndexQueryCount'] = self.quick_index_query_count
        if self.repeat_query_percent is not None:
            result['RepeatQueryPercent'] = self.repeat_query_percent
        if self.repeat_query_percent_num is not None:
            result['RepeatQueryPercentNum'] = self.repeat_query_percent_num
        if self.repeat_sql_query_count is not None:
            result['RepeatSqlQueryCount'] = self.repeat_sql_query_count
        if self.repeat_sql_query_percent is not None:
            result['RepeatSqlQueryPercent'] = self.repeat_sql_query_percent
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostTimeAvg') is not None:
            self.cache_cost_time_avg = m.get('CacheCostTimeAvg')
        if m.get('CacheQueryCount') is not None:
            self.cache_query_count = m.get('CacheQueryCount')
        if m.get('CostTimeAvg') is not None:
            self.cost_time_avg = m.get('CostTimeAvg')
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('QueryCountAvg') is not None:
            self.query_count_avg = m.get('QueryCountAvg')
        if m.get('QueryOverFivePercentNum') is not None:
            self.query_over_five_percent_num = m.get('QueryOverFivePercentNum')
        if m.get('QueryOverFiveSecPercent') is not None:
            self.query_over_five_sec_percent = m.get('QueryOverFiveSecPercent')
        if m.get('QueryOverTenSecPercent') is not None:
            self.query_over_ten_sec_percent = m.get('QueryOverTenSecPercent')
        if m.get('QueryOverTenSecPercentNum') is not None:
            self.query_over_ten_sec_percent_num = m.get('QueryOverTenSecPercentNum')
        if m.get('QueryTimeoutCount') is not None:
            self.query_timeout_count = m.get('QueryTimeoutCount')
        if m.get('QueryTimeoutCountPercent') is not None:
            self.query_timeout_count_percent = m.get('QueryTimeoutCountPercent')
        if m.get('QuickIndexCostTimeAvg') is not None:
            self.quick_index_cost_time_avg = m.get('QuickIndexCostTimeAvg')
        if m.get('QuickIndexQueryCount') is not None:
            self.quick_index_query_count = m.get('QuickIndexQueryCount')
        if m.get('RepeatQueryPercent') is not None:
            self.repeat_query_percent = m.get('RepeatQueryPercent')
        if m.get('RepeatQueryPercentNum') is not None:
            self.repeat_query_percent_num = m.get('RepeatQueryPercentNum')
        if m.get('RepeatSqlQueryCount') is not None:
            self.repeat_sql_query_count = m.get('RepeatSqlQueryCount')
        if m.get('RepeatSqlQueryPercent') is not None:
            self.repeat_sql_query_percent = m.get('RepeatSqlQueryPercent')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryCubePerformanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryCubePerformanceResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Array of report objects
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryCubePerformanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCubePerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCubePerformanceResponseBody = None,
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
            temp_model = QueryCubePerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        conditions: str = None,
        return_fields: str = None,
        user_id: str = None,
    ):
        # The API ID in the data service. For more information, see: [Data Service](https://help.aliyun.com/document_detail/144980.html).
        # 
        # This parameter is required.
        self.api_id = api_id
        # The query conditions for the data service, passed in as Key and Value pairs. A map-type string. Here, Key is the name of the request parameter, and Value is the value of the request parameter. Key and Value must appear in pairs.
        # 
        # **Note:**\
        # 
        # - When the operator of the request parameter is set to **enumeration filtering**, the value can contain multiple values, and the format of the value should be a JSON-formatted List. For example: `area=["East China","North China","South China"]`
        # 
        # - For dates, different formats are provided based on the type:
        # 
        #     - Year: 2019
        # 
        #     - Quarter: 2019Q1
        # 
        #     - Month: 201901 (with leading zero)
        #     
        #     - Week: 2019-52
        # 
        #     - Day: 20190101
        # 
        #     - Hour: 14:00:00 (minutes and seconds are 00)
        #     
        #     - Minute: 14:12:00 (seconds are 00)
        # 
        #     - Second: 14:34:34
        self.conditions = conditions
        # A list of return parameter names, in a List-type string.
        self.return_fields = return_fields
        # The userId in Quick BI. For how to obtain the userId, see: [Query User Information by Account Interface](https://next.api.aliyun.com/document/quickbi-public/2022-01-01/QueryUserInfoByAccount)
        # > This parameter is used to specify the identity of the person using the data service, which can be used in conjunction with the row and column permission configurations of the dataset.
        # 
        # 
        # 
        # >Notice: If the parameter is not passed, an empty string is passed, or null is passed, the default userId will be the owner of the current Quick BI organization.</notice>
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.return_fields is not None:
            result['ReturnFields'] = self.return_fields
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ReturnFields') is not None:
            self.return_fields = m.get('ReturnFields')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDataResponseBodyResultHeaders(TeaModel):
    def __init__(
        self,
        aggregator: str = None,
        column: str = None,
        data_type: str = None,
        granularity: str = None,
        label: str = None,
        type: str = None,
    ):
        # Aggregation operator. Only present for measure fields, such as SUM, AVG, and MAX.
        # - SUM: Sum
        # - MAX: Maximum value
        # - MIN: Minimum value
        # - AVG: Average
        # - COUNT: Count
        # - COUNTD: Distinct count
        # - STDDEV_POP: Population standard deviation
        # - STDDEV_SAMP: Sample standard deviation
        # - VAR_POP: Population variance
        # - VAR_SAMP: Sample variance
        self.aggregator = aggregator
        # Field name, corresponding to the physical table field name.
        self.column = column
        # The keyword of the sensitive field type.
        self.data_type = data_type
        # The granularity of the dimension field.
        # This field is returned only when the requested field is a date or geographic dimension, with the following possible values:
        # 
        # - Date Granularity: yearRegion (year), monthRegion (month), weekRegion (week), dayRegion (day), hourRegion (hour), minRegion (minute), secRegion (second)
        # 
        # - Geographic Granularity: COUNTRY (international level), PROVINCE (provincial level), CITY (city level), XIAN (district/county level), REGION (region)
        self.granularity = granularity
        # Field alias, which serves as the key in the map data rows of the `values` parameter.
        self.label = label
        # Field type, used to distinguish between dimension and measure fields.
        # - Dimension: dimension
        # - Measure: measure
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.column is not None:
            result['Column'] = self.column
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        headers: List[QueryDataResponseBodyResultHeaders] = None,
        sql: str = None,
        values: List[Dict[str, Any]] = None,
    ):
        # Column headers.
        self.headers = headers
        # The SQL query that was executed.
        # > The filter conditions in the returned SQL statement include not only the parameters passed through this interface but also the row and column permission configurations.
        self.sql = sql
        # The results of the query.
        self.values = values

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = QueryDataResponseBodyResultHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class QueryDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDataResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution. Possible values:
        # 
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDataResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataResponseBody = None,
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
            temp_model = QueryDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataRangeRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        type: str = None,
    ):
        # Name, for fuzzy search.
        self.keyword = keyword
        # Data range type:
        # 
        # - llmCube: LlmCube resource.
        # - llmCubeTheme: Analysis theme.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_user: str = None,
        llm_cube_id: str = None,
    ):
        # Alias of the LlmCube resource.
        self.alias = alias
        # Nickname of the creator.
        self.create_user = create_user
        # LlmCube resource ID.
        self.llm_cube_id = llm_cube_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.llm_cube_id is not None:
            result['LlmCubeId'] = self.llm_cube_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('LlmCubeId') is not None:
            self.llm_cube_id = m.get('LlmCubeId')
        return self


class QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels(TeaModel):
    def __init__(
        self,
        alias: str = None,
        create_user: str = None,
        llm_cube_id: str = None,
    ):
        # Alias of the LLM cube resource.
        self.alias = alias
        # Nickname of the creator.
        self.create_user = create_user
        # LlmCube resource ID.
        self.llm_cube_id = llm_cube_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.llm_cube_id is not None:
            result['LlmCubeId'] = self.llm_cube_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('LlmCubeId') is not None:
            self.llm_cube_id = m.get('LlmCubeId')
        return self


class QueryDataRangeResponseBodyResultApiCopilotThemeModels(TeaModel):
    def __init__(
        self,
        api_copilot_llm_cube_models: List[QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels] = None,
        create_user: str = None,
        theme_id: str = None,
        theme_name: str = None,
    ):
        # Array of LlmCube resources.
        self.api_copilot_llm_cube_models = api_copilot_llm_cube_models
        # Nickname of the creator.
        self.create_user = create_user
        # Analysis theme ID.
        self.theme_id = theme_id
        # Nickname of the analysis theme.
        self.theme_name = theme_name

    def validate(self):
        if self.api_copilot_llm_cube_models:
            for k in self.api_copilot_llm_cube_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiCopilotLlmCubeModels'] = []
        if self.api_copilot_llm_cube_models is not None:
            for k in self.api_copilot_llm_cube_models:
                result['ApiCopilotLlmCubeModels'].append(k.to_map() if k else None)
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.theme_id is not None:
            result['ThemeId'] = self.theme_id
        if self.theme_name is not None:
            result['ThemeName'] = self.theme_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_copilot_llm_cube_models = []
        if m.get('ApiCopilotLlmCubeModels') is not None:
            for k in m.get('ApiCopilotLlmCubeModels'):
                temp_model = QueryDataRangeResponseBodyResultApiCopilotThemeModelsApiCopilotLlmCubeModels()
                self.api_copilot_llm_cube_models.append(temp_model.from_map(k))
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('ThemeId') is not None:
            self.theme_id = m.get('ThemeId')
        if m.get('ThemeName') is not None:
            self.theme_name = m.get('ThemeName')
        return self


class QueryDataRangeResponseBodyResult(TeaModel):
    def __init__(
        self,
        api_copilot_llm_cube_models: List[QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels] = None,
        api_copilot_theme_models: List[QueryDataRangeResponseBodyResultApiCopilotThemeModels] = None,
    ):
        # Array of LlmCube resources.
        self.api_copilot_llm_cube_models = api_copilot_llm_cube_models
        # Array of analysis themes.
        self.api_copilot_theme_models = api_copilot_theme_models

    def validate(self):
        if self.api_copilot_llm_cube_models:
            for k in self.api_copilot_llm_cube_models:
                if k:
                    k.validate()
        if self.api_copilot_theme_models:
            for k in self.api_copilot_theme_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiCopilotLlmCubeModels'] = []
        if self.api_copilot_llm_cube_models is not None:
            for k in self.api_copilot_llm_cube_models:
                result['ApiCopilotLlmCubeModels'].append(k.to_map() if k else None)
        result['ApiCopilotThemeModels'] = []
        if self.api_copilot_theme_models is not None:
            for k in self.api_copilot_theme_models:
                result['ApiCopilotThemeModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_copilot_llm_cube_models = []
        if m.get('ApiCopilotLlmCubeModels') is not None:
            for k in m.get('ApiCopilotLlmCubeModels'):
                temp_model = QueryDataRangeResponseBodyResultApiCopilotLlmCubeModels()
                self.api_copilot_llm_cube_models.append(temp_model.from_map(k))
        self.api_copilot_theme_models = []
        if m.get('ApiCopilotThemeModels') is not None:
            for k in m.get('ApiCopilotThemeModels'):
                temp_model = QueryDataRangeResponseBodyResultApiCopilotThemeModels()
                self.api_copilot_theme_models.append(temp_model.from_map(k))
        return self


class QueryDataRangeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDataRangeResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Data range object.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDataRangeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDataRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataRangeResponseBody = None,
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
            temp_model = QueryDataRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataServiceRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        conditions: str = None,
        return_fields: str = None,
    ):
        # The API ID in the data service. For more information, see [Data Service](https://help.aliyun.com/document_detail/144980.html).
        # 
        # This parameter is required.
        self.api_id = api_id
        # The query conditions for the data service, passed in as Key-Value pairs. This is a map-type string. Here, Key is the name of the request parameter, and Value is the value of the request parameter. Keys and Values must appear in pairs.
        # 
        # **Note:**\
        # 
        # - When the operator of the request parameter is set to **enumeration filter**, the value can contain multiple values. In this case, the format of the value is a JSON list. For example: `area=["East China","North China","South China"]`     
        # 
        # - For dates, different formats are provided based on the type:
        # 
        #     - Year: 2019
        # 
        #     - Quarter: 2019Q1
        # 
        #     - Month: 201901 (with leading zero)
        #     
        #     - Week: 2019-52
        # 
        #     - Day: 20190101
        # 
        #     - Hour: 14:00:00 (minutes and seconds are 00)
        #     
        #     - Minute: 14:12:00 (seconds are 00)
        # 
        #     - Second: 14:34:34
        self.conditions = conditions
        # A list of parameter names to be returned, as a List-type string.
        self.return_fields = return_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.return_fields is not None:
            result['ReturnFields'] = self.return_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ReturnFields') is not None:
            self.return_fields = m.get('ReturnFields')
        return self


class QueryDataServiceResponseBodyResultHeaders(TeaModel):
    def __init__(
        self,
        aggregator: str = None,
        column: str = None,
        data_type: str = None,
        granularity: str = None,
        label: str = None,
        type: str = None,
    ):
        # Aggregation operator. Only present for measure fields, such as SUM, AVG, and MAX.
        self.aggregator = aggregator
        # Field name, corresponding to the physical table field name.
        self.column = column
        # The data type of the field. Common types include number, string, date, datetime, time, and geographic.
        self.data_type = data_type
        # The granularity of the dimension field.
        # This field is returned only when the requested field is a date or geographic dimension, with the following possible values:
        # 
        # - Date granularity: yearRegion (year), monthRegion (month), weekRegion (week), dayRegion (day), hourRegion (hour), minRegion (minute), secRegion (second)
        # 
        # - Geographic granularity: COUNTRY (country level), PROVINCE (province level), CITY (city level), XIAN (district/county level), REGION (region)
        self.granularity = granularity
        # 字段别名，结果参数values中map数据行的key。
        self.label = label
        # Field type, used to distinguish between dimension and measure fields.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.column is not None:
            result['Column'] = self.column
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.label is not None:
            result['Label'] = self.label
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataServiceResponseBodyResult(TeaModel):
    def __init__(
        self,
        headers: List[QueryDataServiceResponseBodyResultHeaders] = None,
        sql: str = None,
        values: List[Dict[str, Any]] = None,
    ):
        # Column headers.
        self.headers = headers
        # The SQL of the query request.
        self.sql = sql
        # The queried results returned.
        self.values = values

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = QueryDataServiceResponseBodyResultHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class QueryDataServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDataServiceResponseBodyResult = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Returns the result of the interface query.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful
        # 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDataServiceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDataServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataServiceResponseBody = None,
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
            temp_model = QueryDataServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataServiceListRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # Data service name.
        self.name = name
        # Page number. Default value: **1**.
        self.page_no = page_no
        # Number of items per page in a paginated query:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryDataServiceListResponseBodyResultDataContentFilter(TeaModel):
    def __init__(
        self,
        filters: List[Dict[str, Any]] = None,
        logical_operator: str = None,
        type: str = None,
    ):
        # Combined conditions.
        self.filters = filters
        # Logical relationship between multiple SQL text keywords.
        # 
        # - **or**: or
        # - **and**: and
        self.logical_operator = logical_operator
        # Type.
        # 
        # - basic: basic
        # - combined: complex
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataServiceListResponseBodyResultDataContentReturnFieldsField(TeaModel):
    def __init__(
        self,
        caption: str = None,
        column: str = None,
        data_type: str = None,
        fid: str = None,
        granularity: str = None,
        name: str = None,
        type: str = None,
    ):
        # Display name in the cube model (can be in Chinese or English).
        self.caption = caption
        # The corresponding physical field name.
        self.column = column
        # Data type.
        # 
        # - number: numeric
        # - string: string
        # - date: date
        # - datetime: datetime
        # - time: time
        # - geographic: geographic
        # - boolean: boolean
        # - url: URL
        self.data_type = data_type
        # Unique identifier for the original field.
        self.fid = fid
        # This attribute is included for date and geographic dimensions, indicating the supported granularity.
        self.granularity = granularity
        # Unique name of the cube field, mainly used for unique positioning in the returned result.
        self.name = name
        # Type.
        # 
        # - Dimension: Dimension
        # - Measure: Measure
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.column is not None:
            result['Column'] = self.column
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.fid is not None:
            result['Fid'] = self.fid
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Fid') is not None:
            self.fid = m.get('Fid')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryDataServiceListResponseBodyResultDataContentReturnFields(TeaModel):
    def __init__(
        self,
        aggregator: str = None,
        alias: str = None,
        desc: str = None,
        field: QueryDataServiceListResponseBodyResultDataContentReturnFieldsField = None,
        orderby: str = None,
    ):
        # Aggregation operator. For example, SUM, AVG, and MAX.
        self.aggregator = aggregator
        # Field parameter name.
        self.alias = alias
        # Remark for the returned field.
        self.desc = desc
        # Corresponding cube field information.
        self.field = field
        # Sorting.
        # 
        # - asc: Ascending
        # - desc: Descending
        # - no: No sorting
        self.orderby = orderby

    def validate(self):
        if self.field:
            self.field.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.field is not None:
            result['Field'] = self.field.to_map()
        if self.orderby is not None:
            result['Orderby'] = self.orderby
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Field') is not None:
            temp_model = QueryDataServiceListResponseBodyResultDataContentReturnFieldsField()
            self.field = temp_model.from_map(m['Field'])
        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')
        return self


class QueryDataServiceListResponseBodyResultDataContent(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        cube_name: str = None,
        detail: bool = None,
        filter: QueryDataServiceListResponseBodyResultDataContentFilter = None,
        return_fields: List[QueryDataServiceListResponseBodyResultDataContentReturnFields] = None,
    ):
        # Cube identifier ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Detail or Summary
        self.detail = detail
        # Request parameter information.
        self.filter = filter
        # Return information.
        self.return_fields = return_fields

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.return_fields:
            for k in self.return_fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.cube_name is not None:
            result['CubeName'] = self.cube_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        result['ReturnFields'] = []
        if self.return_fields is not None:
            for k in self.return_fields:
                result['ReturnFields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Filter') is not None:
            temp_model = QueryDataServiceListResponseBodyResultDataContentFilter()
            self.filter = temp_model.from_map(m['Filter'])
        self.return_fields = []
        if m.get('ReturnFields') is not None:
            for k in m.get('ReturnFields'):
                temp_model = QueryDataServiceListResponseBodyResultDataContentReturnFields()
                self.return_fields.append(temp_model.from_map(k))
        return self


class QueryDataServiceListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        content: QueryDataServiceListResponseBodyResultDataContent = None,
        creator_id: str = None,
        creator_name: str = None,
        cube_id: str = None,
        cube_name: str = None,
        desc: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier_id: str = None,
        modifier_name: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        sid: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The model of the data service in JSON format.
        self.content = content
        # Creator ID.
        self.creator_id = creator_id
        # Creator\\"s name.
        self.creator_name = creator_name
        # Cube identifier ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Description
        self.desc = desc
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Modifier\\"s userId.
        self.modifier_id = modifier_id
        # Modifier\\"s name
        self.modifier_name = modifier_name
        # Data service name.
        self.name = name
        # Owner ID
        self.owner_id = owner_id
        # Owner\\"s name
        self.owner_name = owner_name
        # Unique ID of the data service.
        self.sid = sid
        # Workspace ID.
        self.workspace_id = workspace_id
        # Workspace name.
        self.workspace_name = workspace_name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.cube_name is not None:
            result['CubeName'] = self.cube_name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = QueryDataServiceListResponseBodyResultDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryDataServiceListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryDataServiceListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Data service information.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of records per page.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDataServiceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryDataServiceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDataServiceListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request was successful 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDataServiceListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDataServiceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDataServiceListResponseBody = None,
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
            temp_model = QueryDataServiceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetDetailInfoRequest(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetDetailInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Returns the dataset data in JSON format: `{ "cube": { "dimensions": [ { "caption": "customer name", "dataType": "string", "dimensionType": "standard_dimension", "factColumn": "customer_name", "uid": "N5820f5_customer_name" }, { "caption": "datastring", "" standard_dimension", "factColumn": "order_id", "uid": "N5820f5_order_id" }, ], "measures": [ { "caption": "order amount ", "dataType": "number", "factColumn": "order_amt", "measureType": "standard_measure ": " Nderamid " }, " { "customsql": false, "dsId": "261b252d-c3c3-498a-a0a7-5d1ec6cd****", "tableName": "company_sales_record_copy" } }, "datasetId": "5820f58c-c734-4d8a-baf1-7979af4f****", "datasetName": "company_sales_record_copy12", "datasource": { "dsId": "261b252d-c3c3-498a-a0a7-5d1ec6cd****", "dsName": "Self-use", "dsType": "mysql" }, "directory" { "id": "schemaad8aad00-9c55-4984-a767-b4e0ec60****", "name": "My dataset", "pathId": "schemaad8aad00-9c55-4984-a767-b4e0ec60****", "pathName": "My dataset" }, "ownerId": "13651626232****", "ownerName": "Zhang San", "rowLevel": false, "workspaceId": "95296e95-ca89-4c7d-8af9-dedf0ad0****", "workspaceName": "Test Workspace" }`
        self.result = result
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetDetailInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetDetailInfoResponseBody = None,
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
            temp_model = QueryDatasetDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetInfoRequest(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
    ):
        # Queries information about a specified dataset.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class QueryDatasetInfoResponseBodyResultCubeTableList(TeaModel):
    def __init__(
        self,
        caption: str = None,
        customsql: bool = None,
        datasource_id: str = None,
        ds_type: str = None,
        fact_table: bool = None,
        sql: str = None,
        table_name: str = None,
        unique_id: str = None,
    ):
        # Indicates whether the data source table is valid. Valid values:
        # 
        # *   true: data source table
        # *   false: custom table
        self.caption = caption
        # The display name of the table.
        self.customsql = customsql
        # The name of the table.
        self.datasource_id = datasource_id
        # The ID of the data source.
        self.ds_type = ds_type
        # The unique ID of the table.
        self.fact_table = fact_table
        # Indicates whether the table is a custom SQL table. Valid values:
        # 
        # *   true: custom SQL table
        # *   false: non-custom SQL table
        self.sql = sql
        # The list of tables used by the dataset.
        self.table_name = table_name
        # The type of the data source. Valid values:
        # 
        # *   mysql
        # *   odps
        # *   oracle
        # *   ... and other data source types supported by Quick BI
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.customsql is not None:
            result['Customsql'] = self.customsql
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.fact_table is not None:
            result['FactTable'] = self.fact_table
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('Customsql') is not None:
            self.customsql = m.get('Customsql')
        if m.get('DatasourceId') is not None:
            self.datasource_id = m.get('DatasourceId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('FactTable') is not None:
            self.fact_table = m.get('FactTable')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class QueryDatasetInfoResponseBodyResultDimensionList(TeaModel):
    def __init__(
        self,
        caption: str = None,
        data_type: str = None,
        dimension_type: str = None,
        expression: str = None,
        expression_v2: str = None,
        fact_column: str = None,
        field_description: str = None,
        granularity: str = None,
        ref_uid: str = None,
        table_unique_id: str = None,
        uid: str = None,
    ):
        # The unique ID of the field that is referenced by the group measure. Non-NULL if and only if the metric is a grouping metric.
        self.caption = caption
        # A list of all dimensions in the dataset.
        self.data_type = data_type
        # The actual physical field.
        self.dimension_type = dimension_type
        # Data type; value:
        # 
        # *   string: character
        # *   number: a number
        # *   datetime: time
        self.expression = expression
        # Expression for the flattened calculation dimensions.
        self.expression_v2 = expression_v2
        # Expression for a calculated dimension; valid only for calculated dimensions.
        self.fact_column = fact_column
        # The description of the field.
        self.field_description = field_description
        # The type of the dimension. Valid values:
        # 
        # *   standard_dimension: General Dimension
        # *   calculate_dimension: calculating dimensions
        # *   group_dimension: grouping dimensions
        self.granularity = granularity
        # The granularity.
        self.ref_uid = ref_uid
        # The ARN.
        self.table_unique_id = table_unique_id
        # The display name of the dimension.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.expression_v2 is not None:
            result['ExpressionV2'] = self.expression_v2
        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.ref_uid is not None:
            result['RefUid'] = self.ref_uid
        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ExpressionV2') is not None:
            self.expression_v2 = m.get('ExpressionV2')
        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('RefUid') is not None:
            self.ref_uid = m.get('RefUid')
        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryDatasetInfoResponseBodyResultDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # Test directory
        self.id = id
        # Test directory
        self.name = name
        # The information about the directory to which the dataset belongs.
        self.path_id = path_id
        # The path of the directory ID, for example, aa/bb/cc/dd.
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryDatasetInfoResponseBodyResultMeasureList(TeaModel):
    def __init__(
        self,
        caption: str = None,
        data_type: str = None,
        expression: str = None,
        expression_v2: str = None,
        fact_column: str = None,
        field_description: str = None,
        measure_type: str = None,
        table_unique_id: str = None,
        uid: str = None,
    ):
        # The actual physical field.
        self.caption = caption
        # A list of all measures for the dataset.
        self.data_type = data_type
        # Data type; value:
        # 
        # *   string: character
        # *   number: a number
        # *   datetime: time
        self.expression = expression
        # Expression for flattened computation metrics.
        self.expression_v2 = expression_v2
        # The type of the measure. Valid values:
        # 
        # *   standard_measure: General Metrics
        # *   calculate_measure: Calculating Measures
        self.fact_column = fact_column
        # The description of the field.
        self.field_description = field_description
        # An expression that calculates a measure; valid only for calculated measures.
        self.measure_type = measure_type
        # The display name of the metric.
        self.table_unique_id = table_unique_id
        # The unique ID of the table to which the table belongs, which corresponds to the UniqueId of the CubeTypeList.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.expression_v2 is not None:
            result['ExpressionV2'] = self.expression_v2
        if self.fact_column is not None:
            result['FactColumn'] = self.fact_column
        if self.field_description is not None:
            result['FieldDescription'] = self.field_description
        if self.measure_type is not None:
            result['MeasureType'] = self.measure_type
        if self.table_unique_id is not None:
            result['TableUniqueId'] = self.table_unique_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ExpressionV2') is not None:
            self.expression_v2 = m.get('ExpressionV2')
        if m.get('FactColumn') is not None:
            self.fact_column = m.get('FactColumn')
        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')
        if m.get('MeasureType') is not None:
            self.measure_type = m.get('MeasureType')
        if m.get('TableUniqueId') is not None:
            self.table_unique_id = m.get('TableUniqueId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryDatasetInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        cube_table_list: List[QueryDatasetInfoResponseBodyResultCubeTableList] = None,
        custimze_sql: bool = None,
        dataset_id: str = None,
        dataset_name: str = None,
        dimension_list: List[QueryDatasetInfoResponseBodyResultDimensionList] = None,
        directory: QueryDatasetInfoResponseBodyResultDirectory = None,
        ds_id: str = None,
        ds_name: str = None,
        ds_type: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        measure_list: List[QueryDatasetInfoResponseBodyResultMeasureList] = None,
        open_offline_acceleration: bool = None,
        owner_id: str = None,
        owner_name: str = None,
        row_level: bool = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The unique ID of the dataset.
        self.cube_table_list = cube_table_list
        # The unique ID of the workspace to which the dataset belongs.
        self.custimze_sql = custimze_sql
        # The type of the data source. Valid values:
        # 
        # *   mysql
        # *   odps
        # *   oracle
        # *   ... Data source types supported by Quick BI such as
        self.dataset_id = dataset_id
        # The user ID of the dataset owner in the Quick BI.
        self.dataset_name = dataset_name
        # A list of all dimensions in the dataset.
        self.dimension_list = dimension_list
        # The unique ID of the metric.
        self.directory = directory
        # The name of the data source.
        self.ds_id = ds_id
        # The time when the dataset was last modified.
        self.ds_name = ds_name
        # The point in time when the training dataset was created.
        self.ds_type = ds_type
        # Indicates whether to customize SQL statements. Valid values:
        # 
        # *   true
        # *   false
        self.gmt_create = gmt_create
        # The information about the dataset.
        self.gmt_modify = gmt_modify
        # A list of all measures for the dataset.
        self.measure_list = measure_list
        # Whether to enable extraction acceleration. Valid values:
        # 
        # *   true
        # *   false
        self.open_offline_acceleration = open_offline_acceleration
        # Test Space
        self.owner_id = owner_id
        # The unique ID of the data source.
        self.owner_name = owner_name
        # The name of the training dataset.
        self.row_level = row_level
        # Whether row-level permissions are enabled. Valid values:
        # 
        # *   true: The VIP Netty channel is enabled.
        # *   false: The VIP Netty channel is disabled.
        self.workspace_id = workspace_id
        # Big Baby
        self.workspace_name = workspace_name

    def validate(self):
        if self.cube_table_list:
            for k in self.cube_table_list:
                if k:
                    k.validate()
        if self.dimension_list:
            for k in self.dimension_list:
                if k:
                    k.validate()
        if self.directory:
            self.directory.validate()
        if self.measure_list:
            for k in self.measure_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CubeTableList'] = []
        if self.cube_table_list is not None:
            for k in self.cube_table_list:
                result['CubeTableList'].append(k.to_map() if k else None)
        if self.custimze_sql is not None:
            result['CustimzeSql'] = self.custimze_sql
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        result['DimensionList'] = []
        if self.dimension_list is not None:
            for k in self.dimension_list:
                result['DimensionList'].append(k.to_map() if k else None)
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_name is not None:
            result['DsName'] = self.ds_name
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        result['MeasureList'] = []
        if self.measure_list is not None:
            for k in self.measure_list:
                result['MeasureList'].append(k.to_map() if k else None)
        if self.open_offline_acceleration is not None:
            result['OpenOfflineAcceleration'] = self.open_offline_acceleration
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.row_level is not None:
            result['RowLevel'] = self.row_level
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cube_table_list = []
        if m.get('CubeTableList') is not None:
            for k in m.get('CubeTableList'):
                temp_model = QueryDatasetInfoResponseBodyResultCubeTableList()
                self.cube_table_list.append(temp_model.from_map(k))
        if m.get('CustimzeSql') is not None:
            self.custimze_sql = m.get('CustimzeSql')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        self.dimension_list = []
        if m.get('DimensionList') is not None:
            for k in m.get('DimensionList'):
                temp_model = QueryDatasetInfoResponseBodyResultDimensionList()
                self.dimension_list.append(temp_model.from_map(k))
        if m.get('Directory') is not None:
            temp_model = QueryDatasetInfoResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        self.measure_list = []
        if m.get('MeasureList') is not None:
            for k in m.get('MeasureList'):
                temp_model = QueryDatasetInfoResponseBodyResultMeasureList()
                self.measure_list.append(temp_model.from_map(k))
        if m.get('OpenOfflineAcceleration') is not None:
            self.open_offline_acceleration = m.get('OpenOfflineAcceleration')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryDatasetInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDatasetInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Whether the operation is successfully returned. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.request_id = request_id
        # The dataset information.
        self.result = result
        # The unique ID of the dataset.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetInfoResponseBody = None,
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
            temp_model = QueryDatasetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetListRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        with_children: bool = None,
        workspace_id: str = None,
    ):
        # The ID of the request.
        self.directory_id = directory_id
        # Information about the directory where the dataset is located
        self.keyword = keyword
        # The ID of the workspace.
        self.page_num = page_num
        # Specifies the directory ID.
        # 
        # *   If this field is not empty, all datasets in the directory are obtained.
        self.page_size = page_size
        # The total number of pages returned.
        self.with_children = with_children
        # The name of the data source.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.with_children is not None:
            result['WithChildren'] = self.with_children
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WithChildren') is not None:
            self.with_children = m.get('WithChildren')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryDatasetListResponseBodyResultDataDataSource(TeaModel):
    def __init__(
        self,
        ds_id: str = None,
        ds_name: str = None,
        ds_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        self.ds_id = ds_id
        # The time when the scaling group was modified.
        self.ds_name = ds_name
        # The user ID of the dataset owner in the Quick BI.
        self.ds_type = ds_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ds_id is not None:
            result['DsId'] = self.ds_id
        if self.ds_name is not None:
            result['DsName'] = self.ds_name
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')
        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        return self


class QueryDatasetListResponseBodyResultDataDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory path.
        self.id = id
        # The ID of the data source.
        self.name = name
        # The type of the data source.
        self.path_id = path_id
        # The name of the data source.
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryDatasetListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_source: QueryDatasetListResponseBodyResultDataDataSource = None,
        dataset_id: str = None,
        dataset_name: str = None,
        description: str = None,
        directory: QueryDatasetListResponseBodyResultDataDirectory = None,
        modify_time: str = None,
        open_offline_acceleration: bool = None,
        owner_id: str = None,
        owner_name: str = None,
        row_level: bool = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The details of the dataset list.
        self.create_time = create_time
        # Test Space
        self.data_source = data_source
        # The name of the workspace.
        self.dataset_id = dataset_id
        # Tom
        self.dataset_name = dataset_name
        # The number of rows per page set when the interface is requested.
        self.description = description
        # The information about the data source to which the dataset belongs.
        self.directory = directory
        # The nickname of the dataset owner.
        self.modify_time = modify_time
        self.open_offline_acceleration = open_offline_acceleration
        # The creation time.
        self.owner_id = owner_id
        # Whether to enable row-level permissions. Valid values:
        # 
        # *   true: The VIP Netty channel is enabled.
        # *   false: The incremental log backup feature is disabled.
        self.owner_name = owner_name
        # The total number of pages returned.
        self.row_level = row_level
        # The page number of the returned page.
        self.workspace_id = workspace_id
        # The description of the dataset.
        self.workspace_name = workspace_name

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.open_offline_acceleration is not None:
            result['OpenOfflineAcceleration'] = self.open_offline_acceleration
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.row_level is not None:
            result['RowLevel'] = self.row_level
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryDatasetListResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OpenOfflineAcceleration') is not None:
            self.open_offline_acceleration = m.get('OpenOfflineAcceleration')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryDatasetListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryDatasetListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Returns the pagination results of the dataset list. The detailed information of the dataset list is stored in the response parameter Data.
        self.data = data
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_num = page_num
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.page_size = page_size
        # The ID of the request.
        self.total_num = total_num
        # Current page number for dataset list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDatasetListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryDatasetListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDatasetListResponseBodyResult = None,
        success: bool = None,
    ):
        # The keyword used to search for the dataset name.
        self.request_id = request_id
        # Test dataset
        self.result = result
        # Whether to recursively wrap the dataset in the subdirectory. Valid values:
        # 
        # *   true: returns datasets in all recursive subdirectories in the directoryId directory.
        # *   false: Only datasets in the directory specified by directoryId are returned, excluding subdirectories.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetListResponseBody = None,
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
            temp_model = QueryDatasetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetSmartqStatusRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
    ):
        # Dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        return self


class QueryDatasetSmartqStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Result of the API execution. Possible values:
        # - true: Request succeeded
        # - false: Request failed
        self.result = result
        # 是否请求成功。取值范围：
        # 
        # - true：请求成功
        # - false：请求失败
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetSmartqStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetSmartqStatusResponseBody = None,
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
            temp_model = QueryDatasetSmartqStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetSwitchInfoRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
    ):
        # This parameter is required.
        self.cube_id = cube_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        return self


class QueryDatasetSwitchInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        is_open_column_level_permission: int = None,
        is_open_row_level_permission: int = None,
    ):
        self.cube_id = cube_id
        self.is_open_column_level_permission = is_open_column_level_permission
        self.is_open_row_level_permission = is_open_row_level_permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.is_open_column_level_permission is not None:
            result['IsOpenColumnLevelPermission'] = self.is_open_column_level_permission
        if self.is_open_row_level_permission is not None:
            result['IsOpenRowLevelPermission'] = self.is_open_row_level_permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('IsOpenColumnLevelPermission') is not None:
            self.is_open_column_level_permission = m.get('IsOpenColumnLevelPermission')
        if m.get('IsOpenRowLevelPermission') is not None:
            self.is_open_row_level_permission = m.get('IsOpenRowLevelPermission')
        return self


class QueryDatasetSwitchInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryDatasetSwitchInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryDatasetSwitchInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDatasetSwitchInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDatasetSwitchInfoResponseBody = None,
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
            temp_model = QueryDatasetSwitchInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEmbeddedInfoResponseBodyResultDetail(TeaModel):
    def __init__(
        self,
        dashboard_offline_query: int = None,
        page: int = None,
        report: int = None,
    ):
        # The number of embedded self-service fetching.
        self.dashboard_offline_query = dashboard_offline_query
        # The number of embedded dashboards.
        self.page = page
        # The number of embedded spreadsheets.
        self.report = report

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dashboard_offline_query is not None:
            result['DashboardOfflineQuery'] = self.dashboard_offline_query
        if self.page is not None:
            result['Page'] = self.page
        if self.report is not None:
            result['Report'] = self.report
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardOfflineQuery') is not None:
            self.dashboard_offline_query = m.get('DashboardOfflineQuery')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Report') is not None:
            self.report = m.get('Report')
        return self


class QueryEmbeddedInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail: QueryEmbeddedInfoResponseBodyResultDetail = None,
        embedded_count: int = None,
        max_count: int = None,
    ):
        # Embed the statistics of the work.
        self.detail = detail
        # The number of reports that are currently embedded.
        self.embedded_count = embedded_count
        # The maximum number of reports that can be embedded.
        self.max_count = max_count

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.embedded_count is not None:
            result['EmbeddedCount'] = self.embedded_count
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = QueryEmbeddedInfoResponseBodyResultDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('EmbeddedCount') is not None:
            self.embedded_count = m.get('EmbeddedCount')
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        return self


class QueryEmbeddedInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryEmbeddedInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The embedded information of the reports under the organization.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryEmbeddedInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEmbeddedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEmbeddedInfoResponseBody = None,
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
            temp_model = QueryEmbeddedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEmbeddedStatusRequest(TeaModel):
    def __init__(
        self,
        works_id: str = None,
    ):
        # The work ID of the query.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryEmbeddedStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Whether the work is enabled for embedding. Valid values:
        # 
        # *   true: embedded
        # *   false: not embedded
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEmbeddedStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryEmbeddedStatusResponseBody = None,
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
            temp_model = QueryEmbeddedStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLlmCubeWithThemeListByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # User ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryLlmCubeWithThemeListByUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        cube_ids: Dict[str, str] = None,
        theme_ids: Dict[str, str] = None,
    ):
        # Dataset map.
        # 
        # - key - Dataset ID
        # - value - Dataset name
        self.cube_ids = cube_ids
        # Analysis theme map.
        # - key - Analysis theme ID 
        # - value - Analysis theme name
        self.theme_ids = theme_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_ids is not None:
            result['CubeIds'] = self.cube_ids
        if self.theme_ids is not None:
            result['ThemeIds'] = self.theme_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeIds') is not None:
            self.cube_ids = m.get('CubeIds')
        if m.get('ThemeIds') is not None:
            self.theme_ids = m.get('ThemeIds')
        return self


class QueryLlmCubeWithThemeListByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryLlmCubeWithThemeListByUserIdResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of datasets and analysis themes.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryLlmCubeWithThemeListByUserIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLlmCubeWithThemeListByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLlmCubeWithThemeListByUserIdResponseBody = None,
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
            temp_model = QueryLlmCubeWithThemeListByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrganizationRoleConfigRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
    ):
        # Organization role ID, including predefined roles and custom roles:
        # 
        # - Organization Administrator (predefined role): 111111111
        # - Permission Administrator (predefined role): 111111112
        # - Regular User (predefined role): 111111113
        # - Custom Role: The corresponding role ID of the custom role
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class QueryOrganizationRoleConfigResponseBodyResultAuthConfigList(TeaModel):
    def __init__(
        self,
        auth_key: str = None,
    ):
        # Permission type:
        # - quick_monitor: Metric Monitoring
        # - subscription: Subscription Management
        # - offline_download: Self-service Data Retrieval
        # - resource_package: Resource Package Management
        # - organization_ask: Organization Access Key/Secret (AK/SK)
        # - developer_openapi: OpenAPI
        # - data_service: Data Service
        # - admin_authorize3rd: Embedded Analysis
        # - component_manage: Custom Component
        # - template_open: Custom Template
        # - custom_driver: Custom Driver (supported only in standalone deployment)
        # - open_platform_custom_plugin: Custom Plugin (supported only in standalone deployment)
        # - enterprise_safety: Enterprise Security
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class QueryOrganizationRoleConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_config_list: List[QueryOrganizationRoleConfigResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role permission configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Possible values:
        # 
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Organization role ID, including predefined roles and custom roles:
        # 
        # - Organization Administrator (predefined role): 111111111
        # - Permission Administrator (predefined role): 111111112
        # - Regular User (predefined role): 111111113
        # - Custom Role: The corresponding role ID of the custom role
        self.role_id = role_id
        # Role name.
        self.role_name = role_name

    def validate(self):
        if self.auth_config_list:
            for k in self.auth_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthConfigList'] = []
        if self.auth_config_list is not None:
            for k in self.auth_config_list:
                result['AuthConfigList'].append(k.to_map() if k else None)
        if self.is_system_role is not None:
            result['IsSystemRole'] = self.is_system_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_config_list = []
        if m.get('AuthConfigList') is not None:
            for k in m.get('AuthConfigList'):
                temp_model = QueryOrganizationRoleConfigResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k))
        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryOrganizationRoleConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryOrganizationRoleConfigResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Details of the organization role configuration.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful 
        # - false: The request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryOrganizationRoleConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrganizationRoleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrganizationRoleConfigResponseBody = None,
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
            temp_model = QueryOrganizationRoleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrganizationWorkspaceListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # Keyword for the workspace name.
        self.keyword = keyword
        # Current page number of the workspace list:
        # 
        # - Starting value: 1
        # - Default value: 1
        self.page_num = page_num
        # Number of rows per page in a paginated query:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # User ID in Quick BI.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryOrganizationWorkspaceListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        allow_publish_operation: bool = None,
        allow_share_operation: bool = None,
        create_time: str = None,
        create_user: str = None,
        create_user_account_name: str = None,
        modified_time: str = None,
        modify_user: str = None,
        modify_user_account_name: str = None,
        organization_id: str = None,
        owner: str = None,
        owner_account_name: str = None,
        workspace_description: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Whether the work can be made public. Value range:
        # 
        # - true: Public
        # - false: Not public
        self.allow_publish_operation = allow_publish_operation
        # Indicates whether the work can be authorized for sharing. Possible values:
        # 
        # - true: Authorized
        # - false: Not authorized
        self.allow_share_operation = allow_share_operation
        # Creation time of the workspace.
        self.create_time = create_time
        # Quick BI user ID of the creator.
        self.create_user = create_user
        # Aliyun account name of the creator.
        self.create_user_account_name = create_user_account_name
        # Last modified time of the workspace.
        self.modified_time = modified_time
        # ID of the Quick BI user who modified the workspace.
        self.modify_user = modify_user
        # Aliyun account name of the modifier.
        self.modify_user_account_name = modify_user_account_name
        # ID of the organization to which the workspace belongs.
        self.organization_id = organization_id
        # Quick BI user ID of the workspace owner.
        self.owner = owner
        # Aliyun account name of the workspace owner.
        self.owner_account_name = owner_account_name
        # Workspace description.
        self.workspace_description = workspace_description
        # Workspace ID.
        self.workspace_id = workspace_id
        # Name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_publish_operation is not None:
            result['AllowPublishOperation'] = self.allow_publish_operation
        if self.allow_share_operation is not None:
            result['AllowShareOperation'] = self.allow_share_operation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.create_user_account_name is not None:
            result['CreateUserAccountName'] = self.create_user_account_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.modify_user_account_name is not None:
            result['ModifyUserAccountName'] = self.modify_user_account_name
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_account_name is not None:
            result['OwnerAccountName'] = self.owner_account_name
        if self.workspace_description is not None:
            result['WorkspaceDescription'] = self.workspace_description
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowPublishOperation') is not None:
            self.allow_publish_operation = m.get('AllowPublishOperation')
        if m.get('AllowShareOperation') is not None:
            self.allow_share_operation = m.get('AllowShareOperation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('CreateUserAccountName') is not None:
            self.create_user_account_name = m.get('CreateUserAccountName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ModifyUserAccountName') is not None:
            self.modify_user_account_name = m.get('ModifyUserAccountName')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerAccountName') is not None:
            self.owner_account_name = m.get('OwnerAccountName')
        if m.get('WorkspaceDescription') is not None:
            self.workspace_description = m.get('WorkspaceDescription')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryOrganizationWorkspaceListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryOrganizationWorkspaceListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # List of workspaces.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page as set in the request.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryOrganizationWorkspaceListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryOrganizationWorkspaceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryOrganizationWorkspaceListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the paginated result of the workspace list, with detailed information about the workspaces stored in the Data parameter.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryOrganizationWorkspaceListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrganizationWorkspaceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrganizationWorkspaceListResponseBody = None,
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
            temp_model = QueryOrganizationWorkspaceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReadableResourcesListByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # Quick BI the user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryReadableResourcesListByUserIdResponseBodyResultDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory.
        self.id = id
        # The name of the directory.
        self.name = name
        # The hierarchical structure of the directory ID, which is separated with \\"/\\".
        self.path_id = path_id
        # The hierarchical structure of the directory name, which is separated with \\"/\\".
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryReadableResourcesListByUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        directory: QueryReadableResourcesListByUserIdResponseBodyResultDirectory = None,
        modify_name: str = None,
        modify_time: str = None,
        owner_id: str = None,
        owner_name: str = None,
        security_level: str = None,
        status: int = None,
        third_part_auth_flag: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The timestamp of the creation time in milliseconds.
        self.create_time = create_time
        # Remarks on the work.
        self.description = description
        # The directory structure in which the work is located.
        self.directory = directory
        # The name of the Alibaba Cloud account to which the modifier belongs.
        self.modify_name = modify_name
        # The timestamp of the modification time in milliseconds.
        self.modify_time = modify_time
        # The Quick BI UserID of the work owner.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the owner.
        self.owner_name = owner_name
        # Security policies for collaborative authorization of works. Valid values:
        # 
        # *   0: private
        # *   12: Authorize specified members
        # *   1 or 11: Authorize all workspace members
        # 
        # > 
        # 
        # *   If you use legacy permissions, the return value is 1.
        # 
        # *   If you use the new permissions, the return value is 11.
        self.security_level = security_level
        # The status of the report. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.third_part_auth_flag = third_part_auth_flag
        # The name of the work.
        self.work_name = work_name
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        self.work_type = work_type
        # The ID of the work.
        self.works_id = works_id
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryReadableResourcesListByUserIdResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryReadableResourcesListByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryReadableResourcesListByUserIdResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of works that the user has permission to view.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryReadableResourcesListByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryReadableResourcesListByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReadableResourcesListByUserIdResponseBody = None,
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
            temp_model = QueryReadableResourcesListByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReadableResourcesListByUserIdV2Request(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        work_type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.user_id = user_id
        self.work_type = work_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryReadableResourcesListByUserIdV2ResponseBodyResultDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        self.id = id
        self.name = name
        self.path_id = path_id
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryReadableResourcesListByUserIdV2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        directory: QueryReadableResourcesListByUserIdV2ResponseBodyResultDirectory = None,
        modify_name: str = None,
        modify_time: str = None,
        owner_id: str = None,
        owner_name: str = None,
        security_level: str = None,
        status: int = None,
        third_part_auth_flag: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.directory = directory
        self.modify_name = modify_name
        self.modify_time = modify_time
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.security_level = security_level
        self.status = status
        self.third_part_auth_flag = third_part_auth_flag
        self.work_name = work_name
        self.work_type = work_type
        self.works_id = works_id
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryReadableResourcesListByUserIdV2ResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryReadableResourcesListByUserIdV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryReadableResourcesListByUserIdV2ResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryReadableResourcesListByUserIdV2ResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryReadableResourcesListByUserIdV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReadableResourcesListByUserIdV2ResponseBody = None,
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
            temp_model = QueryReadableResourcesListByUserIdV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReportPerformanceRequest(TeaModel):
    def __init__(
        self,
        cost_time_avg_min: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        report_id: str = None,
        resource_type: str = None,
        workspace_id: str = None,
    ):
        # The average duration (minutes).
        self.cost_time_avg_min = cost_time_avg_min
        # Current page number for organization member list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_size = page_size
        # The query type. Valid values:
        # 
        # *   **lastDay**: Yesterday
        # *   **sevenDays**: Within seven days
        # *   **thirtyDays**: Within 30 days
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the security report.
        self.report_id = report_id
        # The resource types.
        self.resource_type = resource_type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time_avg_min is not None:
            result['CostTimeAvgMin'] = self.cost_time_avg_min
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTimeAvgMin') is not None:
            self.cost_time_avg_min = m.get('CostTimeAvgMin')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryReportPerformanceResponseBodyResult(TeaModel):
    def __init__(
        self,
        cache_cost_time_avg: float = None,
        cache_query_count: int = None,
        component_query_count: int = None,
        component_query_count_avg: float = None,
        cost_time_avg: float = None,
        query_count: int = None,
        query_count_avg: float = None,
        query_over_five_percent_num: float = None,
        query_over_five_sec_percent: str = None,
        query_over_ten_sec_percent: str = None,
        query_over_ten_sec_percent_num: float = None,
        query_timeout_count: int = None,
        query_timeout_count_percent: float = None,
        quick_index_cost_time_avg: float = None,
        quick_index_query_count: int = None,
        repeat_query_percent: str = None,
        repeat_query_percent_num: float = None,
        repeat_sql_query_count: int = None,
        repeat_sql_query_percent: str = None,
        report_id: str = None,
        report_name: str = None,
        report_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The average duration of cache hits.
        self.cache_cost_time_avg = cache_cost_time_avg
        # The number of cache hits.
        self.cache_query_count = cache_query_count
        # The number of times the chart is queried.
        self.component_query_count = component_query_count
        # The average number of times the chart is queried.
        self.component_query_count_avg = component_query_count_avg
        # The average query duration associated with the SQL pattern.
        self.cost_time_avg = cost_time_avg
        # The number of queries.
        self.query_count = query_count
        # The average number of queries.
        self.query_count_avg = query_count_avg
        # The percentage of the number of queries that exceed the 5S.
        self.query_over_five_percent_num = query_over_five_percent_num
        # Query the proportion of more than 5S.
        self.query_over_five_sec_percent = query_over_five_sec_percent
        # The percentage of queries that exceed 10s.
        self.query_over_ten_sec_percent = query_over_ten_sec_percent
        # The number of queries that exceed 10 seconds.
        self.query_over_ten_sec_percent_num = query_over_ten_sec_percent_num
        # The number of times that the chart query times out.
        self.query_timeout_count = query_timeout_count
        # The percentage of timeout times for chart queries.
        self.query_timeout_count_percent = query_timeout_count_percent
        # The average time consumed by the Quick engine query.
        self.quick_index_cost_time_avg = quick_index_cost_time_avg
        # The number of times that the Quick engine is hit.
        self.quick_index_query_count = quick_index_query_count
        # The proportion of duplicate queries.
        self.repeat_query_percent = repeat_query_percent
        # The number of duplicate queries.
        self.repeat_query_percent_num = repeat_query_percent_num
        # The number of times the query is repeated.
        self.repeat_sql_query_count = repeat_sql_query_count
        # The proportion of duplicate queries.
        self.repeat_sql_query_percent = repeat_sql_query_percent
        # The ID of the work.
        self.report_id = report_id
        # The name of the report.
        self.report_name = report_name
        # The format of the report.
        self.report_type = report_type
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the group.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_cost_time_avg is not None:
            result['CacheCostTimeAvg'] = self.cache_cost_time_avg
        if self.cache_query_count is not None:
            result['CacheQueryCount'] = self.cache_query_count
        if self.component_query_count is not None:
            result['ComponentQueryCount'] = self.component_query_count
        if self.component_query_count_avg is not None:
            result['ComponentQueryCountAvg'] = self.component_query_count_avg
        if self.cost_time_avg is not None:
            result['CostTimeAvg'] = self.cost_time_avg
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.query_count_avg is not None:
            result['QueryCountAvg'] = self.query_count_avg
        if self.query_over_five_percent_num is not None:
            result['QueryOverFivePercentNum'] = self.query_over_five_percent_num
        if self.query_over_five_sec_percent is not None:
            result['QueryOverFiveSecPercent'] = self.query_over_five_sec_percent
        if self.query_over_ten_sec_percent is not None:
            result['QueryOverTenSecPercent'] = self.query_over_ten_sec_percent
        if self.query_over_ten_sec_percent_num is not None:
            result['QueryOverTenSecPercentNum'] = self.query_over_ten_sec_percent_num
        if self.query_timeout_count is not None:
            result['QueryTimeoutCount'] = self.query_timeout_count
        if self.query_timeout_count_percent is not None:
            result['QueryTimeoutCountPercent'] = self.query_timeout_count_percent
        if self.quick_index_cost_time_avg is not None:
            result['QuickIndexCostTimeAvg'] = self.quick_index_cost_time_avg
        if self.quick_index_query_count is not None:
            result['QuickIndexQueryCount'] = self.quick_index_query_count
        if self.repeat_query_percent is not None:
            result['RepeatQueryPercent'] = self.repeat_query_percent
        if self.repeat_query_percent_num is not None:
            result['RepeatQueryPercentNum'] = self.repeat_query_percent_num
        if self.repeat_sql_query_count is not None:
            result['RepeatSqlQueryCount'] = self.repeat_sql_query_count
        if self.repeat_sql_query_percent is not None:
            result['RepeatSqlQueryPercent'] = self.repeat_sql_query_percent
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_name is not None:
            result['ReportName'] = self.report_name
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheCostTimeAvg') is not None:
            self.cache_cost_time_avg = m.get('CacheCostTimeAvg')
        if m.get('CacheQueryCount') is not None:
            self.cache_query_count = m.get('CacheQueryCount')
        if m.get('ComponentQueryCount') is not None:
            self.component_query_count = m.get('ComponentQueryCount')
        if m.get('ComponentQueryCountAvg') is not None:
            self.component_query_count_avg = m.get('ComponentQueryCountAvg')
        if m.get('CostTimeAvg') is not None:
            self.cost_time_avg = m.get('CostTimeAvg')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('QueryCountAvg') is not None:
            self.query_count_avg = m.get('QueryCountAvg')
        if m.get('QueryOverFivePercentNum') is not None:
            self.query_over_five_percent_num = m.get('QueryOverFivePercentNum')
        if m.get('QueryOverFiveSecPercent') is not None:
            self.query_over_five_sec_percent = m.get('QueryOverFiveSecPercent')
        if m.get('QueryOverTenSecPercent') is not None:
            self.query_over_ten_sec_percent = m.get('QueryOverTenSecPercent')
        if m.get('QueryOverTenSecPercentNum') is not None:
            self.query_over_ten_sec_percent_num = m.get('QueryOverTenSecPercentNum')
        if m.get('QueryTimeoutCount') is not None:
            self.query_timeout_count = m.get('QueryTimeoutCount')
        if m.get('QueryTimeoutCountPercent') is not None:
            self.query_timeout_count_percent = m.get('QueryTimeoutCountPercent')
        if m.get('QuickIndexCostTimeAvg') is not None:
            self.quick_index_cost_time_avg = m.get('QuickIndexCostTimeAvg')
        if m.get('QuickIndexQueryCount') is not None:
            self.quick_index_query_count = m.get('QuickIndexQueryCount')
        if m.get('RepeatQueryPercent') is not None:
            self.repeat_query_percent = m.get('RepeatQueryPercent')
        if m.get('RepeatQueryPercentNum') is not None:
            self.repeat_query_percent_num = m.get('RepeatQueryPercentNum')
        if m.get('RepeatSqlQueryCount') is not None:
            self.repeat_sql_query_count = m.get('RepeatSqlQueryCount')
        if m.get('RepeatSqlQueryPercent') is not None:
            self.repeat_sql_query_percent = m.get('RepeatSqlQueryPercent')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportName') is not None:
            self.report_name = m.get('ReportName')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryReportPerformanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryReportPerformanceResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryReportPerformanceResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryReportPerformanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryReportPerformanceResponseBody = None,
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
            temp_model = QueryReportPerformanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShareListRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        # The ID of the work. The works include data portal, dashboard, spreadsheet, self-service data retrieval, ad-hoc analysis, data entry, and data screen.
        # 
        # This parameter is required.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class QueryShareListResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_point: int = None,
        expire_date: int = None,
        report_id: str = None,
        share_id: str = None,
        share_to_id: str = None,
        share_to_name: str = None,
        share_to_type: int = None,
        share_type: str = None,
    ):
        # Sharing permissions. Possible values:
        # 
        # - 1: View only
        # - 3: View and export
        self.auth_point = auth_point
        # The timestamp in milliseconds indicating the expiration time of the authorization.
        self.expire_date = expire_date
        # The ID of the work.
        self.report_id = report_id
        # The ID of the sharing configuration.
        self.share_id = share_id
        # The ID of the sharing target, which could be a user ID or a group ID in Quick BI.
        # 
        # - When ShareToType=2 (all members within an organization), ShareToId is the organization ID.
        self.share_to_id = share_to_id
        # The name of the sharing target.
        self.share_to_name = share_to_name
        # The type of sharing. Possible values:
        # 
        # - 0: User
        # - 1: Group
        # - 2: Organization
        # - 3: Space
        self.share_to_type = share_to_type
        # The type of the shared work. The value range includes: 
        # - dataProduct: Data Portal 
        # - dashboard: Dashboard 
        # - report: Spreadsheet 
        # - dashboardOfflineQuery: Self-service Data Extraction 
        # - ANALYSIS: Ad-hoc Analysis 
        # - DATAFORM: Data Entry 
        # - SCREEN: Data Visualization Screen
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_point is not None:
            result['AuthPoint'] = self.auth_point
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.share_id is not None:
            result['ShareId'] = self.share_id
        if self.share_to_id is not None:
            result['ShareToId'] = self.share_to_id
        if self.share_to_name is not None:
            result['ShareToName'] = self.share_to_name
        if self.share_to_type is not None:
            result['ShareToType'] = self.share_to_type
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoint') is not None:
            self.auth_point = m.get('AuthPoint')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')
        if m.get('ShareToId') is not None:
            self.share_to_id = m.get('ShareToId')
        if m.get('ShareToName') is not None:
            self.share_to_name = m.get('ShareToName')
        if m.get('ShareToType') is not None:
            self.share_to_type = m.get('ShareToType')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class QueryShareListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryShareListResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Returns the list of objects to which the work has been shared.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryShareListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryShareListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryShareListResponseBody = None,
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
            temp_model = QueryShareListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySharesToUserListRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the user. The user ID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuerySharesToUserListResponseBodyResultDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory where the resource is located.
        self.id = id
        # The name of the resource.
        self.name = name
        # The path ID of the directory where the resource is located.
        self.path_id = path_id
        # The path name of the directory where the resource is located.
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QuerySharesToUserListResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        directory: QuerySharesToUserListResponseBodyResultDirectory = None,
        modify_name: str = None,
        modify_time: str = None,
        owner_id: str = None,
        owner_name: str = None,
        security_level: str = None,
        status: int = None,
        third_part_auth_flag: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The timestamp of the creation time in milliseconds.
        self.create_time = create_time
        # Remarks on the work.
        self.description = description
        # Information about the directory where the work is located.
        self.directory = directory
        # The name of the Alibaba Cloud account to which the modifier belongs.
        self.modify_name = modify_name
        # The timestamp of the modification time in milliseconds.
        self.modify_time = modify_time
        # The UserID of the work owner in Quickbi.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # Security policies for collaborative authorization of works. Valid values:
        # 
        # *   0: private
        # *   12: Authorize specified members
        # *   1 or 11: Authorize all workspace members
        # 
        # > 
        # 
        # *   If you use legacy permissions, the return value is 1.
        # 
        # *   If you use the new permissions, the return value is 11.
        self.security_level = security_level
        # The publishing status of the report. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # Third-party embedding status. Valid values:
        # 
        # *   0: No embedding is enabled.
        # *   1: Embed is enabled.
        self.third_part_auth_flag = third_part_auth_flag
        # The name of the report.
        self.work_name = work_name
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        # *   dashboardOfflineQuery: self-service data retrieval
        self.work_type = work_type
        # The ID of the operations report.
        self.works_id = works_id
        # The ID of the workspace to which the report belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the report belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QuerySharesToUserListResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QuerySharesToUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QuerySharesToUserListResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Returns a list of works authorized to the user.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QuerySharesToUserListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySharesToUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySharesToUserListResponseBody = None,
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
            temp_model = QuerySharesToUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmartqPermissionByCubeIdRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        user_id: str = None,
    ):
        # Dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # User ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QuerySmartqPermissionByCubeIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        cube_name: str = None,
        has_perssion: bool = None,
    ):
        # Dataset ID.
        self.cube_id = cube_id
        # Dataset name.
        self.cube_name = cube_name
        # Whether the current user has permission for the smart question. Note: \\"HasPerssion\\" seems to be a typo, it should probably be \\"HasPermission\\".
        self.has_perssion = has_perssion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.cube_name is not None:
            result['CubeName'] = self.cube_name
        if self.has_perssion is not None:
            result['HasPerssion'] = self.has_perssion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('CubeName') is not None:
            self.cube_name = m.get('CubeName')
        if m.get('HasPerssion') is not None:
            self.has_perssion = m.get('HasPerssion')
        return self


class QuerySmartqPermissionByCubeIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QuerySmartqPermissionByCubeIdResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Basic information of the dataset.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QuerySmartqPermissionByCubeIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySmartqPermissionByCubeIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmartqPermissionByCubeIdResponseBody = None,
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
            temp_model = QuerySmartqPermissionByCubeIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTicketInfoRequest(TeaModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        # The value of the bill.
        # 
        # This parameter is required.
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class QueryTicketInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_ticket: str = None,
        cmpt_id: str = None,
        global_param: str = None,
        invalid_time: str = None,
        max_ticket_num: int = None,
        organization_id: str = None,
        register_time: str = None,
        used_ticket_num: int = None,
        user_id: str = None,
        watermark_param: str = None,
        works_id: str = None,
    ):
        # Notes.
        self.access_ticket = access_ticket
        # The ID of the component in the report.
        self.cmpt_id = cmpt_id
        # Global parameters.
        self.global_param = global_param
        # Expiration time of the note.
        self.invalid_time = invalid_time
        # The maximum number of supported bills.
        self.max_ticket_num = max_ticket_num
        # The ID of the organization.
        self.organization_id = organization_id
        # The registration time of the ticket.
        self.register_time = register_time
        # The number of bills that have been consumed.
        self.used_ticket_num = used_ticket_num
        # The user ID of the Quick BI.
        self.user_id = user_id
        # Set the watermarking parameters.
        self.watermark_param = watermark_param
        # The ID of the operations report.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_ticket is not None:
            result['AccessTicket'] = self.access_ticket
        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id
        if self.global_param is not None:
            result['GlobalParam'] = self.global_param
        if self.invalid_time is not None:
            result['InvalidTime'] = self.invalid_time
        if self.max_ticket_num is not None:
            result['MaxTicketNum'] = self.max_ticket_num
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.used_ticket_num is not None:
            result['UsedTicketNum'] = self.used_ticket_num
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTicket') is not None:
            self.access_ticket = m.get('AccessTicket')
        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')
        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')
        if m.get('InvalidTime') is not None:
            self.invalid_time = m.get('InvalidTime')
        if m.get('MaxTicketNum') is not None:
            self.max_ticket_num = m.get('MaxTicketNum')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('UsedTicketNum') is not None:
            self.used_ticket_num = m.get('UsedTicketNum')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryTicketInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryTicketInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the generated ticket.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryTicketInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTicketInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTicketInfoResponseBody = None,
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
            temp_model = QueryTicketInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserGroupListByParentIdRequest(TeaModel):
    def __init__(
        self,
        parent_user_group_id: str = None,
    ):
        # The ID of the parent user group.
        # 
        # *   If you enter the ID of the parent user group, you can obtain the information of the child user group under this ID.
        # *   If you enter -1, you can obtain the sub-user group information under the root directory.
        # 
        # This parameter is required.
        self.parent_user_group_id = parent_user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        return self


class QueryUserGroupListByParentIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        identified_path: str = None,
        modified_time: str = None,
        modify_user: str = None,
        parent_user_group_id: str = None,
        user_group_description: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The time when the sub-user group was created.
        self.create_time = create_time
        # The creator of the sub-user group. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        self.create_user = create_user
        # Directory level of the sub-user group.
        self.identified_path = identified_path
        # The time when the sub-user group was last modified.
        self.modified_time = modified_time
        # The user who modified the subgroup. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        self.modify_user = modify_user
        # The ID of the parent user group.
        self.parent_user_group_id = parent_user_group_id
        # The description of the sub-user group.
        self.user_group_description = user_group_description
        # The ID of the sub-user group.
        self.user_group_id = user_group_id
        # The name of the sub-user group.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.identified_path is not None:
            result['IdentifiedPath'] = self.identified_path
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('IdentifiedPath') is not None:
            self.identified_path = m.get('IdentifiedPath')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryUserGroupListByParentIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryUserGroupListByParentIdResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the sub-user group.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserGroupListByParentIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserGroupListByParentIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserGroupListByParentIdResponseBody = None,
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
            temp_model = QueryUserGroupListByParentIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserGroupMemberRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        user_group_id: str = None,
    ):
        # Keyword for the username or nickname of the user group member.
        self.keyword = keyword
        # User group ID.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryUserGroupMemberResponseBodyResult(TeaModel):
    def __init__(
        self,
        id: str = None,
        is_user_group: bool = None,
        name: str = None,
        parent_user_group_id: str = None,
        parent_user_group_name: str = None,
    ):
        # ID of the user group or the user group member.
        self.id = id
        # Indicates whether it is a user group. Possible values:
        # 
        # - true: It is a user group.
        # - false: It is a user.
        self.is_user_group = is_user_group
        # Name or nickname of the user group or its member.
        self.name = name
        # ID of the parent user group.
        self.parent_user_group_id = parent_user_group_id
        # Name of the parent user group.
        self.parent_user_group_name = parent_user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_user_group is not None:
            result['IsUserGroup'] = self.is_user_group
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_user_group_id is not None:
            result['ParentUserGroupId'] = self.parent_user_group_id
        if self.parent_user_group_name is not None:
            result['ParentUserGroupName'] = self.parent_user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsUserGroup') is not None:
            self.is_user_group = m.get('IsUserGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentUserGroupId') is not None:
            self.parent_user_group_id = m.get('ParentUserGroupId')
        if m.get('ParentUserGroupName') is not None:
            self.parent_user_group_name = m.get('ParentUserGroupName')
        return self


class QueryUserGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryUserGroupMemberResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The result of the request for the user group member list.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserGroupMemberResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserGroupMemberResponseBody = None,
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
            temp_model = QueryUserGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoByAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        parent_account_name: str = None,
    ):
        # Enter the name or ID of the Alibaba Cloud account that you want to query.
        # 
        # *   When you enter an account name:
        # 
        #     *   If the organization user is a master account, such as main_account, the query account format is master account. That is, the main account main_account to be entered.
        #     *   If the organization user is a RAM user, such as a <zhangsan@test.onaliyun.com>, the query account format is the head of the RAM user, that is, the RAM user to be entered is zhangsan.
        # 
        # *   ID:
        # 
        #     *   Enter the UID of the account to query the account information.
        # 
        # This parameter is required.
        self.account = account
        # 当查询子账号出现重复报错时，输入主账号的账号名，
        # 例如zhangsan@test.onaliyun.com。
        self.parent_account_name = parent_account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.parent_account_name is not None:
            result['ParentAccountName'] = self.parent_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('ParentAccountName') is not None:
            self.parent_account_name = m.get('ParentAccountName')
        return self


class QueryUserInfoByAccountResponseBodyResult(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account that corresponds to the member. (If you use a RAM user, the domain name information that follows @ is removed. For example, if you use a <test@test.com>, test is returned.)
        self.account_name = account_name
        # Whether you are an administrator of the organization. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Whether you are a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # The email address of the user.
        self.email = email
        # The nickname of the account.
        self.nick_name = nick_name
        # The phone number of the alert contact.
        self.phone = phone
        # 用户绑定的组织角色ID列表。
        self.role_id_list = role_id_list
        # The UserID in the Quick BI.
        self.user_id = user_id
        # The role type of the organization member. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.email is not None:
            result['Email'] = self.email
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserInfoByAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryUserInfoByAccountResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned organization user information.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserInfoByAccountResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserInfoByAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserInfoByAccountResponseBody = None,
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
            temp_model = QueryUserInfoByAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the user. The UserID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryUserInfoByUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account that corresponds to the member.
        self.account_name = account_name
        # Whether you are an administrator of the organization. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Whether you are a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # The email address of the user.
        self.email = email
        # The nickname of the account.
        self.nick_name = nick_name
        # The phone number of the alert contact.
        self.phone = phone
        self.role_id_list = role_id_list
        # The UserID in the Quick BI.
        self.user_id = user_id
        # The role type of the organization member. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.email is not None:
            result['Email'] = self.email
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserInfoByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryUserInfoByUserIdResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned organization user information.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserInfoByUserIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserInfoByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserInfoByUserIdResponseBody = None,
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
            temp_model = QueryUserInfoByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The keyword of the username or nickname of the organization member.
        self.keyword = keyword
        # Current page number for organization member list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryUserListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        is_deleted: bool = None,
        joined_date: int = None,
        last_login_time: int = None,
        nick_name: str = None,
        role_id_list: List[int] = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The name of the Alibaba Cloud account that corresponds to the member.
        self.account_name = account_name
        # Indicates whether the organization administrator. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Indicate whether the RAM user is a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # User status: 
        # - Active - false 
        # - Inactive - true
        self.is_deleted = is_deleted
        # Join Date
        self.joined_date = joined_date
        # Last login time.
        self.last_login_time = last_login_time
        # The nickname of the organization member.
        self.nick_name = nick_name
        # List of organization role IDs bound to the user.
        self.role_id_list = role_id_list
        # The UserID in the Quick BI.
        self.user_id = user_id
        # The role type of the organization member. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.joined_date is not None:
            result['JoinedDate'] = self.joined_date
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('JoinedDate') is not None:
            self.joined_date = m.get('JoinedDate')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RoleIdList') is not None:
            self.role_id_list = m.get('RoleIdList')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryUserListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryUserListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Returns the list of requested users.
        self.data = data
        # The page number of the returned page.
        self.page_num = page_num
        # The number of rows per page set when the interface is requested.
        self.page_size = page_size
        # The total number of rows in the table.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryUserListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryUserListResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The pagination result of the user list is returned. The detailed information list of organization members is stored in the response parameter Data.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserListResponseBody = None,
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
            temp_model = QueryUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserRoleInfoInWorkspaceRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # Quick BI user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryUserRoleInfoInWorkspaceResponseBodyResult(TeaModel):
    def __init__(
        self,
        role_code: str = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # Preset role code.
        self.role_code = role_code
        # Preset role ID. Possible values:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        self.role_id = role_id
        # Preset role name.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryUserRoleInfoInWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryUserRoleInfoInWorkspaceResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Preset space role information of the user.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request succeeded.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryUserRoleInfoInWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserRoleInfoInWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserRoleInfoInWorkspaceResponseBody = None,
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
            temp_model = QueryUserRoleInfoInWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserTagMetaListResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The description of the tag.
        self.tag_description = tag_description
        # The ID of the label.
        self.tag_id = tag_id
        # The name of the tag.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryUserTagMetaListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryUserTagMetaListResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Returns a list of user tags in an organization.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserTagMetaListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserTagMetaListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserTagMetaListResponseBody = None,
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
            temp_model = QueryUserTagMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserTagValueListRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # This UserID refers to the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryUserTagValueListResponseBodyResult(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_name: str = None,
        tag_value: str = None,
    ):
        # Tag ID.
        self.tag_id = tag_id
        # Tag name.
        self.tag_name = tag_name
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class QueryUserTagValueListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryUserTagValueListResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The result of the request for a list of user tags and their values.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryUserTagValueListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserTagValueListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserTagValueListResponseBody = None,
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
            temp_model = QueryUserTagValueListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksRequest(TeaModel):
    def __init__(
        self,
        works_id: str = None,
    ):
        # Report ID
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryWorksResponseBodyResultDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory.
        self.id = id
        # The name of the directory.
        self.name = name
        # The hierarchical structure of the directory ID to which the directory belongs. Separate the hierarchical structure with a /.
        self.path_id = path_id
        # The hierarchical structure of the directory to which the directory belongs. Separate the hierarchical structure with a (/).
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_3rd_flag: int = None,
        description: str = None,
        directory: QueryWorksResponseBodyResultDirectory = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        modify_name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        public_flag: bool = None,
        public_invalid_time: int = None,
        security_level: str = None,
        status: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.auth_3rd_flag = auth_3rd_flag
        # Remarks on the work.
        self.description = description
        # The directory to which the work belongs.
        self.directory = directory
        # The timestamp of the creation of the work in milliseconds.
        self.gmt_create = gmt_create
        # The timestamp of the modification of the work in milliseconds.
        self.gmt_modify = gmt_modify
        # The Alibaba Cloud account name of the person who modified the work.
        self.modify_name = modify_name
        # The user ID of the work owner in the Quick BI.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # Is it public
        self.public_flag = public_flag
        # Deadline for the public release of the report
        self.public_invalid_time = public_invalid_time
        # Security policies for collaborative authorization of works. Valid values:
        # 
        # *   0: private
        # *   12: Authorize specified members
        # *   1 or 11: Authorize all workspace members
        # 
        # > 
        # 
        # *   If you use legacy permissions, the return value is 1.
        # 
        # *   If you use the new permissions, the return value is 11.
        self.security_level = security_level
        # The status of the report. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # The name of the work.
        self.work_name = work_name
        # Queries the types of works. Fill in the blanks to query all types. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        # *   dashboardOfflineQuery: self-service data retrieval
        self.work_type = work_type
        # The ID of the work.
        self.works_id = works_id
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.public_flag is not None:
            result['PublicFlag'] = self.public_flag
        if self.public_invalid_time is not None:
            result['PublicInvalidTime'] = self.public_invalid_time
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksResponseBodyResultDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PublicFlag') is not None:
            self.public_flag = m.get('PublicFlag')
        if m.get('PublicInvalidTime') is not None:
            self.public_invalid_time = m.get('PublicInvalidTime')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryWorksResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the work.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorksResponseBody = None,
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
            temp_model = QueryWorksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksBloodRelationshipRequest(TeaModel):
    def __init__(
        self,
        works_id: str = None,
    ):
        # The ID of the data work.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class QueryWorksBloodRelationshipResponseBodyResultQueryParams(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        area_name: str = None,
        caption: str = None,
        data_type: str = None,
        expression: str = None,
        is_measure: bool = None,
        path_id: str = None,
        uid: str = None,
    ):
        # The ID of the owning location.
        self.area_id = area_id
        # The name of the owning location.
        self.area_name = area_name
        # The display name of the field.
        self.caption = caption
        # The type of the field. Valid values:
        # 
        # *   string: string type
        # *   date: a date type that contains only the year, month, and day parts
        # *   datetime: a common date type
        # *   time: a date type that contains only hours, minutes, and seconds.
        # *   number: numeric
        # *   boolean: Boolean type
        # *   geographical: geographical location
        # *   url: string type
        # *   imageUrl: the type of the image link.
        # *   multivalue: a multi-value column
        self.data_type = data_type
        # Calculate field expression.
        self.expression = expression
        # Indices whether the metric. Valid values:
        # 
        # true false
        self.is_measure = is_measure
        # The globally unique PathId.
        self.path_id = path_id
        # The unique ID of the field.
        self.uid = uid

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
        if self.caption is not None:
            result['Caption'] = self.caption
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.is_measure is not None:
            result['IsMeasure'] = self.is_measure
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('IsMeasure') is not None:
            self.is_measure = m.get('IsMeasure')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryWorksBloodRelationshipResponseBodyResult(TeaModel):
    def __init__(
        self,
        component_id: str = None,
        component_name: str = None,
        component_type: int = None,
        component_type_cn_name: str = None,
        component_type_name: str = None,
        dataset_id: str = None,
        query_params: List[QueryWorksBloodRelationshipResponseBodyResultQueryParams] = None,
    ):
        # The ID of the component that you want to modify.
        self.component_id = component_id
        # The name of the component.
        self.component_name = component_name
        # The type of the image component.
        self.component_type = component_type
        # Chinese name of the component type
        self.component_type_cn_name = component_type_cn_name
        # The name of the component type.
        self.component_type_name = component_type_name
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        self.dataset_id = dataset_id
        # A list of query parameter reference columns.
        self.query_params = query_params

    def validate(self):
        if self.query_params:
            for k in self.query_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.component_type_cn_name is not None:
            result['ComponentTypeCnName'] = self.component_type_cn_name
        if self.component_type_name is not None:
            result['ComponentTypeName'] = self.component_type_name
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        result['QueryParams'] = []
        if self.query_params is not None:
            for k in self.query_params:
                result['QueryParams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('ComponentTypeCnName') is not None:
            self.component_type_cn_name = m.get('ComponentTypeCnName')
        if m.get('ComponentTypeName') is not None:
            self.component_type_name = m.get('ComponentTypeName')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        self.query_params = []
        if m.get('QueryParams') is not None:
            for k in m.get('QueryParams'):
                temp_model = QueryWorksBloodRelationshipResponseBodyResultQueryParams()
                self.query_params.append(temp_model.from_map(k))
        return self


class QueryWorksBloodRelationshipResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[QueryWorksBloodRelationshipResponseBodyResult] = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # List of work blood information.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryWorksBloodRelationshipResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksBloodRelationshipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorksBloodRelationshipResponseBody = None,
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
            temp_model = QueryWorksBloodRelationshipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksByOrganizationRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        third_part_auth_flag: int = None,
        works_type: str = None,
    ):
        # Page number.
        # 
        # - Default value is 1.
        self.page_num = page_num
        # Number of items per page.
        # 
        # - Default value is 10.
        self.page_size = page_size
        # The status of the work to query. Possible values:
        # 
        # - 0: Unpublished
        # - 1: Published
        # - 2: Modified but not published
        # - 3: Offline
        self.status = status
        # Third-party embedding status. Possible values:
        # 
        # - 0: Embedding not enabled
        # - 1: Embedding enabled
        self.third_part_auth_flag = third_part_auth_flag
        # The type of work to query. Leave blank to query all types. Possible values:
        # 
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        # - dashboardOfflineQuery: Self-service Data Retrieval
        self.works_type = works_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        return self


class QueryWorksByOrganizationResponseBodyResultDataDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # ID of the directory to which it belongs.
        self.id = id
        # Name of the directory to which it belongs.
        self.name = name
        # Hierarchical structure of the directory ID, separated by『/』.
        self.path_id = path_id
        # Hierarchical structure of the directory name, separated by『/』.
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksByOrganizationResponseBodyResultData(TeaModel):
    def __init__(
        self,
        auth_3rd_flag: int = None,
        description: str = None,
        directory: QueryWorksByOrganizationResponseBodyResultDataDirectory = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        modify_name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        public_flag: bool = None,
        public_invalid_time: int = None,
        security_level: str = None,
        status: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Third-party embedding status. Possible values:
        # 
        # - 0: Embedding not enabled
        # - 1: Embedding enabled
        self.auth_3rd_flag = auth_3rd_flag
        # Notes for the work.
        self.description = description
        # Directory to which the work belongs.
        self.directory = directory
        # Timestamp (in milliseconds) when the work was created.
        self.gmt_create = gmt_create
        # 作品修改的毫秒级时间戳。
        self.gmt_modify = gmt_modify
        # 作品修改者的阿里云账户名。
        self.modify_name = modify_name
        # The UserID of the work\\"s owner in Quick BI.
        self.owner_id = owner_id
        # The Alibaba Cloud account name of the work\\"s owner.
        self.owner_name = owner_name
        # Whether it is public
        self.public_flag = public_flag
        # The expiration date for the report to be made public
        self.public_invalid_time = public_invalid_time
        # The security policy for collaborative authorization of the work. Values:
        # - 0: Private
        # - 12: Authorize specific members
        # - 1 or 11: Authorize all space members
        # 
        # >- If you are using the old version of permissions, the returned value is 1.
        # >- If you are using the new version of permissions, the returned value is 11.
        self.security_level = security_level
        # The status of the report. Value range:
        # 
        # - 0: Unpublished
        # - 1: Published
        # - 2: Modified but not published
        # - 3: Offline
        self.status = status
        # The name of the work.
        self.work_name = work_name
        # The type of the work. Value range:
        # 
        # - DATAPRODUCT: Data portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        # - dashboardOfflineQuery: Self-service data retrieval
        self.work_type = work_type
        # The ID of the work.
        self.works_id = works_id
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.public_flag is not None:
            result['PublicFlag'] = self.public_flag
        if self.public_invalid_time is not None:
            result['PublicInvalidTime'] = self.public_invalid_time
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksByOrganizationResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PublicFlag') is not None:
            self.public_flag = m.get('PublicFlag')
        if m.get('PublicInvalidTime') is not None:
            self.public_invalid_time = m.get('PublicInvalidTime')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksByOrganizationResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryWorksByOrganizationResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Details of the work list.
        self.data = data
        # Page number.
        self.page_num = page_num
        # The number of rows per page set when requesting the interface.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorksByOrganizationResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorksByOrganizationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryWorksByOrganizationResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns a list of all works under the organization that meet the request criteria.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksByOrganizationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksByOrganizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorksByOrganizationResponseBody = None,
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
            temp_model = QueryWorksByOrganizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorksByWorkspaceRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        third_part_auth_flag: int = None,
        works_type: str = None,
        workspace_id: str = None,
    ):
        # The page number of the returned page.
        # 
        # *   Default value: 1.
        self.page_num = page_num
        # The number of entries returned per page.
        # 
        # *   Default value: 10.
        self.page_size = page_size
        # The status of the work. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.third_part_auth_flag = third_part_auth_flag
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        self.works_type = works_type
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_type is not None:
            result['WorksType'] = self.works_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryWorksByWorkspaceResponseBodyResultDataDirectory(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory.
        self.id = id
        # The name of the directory.
        self.name = name
        # The hierarchical structure of the directory ID to which the directory belongs. Separate the hierarchical structure with a /.
        self.path_id = path_id
        # The hierarchical structure of the directory to which the directory belongs. Separate the hierarchical structure with a (/).
        self.path_name = path_name

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
        if self.path_id is not None:
            result['PathId'] = self.path_id
        if self.path_name is not None:
            result['PathName'] = self.path_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')
        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')
        return self


class QueryWorksByWorkspaceResponseBodyResultData(TeaModel):
    def __init__(
        self,
        auth_3rd_flag: int = None,
        description: str = None,
        directory: QueryWorksByWorkspaceResponseBodyResultDataDirectory = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        modify_name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        public_flag: bool = None,
        public_invalid_time: int = None,
        security_level: str = None,
        status: int = None,
        work_name: str = None,
        work_type: str = None,
        works_id: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.auth_3rd_flag = auth_3rd_flag
        # Remarks on the work.
        self.description = description
        # The directory to which the work belongs.
        self.directory = directory
        # The timestamp of the creation of the work in milliseconds.
        self.gmt_create = gmt_create
        # The timestamp of the modification of the work in milliseconds.
        self.gmt_modify = gmt_modify
        # Nickname of the work modifier.
        self.modify_name = modify_name
        # The user ID of the work owner in the Quick BI.
        self.owner_id = owner_id
        # The nickname of the work owner.
        self.owner_name = owner_name
        # Is it public
        self.public_flag = public_flag
        # Deadline for the public release of the report
        self.public_invalid_time = public_invalid_time
        # Security policies for collaborative authorization of works. Valid values:
        # 
        # *   0: private
        # *   12: Authorize specified members
        # *   1 or 11: Authorize all workspace members
        # 
        # > 
        # 
        # *   If you use legacy permissions, the return value is 1.
        # 
        # *   If you use the new permissions, the return value is 11.
        self.security_level = security_level
        # Status of dashboards, full-screen dashboards, spreadsheets. The default value of other work types is 1. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # The name of the work.
        self.work_name = work_name
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        # *   dashboardOfflineQuery: self-service data retrieval
        # *   Analysis: Ad hoc analysis
        # *   DATAFORM: form filling
        self.work_type = work_type
        # The ID of the work.
        self.works_id = works_id
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_3rd_flag is not None:
            result['Auth3rdFlag'] = self.auth_3rd_flag
        if self.description is not None:
            result['Description'] = self.description
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.public_flag is not None:
            result['PublicFlag'] = self.public_flag
        if self.public_invalid_time is not None:
            result['PublicInvalidTime'] = self.public_invalid_time
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.status is not None:
            result['Status'] = self.status
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        if self.work_type is not None:
            result['WorkType'] = self.work_type
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth3rdFlag') is not None:
            self.auth_3rd_flag = m.get('Auth3rdFlag')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Directory') is not None:
            temp_model = QueryWorksByWorkspaceResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m['Directory'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PublicFlag') is not None:
            self.public_flag = m.get('PublicFlag')
        if m.get('PublicInvalidTime') is not None:
            self.public_invalid_time = m.get('PublicInvalidTime')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')
        return self


class QueryWorksByWorkspaceResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryWorksByWorkspaceResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # The details of the list of works.
        self.data = data
        # The page number of the returned page.
        self.page_num = page_num
        # The number of rows per page set when the interface is requested.
        self.page_size = page_size
        # The total number of rows in the table.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorksByWorkspaceResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorksByWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryWorksByWorkspaceResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Returns a list of all works in the organization workspace that meet the requested criteria.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorksByWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorksByWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorksByWorkspaceResponseBody = None,
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
            temp_model = QueryWorksByWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorkspaceRoleConfigRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
    ):
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom role: The corresponding role ID for the custom role
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList(TeaModel):
    def __init__(
        self,
        action_auth_keys: List[str] = None,
        auth_key: str = None,
    ):
        # Permission scope.
        self.action_auth_keys = action_auth_keys
        # Permission type:
        # - portal_create: Data Portal
        # - dashboard_create: Dashboard
        # - report_create: Spreadsheet
        # - screen_create: Data Screen
        # - analysis: Ad-hoc Analysis
        # - offline_download: Self-service Data Retrieval
        # - data_form: Data Entry
        # - quick_etl: Data Preparation
        # - cube: Dataset
        # - datasource: Data Source
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_auth_keys is not None:
            result['ActionAuthKeys'] = self.action_auth_keys
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionAuthKeys') is not None:
            self.action_auth_keys = m.get('ActionAuthKeys')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        return self


class QueryWorkspaceRoleConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        auth_config_list: List[QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role permission configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Value range:
        # 
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom role: The corresponding role ID for the custom role
        self.role_id = role_id
        # Role name.
        self.role_name = role_name

    def validate(self):
        if self.auth_config_list:
            for k in self.auth_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthConfigList'] = []
        if self.auth_config_list is not None:
            for k in self.auth_config_list:
                result['AuthConfigList'].append(k.to_map() if k else None)
        if self.is_system_role is not None:
            result['IsSystemRole'] = self.is_system_role
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_config_list = []
        if m.get('AuthConfigList') is not None:
            for k in m.get('AuthConfigList'):
                temp_model = QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k))
        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryWorkspaceRoleConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryWorkspaceRoleConfigResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the query result of the interface.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorkspaceRoleConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorkspaceRoleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorkspaceRoleConfigResponseBody = None,
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
            temp_model = QueryWorkspaceRoleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWorkspaceUserListRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        workspace_id: str = None,
    ):
        # Keyword for the username of the workspace member.
        self.keyword = keyword
        # Current page number of the workspace member list:
        # 
        # - Starting value: 1
        # - Default value: 1
        self.page_num = page_num
        # Number of rows per page in a paginated query:
        # 
        # - Default value: 10
        # - Maximum value: 1000
        self.page_size = page_size
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryWorkspaceUserListResponseBodyResultDataRole(TeaModel):
    def __init__(
        self,
        role_code: str = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # Code corresponding to the preset role.
        self.role_code = role_code
        # Preset role ID. Possible values:
        # 
        # - 25: Workspace Administrator
        # - 26: Workspace Developer
        # - 27: Workspace Analyst
        # - 30: Workspace Viewer
        self.role_id = role_id
        # Name of the preset role.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class QueryWorkspaceUserListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        nick_name: str = None,
        role: QueryWorkspaceUserListResponseBodyResultDataRole = None,
        user_id: str = None,
    ):
        # Alibaba Cloud account ID.
        self.account_id = account_id
        # Alibaba Cloud account name.
        self.account_name = account_name
        # Nickname.
        self.nick_name = nick_name
        # Preset role information for the workspace member.
        self.role = role
        # Quick BI user ID.
        self.user_id = user_id

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role is not None:
            result['Role'] = self.role.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Role') is not None:
            temp_model = QueryWorkspaceUserListResponseBodyResultDataRole()
            self.role = temp_model.from_map(m['Role'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryWorkspaceUserListResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[QueryWorkspaceUserListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Information about the workspace members.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page as set in the request.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWorkspaceUserListResponseBodyResultData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class QueryWorkspaceUserListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: QueryWorkspaceUserListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the paginated result of the member list, with detailed information about the members stored in the Data parameter of the response.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryWorkspaceUserListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWorkspaceUserListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryWorkspaceUserListResponseBody = None,
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
            temp_model = QueryWorkspaceUserListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResultCallbackRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        handle_reason: str = None,
        status: int = None,
    ):
        # The ID of the approval process.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The reason for the approval.
        # 
        # This parameter is required.
        self.handle_reason = handle_reason
        # Approval result:
        # 
        # *   1: passed
        # *   2: rejected
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.handle_reason is not None:
            result['HandleReason'] = self.handle_reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('HandleReason') is not None:
            self.handle_reason = m.get('HandleReason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ResultCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResultCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResultCallbackResponseBody = None,
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
            temp_model = ResultCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveFavoritesRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        works_id: str = None,
    ):
        # The user ID of the person who favorites the work. This user ID is the UserID of Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The ID of the work being favorited.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class SaveFavoritesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution. Possible values:
        # 
        # - true: Execution successful
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request successful
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveFavoritesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveFavoritesResponseBody = None,
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
            temp_model = SaveFavoritesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionExtraConfigRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        miss_hit_policy: str = None,
        rule_type: str = None,
    ):
        # This parameter is required.
        self.cube_id = cube_id
        # This parameter is required.
        self.miss_hit_policy = miss_hit_policy
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.miss_hit_policy is not None:
            result['MissHitPolicy'] = self.miss_hit_policy
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('MissHitPolicy') is not None:
            self.miss_hit_policy = m.get('MissHitPolicy')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class SetDataLevelPermissionExtraConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionExtraConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataLevelPermissionExtraConfigResponseBody = None,
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
            temp_model = SetDataLevelPermissionExtraConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionRuleConfigRequest(TeaModel):
    def __init__(
        self,
        rule_model: str = None,
    ):
        # This parameter is required.
        self.rule_model = rule_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_model is not None:
            result['RuleModel'] = self.rule_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleModel') is not None:
            self.rule_model = m.get('RuleModel')
        return self


class SetDataLevelPermissionRuleConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionRuleConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataLevelPermissionRuleConfigResponseBody = None,
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
            temp_model = SetDataLevelPermissionRuleConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDataLevelPermissionWhiteListRequest(TeaModel):
    def __init__(
        self,
        white_list_model: str = None,
    ):
        # { "ruleType": "ROW_LEVEL", // The row-level permission type. "usersModel": { "userGroups": [ "0d5fb19b- ***-1248 fc27ca51", // The ID of the user group. "3d2c23d4-***-f6390f325c2d" ], "users": [ "4334 ***358", // Quick BI the UserID of the user. "Huang***3fa822" ] }, "cubeId": "7c7223ae-31d1-4d2f-b11f-3c744528014b" }
        # 
        # This parameter is required.
        self.white_list_model = white_list_model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.white_list_model is not None:
            result['WhiteListModel'] = self.white_list_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteListModel') is not None:
            self.white_list_model = m.get('WhiteListModel')
        return self


class SetDataLevelPermissionWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDataLevelPermissionWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDataLevelPermissionWhiteListResponseBody = None,
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
            temp_model = SetDataLevelPermissionWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartqAuthTransferRequest(TeaModel):
    def __init__(
        self,
        origin_user_id: str = None,
        target_user_ids: str = None,
    ):
        # Source user ID.
        # 
        # This parameter is required.
        self.origin_user_id = origin_user_id
        # Target user ID array, separated by English commas.
        # >Warning: The number of user IDs cannot exceed 100.
        # 
        # This parameter is required.
        self.target_user_ids = target_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_user_id is not None:
            result['OriginUserId'] = self.origin_user_id
        if self.target_user_ids is not None:
            result['TargetUserIds'] = self.target_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginUserId') is not None:
            self.origin_user_id = m.get('OriginUserId')
        if m.get('TargetUserIds') is not None:
            self.target_user_ids = m.get('TargetUserIds')
        return self


class SmartqAuthTransferResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # API execution result. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SmartqAuthTransferResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmartqAuthTransferResponseBody = None,
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
            temp_model = SmartqAuthTransferResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartqAuthorizeRequest(TeaModel):
    def __init__(
        self,
        cube_ids: str = None,
        expire_day: str = None,
        llm_cube_themes: str = None,
        llm_cubes: str = None,
        operation_type: int = None,
        user_ids: str = None,
    ):
        # Array of dataset IDs, separated by English commas. <notice>This parameter will be converted to the corresponding question resource ID for authorization. Therefore, if the input cubeId does not correspond to any question resource, an error indicating that the question resource does not exist will be reported. Please ensure the correctness of the cubeId.</notice>
        self.cube_ids = cube_ids
        # Expiration time, with a default of seven days.
        # Format: 2099-12-31
        self.expire_day = expire_day
        # Array of analysis theme IDs, separated by English commas.
        self.llm_cube_themes = llm_cube_themes
        # Array of Q&A resource IDs, separated by English commas.
        self.llm_cubes = llm_cubes
        # Operation type. The values are as follows:
        # - 0: Add authorization
        # - 1: Remove authorization
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # Array of user IDs, separated by English commas.
        # >Notice: The number of user IDs per request * (number of Q&A resources + number of analysis themes) cannot exceed 100.
        # 
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_ids is not None:
            result['CubeIds'] = self.cube_ids
        if self.expire_day is not None:
            result['ExpireDay'] = self.expire_day
        if self.llm_cube_themes is not None:
            result['LlmCubeThemes'] = self.llm_cube_themes
        if self.llm_cubes is not None:
            result['LlmCubes'] = self.llm_cubes
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeIds') is not None:
            self.cube_ids = m.get('CubeIds')
        if m.get('ExpireDay') is not None:
            self.expire_day = m.get('ExpireDay')
        if m.get('LlmCubeThemes') is not None:
            self.llm_cube_themes = m.get('LlmCubeThemes')
        if m.get('LlmCubes') is not None:
            self.llm_cubes = m.get('LlmCubes')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class SmartqAuthorizeResponseBodyResult(TeaModel):
    def __init__(
        self,
        detail_message: str = None,
        llm_cube: str = None,
        llm_cube_theme: str = None,
        user_id: str = None,
    ):
        # Reason for failure.
        self.detail_message = detail_message
        # Q&A resource ID.
        self.llm_cube = llm_cube
        # Analysis theme ID.
        self.llm_cube_theme = llm_cube_theme
        # User ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.llm_cube is not None:
            result['LlmCube'] = self.llm_cube
        if self.llm_cube_theme is not None:
            result['LlmCubeTheme'] = self.llm_cube_theme
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('LlmCube') is not None:
            self.llm_cube = m.get('LlmCube')
        if m.get('LlmCubeTheme') is not None:
            self.llm_cube_theme = m.get('LlmCubeTheme')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SmartqAuthorizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[SmartqAuthorizeResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Array of failed user information.
        self.result = result
        # Indicates whether the request was successful. The value range is as follows:
        # 
        # - true: Request succeeded
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = SmartqAuthorizeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SmartqAuthorizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmartqAuthorizeResponseBody = None,
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
            temp_model = SmartqAuthorizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartqQueryAbilityRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        user_id: str = None,
        user_question: str = None,
    ):
        # Dataset ID.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # User ID.
        # >Notice: If this field is not filled, the data will be queried by default as the organization owner.
        self.user_id = user_id
        # Question text.
        # 
        # This parameter is required.
        self.user_question = user_question

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_question is not None:
            result['UserQuestion'] = self.user_question
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserQuestion') is not None:
            self.user_question = m.get('UserQuestion')
        return self


class SmartqQueryAbilityResponseBodyResultMetaType(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        # Column tuple name.
        self.key = key
        self.type = type
        # Column tuple type.
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
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SmartqQueryAbilityResponseBodyResultValues(TeaModel):
    def __init__(
        self,
        row: List[str] = None,
    ):
        # Data values for each row.
        self.row = row

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['Row'] = self.row
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Row') is not None:
            self.row = m.get('Row')
        return self


class SmartqQueryAbilityResponseBodyResult(TeaModel):
    def __init__(
        self,
        chart_type: str = None,
        conclusion_text: str = None,
        logic_sql: str = None,
        meta_type: List[SmartqQueryAbilityResponseBodyResultMetaType] = None,
        values: List[SmartqQueryAbilityResponseBodyResultValues] = None,
    ):
        # Suggested chart type.
        self.chart_type = chart_type
        # Summary information.
        self.conclusion_text = conclusion_text
        # Visualized logical SQL.
        self.logic_sql = logic_sql
        # List of column tuple types.
        self.meta_type = meta_type
        # Array of data value lists.
        self.values = values

    def validate(self):
        if self.meta_type:
            for k in self.meta_type:
                if k:
                    k.validate()
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_type is not None:
            result['ChartType'] = self.chart_type
        if self.conclusion_text is not None:
            result['ConclusionText'] = self.conclusion_text
        if self.logic_sql is not None:
            result['LogicSql'] = self.logic_sql
        result['MetaType'] = []
        if self.meta_type is not None:
            for k in self.meta_type:
                result['MetaType'].append(k.to_map() if k else None)
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')
        if m.get('ConclusionText') is not None:
            self.conclusion_text = m.get('ConclusionText')
        if m.get('LogicSql') is not None:
            self.logic_sql = m.get('LogicSql')
        self.meta_type = []
        if m.get('MetaType') is not None:
            for k in m.get('MetaType'):
                temp_model = SmartqQueryAbilityResponseBodyResultMetaType()
                self.meta_type.append(temp_model.from_map(k))
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = SmartqQueryAbilityResponseBodyResultValues()
                self.values.append(temp_model.from_map(k))
        return self


class SmartqQueryAbilityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SmartqQueryAbilityResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return result.
        self.result = result
        # Whether the operation was successful.
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SmartqQueryAbilityResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SmartqQueryAbilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SmartqQueryAbilityResponseBody = None,
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
            temp_model = SmartqQueryAbilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataLevelPermissionStatusRequest(TeaModel):
    def __init__(
        self,
        cube_id: str = None,
        is_open: int = None,
        rule_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        # 
        # This parameter is required.
        self.cube_id = cube_id
        # This parameter is required.
        self.is_open = is_open
        # This parameter is required.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id
        if self.is_open is not None:
            result['IsOpen'] = self.is_open
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')
        if m.get('IsOpen') is not None:
            self.is_open = m.get('IsOpen')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class UpdateDataLevelPermissionStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataLevelPermissionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataLevelPermissionStatusResponseBody = None,
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
            temp_model = UpdateDataLevelPermissionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEmbeddedStatusRequest(TeaModel):
    def __init__(
        self,
        third_part_auth_flag: bool = None,
        works_id: str = None,
    ):
        # Whether to enable the embedding feature for the work. Valid values:
        # 
        # *   true: enables embedding.
        # *   false: disables embedding.
        # 
        # This parameter is required.
        self.third_part_auth_flag = third_part_auth_flag
        # The ID of the work.
        # 
        # *   Batch modification is supported. Separate multiple values with commas (,).
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag
        if self.works_id is not None:
            result['WorksId'] = self.works_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')
        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')
        return self


class UpdateEmbeddedStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: int = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The number of works that are opened or closed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEmbeddedStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEmbeddedStatusResponseBody = None,
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
            temp_model = UpdateEmbeddedStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketNumRequest(TeaModel):
    def __init__(
        self,
        ticket: str = None,
        ticket_num: int = None,
    ):
        # The value of the third-party embedded ticket, that is, the accessTicket value in the URL.
        # 
        # This parameter is required.
        self.ticket = ticket
        # The number of bills.
        # 
        # *   Valid values: 1 to 99998. Recommended value: 1.
        # 
        # This parameter is required.
        self.ticket_num = ticket_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        return self


class UpdateTicketNumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the update is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTicketNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTicketNumResponseBody = None,
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
            temp_model = UpdateTicketNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        admin_user: bool = None,
        auth_admin_user: bool = None,
        is_deleted: bool = None,
        nick_name: str = None,
        role_ids: str = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # Indicates whether the organization administrator. Valid values:
        # 
        # *   true
        # *   false
        self.admin_user = admin_user
        # Indicate whether the RAM user is a permission administrator. Valid values:
        # 
        # *   true
        # *   false
        self.auth_admin_user = auth_admin_user
        # User status: 
        # * **false**: Active
        #  * **true**: Inactive
        self.is_deleted = is_deleted
        # The nickname of the account.
        # 
        # *   Format check: The value can be up to 50 characters in length.
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.nick_name = nick_name
        # The IDs of the preset or custom organization roles bound to the user, separated by English commas \\",\\", with a maximum of 3. The value range is as follows: - Organization Administrator (preset role): 111111111 - Permission Administrator (preset role): 111111112 - Regular User (preset role): 111111113
        self.role_ids = role_ids
        # The ID of the user to be updated. The user ID is the UserID of the Quick BI, not the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The type of user who is a member of the organization. Valid values:
        # 
        # *   1 : developer
        # *   2 : visitors
        # *   3 : Analyst
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admin_user is not None:
            result['AdminUser'] = self.admin_user
        if self.auth_admin_user is not None:
            result['AuthAdminUser'] = self.auth_admin_user
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUser') is not None:
            self.admin_user = m.get('AdminUser')
        if m.get('AuthAdminUser') is not None:
            self.auth_admin_user = m.get('AuthAdminUser')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(
        self,
        user_group_description: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.user_group_description = user_group_description
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The name of the user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class UpdateUserGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Whether the interface is successfully executed. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class UpdateUserTagMetaRequest(TeaModel):
    def __init__(
        self,
        tag_description: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        # The tag description.
        # 
        # - Format check: Maximum length is 255 characters.
        self.tag_description = tag_description
        # The specified TagID.
        # 
        # - Format check: Maximum length is 64 characters.
        # 
        # This parameter is required.
        self.tag_id = tag_id
        # The tag name.
        # - Format check: Maximum length is 50 characters.
        # - Only Chinese, English, numbers, and /\\|[]() symbols are allowed.
        # 
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UpdateUserTagMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Indicates whether the interface was executed successfully. Possible values:
        # 
        # - true: Execution succeeded
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request succeeded - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserTagMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserTagMetaResponseBody = None,
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
            temp_model = UpdateUserTagMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserTagValueRequest(TeaModel):
    def __init__(
        self,
        tag_id: str = None,
        tag_value: str = None,
        user_id: str = None,
    ):
        # The ID of the tag to be modified.
        # 
        # This parameter is required.
        self.tag_id = tag_id
        # The tag value to be modified.
        # 
        # - To clear this tag, set the tag value to ($NULL$).
        # - For multiple values, use English commas to separate them.
        # - Format validation, maximum length: 3000 characters
        # 
        # This parameter is required.
        self.tag_value = tag_value
        # The user ID for which the tag value is to be modified. This user ID refers to the Quick BI UserID, not the Alibaba Cloud UID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserTagValueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of modifying the user tag. Possible values:
        # 
        # - true: Operation succeeded
        # - false: Operation failed
        self.result = result
        # Indicates whether the request was successful. Value range:
        # - true: The request was successful - false: The request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserTagValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserTagValueResponseBody = None,
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
            temp_model = UpdateUserTagValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceUserRoleRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        role_ids: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # Preset workspace role ID, existing roles will be overwritten. Value range:
        # - 25: Workspace Administrator
        # - 26: Workspace Developer
        # - 27: Workspace Analyst
        # - 30: Workspace Viewer
        self.role_id = role_id
        # Multiple workspace role IDs, separated by commas. If this value is provided, it takes precedence.
        # >Notice: roleId and roleIds cannot both be empty
        self.role_ids = role_ids
        # Quick BI user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceUserRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution. Value range:
        # 
        # - true: Execution successful
        # - false: Execution failed
        self.result = result
        # Indicates whether the request was successful. Value range:
        # 
        # - true: Request successful
        # - false: Request failed
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkspaceUserRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceUserRoleResponseBody = None,
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
            temp_model = UpdateWorkspaceUserRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkspaceUsersRoleRequest(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        user_ids: str = None,
        workspace_id: str = None,
    ):
        # Preset space role ID, existing roles will be overwritten. Value range:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        # 
        # This parameter is required.
        self.role_id = role_id
        # User ID. This is the UserID for Quick BI, not the UID for Alibaba Cloud.
        # 
        # - Supports batch parameters, separate user IDs with a comma (,).
        # 
        # This parameter is required.
        self.user_ids = user_ids
        # Workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateWorkspaceUsersRoleResponseBodyResult(TeaModel):
    def __init__(
        self,
        failure: int = None,
        failure_detail: Dict[str, Any] = None,
        success: int = None,
        total: int = None,
    ):
        # Number of users that failed to update.
        self.failure = failure
        # Reasons for the update failures.
        self.failure_detail = failure_detail
        # Number of users that were updated successfully.
        self.success = success
        # Modify the total number of users.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['Failure'] = self.failure
        if self.failure_detail is not None:
            result['FailureDetail'] = self.failure_detail
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failure') is not None:
            self.failure = m.get('Failure')
        if m.get('FailureDetail') is not None:
            self.failure_detail = m.get('FailureDetail')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class UpdateWorkspaceUsersRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateWorkspaceUsersRoleResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the result of the interface execution.
        self.result = result
        # Indicates whether the request was successful. Value range:
        # 
        # - true: The request was successful, some members may have been updated successfully while others failed, refer to FailureDetail in the response for reasons of failure
        # - false: The request failed, no data will be persisted
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateWorkspaceUsersRoleResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkspaceUsersRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkspaceUsersRoleResponseBody = None,
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
            temp_model = UpdateWorkspaceUsersRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawAllUserGroupsRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The ID of the user. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class WithdrawAllUserGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The execution result of the interface is returned. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request fails.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WithdrawAllUserGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: WithdrawAllUserGroupsResponseBody = None,
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
            temp_model = WithdrawAllUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


