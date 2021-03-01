# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class SubmitStructSyncOrderApprovalRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class SubmitStructSyncOrderApprovalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        workflow_instance_id: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class SubmitStructSyncOrderApprovalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitStructSyncOrderApprovalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SubmitStructSyncOrderApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabaseUserPermssionsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        perm_type: str = None,
        db_id: str = None,
        logic: bool = None,
        user_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.perm_type = perm_type
        self.db_id = db_id
        self.logic = logic
        self.user_name = user_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(TeaModel):
    def __init__(
        self,
        origin_from: str = None,
        perm_type: str = None,
        expire_date: str = None,
        create_date: str = None,
        user_access_id: str = None,
        extra_data: str = None,
    ):
        self.origin_from = origin_from
        self.perm_type = perm_type
        self.expire_date = expire_date
        self.create_date = create_date
        self.user_access_id = user_access_id
        self.extra_data = extra_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        return self


class ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetails(TeaModel):
    def __init__(
        self,
        perm_detail: List[ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail] = None,
    ):
        self.perm_detail = perm_detail

    def validate(self):
        if self.perm_detail:
            for k in self.perm_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PermDetail'] = []
        if self.perm_detail is not None:
            for k in self.perm_detail:
                result['PermDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perm_detail = []
        if m.get('PermDetail') is not None:
            for k in m.get('PermDetail'):
                temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail()
                self.perm_detail.append(temp_model.from_map(k))
        return self


class ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermission(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        table_name: str = None,
        user_id: str = None,
        schema_name: str = None,
        logic: bool = None,
        user_nick_name: str = None,
        instance_id: str = None,
        perm_details: ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        env_type: str = None,
        column_name: str = None,
        db_type: str = None,
        ds_type: str = None,
        table_id: str = None,
        search_name: str = None,
        alias: str = None,
    ):
        self.db_id = db_id
        self.table_name = table_name
        self.user_id = user_id
        self.schema_name = schema_name
        self.logic = logic
        self.user_nick_name = user_nick_name
        self.instance_id = instance_id
        self.perm_details = perm_details
        self.env_type = env_type
        self.column_name = column_name
        self.db_type = db_type
        self.ds_type = ds_type
        self.table_id = table_id
        self.search_name = search_name
        self.alias = alias

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PermDetails') is not None:
            temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m['PermDetails'])
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class ListDatabaseUserPermssionsResponseBodyUserPermissions(TeaModel):
    def __init__(
        self,
        user_permission: List[ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermission] = None,
    ):
        self.user_permission = user_permission

    def validate(self):
        if self.user_permission:
            for k in self.user_permission:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserPermission'] = []
        if self.user_permission is not None:
            for k in self.user_permission:
                result['UserPermission'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_permission = []
        if m.get('UserPermission') is not None:
            for k in m.get('UserPermission'):
                temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermission()
                self.user_permission.append(temp_model.from_map(k))
        return self


class ListDatabaseUserPermssionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        user_permissions: ListDatabaseUserPermssionsResponseBodyUserPermissions = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.user_permissions = user_permissions
        self.success = success

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('UserPermissions') is not None:
            temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m['UserPermissions'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDatabaseUserPermssionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDatabaseUserPermssionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListDatabaseUserPermssionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveColumnsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        schema_name: str = None,
        table_name: str = None,
        column_name: str = None,
        security_level: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.schema_name = schema_name
        self.table_name = table_name
        self.column_name = column_name
        self.security_level = security_level
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        table_name: str = None,
        security_level: str = None,
        column_count: int = None,
        schema_name: str = None,
        function_type: str = None,
    ):
        self.column_name = column_name
        self.table_name = table_name
        self.security_level = security_level
        self.column_count = column_count
        self.schema_name = schema_name
        self.function_type = function_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        return self


class ListSensitiveColumnsResponseBodySensitiveColumnList(TeaModel):
    def __init__(
        self,
        sensitive_column: List[ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn] = None,
    ):
        self.sensitive_column = sensitive_column

    def validate(self):
        if self.sensitive_column:
            for k in self.sensitive_column:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SensitiveColumn'] = []
        if self.sensitive_column is not None:
            for k in self.sensitive_column:
                result['SensitiveColumn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_column = []
        if m.get('SensitiveColumn') is not None:
            for k in m.get('SensitiveColumn'):
                temp_model = ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn()
                self.sensitive_column.append(temp_model.from_map(k))
        return self


class ListSensitiveColumnsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        sensitive_column_list: ListSensitiveColumnsResponseBodySensitiveColumnList = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.sensitive_column_list = sensitive_column_list
        self.success = success

    def validate(self):
        if self.sensitive_column_list:
            self.sensitive_column_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.sensitive_column_list is not None:
            result['SensitiveColumnList'] = self.sensitive_column_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SensitiveColumnList') is not None:
            temp_model = ListSensitiveColumnsResponseBodySensitiveColumnList()
            self.sensitive_column_list = temp_model.from_map(m['SensitiveColumnList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSensitiveColumnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSensitiveColumnsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListSensitiveColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        role: str = None,
        user_state: str = None,
        search_key: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.role = role
        self.user_state = user_state
        self.search_key = search_key
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.role is not None:
            result['Role'] = self.role
        if self.user_state is not None:
            result['UserState'] = self.user_state
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBodyUserListUserRoleIdList(TeaModel):
    def __init__(
        self,
        role_ids: List[int] = None,
    ):
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        return self


class ListUsersResponseBodyUserListUserRoleNameList(TeaModel):
    def __init__(
        self,
        role_names: List[str] = None,
    ):
        self.role_names = role_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        return self


class ListUsersResponseBodyUserListUser(TeaModel):
    def __init__(
        self,
        state: str = None,
        cur_result_count: int = None,
        user_id: str = None,
        last_login_time: str = None,
        max_result_count: int = None,
        parent_uid: str = None,
        role_id_list: ListUsersResponseBodyUserListUserRoleIdList = None,
        role_name_list: ListUsersResponseBodyUserListUserRoleNameList = None,
        nick_name: str = None,
        max_execute_count: int = None,
        cur_execute_count: int = None,
        mobile: str = None,
        uid: str = None,
    ):
        self.state = state
        self.cur_result_count = cur_result_count
        self.user_id = user_id
        self.last_login_time = last_login_time
        self.max_result_count = max_result_count
        self.parent_uid = parent_uid
        self.role_id_list = role_id_list
        self.role_name_list = role_name_list
        self.nick_name = nick_name
        self.max_execute_count = max_execute_count
        self.cur_execute_count = cur_execute_count
        self.mobile = mobile
        self.uid = uid

    def validate(self):
        if self.role_id_list:
            self.role_id_list.validate()
        if self.role_name_list:
            self.role_name_list.validate()

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.cur_result_count is not None:
            result['CurResultCount'] = self.cur_result_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list.to_map()
        if self.role_name_list is not None:
            result['RoleNameList'] = self.role_name_list.to_map()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.cur_execute_count is not None:
            result['CurExecuteCount'] = self.cur_execute_count
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurResultCount') is not None:
            self.cur_result_count = m.get('CurResultCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('RoleIdList') is not None:
            temp_model = ListUsersResponseBodyUserListUserRoleIdList()
            self.role_id_list = temp_model.from_map(m['RoleIdList'])
        if m.get('RoleNameList') is not None:
            temp_model = ListUsersResponseBodyUserListUserRoleNameList()
            self.role_name_list = temp_model.from_map(m['RoleNameList'])
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('CurExecuteCount') is not None:
            self.cur_execute_count = m.get('CurExecuteCount')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListUsersResponseBodyUserList(TeaModel):
    def __init__(
        self,
        user: List[ListUsersResponseBodyUserListUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for k in self.user:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['User'] = []
        if self.user is not None:
            for k in self.user:
                result['User'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k in m.get('User'):
                temp_model = ListUsersResponseBodyUserListUser()
                self.user.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        user_list: ListUsersResponseBodyUserList = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.user_list = user_list
        self.success = success

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('UserList') is not None:
            temp_model = ListUsersResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitOrderApprovalRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
    ):
        self.tid = tid
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class SubmitOrderApprovalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitOrderApprovalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitOrderApprovalResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SubmitOrderApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantUserPermissionRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        user_id: str = None,
        ds_type: str = None,
        db_id: str = None,
        logic: bool = None,
        table_id: str = None,
        table_name: str = None,
        perm_types: str = None,
        expire_date: str = None,
    ):
        self.tid = tid
        self.user_id = user_id
        self.ds_type = ds_type
        self.db_id = db_id
        self.logic = logic
        self.table_id = table_id
        self.table_name = table_name
        self.perm_types = perm_types
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.perm_types is not None:
            result['PermTypes'] = self.perm_types
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PermTypes') is not None:
            self.perm_types = m.get('PermTypes')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        return self


class GrantUserPermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantUserPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantUserPermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GrantUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetaTableDetailInfoRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        table_guid: str = None,
    ):
        self.tid = tid
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfoIndexList(TeaModel):
    def __init__(
        self,
        index_columns: List[str] = None,
        index_name: str = None,
        unique: bool = None,
        index_type: str = None,
        index_id: str = None,
    ):
        self.index_columns = index_columns
        self.index_name = index_name
        self.unique = unique
        self.index_type = index_type
        self.index_id = index_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index_columns is not None:
            result['IndexColumns'] = self.index_columns
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.unique is not None:
            result['Unique'] = self.unique
        if self.index_type is not None:
            result['IndexType'] = self.index_type
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexColumns') is not None:
            self.index_columns = m.get('IndexColumns')
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('Unique') is not None:
            self.unique = m.get('Unique')
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfoColumnList(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        description: str = None,
        data_scale: int = None,
        data_precision: int = None,
        column_type: str = None,
        auto_increment: bool = None,
        position: str = None,
        nullable: bool = None,
        column_id: str = None,
        data_length: int = None,
    ):
        self.column_name = column_name
        self.description = description
        self.data_scale = data_scale
        self.data_precision = data_precision
        self.column_type = column_type
        self.auto_increment = auto_increment
        self.position = position
        self.nullable = nullable
        self.column_id = column_id
        self.data_length = data_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.description is not None:
            result['Description'] = self.description
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.position is not None:
            result['Position'] = self.position
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfo(TeaModel):
    def __init__(
        self,
        index_list: List[GetMetaTableDetailInfoResponseBodyDetailInfoIndexList] = None,
        column_list: List[GetMetaTableDetailInfoResponseBodyDetailInfoColumnList] = None,
    ):
        self.index_list = index_list
        self.column_list = column_list

    def validate(self):
        if self.index_list:
            for k in self.index_list:
                if k:
                    k.validate()
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IndexList'] = []
        if self.index_list is not None:
            for k in self.index_list:
                result['IndexList'].append(k.to_map() if k else None)
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index_list = []
        if m.get('IndexList') is not None:
            for k in m.get('IndexList'):
                temp_model = GetMetaTableDetailInfoResponseBodyDetailInfoIndexList()
                self.index_list.append(temp_model.from_map(k))
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k in m.get('ColumnList'):
                temp_model = GetMetaTableDetailInfoResponseBodyDetailInfoColumnList()
                self.column_list.append(temp_model.from_map(k))
        return self


class GetMetaTableDetailInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        detail_info: GetMetaTableDetailInfoResponseBodyDetailInfo = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.detail_info = detail_info
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DetailInfo') is not None:
            temp_model = GetMetaTableDetailInfoResponseBodyDetailInfo()
            self.detail_info = temp_model.from_map(m['DetailInfo'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMetaTableDetailInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetaTableDetailInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetMetaTableDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectSQLFileRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        order_action_name: str = None,
    ):
        self.order_id = order_id
        self.order_action_name = order_action_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_action_name is not None:
            result['OrderActionName'] = self.order_action_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderActionName') is not None:
            self.order_action_name = m.get('OrderActionName')
        return self


class GetDataCorrectSQLFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        file_url: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetDataCorrectSQLFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataCorrectSQLFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDataCorrectSQLFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        comment: str = None,
        plugin_param: Dict[str, Any] = None,
        related_user_list: str = None,
        plugin_type: str = None,
    ):
        self.tid = tid
        self.comment = comment
        self.plugin_param = plugin_param
        self.related_user_list = related_user_list
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.plugin_param is not None:
            result['PluginParam'] = self.plugin_param
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PluginParam') is not None:
            self.plugin_param = m.get('PluginParam')
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class CreateOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        comment: str = None,
        plugin_param_shrink: str = None,
        related_user_list: str = None,
        plugin_type: str = None,
    ):
        self.tid = tid
        self.comment = comment
        self.plugin_param_shrink = plugin_param_shrink
        self.related_user_list = related_user_list
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.plugin_param_shrink is not None:
            result['PluginParam'] = self.plugin_param_shrink
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PluginParam') is not None:
            self.plugin_param_shrink = m.get('PluginParam')
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        return self


class CreateOrderResponseBodyCreateOrderResult(TeaModel):
    def __init__(
        self,
        order_ids: List[int] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: CreateOrderResponseBodyCreateOrderResult = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.create_order_result:
            self.create_order_result.validate()

    def to_map(self):
        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            temp_model = CreateOrderResponseBodyCreateOrderResult()
            self.create_order_result = temp_model.from_map(m['CreateOrderResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class ListDatabasesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDatabasesResponseBodyDatabaseListDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class ListDatabasesResponseBodyDatabaseListDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListDatabasesResponseBodyDatabaseListDatabase(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        host: str = None,
        catalog_name: str = None,
        dba_name: str = None,
        state: str = None,
        dba_id: str = None,
        schema_name: str = None,
        instance_id: str = None,
        port: int = None,
        env_type: str = None,
        sid: str = None,
        owner_id_list: ListDatabasesResponseBodyDatabaseListDatabaseOwnerIdList = None,
        encoding: str = None,
        db_type: str = None,
        owner_name_list: ListDatabasesResponseBodyDatabaseListDatabaseOwnerNameList = None,
        search_name: str = None,
    ):
        self.database_id = database_id
        self.host = host
        self.catalog_name = catalog_name
        self.dba_name = dba_name
        self.state = state
        self.dba_id = dba_id
        self.schema_name = schema_name
        self.instance_id = instance_id
        self.port = port
        self.env_type = env_type
        self.sid = sid
        self.owner_id_list = owner_id_list
        self.encoding = encoding
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.search_name = search_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.host is not None:
            result['Host'] = self.host
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.dba_name is not None:
            result['DbaName'] = self.dba_name
        if self.state is not None:
            result['State'] = self.state
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('OwnerIdList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseListDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseListDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListDatabasesResponseBodyDatabaseList(TeaModel):
    def __init__(
        self,
        database: List[ListDatabasesResponseBodyDatabaseListDatabase] = None,
    ):
        self.database = database

    def validate(self):
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Database'] = []
        if self.database is not None:
            for k in self.database:
                result['Database'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k in m.get('Database'):
                temp_model = ListDatabasesResponseBodyDatabaseListDatabase()
                self.database.append(temp_model.from_map(k))
        return self


class ListDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        database_list: ListDatabasesResponseBodyDatabaseList = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.database_list = database_list
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.database_list:
            self.database_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.database_list is not None:
            result['DatabaseList'] = self.database_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DatabaseList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseList()
            self.database_list = temp_model.from_map(m['DatabaseList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPermissionsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        perm_type: str = None,
        user_id: str = None,
        database_name: str = None,
        logic: bool = None,
        env_type: str = None,
        db_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.perm_type = perm_type
        self.user_id = user_id
        self.database_name = database_name
        self.logic = logic
        self.env_type = env_type
        self.db_type = db_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(TeaModel):
    def __init__(
        self,
        origin_from: str = None,
        perm_type: str = None,
        expire_date: str = None,
        create_date: str = None,
        user_access_id: str = None,
        extra_data: str = None,
    ):
        self.origin_from = origin_from
        self.perm_type = perm_type
        self.expire_date = expire_date
        self.create_date = create_date
        self.user_access_id = user_access_id
        self.extra_data = extra_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        return self


class ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails(TeaModel):
    def __init__(
        self,
        perm_detail: List[ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail] = None,
    ):
        self.perm_detail = perm_detail

    def validate(self):
        if self.perm_detail:
            for k in self.perm_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PermDetail'] = []
        if self.perm_detail is not None:
            for k in self.perm_detail:
                result['PermDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perm_detail = []
        if m.get('PermDetail') is not None:
            for k in m.get('PermDetail'):
                temp_model = ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail()
                self.perm_detail.append(temp_model.from_map(k))
        return self


class ListUserPermissionsResponseBodyUserPermissionsUserPermission(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        table_name: str = None,
        user_id: str = None,
        schema_name: str = None,
        logic: bool = None,
        user_nick_name: str = None,
        instance_id: str = None,
        perm_details: ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        env_type: str = None,
        column_name: str = None,
        db_type: str = None,
        ds_type: str = None,
        table_id: str = None,
        search_name: str = None,
        alias: str = None,
    ):
        self.db_id = db_id
        self.table_name = table_name
        self.user_id = user_id
        self.schema_name = schema_name
        self.logic = logic
        self.user_nick_name = user_nick_name
        self.instance_id = instance_id
        self.perm_details = perm_details
        self.env_type = env_type
        self.column_name = column_name
        self.db_type = db_type
        self.ds_type = ds_type
        self.table_id = table_id
        self.search_name = search_name
        self.alias = alias

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PermDetails') is not None:
            temp_model = ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m['PermDetails'])
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class ListUserPermissionsResponseBodyUserPermissions(TeaModel):
    def __init__(
        self,
        user_permission: List[ListUserPermissionsResponseBodyUserPermissionsUserPermission] = None,
    ):
        self.user_permission = user_permission

    def validate(self):
        if self.user_permission:
            for k in self.user_permission:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UserPermission'] = []
        if self.user_permission is not None:
            for k in self.user_permission:
                result['UserPermission'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_permission = []
        if m.get('UserPermission') is not None:
            for k in m.get('UserPermission'):
                temp_model = ListUserPermissionsResponseBodyUserPermissionsUserPermission()
                self.user_permission.append(temp_model.from_map(k))
        return self


class ListUserPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        user_permissions: ListUserPermissionsResponseBodyUserPermissions = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.user_permissions = user_permissions
        self.success = success

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('UserPermissions') is not None:
            temp_model = ListUserPermissionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m['UserPermissions'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkFlowTemplatesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        search_name: str = None,
    ):
        self.tid = tid
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode(TeaModel):
    def __init__(
        self,
        comment: str = None,
        node_type: str = None,
        node_name: str = None,
        position: int = None,
        create_user_id: int = None,
        template_id: int = None,
        node_id: int = None,
    ):
        self.comment = comment
        self.node_type = node_type
        self.node_name = node_name
        self.position = position
        self.create_user_id = create_user_id
        self.template_id = template_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.position is not None:
            result['Position'] = self.position
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes(TeaModel):
    def __init__(
        self,
        workflow_node: List[ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode] = None,
    ):
        self.workflow_node = workflow_node

    def validate(self):
        if self.workflow_node:
            for k in self.workflow_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['WorkflowNode'] = []
        if self.workflow_node is not None:
            for k in self.workflow_node:
                result['WorkflowNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workflow_node = []
        if m.get('WorkflowNode') is not None:
            for k in m.get('WorkflowNode'):
                temp_model = ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k))
        return self


class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate(TeaModel):
    def __init__(
        self,
        is_system: int = None,
        workflow_nodes: ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes = None,
        comment: str = None,
        enabled: str = None,
        template_name: str = None,
        template_id: int = None,
        create_user_id: int = None,
    ):
        self.is_system = is_system
        self.workflow_nodes = workflow_nodes
        self.comment = comment
        self.enabled = enabled
        self.template_name = template_name
        self.template_id = template_id
        self.create_user_id = create_user_id

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        result = dict()
        if self.is_system is not None:
            result['IsSystem'] = self.is_system
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSystem') is not None:
            self.is_system = m.get('IsSystem')
        if m.get('WorkflowNodes') is not None:
            temp_model = ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        return self


class ListWorkFlowTemplatesResponseBodyWorkFlowTemplates(TeaModel):
    def __init__(
        self,
        work_flow_template: List[ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate] = None,
    ):
        self.work_flow_template = work_flow_template

    def validate(self):
        if self.work_flow_template:
            for k in self.work_flow_template:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['WorkFlowTemplate'] = []
        if self.work_flow_template is not None:
            for k in self.work_flow_template:
                result['WorkFlowTemplate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.work_flow_template = []
        if m.get('WorkFlowTemplate') is not None:
            for k in m.get('WorkFlowTemplate'):
                temp_model = ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate()
                self.work_flow_template.append(temp_model.from_map(k))
        return self


class ListWorkFlowTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        work_flow_templates: ListWorkFlowTemplatesResponseBodyWorkFlowTemplates = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.work_flow_templates = work_flow_templates

    def validate(self):
        if self.work_flow_templates:
            self.work_flow_templates.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.work_flow_templates is not None:
            result['WorkFlowTemplates'] = self.work_flow_templates.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WorkFlowTemplates') is not None:
            temp_model = ListWorkFlowTemplatesResponseBodyWorkFlowTemplates()
            self.work_flow_templates = temp_model.from_map(m['WorkFlowTemplates'])
        return self


class ListWorkFlowTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWorkFlowTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListWorkFlowTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataExportOrderDetailRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
    ):
        self.tid = tid
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo(TeaModel):
    def __init__(
        self,
        pre_check_id: int = None,
        job_status: str = None,
    ):
        self.pre_check_id = pre_check_id
        self.job_status = job_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pre_check_id is not None:
            result['PreCheckId'] = self.pre_check_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheckId') is not None:
            self.pre_check_id = m.get('PreCheckId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        return self


class GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        database: str = None,
        classify: str = None,
        exe_sql: str = None,
        logic: bool = None,
        actual_affect_rows: int = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        env_type: str = None,
    ):
        self.db_id = db_id
        self.database = database
        self.classify = classify
        self.exe_sql = exe_sql
        self.logic = logic
        self.actual_affect_rows = actual_affect_rows
        self.ignore_affect_rows = ignore_affect_rows
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        self.env_type = env_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.database is not None:
            result['Database'] = self.database
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows
        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')
        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class GetDataExportOrderDetailResponseBodyDataExportOrderDetail(TeaModel):
    def __init__(
        self,
        key_info: GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo = None,
        order_detail: GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail = None,
    ):
        self.key_info = key_info
        self.order_detail = order_detail

    def validate(self):
        if self.key_info:
            self.key_info.validate()
        if self.order_detail:
            self.order_detail.validate()

    def to_map(self):
        result = dict()
        if self.key_info is not None:
            result['KeyInfo'] = self.key_info.to_map()
        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyInfo') is not None:
            temp_model = GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo()
            self.key_info = temp_model.from_map(m['KeyInfo'])
        if m.get('OrderDetail') is not None:
            temp_model = GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail()
            self.order_detail = temp_model.from_map(m['OrderDetail'])
        return self


class GetDataExportOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_export_order_detail: GetDataExportOrderDetailResponseBodyDataExportOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data_export_order_detail = data_export_order_detail
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.data_export_order_detail:
            self.data_export_order_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_export_order_detail is not None:
            result['DataExportOrderDetail'] = self.data_export_order_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataExportOrderDetail') is not None:
            temp_model = GetDataExportOrderDetailResponseBodyDataExportOrderDetail()
            self.data_export_order_detail = temp_model.from_map(m['DataExportOrderDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataExportOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataExportOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDataExportOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        search_key: str = None,
        db_type: str = None,
        env_type: str = None,
        instance_source: str = None,
        net_type: str = None,
        instance_state: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.search_key = search_key
        self.db_type = db_type
        self.env_type = env_type
        self.instance_source = instance_source
        self.net_type = net_type
        self.instance_state = instance_state
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstancesResponseBodyInstanceListInstanceOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class ListInstancesResponseBodyInstanceListInstanceOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListInstancesResponseBodyInstanceListInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        database_user: str = None,
        dba_id: str = None,
        use_dsql: int = None,
        port: int = None,
        ecs_instance_id: str = None,
        env_type: str = None,
        sid: str = None,
        owner_id_list: ListInstancesResponseBodyInstanceListInstanceOwnerIdList = None,
        safe_rule_id: str = None,
        owner_name_list: ListInstancesResponseBodyInstanceListInstanceOwnerNameList = None,
        dba_nick_name: str = None,
        query_timeout: int = None,
        instance_source: str = None,
        host: str = None,
        state: str = None,
        data_link_name: str = None,
        export_timeout: int = None,
        instance_id: str = None,
        instance_type: str = None,
        database_password: str = None,
        instance_alias: str = None,
        ddl_online: int = None,
        ecs_region: str = None,
    ):
        self.vpc_id = vpc_id
        self.database_user = database_user
        self.dba_id = dba_id
        self.use_dsql = use_dsql
        self.port = port
        self.ecs_instance_id = ecs_instance_id
        self.env_type = env_type
        self.sid = sid
        self.owner_id_list = owner_id_list
        self.safe_rule_id = safe_rule_id
        self.owner_name_list = owner_name_list
        self.dba_nick_name = dba_nick_name
        self.query_timeout = query_timeout
        self.instance_source = instance_source
        self.host = host
        self.state = state
        self.data_link_name = data_link_name
        self.export_timeout = export_timeout
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.database_password = database_password
        self.instance_alias = instance_alias
        self.ddl_online = ddl_online
        self.ecs_region = ecs_region

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.port is not None:
            result['Port'] = self.port
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.host is not None:
            result['Host'] = self.host
        if self.state is not None:
            result['State'] = self.state
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('OwnerIdList') is not None:
            temp_model = ListInstancesResponseBodyInstanceListInstanceOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('OwnerNameList') is not None:
            temp_model = ListInstancesResponseBodyInstanceListInstanceOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        return self


class ListInstancesResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        instance: List[ListInstancesResponseBodyInstanceListInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListInstancesResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        instance_list: ListInstancesResponseBodyInstanceList = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.instance_list = instance_list
        self.success = success

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceList') is not None:
            temp_model = ListInstancesResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserUploadFileJobRequest(TeaModel):
    def __init__(
        self,
        job_key: str = None,
    ):
        self.job_key = job_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        return self


class GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        bucket_name: str = None,
        object_name: str = None,
    ):
        self.endpoint = endpoint
        self.bucket_name = bucket_name
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class GetUserUploadFileJobResponseBodyUploadFileJobDetail(TeaModel):
    def __init__(
        self,
        job_key: str = None,
        file_name: str = None,
        file_size: int = None,
        file_source: str = None,
        upload_type: str = None,
        upload_url: str = None,
        upload_ossparam: GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam = None,
        uploaded_size: int = None,
        job_status: str = None,
        job_status_desc: str = None,
        attachment_key: str = None,
    ):
        self.job_key = job_key
        self.file_name = file_name
        self.file_size = file_size
        self.file_source = file_source
        self.upload_type = upload_type
        self.upload_url = upload_url
        self.upload_ossparam = upload_ossparam
        self.uploaded_size = uploaded_size
        self.job_status = job_status
        self.job_status_desc = job_status_desc
        self.attachment_key = attachment_key

    def validate(self):
        if self.upload_ossparam:
            self.upload_ossparam.validate()

    def to_map(self):
        result = dict()
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        if self.upload_ossparam is not None:
            result['UploadOSSParam'] = self.upload_ossparam.to_map()
        if self.uploaded_size is not None:
            result['UploadedSize'] = self.uploaded_size
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.job_status_desc is not None:
            result['JobStatusDesc'] = self.job_status_desc
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        if m.get('UploadOSSParam') is not None:
            temp_model = GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam()
            self.upload_ossparam = temp_model.from_map(m['UploadOSSParam'])
        if m.get('UploadedSize') is not None:
            self.uploaded_size = m.get('UploadedSize')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('JobStatusDesc') is not None:
            self.job_status_desc = m.get('JobStatusDesc')
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        return self


class GetUserUploadFileJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        upload_file_job_detail: GetUserUploadFileJobResponseBodyUploadFileJobDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.upload_file_job_detail = upload_file_job_detail

    def validate(self):
        if self.upload_file_job_detail:
            self.upload_file_job_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.upload_file_job_detail is not None:
            result['UploadFileJobDetail'] = self.upload_file_job_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('UploadFileJobDetail') is not None:
            temp_model = GetUserUploadFileJobResponseBodyUploadFileJobDetail()
            self.upload_file_job_detail = temp_model.from_map(m['UploadFileJobDetail'])
        return self


class GetUserUploadFileJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserUploadFileJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetUserUploadFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncJobDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetStructSyncJobDetailResponseBodyStructSyncJobDetail(TeaModel):
    def __init__(
        self,
        job_status: str = None,
        message: str = None,
        table_analyzed: int = None,
        table_count: int = None,
        sql_count: int = None,
        execute_count: int = None,
        security_rule: str = None,
    ):
        self.job_status = job_status
        self.message = message
        self.table_analyzed = table_analyzed
        self.table_count = table_count
        self.sql_count = sql_count
        self.execute_count = execute_count
        self.security_rule = security_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.message is not None:
            result['Message'] = self.message
        if self.table_analyzed is not None:
            result['TableAnalyzed'] = self.table_analyzed
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count
        if self.security_rule is not None:
            result['SecurityRule'] = self.security_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TableAnalyzed') is not None:
            self.table_analyzed = m.get('TableAnalyzed')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')
        if m.get('SecurityRule') is not None:
            self.security_rule = m.get('SecurityRule')
        return self


class GetStructSyncJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        struct_sync_job_detail: GetStructSyncJobDetailResponseBodyStructSyncJobDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.struct_sync_job_detail = struct_sync_job_detail

    def validate(self):
        if self.struct_sync_job_detail:
            self.struct_sync_job_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.struct_sync_job_detail is not None:
            result['StructSyncJobDetail'] = self.struct_sync_job_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('StructSyncJobDetail') is not None:
            temp_model = GetStructSyncJobDetailResponseBodyStructSyncJobDetail()
            self.struct_sync_job_detail = temp_model.from_map(m['StructSyncJobDetail'])
        return self


class GetStructSyncJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStructSyncJobDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetStructSyncJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadOSSFileJobRequestUploadTarget(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        bucket_name: str = None,
        object_name: str = None,
    ):
        self.endpoint = endpoint
        self.bucket_name = bucket_name
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class CreateUploadOSSFileJobRequest(TeaModel):
    def __init__(
        self,
        file_source: str = None,
        file_name: str = None,
        upload_type: str = None,
        upload_target: CreateUploadOSSFileJobRequestUploadTarget = None,
    ):
        self.file_source = file_source
        self.file_name = file_name
        self.upload_type = upload_type
        self.upload_target = upload_target

    def validate(self):
        if self.upload_target:
            self.upload_target.validate()

    def to_map(self):
        result = dict()
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_target is not None:
            result['UploadTarget'] = self.upload_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadTarget') is not None:
            temp_model = CreateUploadOSSFileJobRequestUploadTarget()
            self.upload_target = temp_model.from_map(m['UploadTarget'])
        return self


class CreateUploadOSSFileJobShrinkRequest(TeaModel):
    def __init__(
        self,
        file_source: str = None,
        file_name: str = None,
        upload_type: str = None,
        upload_target_shrink: str = None,
    ):
        self.file_source = file_source
        self.file_name = file_name
        self.upload_type = upload_type
        self.upload_target_shrink = upload_target_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_target_shrink is not None:
            result['UploadTarget'] = self.upload_target_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadTarget') is not None:
            self.upload_target_shrink = m.get('UploadTarget')
        return self


class CreateUploadOSSFileJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        job_key: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.job_key = job_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        return self


class CreateUploadOSSFileJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUploadOSSFileJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateUploadOSSFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDatabaseRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        search_key: str = None,
        page_number: int = None,
        page_size: int = None,
        env_type: str = None,
        search_range: str = None,
        search_target: str = None,
        db_type: str = None,
    ):
        self.tid = tid
        self.search_key = search_key
        self.page_number = page_number
        self.page_size = page_size
        self.env_type = env_type
        self.search_range = search_range
        self.search_target = search_target
        self.db_type = db_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.search_range is not None:
            result['SearchRange'] = self.search_range
        if self.search_target is not None:
            result['SearchTarget'] = self.search_target
        if self.db_type is not None:
            result['DbType'] = self.db_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')
        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        return self


class SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class SearchDatabaseResponseBodySearchDatabaseListSearchDatabase(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        host: str = None,
        dba_id: str = None,
        schema_name: str = None,
        logic: bool = None,
        datalink_name: str = None,
        port: int = None,
        env_type: str = None,
        sid: str = None,
        owner_id_list: SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList = None,
        encoding: str = None,
        db_type: str = None,
        owner_name_list: SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList = None,
        search_name: str = None,
        alias: str = None,
    ):
        self.database_id = database_id
        self.host = host
        self.dba_id = dba_id
        self.schema_name = schema_name
        self.logic = logic
        self.datalink_name = datalink_name
        self.port = port
        self.env_type = env_type
        self.sid = sid
        self.owner_id_list = owner_id_list
        self.encoding = encoding
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.search_name = search_name
        self.alias = alias

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.host is not None:
            result['Host'] = self.host
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.datalink_name is not None:
            result['DatalinkName'] = self.datalink_name
        if self.port is not None:
            result['Port'] = self.port
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('DatalinkName') is not None:
            self.datalink_name = m.get('DatalinkName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('OwnerIdList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class SearchDatabaseResponseBodySearchDatabaseList(TeaModel):
    def __init__(
        self,
        search_database: List[SearchDatabaseResponseBodySearchDatabaseListSearchDatabase] = None,
    ):
        self.search_database = search_database

    def validate(self):
        if self.search_database:
            for k in self.search_database:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SearchDatabase'] = []
        if self.search_database is not None:
            for k in self.search_database:
                result['SearchDatabase'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_database = []
        if m.get('SearchDatabase') is not None:
            for k in m.get('SearchDatabase'):
                temp_model = SearchDatabaseResponseBodySearchDatabaseListSearchDatabase()
                self.search_database.append(temp_model.from_map(k))
        return self


class SearchDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        search_database_list: SearchDatabaseResponseBodySearchDatabaseList = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.search_database_list = search_database_list
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.search_database_list:
            self.search_database_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_database_list is not None:
            result['SearchDatabaseList'] = self.search_database_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchDatabaseList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseList()
            self.search_database_list = temp_model.from_map(m['SearchDatabaseList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SearchDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDatabaseMetaRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        db_id: str = None,
        logic: bool = None,
    ):
        self.tid = tid
        self.db_id = db_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class SyncDatabaseMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncDatabaseMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncDatabaseMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SyncDatabaseMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
        user_id: str = None,
    ):
        self.tid = tid
        self.uid = uid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUserRoleIdList(TeaModel):
    def __init__(
        self,
        role_ids: List[int] = None,
    ):
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        return self


class GetUserResponseBodyUserRoleNameList(TeaModel):
    def __init__(
        self,
        role_names: List[str] = None,
    ):
        self.role_names = role_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        state: str = None,
        cur_result_count: int = None,
        user_id: str = None,
        last_login_time: str = None,
        max_result_count: int = None,
        parent_uid: int = None,
        role_id_list: GetUserResponseBodyUserRoleIdList = None,
        role_name_list: GetUserResponseBodyUserRoleNameList = None,
        nick_name: str = None,
        max_execute_count: int = None,
        cur_execute_count: int = None,
        mobile: str = None,
        uid: str = None,
    ):
        self.state = state
        self.cur_result_count = cur_result_count
        self.user_id = user_id
        self.last_login_time = last_login_time
        self.max_result_count = max_result_count
        self.parent_uid = parent_uid
        self.role_id_list = role_id_list
        self.role_name_list = role_name_list
        self.nick_name = nick_name
        self.max_execute_count = max_execute_count
        self.cur_execute_count = cur_execute_count
        self.mobile = mobile
        self.uid = uid

    def validate(self):
        if self.role_id_list:
            self.role_id_list.validate()
        if self.role_name_list:
            self.role_name_list.validate()

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.cur_result_count is not None:
            result['CurResultCount'] = self.cur_result_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list.to_map()
        if self.role_name_list is not None:
            result['RoleNameList'] = self.role_name_list.to_map()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.cur_execute_count is not None:
            result['CurExecuteCount'] = self.cur_execute_count
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('CurResultCount') is not None:
            self.cur_result_count = m.get('CurResultCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('RoleIdList') is not None:
            temp_model = GetUserResponseBodyUserRoleIdList()
            self.role_id_list = temp_model.from_map(m['RoleIdList'])
        if m.get('RoleNameList') is not None:
            temp_model = GetUserResponseBodyUserRoleNameList()
            self.role_name_list = temp_model.from_map(m['RoleNameList'])
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('CurExecuteCount') is not None:
            self.cur_execute_count = m.get('CurExecuteCount')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        user: GetUserResponseBodyUser = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.user = user
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteStructSyncRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ExecuteStructSyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class ExecuteStructSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteStructSyncResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExecuteStructSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectOrderDetailRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
    ):
        self.tid = tid
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO(TeaModel):
    def __init__(
        self,
        user_tip: str = None,
        check_status: str = None,
        check_step: str = None,
    ):
        self.user_tip = user_tip
        self.check_status = check_status
        self.check_step = check_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_tip is not None:
            result['UserTip'] = self.user_tip
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_step is not None:
            result['CheckStep'] = self.check_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserTip') is not None:
            self.user_tip = m.get('UserTip')
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStep') is not None:
            self.check_step = m.get('CheckStep')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail(TeaModel):
    def __init__(
        self,
        task_check_do: List[GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO] = None,
    ):
        self.task_check_do = task_check_do

    def validate(self):
        if self.task_check_do:
            for k in self.task_check_do:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TaskCheckDO'] = []
        if self.task_check_do is not None:
            for k in self.task_check_do:
                result['TaskCheckDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_check_do = []
        if m.get('TaskCheckDO') is not None:
            for k in m.get('TaskCheckDO'):
                temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO()
                self.task_check_do.append(temp_model.from_map(k))
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail(TeaModel):
    def __init__(
        self,
        rb_sql: str = None,
        rb_attachment_name: str = None,
        classify: str = None,
        exe_sql: str = None,
        estimate_affect_rows: int = None,
        rb_sqltype: str = None,
        actual_affect_rows: int = None,
        ignore_affect_rows: bool = None,
        attachment_name: str = None,
        sql_type: str = None,
        ignore_affect_rows_reason: str = None,
    ):
        self.rb_sql = rb_sql
        self.rb_attachment_name = rb_attachment_name
        self.classify = classify
        self.exe_sql = exe_sql
        self.estimate_affect_rows = estimate_affect_rows
        self.rb_sqltype = rb_sqltype
        self.actual_affect_rows = actual_affect_rows
        self.ignore_affect_rows = ignore_affect_rows
        self.attachment_name = attachment_name
        self.sql_type = sql_type
        self.ignore_affect_rows_reason = ignore_affect_rows_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rb_sql is not None:
            result['RbSQL'] = self.rb_sql
        if self.rb_attachment_name is not None:
            result['RbAttachmentName'] = self.rb_attachment_name
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql
        if self.estimate_affect_rows is not None:
            result['EstimateAffectRows'] = self.estimate_affect_rows
        if self.rb_sqltype is not None:
            result['RbSQLType'] = self.rb_sqltype
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RbSQL') is not None:
            self.rb_sql = m.get('RbSQL')
        if m.get('RbAttachmentName') is not None:
            self.rb_attachment_name = m.get('RbAttachmentName')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')
        if m.get('EstimateAffectRows') is not None:
            self.estimate_affect_rows = m.get('EstimateAffectRows')
        if m.get('RbSQLType') is not None:
            self.rb_sqltype = m.get('RbSQLType')
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        logic: bool = None,
        search_name: str = None,
        env_type: str = None,
    ):
        self.db_id = db_id
        self.db_type = db_type
        self.logic = logic
        self.search_name = search_name
        self.env_type = env_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList(TeaModel):
    def __init__(
        self,
        database: List[GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase] = None,
    ):
        self.database = database

    def validate(self):
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Database'] = []
        if self.database is not None:
            for k in self.database:
                result['Database'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k in m.get('Database'):
                temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase()
                self.database.append(temp_model.from_map(k))
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail(TeaModel):
    def __init__(
        self,
        pre_check_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail = None,
        order_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail = None,
        database_list: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList = None,
    ):
        self.pre_check_detail = pre_check_detail
        self.order_detail = order_detail
        self.database_list = database_list

    def validate(self):
        if self.pre_check_detail:
            self.pre_check_detail.validate()
        if self.order_detail:
            self.order_detail.validate()
        if self.database_list:
            self.database_list.validate()

    def to_map(self):
        result = dict()
        if self.pre_check_detail is not None:
            result['PreCheckDetail'] = self.pre_check_detail.to_map()
        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()
        if self.database_list is not None:
            result['DatabaseList'] = self.database_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheckDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail()
            self.pre_check_detail = temp_model.from_map(m['PreCheckDetail'])
        if m.get('OrderDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail()
            self.order_detail = temp_model.from_map(m['OrderDetail'])
        if m.get('DatabaseList') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList()
            self.database_list = temp_model.from_map(m['DatabaseList'])
        return self


class GetDataCorrectOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data_correct_order_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.data_correct_order_detail = data_correct_order_detail
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.data_correct_order_detail:
            self.data_correct_order_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data_correct_order_detail is not None:
            result['DataCorrectOrderDetail'] = self.data_correct_order_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DataCorrectOrderDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail()
            self.data_correct_order_detail = temp_model.from_map(m['DataCorrectOrderDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataCorrectOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataCorrectOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDataCorrectOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListColumnsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        table_id: str = None,
        logic: bool = None,
    ):
        self.tid = tid
        self.table_id = table_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class ListColumnsResponseBodyColumnListColumn(TeaModel):
    def __init__(
        self,
        column_type: str = None,
        auto_increment: bool = None,
        column_id: str = None,
        default_value: str = None,
        sensitive: bool = None,
        column_name: str = None,
        security_level: str = None,
        description: str = None,
        data_precision: int = None,
        data_scale: int = None,
        function_type: str = None,
        nullable: bool = None,
        data_length: int = None,
    ):
        self.column_type = column_type
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.default_value = default_value
        self.sensitive = sensitive
        self.column_name = column_name
        self.security_level = security_level
        self.description = description
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.function_type = function_type
        self.nullable = nullable
        self.data_length = data_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.description is not None:
            result['Description'] = self.description
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        return self


class ListColumnsResponseBodyColumnList(TeaModel):
    def __init__(
        self,
        column: List[ListColumnsResponseBodyColumnListColumn] = None,
    ):
        self.column = column

    def validate(self):
        if self.column:
            for k in self.column:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Column'] = []
        if self.column is not None:
            for k in self.column:
                result['Column'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column = []
        if m.get('Column') is not None:
            for k in m.get('Column'):
                temp_model = ListColumnsResponseBodyColumnListColumn()
                self.column.append(temp_model.from_map(k))
        return self


class ListColumnsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        column_list: ListColumnsResponseBodyColumnList = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.column_list = column_list
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.column_list:
            self.column_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.column_list is not None:
            result['ColumnList'] = self.column_list.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ColumnList') is not None:
            temp_model = ListColumnsResponseBodyColumnList()
            self.column_list = temp_model.from_map(m['ColumnList'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListColumnsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListColumnsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeUserPermissionRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        user_id: str = None,
        ds_type: str = None,
        db_id: str = None,
        logic: bool = None,
        table_id: str = None,
        table_name: str = None,
        perm_types: str = None,
        user_access_id: str = None,
    ):
        self.tid = tid
        self.user_id = user_id
        self.ds_type = ds_type
        self.db_id = db_id
        self.logic = logic
        self.table_id = table_id
        self.table_name = table_name
        self.perm_types = perm_types
        self.user_access_id = user_access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.perm_types is not None:
            result['PermTypes'] = self.perm_types
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PermTypes') is not None:
            self.perm_types = m.get('PermTypes')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
        return self


class RevokeUserPermissionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeUserPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokeUserPermissionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RevokeUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetaTableColumnRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        table_guid: str = None,
    ):
        self.tid = tid
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        return self


class GetMetaTableColumnResponseBodyColumnList(TeaModel):
    def __init__(
        self,
        column_type: str = None,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        security_level: str = None,
        primary_key: str = None,
        description: str = None,
        data_precision: int = None,
        data_scale: int = None,
        position: int = None,
        nullable: bool = None,
        data_length: int = None,
    ):
        self.column_type = column_type
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.column_name = column_name
        self.security_level = security_level
        self.primary_key = primary_key
        self.description = description
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.position = position
        self.nullable = nullable
        self.data_length = data_length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.description is not None:
            result['Description'] = self.description
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.position is not None:
            result['Position'] = self.position
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        return self


class GetMetaTableColumnResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        column_list: List[GetMetaTableColumnResponseBodyColumnList] = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.column_list = column_list
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k in m.get('ColumnList'):
                temp_model = GetMetaTableColumnResponseBodyColumnList()
                self.column_list.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMetaTableColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetaTableColumnResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetMetaTableColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        self.tid = tid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class EnableUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = EnableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        instance_type: str = None,
        instance_source: str = None,
        env_type: str = None,
        ecs_instance_id: str = None,
        vpc_id: str = None,
        ecs_region: str = None,
        host: str = None,
        port: int = None,
        sid: str = None,
        database_user: str = None,
        database_password: str = None,
        instance_alias: str = None,
        dba_id: str = None,
        safe_rule_id: str = None,
        query_timeout: int = None,
        export_timeout: int = None,
        data_link_name: str = None,
        ddl_online: int = None,
        use_dsql: int = None,
        instance_id: str = None,
        skip_test: bool = None,
    ):
        self.tid = tid
        self.instance_type = instance_type
        self.instance_source = instance_source
        self.env_type = env_type
        self.ecs_instance_id = ecs_instance_id
        self.vpc_id = vpc_id
        self.ecs_region = ecs_region
        self.host = host
        self.port = port
        self.sid = sid
        self.database_user = database_user
        self.database_password = database_password
        self.instance_alias = instance_alias
        self.dba_id = dba_id
        self.safe_rule_id = safe_rule_id
        self.query_timeout = query_timeout
        self.export_timeout = export_timeout
        self.data_link_name = data_link_name
        self.ddl_online = ddl_online
        self.use_dsql = use_dsql
        self.instance_id = instance_id
        self.skip_test = skip_test

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skip_test is not None:
            result['SkipTest'] = self.skip_test
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkipTest') is not None:
            self.skip_test = m.get('SkipTest')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteScriptRequest(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        script: str = None,
        logic: bool = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.script = script
        self.logic = logic
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.script is not None:
            result['Script'] = self.script
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteScriptResponseBodyResults(TeaModel):
    def __init__(
        self,
        column_names: List[str] = None,
        rows: List[Dict[str, Any]] = None,
        success: bool = None,
        message: str = None,
        row_count: int = None,
    ):
        self.column_names = column_names
        self.rows = rows
        self.success = success
        self.message = message
        self.row_count = row_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        return self


class ExecuteScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ExecuteScriptResponseBodyResults] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.results = results
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ExecuteScriptResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExecuteScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDBTaskSQLJobDetailRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList(TeaModel):
    def __init__(
        self,
        job_detail_id: int = None,
        current_sql: str = None,
        execute_count: int = None,
        job_id: int = None,
        db_id: int = None,
        logic: bool = None,
        skip: bool = None,
        sql_type: str = None,
        status: str = None,
    ):
        self.job_detail_id = job_detail_id
        self.current_sql = current_sql
        self.execute_count = execute_count
        self.job_id = job_id
        self.db_id = db_id
        self.logic = logic
        self.skip = skip
        self.sql_type = sql_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_detail_id is not None:
            result['JobDetailId'] = self.job_detail_id
        if self.current_sql is not None:
            result['CurrentSql'] = self.current_sql
        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobDetailId') is not None:
            self.job_detail_id = m.get('JobDetailId')
        if m.get('CurrentSql') is not None:
            self.current_sql = m.get('CurrentSql')
        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDBTaskSQLJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        dbtask_sqljob_detail_list: List[ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.dbtask_sqljob_detail_list = dbtask_sqljob_detail_list
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_detail_list:
            for k in self.dbtask_sqljob_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['DBTaskSQLJobDetailList'] = []
        if self.dbtask_sqljob_detail_list is not None:
            for k in self.dbtask_sqljob_detail_list:
                result['DBTaskSQLJobDetailList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.dbtask_sqljob_detail_list = []
        if m.get('DBTaskSQLJobDetailList') is not None:
            for k in m.get('DBTaskSQLJobDetailList'):
                temp_model = ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList()
                self.dbtask_sqljob_detail_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDBTaskSQLJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDBTaskSQLJobDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListDBTaskSQLJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        self.tid = tid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DisableUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DisableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApprovalDetailRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        workflow_instance_id: int = None,
    ):
        self.tid = tid
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList(TeaModel):
    def __init__(
        self,
        audit_user_ids: List[str] = None,
    ):
        self.audit_user_ids = audit_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.audit_user_ids is not None:
            result['AuditUserIds'] = self.audit_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUserIds') is not None:
            self.audit_user_ids = m.get('AuditUserIds')
        return self


class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode(TeaModel):
    def __init__(
        self,
        operate_time: str = None,
        operator_id: int = None,
        node_name: str = None,
        audit_user_id_list: GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList = None,
        operate_comment: str = None,
        workflow_ins_code: str = None,
    ):
        self.operate_time = operate_time
        self.operator_id = operator_id
        self.node_name = node_name
        self.audit_user_id_list = audit_user_id_list
        self.operate_comment = operate_comment
        self.workflow_ins_code = workflow_ins_code

    def validate(self):
        if self.audit_user_id_list:
            self.audit_user_id_list.validate()

    def to_map(self):
        result = dict()
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.audit_user_id_list is not None:
            result['AuditUserIdList'] = self.audit_user_id_list.to_map()
        if self.operate_comment is not None:
            result['OperateComment'] = self.operate_comment
        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AuditUserIdList') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList()
            self.audit_user_id_list = temp_model.from_map(m['AuditUserIdList'])
        if m.get('OperateComment') is not None:
            self.operate_comment = m.get('OperateComment')
        if m.get('WorkflowInsCode') is not None:
            self.workflow_ins_code = m.get('WorkflowInsCode')
        return self


class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes(TeaModel):
    def __init__(
        self,
        workflow_node: List[GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode] = None,
    ):
        self.workflow_node = workflow_node

    def validate(self):
        if self.workflow_node:
            for k in self.workflow_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['WorkflowNode'] = []
        if self.workflow_node is not None:
            for k in self.workflow_node:
                result['WorkflowNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workflow_node = []
        if m.get('WorkflowNode') is not None:
            for k in m.get('WorkflowNode'):
                temp_model = GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k))
        return self


class GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        id: int = None,
    ):
        self.nick_name = nick_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers(TeaModel):
    def __init__(
        self,
        current_handler: List[GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler] = None,
    ):
        self.current_handler = current_handler

    def validate(self):
        if self.current_handler:
            for k in self.current_handler:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CurrentHandler'] = []
        if self.current_handler is not None:
            for k in self.current_handler:
                result['CurrentHandler'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_handler = []
        if m.get('CurrentHandler') is not None:
            for k in m.get('CurrentHandler'):
                temp_model = GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler()
                self.current_handler.append(temp_model.from_map(k))
        return self


class GetApprovalDetailResponseBodyApprovalDetailReasonList(TeaModel):
    def __init__(
        self,
        reasons: List[str] = None,
    ):
        self.reasons = reasons

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.reasons is not None:
            result['Reasons'] = self.reasons
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reasons') is not None:
            self.reasons = m.get('Reasons')
        return self


class GetApprovalDetailResponseBodyApprovalDetail(TeaModel):
    def __init__(
        self,
        workflow_nodes: GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes = None,
        description: str = None,
        current_handlers: GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers = None,
        order_type: str = None,
        title: str = None,
        audit_id: int = None,
        order_id: int = None,
        workflow_ins_code: str = None,
        reason_list: GetApprovalDetailResponseBodyApprovalDetailReasonList = None,
    ):
        self.workflow_nodes = workflow_nodes
        self.description = description
        self.current_handlers = current_handlers
        self.order_type = order_type
        self.title = title
        self.audit_id = audit_id
        self.order_id = order_id
        self.workflow_ins_code = workflow_ins_code
        self.reason_list = reason_list

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()
        if self.current_handlers:
            self.current_handlers.validate()
        if self.reason_list:
            self.reason_list.validate()

    def to_map(self):
        result = dict()
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.current_handlers is not None:
            result['CurrentHandlers'] = self.current_handlers.to_map()
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.title is not None:
            result['Title'] = self.title
        if self.audit_id is not None:
            result['AuditId'] = self.audit_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code
        if self.reason_list is not None:
            result['ReasonList'] = self.reason_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkflowNodes') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CurrentHandlers') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers()
            self.current_handlers = temp_model.from_map(m['CurrentHandlers'])
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('AuditId') is not None:
            self.audit_id = m.get('AuditId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('WorkflowInsCode') is not None:
            self.workflow_ins_code = m.get('WorkflowInsCode')
        if m.get('ReasonList') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailReasonList()
            self.reason_list = temp_model.from_map(m['ReasonList'])
        return self


class GetApprovalDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        approval_detail: GetApprovalDetailResponseBodyApprovalDetail = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.approval_detail = approval_detail
        self.success = success

    def validate(self):
        if self.approval_detail:
            self.approval_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ApprovalDetail') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetail()
            self.approval_detail = temp_model.from_map(m['ApprovalDetail'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetApprovalDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetApprovalDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetApprovalDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserActiveTenantResponseBodyTenant(TeaModel):
    def __init__(
        self,
        status: str = None,
        tid: int = None,
        tenant_name: str = None,
    ):
        self.status = status
        self.tid = tid
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class GetUserActiveTenantResponseBody(TeaModel):
    def __init__(
        self,
        tenant: GetUserActiveTenantResponseBodyTenant = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.tenant = tenant
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        result = dict()
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tenant') is not None:
            temp_model = GetUserActiveTenantResponseBodyTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserActiveTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserActiveTenantResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetUserActiveTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
        user_nick: str = None,
        role_names: str = None,
        mobile: str = None,
    ):
        self.tid = tid
        self.uid = uid
        self.user_nick = user_nick
        self.role_names = role_names
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class RegisterUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RegisterUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RegisterUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        host: str = None,
        port: int = None,
        sid: str = None,
    ):
        self.tid = tid
        self.host = host
        self.port = port
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        return self


class GetInstanceResponseBodyInstanceOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class GetInstanceResponseBodyInstanceOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        database_user: str = None,
        dba_id: str = None,
        use_dsql: int = None,
        port: int = None,
        ecs_instance_id: str = None,
        env_type: str = None,
        sid: str = None,
        owner_id_list: GetInstanceResponseBodyInstanceOwnerIdList = None,
        safe_rule_id: str = None,
        owner_name_list: GetInstanceResponseBodyInstanceOwnerNameList = None,
        dba_nick_name: str = None,
        query_timeout: int = None,
        instance_source: str = None,
        host: str = None,
        state: str = None,
        data_link_name: str = None,
        export_timeout: int = None,
        instance_id: str = None,
        instance_type: str = None,
        database_password: str = None,
        instance_alias: str = None,
        ddl_online: int = None,
        ecs_region: str = None,
    ):
        self.vpc_id = vpc_id
        self.database_user = database_user
        self.dba_id = dba_id
        self.use_dsql = use_dsql
        self.port = port
        self.ecs_instance_id = ecs_instance_id
        self.env_type = env_type
        self.sid = sid
        self.owner_id_list = owner_id_list
        self.safe_rule_id = safe_rule_id
        self.owner_name_list = owner_name_list
        self.dba_nick_name = dba_nick_name
        self.query_timeout = query_timeout
        self.instance_source = instance_source
        self.host = host
        self.state = state
        self.data_link_name = data_link_name
        self.export_timeout = export_timeout
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.database_password = database_password
        self.instance_alias = instance_alias
        self.ddl_online = ddl_online
        self.ecs_region = ecs_region

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.port is not None:
            result['Port'] = self.port
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.host is not None:
            result['Host'] = self.host
        if self.state is not None:
            result['State'] = self.state
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('OwnerIdList') is not None:
            temp_model = GetInstanceResponseBodyInstanceOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('OwnerNameList') is not None:
            temp_model = GetInstanceResponseBodyInstanceOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance: GetInstanceResponseBodyInstance = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.instance = instance
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermApplyOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        db_type: str = None,
        search_name: str = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        env_type: str = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.db_type = db_type
        self.search_name = search_name
        self.owner_ids = owner_ids
        self.owner_nick_names = owner_nick_names
        self.env_type = env_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        column_name: str = None,
    ):
        self.table_name = table_name
        self.column_name = column_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        search_name: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        port: int = None,
        owner_ids: List[int] = None,
        owner_nick_name: List[str] = None,
        dba_id: int = None,
        dba_nick_name: str = None,
    ):
        self.instance_id = instance_id
        self.search_name = search_name
        self.db_type = db_type
        self.env_type = env_type
        self.host = host
        self.port = port
        self.owner_ids = owner_ids
        self.owner_nick_name = owner_nick_name
        self.dba_id = dba_id
        self.dba_nick_name = dba_nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources(TeaModel):
    def __init__(
        self,
        database_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo = None,
        table_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo = None,
        column_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo = None,
        instance_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo = None,
    ):
        self.database_info = database_info
        self.table_info = table_info
        self.column_info = column_info
        self.instance_info = instance_info

    def validate(self):
        if self.database_info:
            self.database_info.validate()
        if self.table_info:
            self.table_info.validate()
        if self.column_info:
            self.column_info.validate()
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        result = dict()
        if self.database_info is not None:
            result['DatabaseInfo'] = self.database_info.to_map()
        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()
        if self.column_info is not None:
            result['ColumnInfo'] = self.column_info.to_map()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo()
            self.database_info = temp_model.from_map(m['DatabaseInfo'])
        if m.get('TableInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo()
            self.table_info = temp_model.from_map(m['TableInfo'])
        if m.get('ColumnInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo()
            self.column_info = temp_model.from_map(m['ColumnInfo'])
        if m.get('InstanceInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail(TeaModel):
    def __init__(
        self,
        resources: List[GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources] = None,
        perm_type: int = None,
        seconds: int = None,
        apply_type: str = None,
    ):
        self.resources = resources
        self.perm_type = perm_type
        self.seconds = seconds
        self.apply_type = apply_type

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.seconds is not None:
            result['Seconds'] = self.seconds
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('Seconds') is not None:
            self.seconds = m.get('Seconds')
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        return self


class GetPermApplyOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        perm_apply_order_detail: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.perm_apply_order_detail = perm_apply_order_detail

    def validate(self):
        if self.perm_apply_order_detail:
            self.perm_apply_order_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.perm_apply_order_detail is not None:
            result['PermApplyOrderDetail'] = self.perm_apply_order_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('PermApplyOrderDetail') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail()
            self.perm_apply_order_detail = temp_model.from_map(m['PermApplyOrderDetail'])
        return self


class GetPermApplyOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPermApplyOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetPermApplyOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        table_id: str = None,
        logic: bool = None,
    ):
        self.tid = tid
        self.table_id = table_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class ListIndexesResponseBodyIndexListIndex(TeaModel):
    def __init__(
        self,
        index_name: str = None,
        index_type: str = None,
        table_id: str = None,
        index_id: str = None,
        index_comment: str = None,
    ):
        self.index_name = index_name
        self.index_type = index_type
        self.table_id = table_id
        self.index_id = index_id
        self.index_comment = index_comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_type is not None:
            result['IndexType'] = self.index_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.index_comment is not None:
            result['IndexComment'] = self.index_comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IndexComment') is not None:
            self.index_comment = m.get('IndexComment')
        return self


class ListIndexesResponseBodyIndexList(TeaModel):
    def __init__(
        self,
        index: List[ListIndexesResponseBodyIndexListIndex] = None,
    ):
        self.index = index

    def validate(self):
        if self.index:
            for k in self.index:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Index'] = []
        if self.index is not None:
            for k in self.index:
                result['Index'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.index = []
        if m.get('Index') is not None:
            for k in m.get('Index'):
                temp_model = ListIndexesResponseBodyIndexListIndex()
                self.index.append(temp_model.from_map(k))
        return self


class ListIndexesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        index_list: ListIndexesResponseBodyIndexList = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.index_list = index_list
        self.success = success

    def validate(self):
        if self.index_list:
            self.index_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.index_list is not None:
            result['IndexList'] = self.index_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IndexList') is not None:
            temp_model = ListIndexesResponseBodyIndexList()
            self.index_list = temp_model.from_map(m['IndexList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIndexesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIndexesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListIndexesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogicTablesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        database_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        return_guid: bool = None,
    ):
        self.tid = tid
        self.database_id = database_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_name = search_name
        self.return_guid = return_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        return self


class ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListLogicTablesResponseBodyLogicTableListLogicTable(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        table_name: str = None,
        table_count: str = None,
        owner_id_list: ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList = None,
        owner_name_list: ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList = None,
        schema_name: str = None,
        logic: bool = None,
        table_expr: str = None,
        table_guid: str = None,
        table_id: str = None,
    ):
        self.database_id = database_id
        self.table_name = table_name
        self.table_count = table_count
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.schema_name = schema_name
        self.logic = logic
        self.table_expr = table_expr
        self.table_guid = table_guid
        self.table_id = table_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_expr is not None:
            result['TableExpr'] = self.table_expr
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        if m.get('OwnerIdList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableExpr') is not None:
            self.table_expr = m.get('TableExpr')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class ListLogicTablesResponseBodyLogicTableList(TeaModel):
    def __init__(
        self,
        logic_table: List[ListLogicTablesResponseBodyLogicTableListLogicTable] = None,
    ):
        self.logic_table = logic_table

    def validate(self):
        if self.logic_table:
            for k in self.logic_table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LogicTable'] = []
        if self.logic_table is not None:
            for k in self.logic_table:
                result['LogicTable'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_table = []
        if m.get('LogicTable') is not None:
            for k in m.get('LogicTable'):
                temp_model = ListLogicTablesResponseBodyLogicTableListLogicTable()
                self.logic_table.append(temp_model.from_map(k))
        return self


class ListLogicTablesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        logic_table_list: ListLogicTablesResponseBodyLogicTableList = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.logic_table_list = logic_table_list
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.logic_table_list:
            self.logic_table_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logic_table_list is not None:
            result['LogicTableList'] = self.logic_table_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogicTableList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableList()
            self.logic_table_list = temp_model.from_map(m['LogicTableList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLogicTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogicTablesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListLogicTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataExportDownloadURLRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        action_name: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        return self


class GetDataExportDownloadURLResponseBodyDownloadURLResult(TeaModel):
    def __init__(
        self,
        has_result: bool = None,
        tip_message: str = None,
        url: str = None,
    ):
        self.has_result = has_result
        self.tip_message = tip_message
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.has_result is not None:
            result['HasResult'] = self.has_result
        if self.tip_message is not None:
            result['TipMessage'] = self.tip_message
        if self.url is not None:
            result['URL'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasResult') is not None:
            self.has_result = m.get('HasResult')
        if m.get('TipMessage') is not None:
            self.tip_message = m.get('TipMessage')
        if m.get('URL') is not None:
            self.url = m.get('URL')
        return self


class GetDataExportDownloadURLResponseBody(TeaModel):
    def __init__(
        self,
        download_urlresult: GetDataExportDownloadURLResponseBodyDownloadURLResult = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.download_urlresult = download_urlresult
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.download_urlresult:
            self.download_urlresult.validate()

    def to_map(self):
        result = dict()
        if self.download_urlresult is not None:
            result['DownloadURLResult'] = self.download_urlresult.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadURLResult') is not None:
            temp_model = GetDataExportDownloadURLResponseBodyDownloadURLResult()
            self.download_urlresult = temp_model.from_map(m['DownloadURLResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataExportDownloadURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataExportDownloadURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDataExportDownloadURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishGroupTaskRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        db_id: int = None,
        logic: bool = None,
        publish_strategy: str = None,
        plan_time: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.db_id = db_id
        self.logic = logic
        self.publish_strategy = publish_strategy
        self.plan_time = plan_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.publish_strategy is not None:
            result['PublishStrategy'] = self.publish_strategy
        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PublishStrategy') is not None:
            self.publish_strategy = m.get('PublishStrategy')
        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')
        return self


class CreatePublishGroupTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePublishGroupTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePublishGroupTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreatePublishGroupTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        host: str = None,
        port: int = None,
        sid: str = None,
        schema_name: str = None,
    ):
        self.tid = tid
        self.host = host
        self.port = port
        self.sid = sid
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        return self


class GetDatabaseResponseBodyDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class GetDatabaseResponseBodyDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class GetDatabaseResponseBodyDatabase(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        host: str = None,
        catalog_name: str = None,
        dba_name: str = None,
        state: str = None,
        dba_id: str = None,
        schema_name: str = None,
        instance_id: str = None,
        port: int = None,
        env_type: str = None,
        sid: str = None,
        owner_id_list: GetDatabaseResponseBodyDatabaseOwnerIdList = None,
        encoding: str = None,
        db_type: str = None,
        owner_name_list: GetDatabaseResponseBodyDatabaseOwnerNameList = None,
        search_name: str = None,
    ):
        self.database_id = database_id
        self.host = host
        self.catalog_name = catalog_name
        self.dba_name = dba_name
        self.state = state
        self.dba_id = dba_id
        self.schema_name = schema_name
        self.instance_id = instance_id
        self.port = port
        self.env_type = env_type
        self.sid = sid
        self.owner_id_list = owner_id_list
        self.encoding = encoding
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.search_name = search_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.host is not None:
            result['Host'] = self.host
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.dba_name is not None:
            result['DbaName'] = self.dba_name
        if self.state is not None:
            result['State'] = self.state
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('OwnerIdList') is not None:
            temp_model = GetDatabaseResponseBodyDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = GetDatabaseResponseBodyDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        database: GetDatabaseResponseBodyDatabase = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.database = database
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Database') is not None:
            temp_model = GetDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOwnerApplyOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail(TeaModel):
    def __init__(
        self,
        search_name: str = None,
        db_type: str = None,
        env_type: str = None,
        table_name: str = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
    ):
        self.search_name = search_name
        self.db_type = db_type
        self.env_type = env_type
        self.table_name = table_name
        self.owner_ids = owner_ids
        self.owner_nick_names = owner_nick_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')
        return self


class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources(TeaModel):
    def __init__(
        self,
        logic: bool = None,
        target_id: str = None,
        resource_detail: GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail = None,
    ):
        self.logic = logic
        self.target_id = target_id
        self.resource_detail = resource_detail

    def validate(self):
        if self.resource_detail:
            self.resource_detail.validate()

    def to_map(self):
        result = dict()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.resource_detail is not None:
            result['ResourceDetail'] = self.resource_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('ResourceDetail') is not None:
            temp_model = GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail()
            self.resource_detail = temp_model.from_map(m['ResourceDetail'])
        return self


class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail(TeaModel):
    def __init__(
        self,
        apply_type: str = None,
        resources: List[GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources] = None,
    ):
        self.apply_type = apply_type
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources()
                self.resources.append(temp_model.from_map(k))
        return self


class GetOwnerApplyOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        owner_apply_order_detail: GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.owner_apply_order_detail = owner_apply_order_detail

    def validate(self):
        if self.owner_apply_order_detail:
            self.owner_apply_order_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.owner_apply_order_detail is not None:
            result['OwnerApplyOrderDetail'] = self.owner_apply_order_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OwnerApplyOrderDetail') is not None:
            temp_model = GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail()
            self.owner_apply_order_detail = temp_model.from_map(m['OwnerApplyOrderDetail'])
        return self


class GetOwnerApplyOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOwnerApplyOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetOwnerApplyOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpLogRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        module: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.tid = tid
        self.module = module
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.module is not None:
            result['Module'] = self.module
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class GetOpLogResponseBodyOpLogDetailsOpLogDetail(TeaModel):
    def __init__(
        self,
        module: str = None,
        database: str = None,
        user_id: int = None,
        op_content: str = None,
        user_nick: str = None,
        order_id: int = None,
        op_time: str = None,
    ):
        self.module = module
        self.database = database
        self.user_id = user_id
        self.op_content = op_content
        self.user_nick = user_nick
        self.order_id = order_id
        self.op_time = op_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module is not None:
            result['Module'] = self.module
        if self.database is not None:
            result['Database'] = self.database
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.op_content is not None:
            result['OpContent'] = self.op_content
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.op_time is not None:
            result['OpTime'] = self.op_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('OpContent') is not None:
            self.op_content = m.get('OpContent')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')
        return self


class GetOpLogResponseBodyOpLogDetails(TeaModel):
    def __init__(
        self,
        op_log_detail: List[GetOpLogResponseBodyOpLogDetailsOpLogDetail] = None,
    ):
        self.op_log_detail = op_log_detail

    def validate(self):
        if self.op_log_detail:
            for k in self.op_log_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['OpLogDetail'] = []
        if self.op_log_detail is not None:
            for k in self.op_log_detail:
                result['OpLogDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.op_log_detail = []
        if m.get('OpLogDetail') is not None:
            for k in m.get('OpLogDetail'):
                temp_model = GetOpLogResponseBodyOpLogDetailsOpLogDetail()
                self.op_log_detail.append(temp_model.from_map(k))
        return self


class GetOpLogResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        op_log_details: GetOpLogResponseBodyOpLogDetails = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.op_log_details = op_log_details
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.op_log_details:
            self.op_log_details.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.op_log_details is not None:
            result['OpLogDetails'] = self.op_log_details.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OpLogDetails') is not None:
            temp_model = GetOpLogResponseBodyOpLogDetails()
            self.op_log_details = temp_model.from_map(m['OpLogDetails'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOpLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetOpLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTableRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        search_key: str = None,
        page_number: int = None,
        page_size: int = None,
        env_type: str = None,
        search_range: str = None,
        search_target: str = None,
        db_type: str = None,
        return_guid: bool = None,
    ):
        self.tid = tid
        self.search_key = search_key
        self.page_number = page_number
        self.page_size = page_size
        self.env_type = env_type
        self.search_range = search_range
        self.search_target = search_target
        self.db_type = db_type
        self.return_guid = return_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.search_range is not None:
            result['SearchRange'] = self.search_range
        if self.search_target is not None:
            result['SearchTarget'] = self.search_target
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')
        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        return self


class SearchTableResponseBodySearchTableListSearchTableOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class SearchTableResponseBodySearchTableListSearchTableOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class SearchTableResponseBodySearchTableListSearchTable(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        table_name: str = None,
        dbsearch_name: str = None,
        logic: bool = None,
        env_type: str = None,
        db_name: str = None,
        owner_id_list: SearchTableResponseBodySearchTableListSearchTableOwnerIdList = None,
        description: str = None,
        encoding: str = None,
        db_type: str = None,
        owner_name_list: SearchTableResponseBodySearchTableListSearchTableOwnerNameList = None,
        table_schema_name: str = None,
        table_guid: str = None,
        engine: str = None,
        table_id: str = None,
    ):
        self.database_id = database_id
        self.table_name = table_name
        self.dbsearch_name = dbsearch_name
        self.logic = logic
        self.env_type = env_type
        self.db_name = db_name
        self.owner_id_list = owner_id_list
        self.description = description
        self.encoding = encoding
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.table_schema_name = table_schema_name
        self.table_guid = table_guid
        self.engine = engine
        self.table_id = table_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.dbsearch_name is not None:
            result['DBSearchName'] = self.dbsearch_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('DBSearchName') is not None:
            self.dbsearch_name = m.get('DBSearchName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('OwnerIdList') is not None:
            temp_model = SearchTableResponseBodySearchTableListSearchTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = SearchTableResponseBodySearchTableListSearchTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class SearchTableResponseBodySearchTableList(TeaModel):
    def __init__(
        self,
        search_table: List[SearchTableResponseBodySearchTableListSearchTable] = None,
    ):
        self.search_table = search_table

    def validate(self):
        if self.search_table:
            for k in self.search_table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SearchTable'] = []
        if self.search_table is not None:
            for k in self.search_table:
                result['SearchTable'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_table = []
        if m.get('SearchTable') is not None:
            for k in m.get('SearchTable'):
                temp_model = SearchTableResponseBodySearchTableListSearchTable()
                self.search_table.append(temp_model.from_map(k))
        return self


class SearchTableResponseBody(TeaModel):
    def __init__(
        self,
        search_table_list: SearchTableResponseBodySearchTableList = None,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.search_table_list = search_table_list
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.search_table_list:
            self.search_table_list.validate()

    def to_map(self):
        result = dict()
        if self.search_table_list is not None:
            result['SearchTableList'] = self.search_table_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchTableList') is not None:
            temp_model = SearchTableResponseBodySearchTableList()
            self.search_table_list = temp_model.from_map(m['SearchTableList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SearchTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDBTaskSQLJobRequest(TeaModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.dbtask_group_id = dbtask_group_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDBTaskSQLJobResponseBodyDBTaskSQLJobList(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        job_type: str = None,
        comment: str = None,
        db_search_name: str = None,
        db_id: int = None,
        logic: bool = None,
        create_time: str = None,
        last_exec_time: str = None,
        db_task_group_id: int = None,
        status: str = None,
        transactional: bool = None,
    ):
        self.job_id = job_id
        self.job_type = job_type
        self.comment = comment
        self.db_search_name = db_search_name
        self.db_id = db_id
        self.logic = logic
        self.create_time = create_time
        self.last_exec_time = last_exec_time
        self.db_task_group_id = db_task_group_id
        self.status = status
        self.transactional = transactional

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_exec_time is not None:
            result['LastExecTime'] = self.last_exec_time
        if self.db_task_group_id is not None:
            result['DbTaskGroupId'] = self.db_task_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.transactional is not None:
            result['Transactional'] = self.transactional
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastExecTime') is not None:
            self.last_exec_time = m.get('LastExecTime')
        if m.get('DbTaskGroupId') is not None:
            self.db_task_group_id = m.get('DbTaskGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Transactional') is not None:
            self.transactional = m.get('Transactional')
        return self


class ListDBTaskSQLJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        dbtask_sqljob_list: List[ListDBTaskSQLJobResponseBodyDBTaskSQLJobList] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.dbtask_sqljob_list = dbtask_sqljob_list
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_list:
            for k in self.dbtask_sqljob_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['DBTaskSQLJobList'] = []
        if self.dbtask_sqljob_list is not None:
            for k in self.dbtask_sqljob_list:
                result['DBTaskSQLJobList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.dbtask_sqljob_list = []
        if m.get('DBTaskSQLJobList') is not None:
            for k in m.get('DBTaskSQLJobList'):
                temp_model = ListDBTaskSQLJobResponseBodyDBTaskSQLJobList()
                self.dbtask_sqljob_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDBTaskSQLJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDBTaskSQLJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListDBTaskSQLJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        self.tid = tid
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncJobAnalyzeResultRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        compare_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.order_id = order_id
        self.compare_type = compare_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.compare_type is not None:
            result['CompareType'] = self.compare_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('CompareType') is not None:
            self.compare_type = m.get('CompareType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList(TeaModel):
    def __init__(
        self,
        compare_type: str = None,
        count: int = None,
    ):
        self.compare_type = compare_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.compare_type is not None:
            result['CompareType'] = self.compare_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareType') is not None:
            self.compare_type = m.get('CompareType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList(TeaModel):
    def __init__(
        self,
        source_table_name: str = None,
        target_table_name: str = None,
        script: str = None,
    ):
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult(TeaModel):
    def __init__(
        self,
        summary_list: List[GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList] = None,
        result_list: List[GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList] = None,
    ):
        self.summary_list = summary_list
        self.result_list = result_list

    def validate(self):
        if self.summary_list:
            for k in self.summary_list:
                if k:
                    k.validate()
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SummaryList'] = []
        if self.summary_list is not None:
            for k in self.summary_list:
                result['SummaryList'].append(k.to_map() if k else None)
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary_list = []
        if m.get('SummaryList') is not None:
            for k in m.get('SummaryList'):
                temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList()
                self.summary_list.append(temp_model.from_map(k))
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class GetStructSyncJobAnalyzeResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        struct_sync_job_analyze_result: GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.struct_sync_job_analyze_result = struct_sync_job_analyze_result

    def validate(self):
        if self.struct_sync_job_analyze_result:
            self.struct_sync_job_analyze_result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.struct_sync_job_analyze_result is not None:
            result['StructSyncJobAnalyzeResult'] = self.struct_sync_job_analyze_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('StructSyncJobAnalyzeResult') is not None:
            temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult()
            self.struct_sync_job_analyze_result = temp_model.from_map(m['StructSyncJobAnalyzeResult'])
        return self


class GetStructSyncJobAnalyzeResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStructSyncJobAnalyzeResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetStructSyncJobAnalyzeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveOrderRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        workflow_instance_id: int = None,
        approval_type: str = None,
        comment: str = None,
    ):
        self.tid = tid
        self.workflow_instance_id = workflow_instance_id
        self.approval_type = approval_type
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.comment is not None:
            result['Comment'] = self.comment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        return self


class ApproveOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApproveOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApproveOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ApproveOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadFileJobRequest(TeaModel):
    def __init__(
        self,
        file_source: str = None,
        file_name: str = None,
        upload_type: str = None,
        upload_url: str = None,
    ):
        self.file_source = file_source
        self.file_name = file_name
        self.upload_type = upload_type
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        return self


class CreateUploadFileJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        job_key: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.job_key = job_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        return self


class CreateUploadFileJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateUploadFileJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateUploadFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogicDatabasesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.tid = tid
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        owner_id_list: ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList = None,
        db_type: str = None,
        owner_name_list: ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
        env_type: str = None,
    ):
        self.database_id = database_id
        self.owner_id_list = owner_id_list
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.logic = logic
        self.schema_name = schema_name
        self.search_name = search_name
        self.env_type = env_type

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('OwnerIdList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class ListLogicDatabasesResponseBodyLogicDatabaseList(TeaModel):
    def __init__(
        self,
        logic_database: List[ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase] = None,
    ):
        self.logic_database = logic_database

    def validate(self):
        if self.logic_database:
            for k in self.logic_database:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LogicDatabase'] = []
        if self.logic_database is not None:
            for k in self.logic_database:
                result['LogicDatabase'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_database = []
        if m.get('LogicDatabase') is not None:
            for k in m.get('LogicDatabase'):
                temp_model = ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabase()
                self.logic_database.append(temp_model.from_map(k))
        return self


class ListLogicDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        logic_database_list: ListLogicDatabasesResponseBodyLogicDatabaseList = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.logic_database_list = logic_database_list
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.logic_database_list:
            self.logic_database_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logic_database_list is not None:
            result['LogicDatabaseList'] = self.logic_database_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogicDatabaseList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseList()
            self.logic_database_list = temp_model.from_map(m['LogicDatabaseList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLogicDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogicDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListLogicDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseOrderRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        close_reason: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.close_reason = close_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.close_reason is not None:
            result['CloseReason'] = self.close_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('CloseReason') is not None:
            self.close_reason = m.get('CloseReason')
        return self


class CloseOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CloseOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncInstanceMetaRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        instance_id: str = None,
        ignore_table: bool = None,
    ):
        self.tid = tid
        self.instance_id = instance_id
        self.ignore_table = ignore_table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ignore_table is not None:
            result['IgnoreTable'] = self.ignore_table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IgnoreTable') is not None:
            self.ignore_table = m.get('IgnoreTable')
        return self


class SyncInstanceMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncInstanceMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncInstanceMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SyncInstanceMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrdersRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        plugin_type: str = None,
        order_result_type: str = None,
        search_date_type: str = None,
        start_time: str = None,
        end_time: str = None,
        search_content: str = None,
        order_status: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.tid = tid
        self.plugin_type = plugin_type
        self.order_result_type = order_result_type
        self.search_date_type = search_date_type
        self.start_time = start_time
        self.end_time = end_time
        self.search_content = search_content
        self.order_status = order_status
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.order_result_type is not None:
            result['OrderResultType'] = self.order_result_type
        if self.search_date_type is not None:
            result['SearchDateType'] = self.search_date_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.search_content is not None:
            result['SearchContent'] = self.search_content
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('OrderResultType') is not None:
            self.order_result_type = m.get('OrderResultType')
        if m.get('SearchDateType') is not None:
            self.search_date_type = m.get('SearchDateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SearchContent') is not None:
            self.search_content = m.get('SearchContent')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListOrdersResponseBodyOrdersOrder(TeaModel):
    def __init__(
        self,
        comment: str = None,
        last_modify_time: str = None,
        status_code: str = None,
        create_time: str = None,
        committer: str = None,
        committer_id: int = None,
        status_desc: str = None,
        plugin_type: str = None,
        order_id: int = None,
    ):
        self.comment = comment
        self.last_modify_time = last_modify_time
        self.status_code = status_code
        self.create_time = create_time
        self.committer = committer
        self.committer_id = committer_id
        self.status_desc = status_desc
        self.plugin_type = plugin_type
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.committer is not None:
            result['Committer'] = self.committer
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Committer') is not None:
            self.committer = m.get('Committer')
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ListOrdersResponseBodyOrders(TeaModel):
    def __init__(
        self,
        order: List[ListOrdersResponseBodyOrdersOrder] = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = ListOrdersResponseBodyOrdersOrder()
                self.order.append(temp_model.from_map(k))
        return self


class ListOrdersResponseBody(TeaModel):
    def __init__(
        self,
        orders: ListOrdersResponseBodyOrders = None,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.orders = orders
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.orders:
            self.orders.validate()

    def to_map(self):
        result = dict()
        if self.orders is not None:
            result['Orders'] = self.orders.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Orders') is not None:
            temp_model = ListOrdersResponseBodyOrders()
            self.orders = temp_model.from_map(m['Orders'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOrdersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderBaseInfoRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
    ):
        self.tid = tid
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList(TeaModel):
    def __init__(
        self,
        user_nicks: List[str] = None,
    ):
        self.user_nicks = user_nicks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_nicks is not None:
            result['UserNicks'] = self.user_nicks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserNicks') is not None:
            self.user_nicks = m.get('UserNicks')
        return self


class GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList(TeaModel):
    def __init__(
        self,
        user_ids: List[str] = None,
    ):
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class GetOrderBaseInfoResponseBodyOrderBaseInfo(TeaModel):
    def __init__(
        self,
        related_user_nick_list: GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList = None,
        comment: str = None,
        create_time: str = None,
        committer: str = None,
        workflow_instance_id: int = None,
        committer_id: int = None,
        last_modify_time: str = None,
        status_code: str = None,
        related_user_list: GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList = None,
        workflow_status_desc: str = None,
        status_desc: str = None,
        plugin_type: str = None,
        order_id: int = None,
    ):
        self.related_user_nick_list = related_user_nick_list
        self.comment = comment
        self.create_time = create_time
        self.committer = committer
        self.workflow_instance_id = workflow_instance_id
        self.committer_id = committer_id
        self.last_modify_time = last_modify_time
        self.status_code = status_code
        self.related_user_list = related_user_list
        self.workflow_status_desc = workflow_status_desc
        self.status_desc = status_desc
        self.plugin_type = plugin_type
        self.order_id = order_id

    def validate(self):
        if self.related_user_nick_list:
            self.related_user_nick_list.validate()
        if self.related_user_list:
            self.related_user_list.validate()

    def to_map(self):
        result = dict()
        if self.related_user_nick_list is not None:
            result['RelatedUserNickList'] = self.related_user_nick_list.to_map()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.committer is not None:
            result['Committer'] = self.committer
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list.to_map()
        if self.workflow_status_desc is not None:
            result['WorkflowStatusDesc'] = self.workflow_status_desc
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelatedUserNickList') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList()
            self.related_user_nick_list = temp_model.from_map(m['RelatedUserNickList'])
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Committer') is not None:
            self.committer = m.get('Committer')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('RelatedUserList') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList()
            self.related_user_list = temp_model.from_map(m['RelatedUserList'])
        if m.get('WorkflowStatusDesc') is not None:
            self.workflow_status_desc = m.get('WorkflowStatusDesc')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetOrderBaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        order_base_info: GetOrderBaseInfoResponseBodyOrderBaseInfo = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.order_base_info = order_base_info
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.order_base_info:
            self.order_base_info.validate()

    def to_map(self):
        result = dict()
        if self.order_base_info is not None:
            result['OrderBaseInfo'] = self.order_base_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderBaseInfo') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m['OrderBaseInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderBaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOrderBaseInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetOrderBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserTenantsResponseBodyTenantList(TeaModel):
    def __init__(
        self,
        status: str = None,
        tid: int = None,
        tenant_name: str = None,
    ):
        self.status = status
        self.tid = tid
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class ListUserTenantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_list: List[ListUserTenantsResponseBodyTenantList] = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.tenant_list = tenant_list
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.tenant_list:
            for k in self.tenant_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantList'] = []
        if self.tenant_list is not None:
            for k in self.tenant_list:
                result['TenantList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_list = []
        if m.get('TenantList') is not None:
            for k in m.get('TenantList'):
                temp_model = ListUserTenantsResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserTenantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUserTenantsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListUserTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOwnersRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        resource_id: str = None,
        owner_type: str = None,
        owner_ids: str = None,
    ):
        self.tid = tid
        self.resource_id = resource_id
        self.owner_type = owner_type
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class SetOwnersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetOwnersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetOwnersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetOwnersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogicDatabaseRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        db_id: str = None,
    ):
        self.tid = tid
        self.db_id = db_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class GetLogicDatabaseResponseBodyLogicDatabase(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        owner_id_list: GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList = None,
        db_type: str = None,
        owner_name_list: GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
        env_type: str = None,
    ):
        self.database_id = database_id
        self.owner_id_list = owner_id_list
        self.db_type = db_type
        self.owner_name_list = owner_name_list
        self.logic = logic
        self.schema_name = schema_name
        self.search_name = search_name
        self.env_type = env_type

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('OwnerIdList') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('OwnerNameList') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class GetLogicDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        logic_database: GetLogicDatabaseResponseBodyLogicDatabase = None,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.logic_database = logic_database
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.logic_database:
            self.logic_database.validate()

    def to_map(self):
        result = dict()
        if self.logic_database is not None:
            result['LogicDatabase'] = self.logic_database.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicDatabase') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabase()
            self.logic_database = temp_model.from_map(m['LogicDatabase'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogicDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogicDatabaseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetLogicDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectBackupFilesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        action_name: str = None,
        action_detail: Dict[str, Any] = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail = action_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        return self


class GetDataCorrectBackupFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        action_name: str = None,
        action_detail_shrink: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail_shrink = action_detail_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        return self


class GetDataCorrectBackupFilesResponseBodyDataCorrectBackupFiles(TeaModel):
    def __init__(
        self,
        file_url: List[str] = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetDataCorrectBackupFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        data_correct_backup_files: GetDataCorrectBackupFilesResponseBodyDataCorrectBackupFiles = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success
        self.data_correct_backup_files = data_correct_backup_files

    def validate(self):
        if self.data_correct_backup_files:
            self.data_correct_backup_files.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.data_correct_backup_files is not None:
            result['DataCorrectBackupFiles'] = self.data_correct_backup_files.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DataCorrectBackupFiles') is not None:
            temp_model = GetDataCorrectBackupFilesResponseBodyDataCorrectBackupFiles()
            self.data_correct_backup_files = temp_model.from_map(m['DataCorrectBackupFiles'])
        return self


class GetDataCorrectBackupFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataCorrectBackupFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDataCorrectBackupFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterInstanceRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        instance_type: str = None,
        instance_source: str = None,
        network_type: str = None,
        env_type: str = None,
        ecs_instance_id: str = None,
        vpc_id: str = None,
        ecs_region: str = None,
        host: str = None,
        port: int = None,
        sid: str = None,
        database_user: str = None,
        database_password: str = None,
        instance_alias: str = None,
        dba_uid: int = None,
        safe_rule: str = None,
        query_timeout: int = None,
        export_timeout: int = None,
        data_link_name: str = None,
        ddl_online: int = None,
        use_dsql: int = None,
        skip_test: bool = None,
    ):
        self.tid = tid
        self.instance_type = instance_type
        self.instance_source = instance_source
        self.network_type = network_type
        self.env_type = env_type
        self.ecs_instance_id = ecs_instance_id
        self.vpc_id = vpc_id
        self.ecs_region = ecs_region
        self.host = host
        self.port = port
        self.sid = sid
        self.database_user = database_user
        self.database_password = database_password
        self.instance_alias = instance_alias
        self.dba_uid = dba_uid
        self.safe_rule = safe_rule
        self.query_timeout = query_timeout
        self.export_timeout = export_timeout
        self.data_link_name = data_link_name
        self.ddl_online = ddl_online
        self.use_dsql = use_dsql
        self.skip_test = skip_test

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.dba_uid is not None:
            result['DbaUid'] = self.dba_uid
        if self.safe_rule is not None:
            result['SafeRule'] = self.safe_rule
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.skip_test is not None:
            result['SkipTest'] = self.skip_test
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('DbaUid') is not None:
            self.dba_uid = m.get('DbaUid')
        if m.get('SafeRule') is not None:
            self.safe_rule = m.get('SafeRule')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('SkipTest') is not None:
            self.skip_test = m.get('SkipTest')
        return self


class RegisterInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RegisterInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RegisterInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStructSyncOrderRequestParamSource(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_search_name: str = None,
        logic: bool = None,
        version_id: str = None,
    ):
        self.db_id = db_id
        self.db_search_name = db_search_name
        self.logic = logic
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateStructSyncOrderRequestParamTarget(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_search_name: str = None,
        logic: bool = None,
        version_id: str = None,
    ):
        self.db_id = db_id
        self.db_search_name = db_search_name
        self.logic = logic
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateStructSyncOrderRequestParamTableInfoList(TeaModel):
    def __init__(
        self,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        return self


class CreateStructSyncOrderRequestParam(TeaModel):
    def __init__(
        self,
        source: CreateStructSyncOrderRequestParamSource = None,
        target: CreateStructSyncOrderRequestParamTarget = None,
        ignore_error: bool = None,
        table_info_list: List[CreateStructSyncOrderRequestParamTableInfoList] = None,
    ):
        self.source = source
        self.target = target
        self.ignore_error = ignore_error
        self.table_info_list = table_info_list

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()
        if self.table_info_list:
            for k in self.table_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source is not None:
            result['Source'] = self.source.to_map()
        if self.target is not None:
            result['Target'] = self.target.to_map()
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error
        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k in self.table_info_list:
                result['TableInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            temp_model = CreateStructSyncOrderRequestParamSource()
            self.source = temp_model.from_map(m['Source'])
        if m.get('Target') is not None:
            temp_model = CreateStructSyncOrderRequestParamTarget()
            self.target = temp_model.from_map(m['Target'])
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')
        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k in m.get('TableInfoList'):
                temp_model = CreateStructSyncOrderRequestParamTableInfoList()
                self.table_info_list.append(temp_model.from_map(k))
        return self


class CreateStructSyncOrderRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        related_user_list: List[int] = None,
        param: CreateStructSyncOrderRequestParam = None,
    ):
        self.comment = comment
        self.related_user_list = related_user_list
        self.param = param

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.param is not None:
            result['Param'] = self.param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Param') is not None:
            temp_model = CreateStructSyncOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        return self


class CreateStructSyncOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        related_user_list_shrink: str = None,
        param_shrink: str = None,
    ):
        self.comment = comment
        self.related_user_list_shrink = related_user_list_shrink
        self.param_shrink = param_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        return self


class CreateStructSyncOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        create_order_result: List[int] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.create_order_result = create_order_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        return self


class CreateStructSyncOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStructSyncOrderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateStructSyncOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteDataExportRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        action_name: str = None,
        action_detail: Dict[str, Any] = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail = action_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        return self


class ExecuteDataExportShrinkRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        order_id: int = None,
        action_name: str = None,
        action_detail_shrink: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail_shrink = action_detail_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        return self


class ExecuteDataExportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteDataExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteDataExportResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExecuteDataExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteDataCorrectRequest(TeaModel):
    def __init__(
        self,
        tid: str = None,
        order_id: int = None,
        action_name: str = None,
        action_detail: Dict[str, Any] = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail = action_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        return self


class ExecuteDataCorrectShrinkRequest(TeaModel):
    def __init__(
        self,
        tid: str = None,
        order_id: int = None,
        action_name: str = None,
        action_detail_shrink: str = None,
    ):
        self.tid = tid
        self.order_id = order_id
        self.action_name = action_name
        self.action_detail_shrink = action_detail_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        return self


class ExecuteDataCorrectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteDataCorrectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteDataCorrectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ExecuteDataCorrectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        database_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        return_guid: bool = None,
    ):
        self.tid = tid
        self.database_id = database_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_name = search_name
        self.return_guid = return_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        return self


class ListTablesResponseBodyTableListTableOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class ListTablesResponseBodyTableListTableOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListTablesResponseBodyTableListTable(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        table_name: str = None,
        store_capacity: int = None,
        owner_id_list: ListTablesResponseBodyTableListTableOwnerIdList = None,
        description: str = None,
        encoding: str = None,
        owner_name_list: ListTablesResponseBodyTableListTableOwnerNameList = None,
        table_schema_name: str = None,
        table_type: str = None,
        table_guid: str = None,
        engine: str = None,
        num_rows: int = None,
        table_id: str = None,
    ):
        self.database_id = database_id
        self.table_name = table_name
        self.store_capacity = store_capacity
        self.owner_id_list = owner_id_list
        self.description = description
        self.encoding = encoding
        self.owner_name_list = owner_name_list
        self.table_schema_name = table_schema_name
        self.table_type = table_type
        self.table_guid = table_guid
        self.engine = engine
        self.num_rows = num_rows
        self.table_id = table_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.store_capacity is not None:
            result['StoreCapacity'] = self.store_capacity
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.num_rows is not None:
            result['NumRows'] = self.num_rows
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('StoreCapacity') is not None:
            self.store_capacity = m.get('StoreCapacity')
        if m.get('OwnerIdList') is not None:
            temp_model = ListTablesResponseBodyTableListTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('OwnerNameList') is not None:
            temp_model = ListTablesResponseBodyTableListTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('NumRows') is not None:
            self.num_rows = m.get('NumRows')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class ListTablesResponseBodyTableList(TeaModel):
    def __init__(
        self,
        table: List[ListTablesResponseBodyTableListTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Table'] = []
        if self.table is not None:
            for k in self.table:
                result['Table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k in m.get('Table'):
                temp_model = ListTablesResponseBodyTableListTable()
                self.table.append(temp_model.from_map(k))
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        error_code: str = None,
        table_list: ListTablesResponseBodyTableList = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.error_code = error_code
        self.table_list = table_list
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('TableList') is not None:
            temp_model = ListTablesResponseBodyTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTablesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkFlowNodesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        search_name: str = None,
    ):
        self.tid = tid
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser(TeaModel):
    def __init__(
        self,
        real_name: str = None,
        user_id: int = None,
        nick_name: str = None,
    ):
        self.real_name = real_name
        self.user_id = user_id
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        return self


class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers(TeaModel):
    def __init__(
        self,
        audit_user: List[ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser] = None,
    ):
        self.audit_user = audit_user

    def validate(self):
        if self.audit_user:
            for k in self.audit_user:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AuditUser'] = []
        if self.audit_user is not None:
            for k in self.audit_user:
                result['AuditUser'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audit_user = []
        if m.get('AuditUser') is not None:
            for k in m.get('AuditUser'):
                temp_model = ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser()
                self.audit_user.append(temp_model.from_map(k))
        return self


class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode(TeaModel):
    def __init__(
        self,
        comment: str = None,
        create_user_nick_name: str = None,
        node_type: str = None,
        node_name: str = None,
        audit_users: ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers = None,
        create_user_id: int = None,
        node_id: int = None,
    ):
        self.comment = comment
        self.create_user_nick_name = create_user_nick_name
        self.node_type = node_type
        self.node_name = node_name
        self.audit_users = audit_users
        self.create_user_id = create_user_id
        self.node_id = node_id

    def validate(self):
        if self.audit_users:
            self.audit_users.validate()

    def to_map(self):
        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_user_nick_name is not None:
            result['CreateUserNickName'] = self.create_user_nick_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.audit_users is not None:
            result['AuditUsers'] = self.audit_users.to_map()
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateUserNickName') is not None:
            self.create_user_nick_name = m.get('CreateUserNickName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('AuditUsers') is not None:
            temp_model = ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers()
            self.audit_users = temp_model.from_map(m['AuditUsers'])
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ListWorkFlowNodesResponseBodyWorkflowNodes(TeaModel):
    def __init__(
        self,
        workflow_node: List[ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode] = None,
    ):
        self.workflow_node = workflow_node

    def validate(self):
        if self.workflow_node:
            for k in self.workflow_node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['WorkflowNode'] = []
        if self.workflow_node is not None:
            for k in self.workflow_node:
                result['WorkflowNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workflow_node = []
        if m.get('WorkflowNode') is not None:
            for k in m.get('WorkflowNode'):
                temp_model = ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k))
        return self


class ListWorkFlowNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        workflow_nodes: ListWorkFlowNodesResponseBodyWorkflowNodes = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.workflow_nodes = workflow_nodes
        self.success = success

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('WorkflowNodes') is not None:
            temp_model = ListWorkFlowNodesResponseBodyWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListWorkFlowNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWorkFlowNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListWorkFlowNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        search_name: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.search_name = search_name
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        search_name: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.search_name = search_name
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo(TeaModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList(TeaModel):
    def __init__(
        self,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail(TeaModel):
    def __init__(
        self,
        source_database_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo = None,
        target_database_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo = None,
        source_type: str = None,
        source_version_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo = None,
        target_type: str = None,
        target_version_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo = None,
        table_info_list: List[GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList] = None,
        ignore_error: bool = None,
    ):
        self.source_database_info = source_database_info
        self.target_database_info = target_database_info
        self.source_type = source_type
        self.source_version_info = source_version_info
        self.target_type = target_type
        self.target_version_info = target_version_info
        self.table_info_list = table_info_list
        self.ignore_error = ignore_error

    def validate(self):
        if self.source_database_info:
            self.source_database_info.validate()
        if self.target_database_info:
            self.target_database_info.validate()
        if self.source_version_info:
            self.source_version_info.validate()
        if self.target_version_info:
            self.target_version_info.validate()
        if self.table_info_list:
            for k in self.table_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_database_info is not None:
            result['SourceDatabaseInfo'] = self.source_database_info.to_map()
        if self.target_database_info is not None:
            result['TargetDatabaseInfo'] = self.target_database_info.to_map()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_version_info is not None:
            result['SourceVersionInfo'] = self.source_version_info.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_version_info is not None:
            result['TargetVersionInfo'] = self.target_version_info.to_map()
        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k in self.table_info_list:
                result['TableInfoList'].append(k.to_map() if k else None)
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceDatabaseInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo()
            self.source_database_info = temp_model.from_map(m['SourceDatabaseInfo'])
        if m.get('TargetDatabaseInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo()
            self.target_database_info = temp_model.from_map(m['TargetDatabaseInfo'])
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceVersionInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo()
            self.source_version_info = temp_model.from_map(m['SourceVersionInfo'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetVersionInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo()
            self.target_version_info = temp_model.from_map(m['TargetVersionInfo'])
        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k in m.get('TableInfoList'):
                temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList()
                self.table_info_list.append(temp_model.from_map(k))
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')
        return self


class GetStructSyncOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        struct_sync_order_detail: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.struct_sync_order_detail = struct_sync_order_detail

    def validate(self):
        if self.struct_sync_order_detail:
            self.struct_sync_order_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.struct_sync_order_detail is not None:
            result['StructSyncOrderDetail'] = self.struct_sync_order_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('StructSyncOrderDetail') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail()
            self.struct_sync_order_detail = temp_model.from_map(m['StructSyncOrderDetail'])
        return self


class GetStructSyncOrderDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStructSyncOrderDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetStructSyncOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveColumnsDetailRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        schema_name: str = None,
        table_name: str = None,
        column_name: str = None,
    ):
        self.tid = tid
        self.schema_name = schema_name
        self.table_name = table_name
        self.column_name = column_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        return self


class ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        column_name: str = None,
        column_description: str = None,
        table_name: str = None,
        db_type: str = None,
        column_type: str = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
        env_type: str = None,
    ):
        self.db_id = db_id
        self.column_name = column_name
        self.column_description = column_description
        self.table_name = table_name
        self.db_type = db_type
        self.column_type = column_type
        self.logic = logic
        self.schema_name = schema_name
        self.search_name = search_name
        self.env_type = env_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_description is not None:
            result['ColumnDescription'] = self.column_description
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnDescription') is not None:
            self.column_description = m.get('ColumnDescription')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList(TeaModel):
    def __init__(
        self,
        sensitive_columns_detail: List[ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail] = None,
    ):
        self.sensitive_columns_detail = sensitive_columns_detail

    def validate(self):
        if self.sensitive_columns_detail:
            for k in self.sensitive_columns_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SensitiveColumnsDetail'] = []
        if self.sensitive_columns_detail is not None:
            for k in self.sensitive_columns_detail:
                result['SensitiveColumnsDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_columns_detail = []
        if m.get('SensitiveColumnsDetail') is not None:
            for k in m.get('SensitiveColumnsDetail'):
                temp_model = ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail()
                self.sensitive_columns_detail.append(temp_model.from_map(k))
        return self


class ListSensitiveColumnsDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sensitive_columns_detail_list: ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.sensitive_columns_detail_list = sensitive_columns_detail_list
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.sensitive_columns_detail_list:
            self.sensitive_columns_detail_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sensitive_columns_detail_list is not None:
            result['SensitiveColumnsDetailList'] = self.sensitive_columns_detail_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SensitiveColumnsDetailList') is not None:
            temp_model = ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList()
            self.sensitive_columns_detail_list = temp_model.from_map(m['SensitiveColumnsDetailList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSensitiveColumnsDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSensitiveColumnsDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListSensitiveColumnsDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        uid: int = None,
        user_nick: str = None,
        role_names: str = None,
        mobile: str = None,
        max_execute_count: int = None,
        max_result_count: int = None,
    ):
        self.tid = tid
        self.uid = uid
        self.user_nick = user_nick
        self.role_names = role_names
        self.mobile = mobile
        self.max_execute_count = max_execute_count
        self.max_result_count = max_result_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncExecSqlDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail(TeaModel):
    def __init__(
        self,
        total_sql_count: int = None,
        exec_sql: str = None,
    ):
        self.total_sql_count = total_sql_count
        self.exec_sql = exec_sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_sql_count is not None:
            result['TotalSqlCount'] = self.total_sql_count
        if self.exec_sql is not None:
            result['ExecSql'] = self.exec_sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalSqlCount') is not None:
            self.total_sql_count = m.get('TotalSqlCount')
        if m.get('ExecSql') is not None:
            self.exec_sql = m.get('ExecSql')
        return self


class GetStructSyncExecSqlDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        error_message: str = None,
        error_code: str = None,
        struct_sync_exec_sql_detail: GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.error_message = error_message
        self.error_code = error_code
        self.struct_sync_exec_sql_detail = struct_sync_exec_sql_detail

    def validate(self):
        if self.struct_sync_exec_sql_detail:
            self.struct_sync_exec_sql_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.struct_sync_exec_sql_detail is not None:
            result['StructSyncExecSqlDetail'] = self.struct_sync_exec_sql_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('StructSyncExecSqlDetail') is not None:
            temp_model = GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail()
            self.struct_sync_exec_sql_detail = temp_model.from_map(m['StructSyncExecSqlDetail'])
        return self


class GetStructSyncExecSqlDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStructSyncExecSqlDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetStructSyncExecSqlDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        host: str = None,
        port: int = None,
        sid: str = None,
    ):
        self.tid = tid
        self.host = host
        self.port = port
        self.sid = sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableDBTopologyRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
        table_guid: str = None,
    ):
        self.tid = tid
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        table_type: str = None,
        table_id: str = None,
    ):
        self.table_name = table_name
        self.table_type = table_type
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        db_name: str = None,
        db_type: str = None,
        table_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList] = None,
        env_type: str = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.db_type = db_type
        self.table_list = table_list
        self.env_type = env_type

    def validate(self):
        if self.table_list:
            for k in self.table_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        result['TableList'] = []
        if self.table_list is not None:
            for k in self.table_list:
                result['TableList'].append(k.to_map() if k else None)
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        self.table_list = []
        if m.get('TableList') is not None:
            for k in m.get('TableList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList()
                self.table_list.append(temp_model.from_map(k))
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceList(TeaModel):
    def __init__(
        self,
        sid: str = None,
        host: str = None,
        db_type: str = None,
        database_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList] = None,
        port: int = None,
    ):
        self.sid = sid
        self.host = host
        self.db_type = db_type
        self.database_list = database_list
        self.port = port

    def validate(self):
        if self.database_list:
            for k in self.database_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.host is not None:
            result['Host'] = self.host
        if self.db_type is not None:
            result['DbType'] = self.db_type
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k in self.database_list:
                result['DatabaseList'].append(k.to_map() if k else None)
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k in m.get('DatabaseList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList()
                self.database_list.append(temp_model.from_map(k))
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class GetTableDBTopologyResponseBodyDBTopology(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        data_source_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceList] = None,
        table_guid: str = None,
    ):
        self.table_name = table_name
        self.data_source_list = data_source_list
        self.table_guid = table_guid

    def validate(self):
        if self.data_source_list:
            for k in self.data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        result['DataSourceList'] = []
        if self.data_source_list is not None:
            for k in self.data_source_list:
                result['DataSourceList'].append(k.to_map() if k else None)
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        self.data_source_list = []
        if m.get('DataSourceList') is not None:
            for k in m.get('DataSourceList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceList()
                self.data_source_list.append(temp_model.from_map(k))
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        return self


class GetTableDBTopologyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dbtopology: GetTableDBTopologyResponseBodyDBTopology = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.dbtopology = dbtopology
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        if self.dbtopology:
            self.dbtopology.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dbtopology is not None:
            result['DBTopology'] = self.dbtopology.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DBTopology') is not None:
            temp_model = GetTableDBTopologyResponseBodyDBTopology()
            self.dbtopology = temp_model.from_map(m['DBTopology'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTableDBTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTableDBTopologyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetTableDBTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


