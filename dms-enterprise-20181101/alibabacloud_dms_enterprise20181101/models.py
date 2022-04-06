# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddLhMembersRequestMembers(TeaModel):
    def __init__(
        self,
        roles: List[str] = None,
        user_id: int = None,
    ):
        self.roles = roles
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddLhMembersRequest(TeaModel):
    def __init__(
        self,
        members: List[AddLhMembersRequestMembers] = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        self.members = members
        self.object_id = object_id
        self.object_type = object_type
        self.tid = tid

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = AddLhMembersRequestMembers()
                self.members.append(temp_model.from_map(k))
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class AddLhMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        members_shrink: str = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        self.members_shrink = members_shrink
        self.object_id = object_id
        self.object_type = object_type
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.members_shrink is not None:
            result['Members'] = self.members_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Members') is not None:
            self.members_shrink = m.get('Members')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class AddLhMembersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddLhMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddLhMembersResponseBody = None,
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
            temp_model = AddLhMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddLogicTableRouteConfigRequest(TeaModel):
    def __init__(
        self,
        route_expr: str = None,
        route_key: str = None,
        table_id: int = None,
        tid: int = None,
    ):
        self.route_expr = route_expr
        self.route_key = route_key
        self.table_id = table_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_expr is not None:
            result['RouteExpr'] = self.route_expr
        if self.route_key is not None:
            result['RouteKey'] = self.route_key
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteExpr') is not None:
            self.route_expr = m.get('RouteExpr')
        if m.get('RouteKey') is not None:
            self.route_key = m.get('RouteKey')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class AddLogicTableRouteConfigResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddLogicTableRouteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddLogicTableRouteConfigResponseBody = None,
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
            temp_model = AddLogicTableRouteConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveOrderRequest(TeaModel):
    def __init__(
        self,
        approval_type: str = None,
        comment: str = None,
        tid: int = None,
        workflow_instance_id: int = None,
    ):
        self.approval_type = approval_type
        self.comment = comment
        self.tid = tid
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class ApproveOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ApproveOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeColumnSecLevelRequest(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        is_logic: bool = None,
        new_level: str = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        self.column_name = column_name
        self.db_id = db_id
        self.is_logic = is_logic
        # 新的敏感等级
        self.new_level = new_level
        self.schema_name = schema_name
        self.table_name = table_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.is_logic is not None:
            result['IsLogic'] = self.is_logic
        if self.new_level is not None:
            result['NewLevel'] = self.new_level
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('IsLogic') is not None:
            self.is_logic = m.get('IsLogic')
        if m.get('NewLevel') is not None:
            self.new_level = m.get('NewLevel')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ChangeColumnSecLevelResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeColumnSecLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeColumnSecLevelResponseBody = None,
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
            temp_model = ChangeColumnSecLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeLhDagOwnerRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        owner_user_id: int = None,
        tid: int = None,
    ):
        self.dag_id = dag_id
        self.owner_user_id = owner_user_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ChangeLhDagOwnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeLhDagOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeLhDagOwnerResponseBody = None,
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
            temp_model = ChangeLhDagOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseOrderRequest(TeaModel):
    def __init__(
        self,
        close_reason: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.close_reason = close_reason
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.close_reason is not None:
            result['CloseReason'] = self.close_reason
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseReason') is not None:
            self.close_reason = m.get('CloseReason')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CloseOrderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = CloseOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCorrectOrderRequestParamDbItemList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class CreateDataCorrectOrderRequestParam(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        classify: str = None,
        db_item_list: List[CreateDataCorrectOrderRequestParamDbItemList] = None,
        estimate_affect_rows: int = None,
        exec_sql: str = None,
        rollback_attachment_name: str = None,
        rollback_sql: str = None,
        rollback_sql_type: str = None,
        sql_type: str = None,
    ):
        self.attachment_name = attachment_name
        self.classify = classify
        self.db_item_list = db_item_list
        self.estimate_affect_rows = estimate_affect_rows
        self.exec_sql = exec_sql
        self.rollback_attachment_name = rollback_attachment_name
        self.rollback_sql = rollback_sql
        self.rollback_sql_type = rollback_sql_type
        self.sql_type = sql_type

    def validate(self):
        if self.db_item_list:
            for k in self.db_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.classify is not None:
            result['Classify'] = self.classify
        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k in self.db_item_list:
                result['DbItemList'].append(k.to_map() if k else None)
        if self.estimate_affect_rows is not None:
            result['EstimateAffectRows'] = self.estimate_affect_rows
        if self.exec_sql is not None:
            result['ExecSQL'] = self.exec_sql
        if self.rollback_attachment_name is not None:
            result['RollbackAttachmentName'] = self.rollback_attachment_name
        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql
        if self.rollback_sql_type is not None:
            result['RollbackSqlType'] = self.rollback_sql_type
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k in m.get('DbItemList'):
                temp_model = CreateDataCorrectOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k))
        if m.get('EstimateAffectRows') is not None:
            self.estimate_affect_rows = m.get('EstimateAffectRows')
        if m.get('ExecSQL') is not None:
            self.exec_sql = m.get('ExecSQL')
        if m.get('RollbackAttachmentName') is not None:
            self.rollback_attachment_name = m.get('RollbackAttachmentName')
        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')
        if m.get('RollbackSqlType') is not None:
            self.rollback_sql_type = m.get('RollbackSqlType')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class CreateDataCorrectOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: CreateDataCorrectOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateDataCorrectOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataCorrectOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataCorrectOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataCorrectOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataCorrectOrderResponseBody = None,
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
            temp_model = CreateDataCorrectOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataCronClearOrderRequestParamCronClearItemList(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        filter_sql: str = None,
        remain_days: int = None,
        table_name: str = None,
        time_unit: str = None,
    ):
        self.column_name = column_name
        self.filter_sql = filter_sql
        self.remain_days = remain_days
        self.table_name = table_name
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.filter_sql is not None:
            result['FilterSQL'] = self.filter_sql
        if self.remain_days is not None:
            result['RemainDays'] = self.remain_days
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('FilterSQL') is not None:
            self.filter_sql = m.get('FilterSQL')
        if m.get('RemainDays') is not None:
            self.remain_days = m.get('RemainDays')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class CreateDataCronClearOrderRequestParamDbItemList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class CreateDataCronClearOrderRequestParam(TeaModel):
    def __init__(
        self,
        classify: str = None,
        cron_clear_item_list: List[CreateDataCronClearOrderRequestParamCronClearItemList] = None,
        cron_format: str = None,
        db_item_list: List[CreateDataCronClearOrderRequestParamDbItemList] = None,
        duration_hour: int = None,
        specify_duration: bool = None,
    ):
        self.classify = classify
        self.cron_clear_item_list = cron_clear_item_list
        self.cron_format = cron_format
        self.db_item_list = db_item_list
        self.duration_hour = duration_hour
        self.specify_duration = specify_duration

    def validate(self):
        if self.cron_clear_item_list:
            for k in self.cron_clear_item_list:
                if k:
                    k.validate()
        if self.db_item_list:
            for k in self.db_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        result['CronClearItemList'] = []
        if self.cron_clear_item_list is not None:
            for k in self.cron_clear_item_list:
                result['CronClearItemList'].append(k.to_map() if k else None)
        if self.cron_format is not None:
            result['CronFormat'] = self.cron_format
        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k in self.db_item_list:
                result['DbItemList'].append(k.to_map() if k else None)
        if self.duration_hour is not None:
            result['DurationHour'] = self.duration_hour
        if self.specify_duration is not None:
            result['specifyDuration'] = self.specify_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        self.cron_clear_item_list = []
        if m.get('CronClearItemList') is not None:
            for k in m.get('CronClearItemList'):
                temp_model = CreateDataCronClearOrderRequestParamCronClearItemList()
                self.cron_clear_item_list.append(temp_model.from_map(k))
        if m.get('CronFormat') is not None:
            self.cron_format = m.get('CronFormat')
        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k in m.get('DbItemList'):
                temp_model = CreateDataCronClearOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k))
        if m.get('DurationHour') is not None:
            self.duration_hour = m.get('DurationHour')
        if m.get('specifyDuration') is not None:
            self.specify_duration = m.get('specifyDuration')
        return self


class CreateDataCronClearOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: CreateDataCronClearOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateDataCronClearOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataCronClearOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataCronClearOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataCronClearOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataCronClearOrderResponseBody = None,
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
            temp_model = CreateDataCronClearOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataImportOrderRequestParamDbItemList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class CreateDataImportOrderRequestParam(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        classify: str = None,
        csv_first_row_is_column_def: bool = None,
        db_item_list: List[CreateDataImportOrderRequestParamDbItemList] = None,
        file_encoding: str = None,
        file_type: str = None,
        ignore_error: bool = None,
        import_mode: str = None,
        insert_type: str = None,
        rollback_attachment_name: str = None,
        rollback_sql: str = None,
        rollback_sql_type: str = None,
        table_name: str = None,
    ):
        self.attachment_name = attachment_name
        self.classify = classify
        self.csv_first_row_is_column_def = csv_first_row_is_column_def
        self.db_item_list = db_item_list
        self.file_encoding = file_encoding
        self.file_type = file_type
        self.ignore_error = ignore_error
        self.import_mode = import_mode
        self.insert_type = insert_type
        self.rollback_attachment_name = rollback_attachment_name
        self.rollback_sql = rollback_sql
        self.rollback_sql_type = rollback_sql_type
        self.table_name = table_name

    def validate(self):
        if self.db_item_list:
            for k in self.db_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.csv_first_row_is_column_def is not None:
            result['CsvFirstRowIsColumnDef'] = self.csv_first_row_is_column_def
        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k in self.db_item_list:
                result['DbItemList'].append(k.to_map() if k else None)
        if self.file_encoding is not None:
            result['FileEncoding'] = self.file_encoding
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error
        if self.import_mode is not None:
            result['ImportMode'] = self.import_mode
        if self.insert_type is not None:
            result['InsertType'] = self.insert_type
        if self.rollback_attachment_name is not None:
            result['RollbackAttachmentName'] = self.rollback_attachment_name
        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql
        if self.rollback_sql_type is not None:
            result['RollbackSqlType'] = self.rollback_sql_type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('CsvFirstRowIsColumnDef') is not None:
            self.csv_first_row_is_column_def = m.get('CsvFirstRowIsColumnDef')
        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k in m.get('DbItemList'):
                temp_model = CreateDataImportOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k))
        if m.get('FileEncoding') is not None:
            self.file_encoding = m.get('FileEncoding')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')
        if m.get('ImportMode') is not None:
            self.import_mode = m.get('ImportMode')
        if m.get('InsertType') is not None:
            self.insert_type = m.get('InsertType')
        if m.get('RollbackAttachmentName') is not None:
            self.rollback_attachment_name = m.get('RollbackAttachmentName')
        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')
        if m.get('RollbackSqlType') is not None:
            self.rollback_sql_type = m.get('RollbackSqlType')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class CreateDataImportOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: CreateDataImportOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateDataImportOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataImportOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateDataImportOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataImportOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataImportOrderResponseBody = None,
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
            temp_model = CreateDataImportOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFreeLockCorrectOrderRequestParamDbItemList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        self.db_id = db_id
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        return self


class CreateFreeLockCorrectOrderRequestParam(TeaModel):
    def __init__(
        self,
        attachment_name: str = None,
        classify: str = None,
        db_item_list: List[CreateFreeLockCorrectOrderRequestParamDbItemList] = None,
        exec_sql: str = None,
        rollback_attachment_name: str = None,
        rollback_sql: str = None,
        rollback_sql_type: str = None,
        sql_type: str = None,
    ):
        self.attachment_name = attachment_name
        self.classify = classify
        self.db_item_list = db_item_list
        self.exec_sql = exec_sql
        self.rollback_attachment_name = rollback_attachment_name
        self.rollback_sql = rollback_sql
        self.rollback_sql_type = rollback_sql_type
        self.sql_type = sql_type

    def validate(self):
        if self.db_item_list:
            for k in self.db_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.classify is not None:
            result['Classify'] = self.classify
        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k in self.db_item_list:
                result['DbItemList'].append(k.to_map() if k else None)
        if self.exec_sql is not None:
            result['ExecSQL'] = self.exec_sql
        if self.rollback_attachment_name is not None:
            result['RollbackAttachmentName'] = self.rollback_attachment_name
        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql
        if self.rollback_sql_type is not None:
            result['RollbackSqlType'] = self.rollback_sql_type
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k in m.get('DbItemList'):
                temp_model = CreateFreeLockCorrectOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k))
        if m.get('ExecSQL') is not None:
            self.exec_sql = m.get('ExecSQL')
        if m.get('RollbackAttachmentName') is not None:
            self.rollback_attachment_name = m.get('RollbackAttachmentName')
        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')
        if m.get('RollbackSqlType') is not None:
            self.rollback_sql_type = m.get('RollbackSqlType')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class CreateFreeLockCorrectOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: CreateFreeLockCorrectOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateFreeLockCorrectOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateFreeLockCorrectOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateFreeLockCorrectOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFreeLockCorrectOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFreeLockCorrectOrderResponseBody = None,
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
            temp_model = CreateFreeLockCorrectOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLakeHouseSpaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dev_db_id: str = None,
        dw_db_type: str = None,
        mode: str = None,
        prod_db_id: str = None,
        space_config: str = None,
        space_name: str = None,
        tid: int = None,
    ):
        self.description = description
        self.dev_db_id = dev_db_id
        self.dw_db_type = dw_db_type
        self.mode = mode
        self.prod_db_id = prod_db_id
        self.space_config = space_config
        self.space_name = space_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_db_id is not None:
            result['DevDbId'] = self.dev_db_id
        if self.dw_db_type is not None:
            result['DwDbType'] = self.dw_db_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.prod_db_id is not None:
            result['ProdDbId'] = self.prod_db_id
        if self.space_config is not None:
            result['SpaceConfig'] = self.space_config
        if self.space_name is not None:
            result['SpaceName'] = self.space_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevDbId') is not None:
            self.dev_db_id = m.get('DevDbId')
        if m.get('DwDbType') is not None:
            self.dw_db_type = m.get('DwDbType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ProdDbId') is not None:
            self.prod_db_id = m.get('ProdDbId')
        if m.get('SpaceConfig') is not None:
            self.space_config = m.get('SpaceConfig')
        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateLakeHouseSpaceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        space_id: int = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.space_id = space_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLakeHouseSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLakeHouseSpaceResponseBody = None,
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
            temp_model = CreateLakeHouseSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogicDatabaseRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        database_ids: List[int] = None,
        tid: int = None,
    ):
        self.alias = alias
        self.database_ids = database_ids
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateLogicDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        database_ids_shrink: str = None,
        tid: int = None,
    ):
        self.alias = alias
        self.database_ids_shrink = database_ids_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_ids_shrink is not None:
            result['DatabaseIds'] = self.database_ids_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseIds') is not None:
            self.database_ids_shrink = m.get('DatabaseIds')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateLogicDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_db_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.logic_db_id = logic_db_id
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLogicDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLogicDatabaseResponseBody = None,
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
            temp_model = CreateLogicDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        plugin_param: Dict[str, Any] = None,
        plugin_type: str = None,
        related_user_list: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.plugin_param = plugin_param
        self.plugin_type = plugin_type
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.plugin_param is not None:
            result['PluginParam'] = self.plugin_param
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PluginParam') is not None:
            self.plugin_param = m.get('PluginParam')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        plugin_param_shrink: str = None,
        plugin_type: str = None,
        related_user_list: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.plugin_param_shrink = plugin_param_shrink
        self.plugin_type = plugin_type
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.plugin_param_shrink is not None:
            result['PluginParam'] = self.plugin_param_shrink
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('PluginParam') is not None:
            self.plugin_param_shrink = m.get('PluginParam')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: CreateOrderResponseBodyCreateOrderResult = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.create_order_result:
            self.create_order_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            temp_model = CreateOrderResponseBodyCreateOrderResult()
            self.create_order_result = temp_model.from_map(m['CreateOrderResult'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class CreateProxyRequest(TeaModel):
    def __init__(
        self,
        instance_id: int = None,
        password: str = None,
        tid: int = None,
        username: str = None,
    ):
        self.instance_id = instance_id
        self.password = password
        self.tid = tid
        self.username = username

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
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class CreateProxyResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.proxy_id = proxy_id
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProxyResponseBody = None,
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
            temp_model = CreateProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProxyAccessRequest(TeaModel):
    def __init__(
        self,
        indep_account: str = None,
        indep_password: str = None,
        proxy_id: int = None,
        tid: int = None,
        user_id: int = None,
    ):
        self.indep_account = indep_account
        self.indep_password = indep_password
        self.proxy_id = proxy_id
        self.tid = tid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.indep_account is not None:
            result['IndepAccount'] = self.indep_account
        if self.indep_password is not None:
            result['IndepPassword'] = self.indep_password
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndepAccount') is not None:
            self.indep_account = m.get('IndepAccount')
        if m.get('IndepPassword') is not None:
            self.indep_password = m.get('IndepPassword')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateProxyAccessResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_access_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.proxy_access_id = proxy_access_id
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProxyAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProxyAccessResponseBody = None,
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
            temp_model = CreateProxyAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePublishGroupTaskRequest(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        order_id: int = None,
        plan_time: str = None,
        publish_strategy: str = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.order_id = order_id
        self.plan_time = plan_time
        self.publish_strategy = publish_strategy
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time
        if self.publish_strategy is not None:
            result['PublishStrategy'] = self.publish_strategy
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')
        if m.get('PublishStrategy') is not None:
            self.publish_strategy = m.get('PublishStrategy')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreatePublishGroupTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
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
            temp_model = CreatePublishGroupTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSQLReviewOrderRequestParam(TeaModel):
    def __init__(
        self,
        attachment_key_list: List[str] = None,
        db_id: int = None,
        project_name: str = None,
    ):
        self.attachment_key_list = attachment_key_list
        self.db_id = db_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key_list is not None:
            result['AttachmentKeyList'] = self.attachment_key_list
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKeyList') is not None:
            self.attachment_key_list = m.get('AttachmentKeyList')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateSQLReviewOrderRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        param: CreateSQLReviewOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateSQLReviewOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateSQLReviewOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateSQLReviewOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSQLReviewOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSQLReviewOrderResponseBody = None,
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
            temp_model = CreateSQLReviewOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStandardGroupRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        group_name: str = None,
        tid: int = None,
    ):
        self.db_type = db_type
        self.description = description
        self.group_name = group_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateStandardGroupResponseBodyStandardGroup(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        group_mode: str = None,
        group_name: str = None,
        last_mender_id: int = None,
    ):
        self.db_type = db_type
        self.description = description
        self.group_mode = group_mode
        self.group_name = group_name
        self.last_mender_id = last_mender_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.last_mender_id is not None:
            result['LastMenderId'] = self.last_mender_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('LastMenderId') is not None:
            self.last_mender_id = m.get('LastMenderId')
        return self


class CreateStandardGroupResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        standard_group: CreateStandardGroupResponseBodyStandardGroup = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.standard_group = standard_group
        self.success = success

    def validate(self):
        if self.standard_group:
            self.standard_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StandardGroup') is not None:
            temp_model = CreateStandardGroupResponseBodyStandardGroup()
            self.standard_group = temp_model.from_map(m['StandardGroup'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStandardGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStandardGroupResponseBody = None,
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
            temp_model = CreateStandardGroupResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class CreateStructSyncOrderRequestParam(TeaModel):
    def __init__(
        self,
        ignore_error: bool = None,
        source: CreateStructSyncOrderRequestParamSource = None,
        table_info_list: List[CreateStructSyncOrderRequestParamTableInfoList] = None,
        target: CreateStructSyncOrderRequestParamTarget = None,
    ):
        self.ignore_error = ignore_error
        self.source = source
        self.table_info_list = table_info_list
        self.target = target

    def validate(self):
        if self.source:
            self.source.validate()
        if self.table_info_list:
            for k in self.table_info_list:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error
        if self.source is not None:
            result['Source'] = self.source.to_map()
        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k in self.table_info_list:
                result['TableInfoList'].append(k.to_map() if k else None)
        if self.target is not None:
            result['Target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')
        if m.get('Source') is not None:
            temp_model = CreateStructSyncOrderRequestParamSource()
            self.source = temp_model.from_map(m['Source'])
        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k in m.get('TableInfoList'):
                temp_model = CreateStructSyncOrderRequestParamTableInfoList()
                self.table_info_list.append(temp_model.from_map(k))
        if m.get('Target') is not None:
            temp_model = CreateStructSyncOrderRequestParamTarget()
            self.target = temp_model.from_map(m['Target'])
        return self


class CreateStructSyncOrderRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: CreateStructSyncOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param = param
        self.related_user_list = related_user_list
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param is not None:
            result['Param'] = self.param.to_map()
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            temp_model = CreateStructSyncOrderRequestParam()
            self.param = temp_model.from_map(m['Param'])
        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateStructSyncOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        self.attachment_key = attachment_key
        self.comment = comment
        self.param_shrink = param_shrink
        self.related_user_list_shrink = related_user_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.param_shrink is not None:
            result['Param'] = self.param_shrink
        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')
        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class CreateStructSyncOrderResponseBody(TeaModel):
    def __init__(
        self,
        create_order_result: List[int] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.create_order_result = create_order_result
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_order_result is not None:
            result['CreateOrderResult'] = self.create_order_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateOrderResult') is not None:
            self.create_order_result = m.get('CreateOrderResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = CreateStructSyncOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadFileJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_source: str = None,
        tid: int = None,
        upload_url: str = None,
    ):
        self.file_name = file_name
        self.file_source = file_source
        self.tid = tid
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        return self


class CreateUploadFileJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_key: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.job_key = job_key
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = CreateUploadFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadOSSFileJobRequestUploadTarget(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        object_name: str = None,
    ):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.object_name = object_name

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
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class CreateUploadOSSFileJobRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_source: str = None,
        tid: int = None,
        upload_target: CreateUploadOSSFileJobRequestUploadTarget = None,
    ):
        self.file_name = file_name
        self.file_source = file_source
        self.tid = tid
        self.upload_target = upload_target

    def validate(self):
        if self.upload_target:
            self.upload_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.upload_target is not None:
            result['UploadTarget'] = self.upload_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UploadTarget') is not None:
            temp_model = CreateUploadOSSFileJobRequestUploadTarget()
            self.upload_target = temp_model.from_map(m['UploadTarget'])
        return self


class CreateUploadOSSFileJobShrinkRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_source: str = None,
        tid: int = None,
        upload_target_shrink: str = None,
    ):
        self.file_name = file_name
        self.file_source = file_source
        self.tid = tid
        self.upload_target_shrink = upload_target_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.upload_target_shrink is not None:
            result['UploadTarget'] = self.upload_target_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UploadTarget') is not None:
            self.upload_target_shrink = m.get('UploadTarget')
        return self


class CreateUploadOSSFileJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        job_key: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.job_key = job_key
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = CreateUploadOSSFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        sid: str = None,
        tid: int = None,
    ):
        self.host = host
        self.port = port
        self.sid = sid
        self.tid = tid

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
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLakeHouseSpaceRequest(TeaModel):
    def __init__(
        self,
        space_id: int = None,
        tid: int = None,
    ):
        self.space_id = space_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteLakeHouseSpaceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLakeHouseSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLakeHouseSpaceResponseBody = None,
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
            temp_model = DeleteLakeHouseSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLhMembersRequest(TeaModel):
    def __init__(
        self,
        member_ids: List[int] = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        self.member_ids = member_ids
        self.object_id = object_id
        self.object_type = object_type
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteLhMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        member_ids_shrink: str = None,
        object_id: int = None,
        object_type: int = None,
        tid: int = None,
    ):
        self.member_ids_shrink = member_ids_shrink
        self.object_id = object_id
        self.object_type = object_type
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_ids_shrink is not None:
            result['MemberIds'] = self.member_ids_shrink
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberIds') is not None:
            self.member_ids_shrink = m.get('MemberIds')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteLhMembersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLhMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLhMembersResponseBody = None,
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
            temp_model = DeleteLhMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogicDatabaseRequest(TeaModel):
    def __init__(
        self,
        logic_db_id: int = None,
        tid: int = None,
    ):
        self.logic_db_id = logic_db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteLogicDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLogicDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLogicDatabaseResponseBody = None,
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
            temp_model = DeleteLogicDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogicTableRouteConfigRequest(TeaModel):
    def __init__(
        self,
        route_key: str = None,
        table_id: int = None,
        tid: int = None,
    ):
        self.route_key = route_key
        self.table_id = table_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_key is not None:
            result['RouteKey'] = self.route_key
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteKey') is not None:
            self.route_key = m.get('RouteKey')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteLogicTableRouteConfigResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLogicTableRouteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLogicTableRouteConfigResponseBody = None,
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
            temp_model = DeleteLogicTableRouteConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProxyRequest(TeaModel):
    def __init__(
        self,
        proxy_id: int = None,
        tid: int = None,
    ):
        self.proxy_id = proxy_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteProxyResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProxyResponseBody = None,
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
            temp_model = DeleteProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProxyAccessRequest(TeaModel):
    def __init__(
        self,
        proxy_access_id: int = None,
        tid: int = None,
    ):
        self.proxy_access_id = proxy_access_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteProxyAccessResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProxyAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProxyAccessResponseBody = None,
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
            temp_model = DeleteProxyAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskFlowRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        tid: int = None,
    ):
        self.dag_id = dag_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class DeleteTaskFlowResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTaskFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTaskFlowResponseBody = None,
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
            temp_model = DeleteTaskFlowResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = DeleteUserResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = DisableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditLogicDatabaseRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        database_ids: List[int] = None,
        logic_db_id: int = None,
        tid: int = None,
    ):
        self.alias = alias
        self.database_ids = database_ids
        self.logic_db_id = logic_db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class EditLogicDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        database_ids_shrink: str = None,
        logic_db_id: int = None,
        tid: int = None,
    ):
        self.alias = alias
        self.database_ids_shrink = database_ids_shrink
        self.logic_db_id = logic_db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_ids_shrink is not None:
            result['DatabaseIds'] = self.database_ids_shrink
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseIds') is not None:
            self.database_ids_shrink = m.get('DatabaseIds')
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class EditLogicDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditLogicDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditLogicDatabaseResponseBody = None,
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
            temp_model = EditLogicDatabaseResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = EnableUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteDataCorrectRequest(TeaModel):
    def __init__(
        self,
        action_detail: Dict[str, Any] = None,
        order_id: int = None,
        tid: str = None,
    ):
        self.action_detail = action_detail
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteDataCorrectShrinkRequest(TeaModel):
    def __init__(
        self,
        action_detail_shrink: str = None,
        order_id: int = None,
        tid: str = None,
    ):
        self.action_detail_shrink = action_detail_shrink
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteDataCorrectResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ExecuteDataCorrectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteDataExportRequest(TeaModel):
    def __init__(
        self,
        action_detail: Dict[str, Any] = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.action_detail = action_detail
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteDataExportShrinkRequest(TeaModel):
    def __init__(
        self,
        action_detail_shrink: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.action_detail_shrink = action_detail_shrink
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteDataExportResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ExecuteDataExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteScriptRequest(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        script: str = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.script = script
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.script is not None:
            result['Script'] = self.script
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteScriptResponseBodyResults(TeaModel):
    def __init__(
        self,
        column_names: List[str] = None,
        message: str = None,
        row_count: int = None,
        rows: List[Dict[str, Any]] = None,
        success: bool = None,
    ):
        self.column_names = column_names
        self.message = message
        self.row_count = row_count
        self.rows = rows
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_names is not None:
            result['ColumnNames'] = self.column_names
        if self.message is not None:
            result['Message'] = self.message
        if self.row_count is not None:
            result['RowCount'] = self.row_count
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNames') is not None:
            self.column_names = m.get('ColumnNames')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteScriptResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        results: List[ExecuteScriptResponseBodyResults] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.results = results
        self.success = success

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ExecuteScriptResponseBodyResults()
                self.results.append(temp_model.from_map(k))
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
            temp_model = ExecuteScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteStructSyncRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ExecuteStructSyncResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ExecuteStructSyncResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler(TeaModel):
    def __init__(
        self,
        id: int = None,
        nick_name: str = None,
    ):
        self.id = id
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reasons is not None:
            result['Reasons'] = self.reasons
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reasons') is not None:
            self.reasons = m.get('Reasons')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        audit_user_id_list: GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList = None,
        node_name: str = None,
        operate_comment: str = None,
        operate_time: str = None,
        operator_id: int = None,
        workflow_ins_code: str = None,
    ):
        self.audit_user_id_list = audit_user_id_list
        self.node_name = node_name
        self.operate_comment = operate_comment
        self.operate_time = operate_time
        self.operator_id = operator_id
        self.workflow_ins_code = workflow_ins_code

    def validate(self):
        if self.audit_user_id_list:
            self.audit_user_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_user_id_list is not None:
            result['AuditUserIdList'] = self.audit_user_id_list.to_map()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.operate_comment is not None:
            result['OperateComment'] = self.operate_comment
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUserIdList') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList()
            self.audit_user_id_list = temp_model.from_map(m['AuditUserIdList'])
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('OperateComment') is not None:
            self.operate_comment = m.get('OperateComment')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetApprovalDetailResponseBodyApprovalDetail(TeaModel):
    def __init__(
        self,
        audit_id: int = None,
        create_time: str = None,
        current_handlers: GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers = None,
        description: str = None,
        order_id: int = None,
        order_type: str = None,
        reason_list: GetApprovalDetailResponseBodyApprovalDetailReasonList = None,
        title: str = None,
        workflow_ins_code: str = None,
        workflow_nodes: GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes = None,
    ):
        self.audit_id = audit_id
        self.create_time = create_time
        self.current_handlers = current_handlers
        self.description = description
        self.order_id = order_id
        self.order_type = order_type
        self.reason_list = reason_list
        self.title = title
        self.workflow_ins_code = workflow_ins_code
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.current_handlers:
            self.current_handlers.validate()
        if self.reason_list:
            self.reason_list.validate()
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_id is not None:
            result['AuditId'] = self.audit_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_handlers is not None:
            result['CurrentHandlers'] = self.current_handlers.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.reason_list is not None:
            result['ReasonList'] = self.reason_list.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditId') is not None:
            self.audit_id = m.get('AuditId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentHandlers') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers()
            self.current_handlers = temp_model.from_map(m['CurrentHandlers'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ReasonList') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailReasonList()
            self.reason_list = temp_model.from_map(m['ReasonList'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('WorkflowInsCode') is not None:
            self.workflow_ins_code = m.get('WorkflowInsCode')
        if m.get('WorkflowNodes') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
        return self


class GetApprovalDetailResponseBody(TeaModel):
    def __init__(
        self,
        approval_detail: GetApprovalDetailResponseBodyApprovalDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.approval_detail = approval_detail
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.approval_detail:
            self.approval_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalDetail') is not None:
            temp_model = GetApprovalDetailResponseBodyApprovalDetail()
            self.approval_detail = temp_model.from_map(m['ApprovalDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetApprovalDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBTaskSQLJobLogRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        tid: int = None,
    ):
        self.job_id = job_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDBTaskSQLJobLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        log: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.log = log
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.log is not None:
            result['Log'] = self.log
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Log') is not None:
            self.log = m.get('Log')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDBTaskSQLJobLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDBTaskSQLJobLogResponseBody = None,
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
            temp_model = GetDBTaskSQLJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBTopologyRequest(TeaModel):
    def __init__(
        self,
        logic_db_id: int = None,
        tid: int = None,
    ):
        self.logic_db_id = logic_db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        instance_id: int = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        region_id: str = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        self.catalog_name = catalog_name
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.instance_id = instance_id
        self.instance_resource_id = instance_resource_id
        self.instance_source = instance_source
        self.region_id = region_id
        self.schema_name = schema_name
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetDBTopologyResponseBodyDBTopology(TeaModel):
    def __init__(
        self,
        alias: str = None,
        dbtopology_info_list: List[GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList] = None,
        db_type: str = None,
        env_type: str = None,
        logic_db_id: int = None,
        logic_db_name: str = None,
        search_name: str = None,
    ):
        self.alias = alias
        self.dbtopology_info_list = dbtopology_info_list
        self.db_type = db_type
        self.env_type = env_type
        self.logic_db_id = logic_db_id
        self.logic_db_name = logic_db_name
        self.search_name = search_name

    def validate(self):
        if self.dbtopology_info_list:
            for k in self.dbtopology_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        result['DBTopologyInfoList'] = []
        if self.dbtopology_info_list is not None:
            for k in self.dbtopology_info_list:
                result['DBTopologyInfoList'].append(k.to_map() if k else None)
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id
        if self.logic_db_name is not None:
            result['LogicDbName'] = self.logic_db_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        self.dbtopology_info_list = []
        if m.get('DBTopologyInfoList') is not None:
            for k in m.get('DBTopologyInfoList'):
                temp_model = GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList()
                self.dbtopology_info_list.append(temp_model.from_map(k))
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')
        if m.get('LogicDbName') is not None:
            self.logic_db_name = m.get('LogicDbName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetDBTopologyResponseBody(TeaModel):
    def __init__(
        self,
        dbtopology: GetDBTopologyResponseBodyDBTopology = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dbtopology = dbtopology
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dbtopology:
            self.dbtopology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtopology is not None:
            result['DBTopology'] = self.dbtopology.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTopology') is not None:
            temp_model = GetDBTopologyResponseBodyDBTopology()
            self.dbtopology = temp_model.from_map(m['DBTopology'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDBTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDBTopologyResponseBody = None,
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
            temp_model = GetDBTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectBackupFilesRequest(TeaModel):
    def __init__(
        self,
        action_detail: Dict[str, Any] = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.action_detail = action_detail
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail is not None:
            result['ActionDetail'] = self.action_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataCorrectBackupFilesShrinkRequest(TeaModel):
    def __init__(
        self,
        action_detail_shrink: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.action_detail_shrink = action_detail_shrink
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data_correct_backup_files: GetDataCorrectBackupFilesResponseBodyDataCorrectBackupFiles = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data_correct_backup_files = data_correct_backup_files
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_correct_backup_files:
            self.data_correct_backup_files.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_correct_backup_files is not None:
            result['DataCorrectBackupFiles'] = self.data_correct_backup_files.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCorrectBackupFiles') is not None:
            temp_model = GetDataCorrectBackupFilesResponseBodyDataCorrectBackupFiles()
            self.data_correct_backup_files = temp_model.from_map(m['DataCorrectBackupFiles'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetDataCorrectBackupFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail(TeaModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        attachment_name: str = None,
        classify: str = None,
        estimate_affect_rows: int = None,
        exe_sql: str = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        rb_attachment_name: str = None,
        rb_sql: str = None,
        rb_sqltype: str = None,
        sql_type: str = None,
    ):
        self.actual_affect_rows = actual_affect_rows
        self.attachment_name = attachment_name
        self.classify = classify
        self.estimate_affect_rows = estimate_affect_rows
        self.exe_sql = exe_sql
        self.ignore_affect_rows = ignore_affect_rows
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        self.rb_attachment_name = rb_attachment_name
        self.rb_sql = rb_sql
        self.rb_sqltype = rb_sqltype
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.estimate_affect_rows is not None:
            result['EstimateAffectRows'] = self.estimate_affect_rows
        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql
        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows
        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason
        if self.rb_attachment_name is not None:
            result['RbAttachmentName'] = self.rb_attachment_name
        if self.rb_sql is not None:
            result['RbSQL'] = self.rb_sql
        if self.rb_sqltype is not None:
            result['RbSQLType'] = self.rb_sqltype
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('EstimateAffectRows') is not None:
            self.estimate_affect_rows = m.get('EstimateAffectRows')
        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')
        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')
        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')
        if m.get('RbAttachmentName') is not None:
            self.rb_attachment_name = m.get('RbAttachmentName')
        if m.get('RbSQL') is not None:
            self.rb_sql = m.get('RbSQL')
        if m.get('RbSQLType') is not None:
            self.rb_sqltype = m.get('RbSQLType')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        check_step: str = None,
        user_tip: str = None,
    ):
        self.check_status = check_status
        self.check_step = check_step
        self.user_tip = user_tip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.check_step is not None:
            result['CheckStep'] = self.check_step
        if self.user_tip is not None:
            result['UserTip'] = self.user_tip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckStep') is not None:
            self.check_step = m.get('CheckStep')
        if m.get('UserTip') is not None:
            self.user_tip = m.get('UserTip')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail(TeaModel):
    def __init__(
        self,
        database_list: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList = None,
        order_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail = None,
        pre_check_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail = None,
        status: str = None,
    ):
        self.database_list = database_list
        self.order_detail = order_detail
        self.pre_check_detail = pre_check_detail
        self.status = status

    def validate(self):
        if self.database_list:
            self.database_list.validate()
        if self.order_detail:
            self.order_detail.validate()
        if self.pre_check_detail:
            self.pre_check_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_list is not None:
            result['DatabaseList'] = self.database_list.to_map()
        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()
        if self.pre_check_detail is not None:
            result['PreCheckDetail'] = self.pre_check_detail.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseList') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList()
            self.database_list = temp_model.from_map(m['DatabaseList'])
        if m.get('OrderDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail()
            self.order_detail = temp_model.from_map(m['OrderDetail'])
        if m.get('PreCheckDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail()
            self.pre_check_detail = temp_model.from_map(m['PreCheckDetail'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDataCorrectOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_correct_order_detail: GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data_correct_order_detail = data_correct_order_detail
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_correct_order_detail:
            self.data_correct_order_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_correct_order_detail is not None:
            result['DataCorrectOrderDetail'] = self.data_correct_order_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCorrectOrderDetail') is not None:
            temp_model = GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail()
            self.data_correct_order_detail = temp_model.from_map(m['DataCorrectOrderDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetDataCorrectOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectSQLFileRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataCorrectSQLFileResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.file_url = file_url
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetDataCorrectSQLFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCorrectTaskDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail(TeaModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        create_time: str = None,
        dbtask_group_id: int = None,
        job_status: str = None,
    ):
        self.actual_affect_rows = actual_affect_rows
        self.create_time = create_time
        self.dbtask_group_id = dbtask_group_id
        self.job_status = job_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        return self


class GetDataCorrectTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_correct_task_detail: GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data_correct_task_detail = data_correct_task_detail
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_correct_task_detail:
            self.data_correct_task_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_correct_task_detail is not None:
            result['DataCorrectTaskDetail'] = self.data_correct_task_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCorrectTaskDetail') is not None:
            temp_model = GetDataCorrectTaskDetailResponseBodyDataCorrectTaskDetail()
            self.data_correct_task_detail = temp_model.from_map(m['DataCorrectTaskDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataCorrectTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataCorrectTaskDetailResponseBody = None,
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
            temp_model = GetDataCorrectTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataCronClearTaskDetailListRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataCronClearTaskDetailListResponseBodyDataCronClearTaskDetailList(TeaModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        create_time: str = None,
        dbtask_group_id: int = None,
        job_status: str = None,
    ):
        self.actual_affect_rows = actual_affect_rows
        self.create_time = create_time
        self.dbtask_group_id = dbtask_group_id
        self.job_status = job_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.job_status is not None:
            result['jobStatus'] = self.job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')
        return self


class GetDataCronClearTaskDetailListResponseBody(TeaModel):
    def __init__(
        self,
        data_cron_clear_task_detail_list: List[GetDataCronClearTaskDetailListResponseBodyDataCronClearTaskDetailList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.data_cron_clear_task_detail_list = data_cron_clear_task_detail_list
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data_cron_clear_task_detail_list:
            for k in self.data_cron_clear_task_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataCronClearTaskDetailList'] = []
        if self.data_cron_clear_task_detail_list is not None:
            for k in self.data_cron_clear_task_detail_list:
                result['DataCronClearTaskDetailList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_cron_clear_task_detail_list = []
        if m.get('DataCronClearTaskDetailList') is not None:
            for k in m.get('DataCronClearTaskDetailList'):
                temp_model = GetDataCronClearTaskDetailListResponseBodyDataCronClearTaskDetailList()
                self.data_cron_clear_task_detail_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetDataCronClearTaskDetailListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDataCronClearTaskDetailListResponseBody = None,
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
            temp_model = GetDataCronClearTaskDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataExportDownloadURLRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.download_urlresult = download_urlresult
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.download_urlresult:
            self.download_urlresult.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_urlresult is not None:
            result['DownloadURLResult'] = self.download_urlresult.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadURLResult') is not None:
            temp_model = GetDataExportDownloadURLResponseBodyDownloadURLResult()
            self.download_urlresult = temp_model.from_map(m['DownloadURLResult'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetDataExportDownloadURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataExportOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetDataExportOrderDetailResponseBodyDataExportOrderDetailKeyInfo(TeaModel):
    def __init__(
        self,
        job_status: str = None,
        pre_check_id: int = None,
    ):
        self.job_status = job_status
        self.pre_check_id = pre_check_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.pre_check_id is not None:
            result['PreCheckId'] = self.pre_check_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('PreCheckId') is not None:
            self.pre_check_id = m.get('PreCheckId')
        return self


class GetDataExportOrderDetailResponseBodyDataExportOrderDetailOrderDetail(TeaModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        classify: str = None,
        database: str = None,
        db_id: int = None,
        env_type: str = None,
        exe_sql: str = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        logic: bool = None,
    ):
        self.actual_affect_rows = actual_affect_rows
        self.classify = classify
        self.database = database
        self.db_id = db_id
        self.env_type = env_type
        self.exe_sql = exe_sql
        self.ignore_affect_rows = ignore_affect_rows
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.database is not None:
            result['Database'] = self.database
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql
        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows
        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason
        if self.logic is not None:
            result['Logic'] = self.logic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')
        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')
        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data_export_order_detail: GetDataExportOrderDetailResponseBodyDataExportOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data_export_order_detail = data_export_order_detail
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data_export_order_detail:
            self.data_export_order_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_export_order_detail is not None:
            result['DataExportOrderDetail'] = self.data_export_order_detail.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataExportOrderDetail') is not None:
            temp_model = GetDataExportOrderDetailResponseBodyDataExportOrderDetail()
            self.data_export_order_detail = temp_model.from_map(m['DataExportOrderDetail'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetDataExportOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        schema_name: str = None,
        sid: str = None,
        tid: int = None,
    ):
        self.host = host
        self.port = port
        self.schema_name = schema_name
        self.sid = sid
        self.tid = tid

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
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        catalog_name: str = None,
        database_id: str = None,
        db_type: str = None,
        dba_id: str = None,
        dba_name: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        owner_id_list: GetDatabaseResponseBodyDatabaseOwnerIdList = None,
        owner_name_list: GetDatabaseResponseBodyDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
        state: str = None,
    ):
        self.catalog_name = catalog_name
        self.database_id = database_id
        self.db_type = db_type
        self.dba_id = dba_id
        self.dba_name = dba_name
        self.encoding = encoding
        self.env_type = env_type
        self.host = host
        self.instance_id = instance_id
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.schema_name = schema_name
        self.search_name = search_name
        self.sid = sid
        self.state = state

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_name is not None:
            result['DbaName'] = self.dba_name
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerIdList') is not None:
            temp_model = GetDatabaseResponseBodyDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = GetDatabaseResponseBodyDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database: GetDatabaseResponseBodyDatabase = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.database = database
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = GetDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
        sid: str = None,
        tid: int = None,
    ):
        self.host = host
        self.port = port
        self.sid = sid
        self.tid = tid

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
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class GetInstanceResponseBodyInstanceStandardGroup(TeaModel):
    def __init__(
        self,
        group_mode: str = None,
        group_name: str = None,
    ):
        self.group_mode = group_mode
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: str = None,
        dba_nick_name: str = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        owner_id_list: GetInstanceResponseBodyInstanceOwnerIdList = None,
        owner_name_list: GetInstanceResponseBodyInstanceOwnerNameList = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule_id: str = None,
        sid: str = None,
        standard_group: GetInstanceResponseBodyInstanceStandardGroup = None,
        state: str = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        self.data_link_name = data_link_name
        self.database_password = database_password
        self.database_user = database_user
        self.dba_id = dba_id
        self.dba_nick_name = dba_nick_name
        self.ddl_online = ddl_online
        self.ecs_instance_id = ecs_instance_id
        self.ecs_region = ecs_region
        self.env_type = env_type
        self.export_timeout = export_timeout
        self.host = host
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.query_timeout = query_timeout
        self.safe_rule_id = safe_rule_id
        self.sid = sid
        self.standard_group = standard_group
        self.state = state
        self.use_dsql = use_dsql
        self.vpc_id = vpc_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()
        if self.standard_group:
            self.standard_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerIdList') is not None:
            temp_model = GetInstanceResponseBodyInstanceOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = GetInstanceResponseBodyInstanceOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('StandardGroup') is not None:
            temp_model = GetInstanceResponseBodyInstanceStandardGroup()
            self.standard_group = temp_model.from_map(m['StandardGroup'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance: GetInstanceResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.instance = instance
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Instance') is not None:
            temp_model = GetInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLhSpaceByNameRequest(TeaModel):
    def __init__(
        self,
        space_name: str = None,
        tid: int = None,
    ):
        self.space_name = space_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_name is not None:
            result['SpaceName'] = self.space_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetLhSpaceByNameResponseBodyLakehouseSpace(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        description: str = None,
        dev_db_id: int = None,
        dw_db_type: str = None,
        id: int = None,
        is_deleted: bool = None,
        mode: int = None,
        prod_db_id: int = None,
        space_config: str = None,
        space_name: str = None,
        tenant_id: str = None,
    ):
        self.creator_id = creator_id
        self.description = description
        self.dev_db_id = dev_db_id
        self.dw_db_type = dw_db_type
        self.id = id
        self.is_deleted = is_deleted
        self.mode = mode
        self.prod_db_id = prod_db_id
        self.space_config = space_config
        self.space_name = space_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_db_id is not None:
            result['DevDbId'] = self.dev_db_id
        if self.dw_db_type is not None:
            result['DwDbType'] = self.dw_db_type
        if self.id is not None:
            result['Id'] = self.id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.prod_db_id is not None:
            result['ProdDbId'] = self.prod_db_id
        if self.space_config is not None:
            result['SpaceConfig'] = self.space_config
        if self.space_name is not None:
            result['SpaceName'] = self.space_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevDbId') is not None:
            self.dev_db_id = m.get('DevDbId')
        if m.get('DwDbType') is not None:
            self.dw_db_type = m.get('DwDbType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('ProdDbId') is not None:
            self.prod_db_id = m.get('ProdDbId')
        if m.get('SpaceConfig') is not None:
            self.space_config = m.get('SpaceConfig')
        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetLhSpaceByNameResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        lakehouse_space: GetLhSpaceByNameResponseBodyLakehouseSpace = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.lakehouse_space = lakehouse_space
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.lakehouse_space:
            self.lakehouse_space.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.lakehouse_space is not None:
            result['LakehouseSpace'] = self.lakehouse_space.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LakehouseSpace') is not None:
            temp_model = GetLhSpaceByNameResponseBodyLakehouseSpace()
            self.lakehouse_space = temp_model.from_map(m['LakehouseSpace'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLhSpaceByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLhSpaceByNameResponseBody = None,
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
            temp_model = GetLhSpaceByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogicDatabaseRequest(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        alias: str = None,
        database_id: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList = None,
        owner_name_list: GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        self.alias = alias
        self.database_id = database_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.schema_name = schema_name
        self.search_name = search_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIdList') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetLogicDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_database: GetLogicDatabaseResponseBodyLogicDatabase = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.logic_database = logic_database
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.logic_database:
            self.logic_database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logic_database is not None:
            result['LogicDatabase'] = self.logic_database.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogicDatabase') is not None:
            temp_model = GetLogicDatabaseResponseBodyLogicDatabase()
            self.logic_database = temp_model.from_map(m['LogicDatabase'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetLogicDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetaTableColumnRequest(TeaModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        self.table_guid = table_guid
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetMetaTableColumnResponseBodyColumnList(TeaModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        column_type: str = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        description: str = None,
        nullable: bool = None,
        position: int = None,
        primary_key: str = None,
        security_level: str = None,
    ):
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.column_name = column_name
        self.column_type = column_type
        self.data_length = data_length
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.description = description
        self.nullable = nullable
        self.position = position
        self.primary_key = primary_key
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.description is not None:
            result['Description'] = self.description
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.position is not None:
            result['Position'] = self.position
        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetMetaTableColumnResponseBody(TeaModel):
    def __init__(
        self,
        column_list: List[GetMetaTableColumnResponseBodyColumnList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.column_list = column_list
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k in m.get('ColumnList'):
                temp_model = GetMetaTableColumnResponseBodyColumnList()
                self.column_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetMetaTableColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetaTableDetailInfoRequest(TeaModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        self.table_guid = table_guid
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfoColumnList(TeaModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        column_type: str = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        description: str = None,
        nullable: bool = None,
        position: str = None,
    ):
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.column_name = column_name
        self.column_type = column_type
        self.data_length = data_length
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.description = description
        self.nullable = nullable
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.description is not None:
            result['Description'] = self.description
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfoIndexList(TeaModel):
    def __init__(
        self,
        index_columns: List[str] = None,
        index_id: str = None,
        index_name: str = None,
        index_type: str = None,
        unique: bool = None,
    ):
        self.index_columns = index_columns
        self.index_id = index_id
        self.index_name = index_name
        self.index_type = index_type
        self.unique = unique

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_columns is not None:
            result['IndexColumns'] = self.index_columns
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_type is not None:
            result['IndexType'] = self.index_type
        if self.unique is not None:
            result['Unique'] = self.unique
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexColumns') is not None:
            self.index_columns = m.get('IndexColumns')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')
        if m.get('Unique') is not None:
            self.unique = m.get('Unique')
        return self


class GetMetaTableDetailInfoResponseBodyDetailInfo(TeaModel):
    def __init__(
        self,
        column_list: List[GetMetaTableDetailInfoResponseBodyDetailInfoColumnList] = None,
        index_list: List[GetMetaTableDetailInfoResponseBodyDetailInfoIndexList] = None,
    ):
        self.column_list = column_list
        self.index_list = index_list

    def validate(self):
        if self.column_list:
            for k in self.column_list:
                if k:
                    k.validate()
        if self.index_list:
            for k in self.index_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ColumnList'] = []
        if self.column_list is not None:
            for k in self.column_list:
                result['ColumnList'].append(k.to_map() if k else None)
        result['IndexList'] = []
        if self.index_list is not None:
            for k in self.index_list:
                result['IndexList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k in m.get('ColumnList'):
                temp_model = GetMetaTableDetailInfoResponseBodyDetailInfoColumnList()
                self.column_list.append(temp_model.from_map(k))
        self.index_list = []
        if m.get('IndexList') is not None:
            for k in m.get('IndexList'):
                temp_model = GetMetaTableDetailInfoResponseBodyDetailInfoIndexList()
                self.index_list.append(temp_model.from_map(k))
        return self


class GetMetaTableDetailInfoResponseBody(TeaModel):
    def __init__(
        self,
        detail_info: GetMetaTableDetailInfoResponseBodyDetailInfo = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.detail_info = detail_info
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.detail_info:
            self.detail_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_info is not None:
            result['DetailInfo'] = self.detail_info.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailInfo') is not None:
            temp_model = GetMetaTableDetailInfoResponseBodyDetailInfo()
            self.detail_info = temp_model.from_map(m['DetailInfo'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetMetaTableDetailInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpLogRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        module: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        tid: int = None,
    ):
        self.end_time = end_time
        self.module = module
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.module is not None:
            result['Module'] = self.module
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetOpLogResponseBodyOpLogDetailsOpLogDetail(TeaModel):
    def __init__(
        self,
        database: str = None,
        module: str = None,
        op_content: str = None,
        op_time: str = None,
        op_user_id: int = None,
        order_id: int = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        self.database = database
        self.module = module
        self.op_content = op_content
        self.op_time = op_time
        self.op_user_id = op_user_id
        self.order_id = order_id
        self.user_id = user_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.module is not None:
            result['Module'] = self.module
        if self.op_content is not None:
            result['OpContent'] = self.op_content
        if self.op_time is not None:
            result['OpTime'] = self.op_time
        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('OpContent') is not None:
            self.op_content = m.get('OpContent')
        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')
        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        op_log_details: GetOpLogResponseBodyOpLogDetails = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.op_log_details = op_log_details
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.op_log_details:
            self.op_log_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.op_log_details is not None:
            result['OpLogDetails'] = self.op_log_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OpLogDetails') is not None:
            temp_model = GetOpLogResponseBodyOpLogDetails()
            self.op_log_details = temp_model.from_map(m['OpLogDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = GetOpLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderBaseInfoRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_nicks is not None:
            result['UserNicks'] = self.user_nicks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserNicks') is not None:
            self.user_nicks = m.get('UserNicks')
        return self


class GetOrderBaseInfoResponseBodyOrderBaseInfo(TeaModel):
    def __init__(
        self,
        comment: str = None,
        committer: str = None,
        committer_id: int = None,
        create_time: str = None,
        last_modify_time: str = None,
        order_id: int = None,
        plugin_type: str = None,
        related_user_list: GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList = None,
        related_user_nick_list: GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList = None,
        status_code: str = None,
        status_desc: str = None,
        workflow_instance_id: int = None,
        workflow_status_desc: str = None,
    ):
        self.comment = comment
        self.committer = committer
        self.committer_id = committer_id
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.order_id = order_id
        self.plugin_type = plugin_type
        self.related_user_list = related_user_list
        self.related_user_nick_list = related_user_nick_list
        self.status_code = status_code
        self.status_desc = status_desc
        self.workflow_instance_id = workflow_instance_id
        self.workflow_status_desc = workflow_status_desc

    def validate(self):
        if self.related_user_list:
            self.related_user_list.validate()
        if self.related_user_nick_list:
            self.related_user_nick_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.committer is not None:
            result['Committer'] = self.committer
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list.to_map()
        if self.related_user_nick_list is not None:
            result['RelatedUserNickList'] = self.related_user_nick_list.to_map()
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        if self.workflow_status_desc is not None:
            result['WorkflowStatusDesc'] = self.workflow_status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Committer') is not None:
            self.committer = m.get('Committer')
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('RelatedUserList') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserList()
            self.related_user_list = temp_model.from_map(m['RelatedUserList'])
        if m.get('RelatedUserNickList') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfoRelatedUserNickList()
            self.related_user_nick_list = temp_model.from_map(m['RelatedUserNickList'])
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        if m.get('WorkflowStatusDesc') is not None:
            self.workflow_status_desc = m.get('WorkflowStatusDesc')
        return self


class GetOrderBaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        order_base_info: GetOrderBaseInfoResponseBodyOrderBaseInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.order_base_info = order_base_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.order_base_info:
            self.order_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.order_base_info is not None:
            result['OrderBaseInfo'] = self.order_base_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OrderBaseInfo') is not None:
            temp_model = GetOrderBaseInfoResponseBodyOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m['OrderBaseInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetOrderBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOwnerApplyOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        search_name: str = None,
        table_name: str = None,
    ):
        self.db_type = db_type
        self.env_type = env_type
        self.owner_ids = owner_ids
        self.owner_nick_names = owner_nick_names
        self.search_name = search_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResources(TeaModel):
    def __init__(
        self,
        logic: bool = None,
        resource_detail: GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail = None,
        target_id: str = None,
    ):
        self.logic = logic
        self.resource_detail = resource_detail
        self.target_id = target_id

    def validate(self):
        if self.resource_detail:
            self.resource_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.resource_detail is not None:
            result['ResourceDetail'] = self.resource_detail.to_map()
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('ResourceDetail') is not None:
            temp_model = GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetailResourcesResourceDetail()
            self.resource_detail = temp_model.from_map(m['ResourceDetail'])
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        owner_apply_order_detail: GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.owner_apply_order_detail = owner_apply_order_detail
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.owner_apply_order_detail:
            self.owner_apply_order_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.owner_apply_order_detail is not None:
            result['OwnerApplyOrderDetail'] = self.owner_apply_order_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OwnerApplyOrderDetail') is not None:
            temp_model = GetOwnerApplyOrderDetailResponseBodyOwnerApplyOrderDetail()
            self.owner_apply_order_detail = temp_model.from_map(m['OwnerApplyOrderDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetOwnerApplyOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermApplyOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        table_name: str = None,
    ):
        self.column_name = column_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        search_name: str = None,
    ):
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.owner_ids = owner_ids
        self.owner_nick_names = owner_nick_names
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        dba_id: int = None,
        dba_nick_name: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        owner_ids: List[int] = None,
        owner_nick_name: List[str] = None,
        port: int = None,
        search_name: str = None,
    ):
        self.db_type = db_type
        self.dba_id = dba_id
        self.dba_nick_name = dba_nick_name
        self.env_type = env_type
        self.host = host
        self.instance_id = instance_id
        self.owner_ids = owner_ids
        self.owner_nick_name = owner_nick_name
        self.port = port
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name
        if self.port is not None:
            result['Port'] = self.port
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources(TeaModel):
    def __init__(
        self,
        column_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo = None,
        database_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo = None,
        instance_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo = None,
        table_info: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo = None,
    ):
        self.column_info = column_info
        self.database_info = database_info
        self.instance_info = instance_info
        self.table_info = table_info

    def validate(self):
        if self.column_info:
            self.column_info.validate()
        if self.database_info:
            self.database_info.validate()
        if self.instance_info:
            self.instance_info.validate()
        if self.table_info:
            self.table_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_info is not None:
            result['ColumnInfo'] = self.column_info.to_map()
        if self.database_info is not None:
            result['DatabaseInfo'] = self.database_info.to_map()
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo()
            self.column_info = temp_model.from_map(m['ColumnInfo'])
        if m.get('DatabaseInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo()
            self.database_info = temp_model.from_map(m['DatabaseInfo'])
        if m.get('InstanceInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        if m.get('TableInfo') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo()
            self.table_info = temp_model.from_map(m['TableInfo'])
        return self


class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail(TeaModel):
    def __init__(
        self,
        apply_type: str = None,
        perm_type: int = None,
        resources: List[GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources] = None,
        seconds: int = None,
    ):
        self.apply_type = apply_type
        self.perm_type = perm_type
        self.resources = resources
        self.seconds = seconds

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.seconds is not None:
            result['Seconds'] = self.seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Seconds') is not None:
            self.seconds = m.get('Seconds')
        return self


class GetPermApplyOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        perm_apply_order_detail: GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.perm_apply_order_detail = perm_apply_order_detail
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.perm_apply_order_detail:
            self.perm_apply_order_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.perm_apply_order_detail is not None:
            result['PermApplyOrderDetail'] = self.perm_apply_order_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PermApplyOrderDetail') is not None:
            temp_model = GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail()
            self.perm_apply_order_detail = temp_model.from_map(m['PermApplyOrderDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetPermApplyOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalDatabaseRequest(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList(TeaModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        return self


class GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList(TeaModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class GetPhysicalDatabaseResponseBodyDatabase(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        database_id: str = None,
        db_type: str = None,
        dba_id: str = None,
        dba_name: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        owner_id_list: GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList = None,
        owner_name_list: GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
        state: str = None,
    ):
        self.catalog_name = catalog_name
        self.database_id = database_id
        self.db_type = db_type
        self.dba_id = dba_id
        self.dba_name = dba_name
        self.encoding = encoding
        self.env_type = env_type
        self.host = host
        self.instance_id = instance_id
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.schema_name = schema_name
        self.search_name = search_name
        self.sid = sid
        self.state = state

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_name is not None:
            result['DbaName'] = self.dba_name
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerIdList') is not None:
            temp_model = GetPhysicalDatabaseResponseBodyDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = GetPhysicalDatabaseResponseBodyDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetPhysicalDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database: GetPhysicalDatabaseResponseBodyDatabase = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.database = database
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = GetPhysicalDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m['Database'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPhysicalDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhysicalDatabaseResponseBody = None,
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
            temp_model = GetPhysicalDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProxyRequest(TeaModel):
    def __init__(
        self,
        instance_id: int = None,
        proxy_id: int = None,
        tid: int = None,
    ):
        self.instance_id = instance_id
        self.proxy_id = proxy_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetProxyResponseBody(TeaModel):
    def __init__(
        self,
        creator_id: int = None,
        creator_name: str = None,
        error_code: str = None,
        error_message: str = None,
        https_port: int = None,
        instance_id: int = None,
        mysql_port: int = None,
        private_enable: bool = None,
        private_host: str = None,
        proxy_id: int = None,
        public_enable: bool = None,
        public_host: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.error_code = error_code
        self.error_message = error_message
        self.https_port = https_port
        self.instance_id = instance_id
        self.mysql_port = mysql_port
        self.private_enable = private_enable
        self.private_host = private_host
        self.proxy_id = proxy_id
        self.public_enable = public_enable
        self.public_host = public_host
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mysql_port is not None:
            result['MysqlPort'] = self.mysql_port
        if self.private_enable is not None:
            result['PrivateEnable'] = self.private_enable
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.public_enable is not None:
            result['PublicEnable'] = self.public_enable
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MysqlPort') is not None:
            self.mysql_port = m.get('MysqlPort')
        if m.get('PrivateEnable') is not None:
            self.private_enable = m.get('PrivateEnable')
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('PublicEnable') is not None:
            self.public_enable = m.get('PublicEnable')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProxyResponseBody = None,
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
            temp_model = GetProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSQLReviewCheckResultStatusRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult(TeaModel):
    def __init__(
        self,
        check_not_pass: int = None,
        check_pass: int = None,
        force_not_pass: int = None,
        force_pass: int = None,
        new: int = None,
        unknown: int = None,
    ):
        self.check_not_pass = check_not_pass
        self.check_pass = check_pass
        self.force_not_pass = force_not_pass
        self.force_pass = force_pass
        self.new = new
        self.unknown = unknown

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_not_pass is not None:
            result['CheckNotPass'] = self.check_not_pass
        if self.check_pass is not None:
            result['CheckPass'] = self.check_pass
        if self.force_not_pass is not None:
            result['ForceNotPass'] = self.force_not_pass
        if self.force_pass is not None:
            result['ForcePass'] = self.force_pass
        if self.new is not None:
            result['New'] = self.new
        if self.unknown is not None:
            result['Unknown'] = self.unknown
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckNotPass') is not None:
            self.check_not_pass = m.get('CheckNotPass')
        if m.get('CheckPass') is not None:
            self.check_pass = m.get('CheckPass')
        if m.get('ForceNotPass') is not None:
            self.force_not_pass = m.get('ForceNotPass')
        if m.get('ForcePass') is not None:
            self.force_pass = m.get('ForcePass')
        if m.get('New') is not None:
            self.new = m.get('New')
        if m.get('Unknown') is not None:
            self.unknown = m.get('Unknown')
        return self


class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult(TeaModel):
    def __init__(
        self,
        must_improve: int = None,
        potential_issue: int = None,
        suggest_improve: int = None,
        table_index_suggest: int = None,
        use_dms_dml_unlock: int = None,
        use_dms_toolkit: int = None,
    ):
        self.must_improve = must_improve
        self.potential_issue = potential_issue
        self.suggest_improve = suggest_improve
        self.table_index_suggest = table_index_suggest
        self.use_dms_dml_unlock = use_dms_dml_unlock
        self.use_dms_toolkit = use_dms_toolkit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.must_improve is not None:
            result['MustImprove'] = self.must_improve
        if self.potential_issue is not None:
            result['PotentialIssue'] = self.potential_issue
        if self.suggest_improve is not None:
            result['SuggestImprove'] = self.suggest_improve
        if self.table_index_suggest is not None:
            result['TableIndexSuggest'] = self.table_index_suggest
        if self.use_dms_dml_unlock is not None:
            result['UseDmsDmlUnlock'] = self.use_dms_dml_unlock
        if self.use_dms_toolkit is not None:
            result['UseDmsToolkit'] = self.use_dms_toolkit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MustImprove') is not None:
            self.must_improve = m.get('MustImprove')
        if m.get('PotentialIssue') is not None:
            self.potential_issue = m.get('PotentialIssue')
        if m.get('SuggestImprove') is not None:
            self.suggest_improve = m.get('SuggestImprove')
        if m.get('TableIndexSuggest') is not None:
            self.table_index_suggest = m.get('TableIndexSuggest')
        if m.get('UseDmsDmlUnlock') is not None:
            self.use_dms_dml_unlock = m.get('UseDmsDmlUnlock')
        if m.get('UseDmsToolkit') is not None:
            self.use_dms_toolkit = m.get('UseDmsToolkit')
        return self


class GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus(TeaModel):
    def __init__(
        self,
        check_status_result: GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult = None,
        checked_count: int = None,
        sqlreview_result: GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult = None,
        total_sqlcount: int = None,
    ):
        self.check_status_result = check_status_result
        self.checked_count = checked_count
        self.sqlreview_result = sqlreview_result
        self.total_sqlcount = total_sqlcount

    def validate(self):
        if self.check_status_result:
            self.check_status_result.validate()
        if self.sqlreview_result:
            self.sqlreview_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status_result is not None:
            result['CheckStatusResult'] = self.check_status_result.to_map()
        if self.checked_count is not None:
            result['CheckedCount'] = self.checked_count
        if self.sqlreview_result is not None:
            result['SQLReviewResult'] = self.sqlreview_result.to_map()
        if self.total_sqlcount is not None:
            result['TotalSQLCount'] = self.total_sqlcount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatusResult') is not None:
            temp_model = GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusCheckStatusResult()
            self.check_status_result = temp_model.from_map(m['CheckStatusResult'])
        if m.get('CheckedCount') is not None:
            self.checked_count = m.get('CheckedCount')
        if m.get('SQLReviewResult') is not None:
            temp_model = GetSQLReviewCheckResultStatusResponseBodyCheckResultStatusSQLReviewResult()
            self.sqlreview_result = temp_model.from_map(m['SQLReviewResult'])
        if m.get('TotalSQLCount') is not None:
            self.total_sqlcount = m.get('TotalSQLCount')
        return self


class GetSQLReviewCheckResultStatusResponseBody(TeaModel):
    def __init__(
        self,
        check_result_status: GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.check_result_status = check_result_status
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.check_result_status:
            self.check_result_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result_status is not None:
            result['CheckResultStatus'] = self.check_result_status.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResultStatus') is not None:
            temp_model = GetSQLReviewCheckResultStatusResponseBodyCheckResultStatus()
            self.check_result_status = temp_model.from_map(m['CheckResultStatus'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSQLReviewCheckResultStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSQLReviewCheckResultStatusResponseBody = None,
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
            temp_model = GetSQLReviewCheckResultStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSQLReviewOptimizeDetailRequest(TeaModel):
    def __init__(
        self,
        sqlreview_query_key: str = None,
        tid: int = None,
    ):
        self.sqlreview_query_key = sqlreview_query_key
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts(TeaModel):
    def __init__(
        self,
        content: str = None,
        op_type: str = None,
        table_name: str = None,
    ):
        self.content = content
        self.op_type = op_type
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults(TeaModel):
    def __init__(
        self,
        comments: str = None,
        feedback: str = None,
        messages: List[str] = None,
        rule_name: str = None,
        rule_type: str = None,
        scripts: List[GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts] = None,
    ):
        self.comments = comments
        self.feedback = feedback
        self.messages = messages
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.scripts = scripts

    def validate(self):
        if self.scripts:
            for k in self.scripts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.messages is not None:
            result['Messages'] = self.messages
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        result['Scripts'] = []
        if self.scripts is not None:
            for k in self.scripts:
                result['Scripts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Messages') is not None:
            self.messages = m.get('Messages')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        self.scripts = []
        if m.get('Scripts') is not None:
            for k in m.get('Scripts'):
                temp_model = GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResultsScripts()
                self.scripts.append(temp_model.from_map(k))
        return self


class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        occur_error: bool = None,
        results: List[GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults] = None,
    ):
        self.error_message = error_message
        self.occur_error = occur_error
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.occur_error is not None:
            result['OccurError'] = self.occur_error
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OccurError') is not None:
            self.occur_error = m.get('OccurError')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResultResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        instance_id: int = None,
        quality_result: GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult = None,
        query_key: str = None,
        sql_type: str = None,
    ):
        self.db_id = db_id
        self.instance_id = instance_id
        self.quality_result = quality_result
        self.query_key = query_key
        self.sql_type = sql_type

    def validate(self):
        if self.quality_result:
            self.quality_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quality_result is not None:
            result['QualityResult'] = self.quality_result.to_map()
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QualityResult') is not None:
            temp_model = GetSQLReviewOptimizeDetailResponseBodyOptimizeDetailQualityResult()
            self.quality_result = temp_model.from_map(m['QualityResult'])
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetSQLReviewOptimizeDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        optimize_detail: GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.optimize_detail = optimize_detail
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.optimize_detail:
            self.optimize_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.optimize_detail is not None:
            result['OptimizeDetail'] = self.optimize_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('OptimizeDetail') is not None:
            temp_model = GetSQLReviewOptimizeDetailResponseBodyOptimizeDetail()
            self.optimize_detail = temp_model.from_map(m['OptimizeDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSQLReviewOptimizeDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSQLReviewOptimizeDetailResponseBody = None,
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
            temp_model = GetSQLReviewOptimizeDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncExecSqlDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail(TeaModel):
    def __init__(
        self,
        exec_sql: str = None,
        total_sql_count: int = None,
    ):
        self.exec_sql = exec_sql
        self.total_sql_count = total_sql_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_sql is not None:
            result['ExecSql'] = self.exec_sql
        if self.total_sql_count is not None:
            result['TotalSqlCount'] = self.total_sql_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecSql') is not None:
            self.exec_sql = m.get('ExecSql')
        if m.get('TotalSqlCount') is not None:
            self.total_sql_count = m.get('TotalSqlCount')
        return self


class GetStructSyncExecSqlDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_exec_sql_detail: GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.struct_sync_exec_sql_detail = struct_sync_exec_sql_detail
        self.success = success

    def validate(self):
        if self.struct_sync_exec_sql_detail:
            self.struct_sync_exec_sql_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.struct_sync_exec_sql_detail is not None:
            result['StructSyncExecSqlDetail'] = self.struct_sync_exec_sql_detail.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StructSyncExecSqlDetail') is not None:
            temp_model = GetStructSyncExecSqlDetailResponseBodyStructSyncExecSqlDetail()
            self.struct_sync_exec_sql_detail = temp_model.from_map(m['StructSyncExecSqlDetail'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetStructSyncExecSqlDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncJobAnalyzeResultRequest(TeaModel):
    def __init__(
        self,
        compare_type: str = None,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.compare_type = compare_type
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compare_type is not None:
            result['CompareType'] = self.compare_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompareType') is not None:
            self.compare_type = m.get('CompareType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList(TeaModel):
    def __init__(
        self,
        script: str = None,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        self.script = script
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script is not None:
            result['Script'] = self.script
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult(TeaModel):
    def __init__(
        self,
        result_list: List[GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList] = None,
        summary_list: List[GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList] = None,
    ):
        self.result_list = result_list
        self.summary_list = summary_list

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()
        if self.summary_list:
            for k in self.summary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        result['SummaryList'] = []
        if self.summary_list is not None:
            for k in self.summary_list:
                result['SummaryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultResultList()
                self.result_list.append(temp_model.from_map(k))
        self.summary_list = []
        if m.get('SummaryList') is not None:
            for k in m.get('SummaryList'):
                temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResultSummaryList()
                self.summary_list.append(temp_model.from_map(k))
        return self


class GetStructSyncJobAnalyzeResultResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_job_analyze_result: GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.struct_sync_job_analyze_result = struct_sync_job_analyze_result
        self.success = success

    def validate(self):
        if self.struct_sync_job_analyze_result:
            self.struct_sync_job_analyze_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.struct_sync_job_analyze_result is not None:
            result['StructSyncJobAnalyzeResult'] = self.struct_sync_job_analyze_result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StructSyncJobAnalyzeResult') is not None:
            temp_model = GetStructSyncJobAnalyzeResultResponseBodyStructSyncJobAnalyzeResult()
            self.struct_sync_job_analyze_result = temp_model.from_map(m['StructSyncJobAnalyzeResult'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetStructSyncJobAnalyzeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncJobDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetStructSyncJobDetailResponseBodyStructSyncJobDetail(TeaModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        execute_count: int = None,
        job_status: str = None,
        message: str = None,
        security_rule: str = None,
        sql_count: int = None,
        table_analyzed: int = None,
        table_count: int = None,
    ):
        self.dbtask_group_id = dbtask_group_id
        self.execute_count = execute_count
        self.job_status = job_status
        self.message = message
        self.security_rule = security_rule
        self.sql_count = sql_count
        self.table_analyzed = table_analyzed
        self.table_count = table_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.message is not None:
            result['Message'] = self.message
        if self.security_rule is not None:
            result['SecurityRule'] = self.security_rule
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.table_analyzed is not None:
            result['TableAnalyzed'] = self.table_analyzed
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SecurityRule') is not None:
            self.security_rule = m.get('SecurityRule')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('TableAnalyzed') is not None:
            self.table_analyzed = m.get('TableAnalyzed')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        return self


class GetStructSyncJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_job_detail: GetStructSyncJobDetailResponseBodyStructSyncJobDetail = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.struct_sync_job_detail = struct_sync_job_detail
        self.success = success

    def validate(self):
        if self.struct_sync_job_detail:
            self.struct_sync_job_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.struct_sync_job_detail is not None:
            result['StructSyncJobDetail'] = self.struct_sync_job_detail.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StructSyncJobDetail') is not None:
            temp_model = GetStructSyncJobDetailResponseBodyStructSyncJobDetail()
            self.struct_sync_job_detail = temp_model.from_map(m['StructSyncJobDetail'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetStructSyncJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStructSyncOrderDetailRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail(TeaModel):
    def __init__(
        self,
        ignore_error: bool = None,
        source_database_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo = None,
        source_type: str = None,
        source_version_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo = None,
        table_info_list: List[GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList] = None,
        target_database_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo = None,
        target_type: str = None,
        target_version_info: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo = None,
    ):
        self.ignore_error = ignore_error
        self.source_database_info = source_database_info
        self.source_type = source_type
        self.source_version_info = source_version_info
        self.table_info_list = table_info_list
        self.target_database_info = target_database_info
        self.target_type = target_type
        self.target_version_info = target_version_info

    def validate(self):
        if self.source_database_info:
            self.source_database_info.validate()
        if self.source_version_info:
            self.source_version_info.validate()
        if self.table_info_list:
            for k in self.table_info_list:
                if k:
                    k.validate()
        if self.target_database_info:
            self.target_database_info.validate()
        if self.target_version_info:
            self.target_version_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error
        if self.source_database_info is not None:
            result['SourceDatabaseInfo'] = self.source_database_info.to_map()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_version_info is not None:
            result['SourceVersionInfo'] = self.source_version_info.to_map()
        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k in self.table_info_list:
                result['TableInfoList'].append(k.to_map() if k else None)
        if self.target_database_info is not None:
            result['TargetDatabaseInfo'] = self.target_database_info.to_map()
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.target_version_info is not None:
            result['TargetVersionInfo'] = self.target_version_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')
        if m.get('SourceDatabaseInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo()
            self.source_database_info = temp_model.from_map(m['SourceDatabaseInfo'])
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceVersionInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo()
            self.source_version_info = temp_model.from_map(m['SourceVersionInfo'])
        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k in m.get('TableInfoList'):
                temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList()
                self.table_info_list.append(temp_model.from_map(k))
        if m.get('TargetDatabaseInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo()
            self.target_database_info = temp_model.from_map(m['TargetDatabaseInfo'])
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TargetVersionInfo') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo()
            self.target_version_info = temp_model.from_map(m['TargetVersionInfo'])
        return self


class GetStructSyncOrderDetailResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_order_detail: GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.struct_sync_order_detail = struct_sync_order_detail
        self.success = success

    def validate(self):
        if self.struct_sync_order_detail:
            self.struct_sync_order_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.struct_sync_order_detail is not None:
            result['StructSyncOrderDetail'] = self.struct_sync_order_detail.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StructSyncOrderDetail') is not None:
            temp_model = GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail()
            self.struct_sync_order_detail = temp_model.from_map(m['StructSyncOrderDetail'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetStructSyncOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableDBTopologyRequest(TeaModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        self.table_guid = table_guid
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList(TeaModel):
    def __init__(
        self,
        table_id: str = None,
        table_name: str = None,
        table_type: str = None,
    ):
        self.table_id = table_id
        self.table_name = table_name
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        db_name: str = None,
        db_type: str = None,
        env_type: str = None,
        table_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList] = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.db_type = db_type
        self.env_type = env_type
        self.table_list = table_list

    def validate(self):
        if self.table_list:
            for k in self.table_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        result['TableList'] = []
        if self.table_list is not None:
            for k in self.table_list:
                result['TableList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        self.table_list = []
        if m.get('TableList') is not None:
            for k in m.get('TableList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList()
                self.table_list.append(temp_model.from_map(k))
        return self


class GetTableDBTopologyResponseBodyDBTopologyDataSourceList(TeaModel):
    def __init__(
        self,
        database_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList] = None,
        db_type: str = None,
        host: str = None,
        port: int = None,
        sid: str = None,
    ):
        self.database_list = database_list
        self.db_type = db_type
        self.host = host
        self.port = port
        self.sid = sid

    def validate(self):
        if self.database_list:
            for k in self.database_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k in self.database_list:
                result['DatabaseList'].append(k.to_map() if k else None)
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.sid is not None:
            result['Sid'] = self.sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k in m.get('DatabaseList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList()
                self.database_list.append(temp_model.from_map(k))
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        return self


class GetTableDBTopologyResponseBodyDBTopology(TeaModel):
    def __init__(
        self,
        data_source_list: List[GetTableDBTopologyResponseBodyDBTopologyDataSourceList] = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        self.data_source_list = data_source_list
        self.table_guid = table_guid
        self.table_name = table_name

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
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_list = []
        if m.get('DataSourceList') is not None:
            for k in m.get('DataSourceList'):
                temp_model = GetTableDBTopologyResponseBodyDBTopologyDataSourceList()
                self.data_source_list.append(temp_model.from_map(k))
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableDBTopologyResponseBody(TeaModel):
    def __init__(
        self,
        dbtopology: GetTableDBTopologyResponseBodyDBTopology = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.dbtopology = dbtopology
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dbtopology:
            self.dbtopology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtopology is not None:
            result['DBTopology'] = self.dbtopology.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTopology') is not None:
            temp_model = GetTableDBTopologyResponseBodyDBTopology()
            self.dbtopology = temp_model.from_map(m['DBTopology'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GetTableDBTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableTopologyRequest(TeaModel):
    def __init__(
        self,
        table_guid: str = None,
        tid: int = None,
    ):
        self.table_guid = table_guid
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        db_search_name: str = None,
        db_type: str = None,
        instance_id: int = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        region_id: str = None,
        table_count: int = None,
        table_name_expr: str = None,
        table_name_list: str = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.db_search_name = db_search_name
        self.db_type = db_type
        self.instance_id = instance_id
        self.instance_resource_id = instance_resource_id
        self.instance_source = instance_source
        self.region_id = region_id
        self.table_count = table_count
        self.table_name_expr = table_name_expr
        self.table_name_list = table_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        if self.table_name_expr is not None:
            result['TableNameExpr'] = self.table_name_expr
        if self.table_name_list is not None:
            result['TableNameList'] = self.table_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        if m.get('TableNameExpr') is not None:
            self.table_name_expr = m.get('TableNameExpr')
        if m.get('TableNameList') is not None:
            self.table_name_list = m.get('TableNameList')
        return self


class GetTableTopologyResponseBodyTableTopology(TeaModel):
    def __init__(
        self,
        logic: bool = None,
        table_guid: str = None,
        table_name: str = None,
        table_topology_info_list: List[GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList] = None,
    ):
        self.logic = logic
        self.table_guid = table_guid
        self.table_name = table_name
        self.table_topology_info_list = table_topology_info_list

    def validate(self):
        if self.table_topology_info_list:
            for k in self.table_topology_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        result['TableTopologyInfoList'] = []
        if self.table_topology_info_list is not None:
            for k in self.table_topology_info_list:
                result['TableTopologyInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        self.table_topology_info_list = []
        if m.get('TableTopologyInfoList') is not None:
            for k in m.get('TableTopologyInfoList'):
                temp_model = GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList()
                self.table_topology_info_list.append(temp_model.from_map(k))
        return self


class GetTableTopologyResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table_topology: GetTableTopologyResponseBodyTableTopology = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.table_topology = table_topology

    def validate(self):
        if self.table_topology:
            self.table_topology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_topology is not None:
            result['TableTopology'] = self.table_topology.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableTopology') is not None:
            temp_model = GetTableTopologyResponseBodyTableTopology()
            self.table_topology = temp_model.from_map(m['TableTopology'])
        return self


class GetTableTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTableTopologyResponseBody = None,
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
            temp_model = GetTableTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskInstanceRelationRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_instance_id: int = None,
        tid: int = None,
    ):
        self.dag_id = dag_id
        self.dag_instance_id = dag_instance_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_instance_id is not None:
            result['DagInstanceId'] = self.dag_instance_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagInstanceId') is not None:
            self.dag_instance_id = m.get('DagInstanceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetTaskInstanceRelationResponseBodyNodeListNode(TeaModel):
    def __init__(
        self,
        business_time: str = None,
        end_time: str = None,
        execute_time: int = None,
        id: int = None,
        message: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: int = None,
        status: int = None,
    ):
        self.business_time = business_time
        self.end_time = end_time
        self.execute_time = execute_time
        self.id = id
        self.message = message
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTaskInstanceRelationResponseBodyNodeList(TeaModel):
    def __init__(
        self,
        node: List[GetTaskInstanceRelationResponseBodyNodeListNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = GetTaskInstanceRelationResponseBodyNodeListNode()
                self.node.append(temp_model.from_map(k))
        return self


class GetTaskInstanceRelationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        node_list: GetTaskInstanceRelationResponseBodyNodeList = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.node_list = node_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_list:
            self.node_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.node_list is not None:
            result['NodeList'] = self.node_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('NodeList') is not None:
            temp_model = GetTaskInstanceRelationResponseBodyNodeList()
            self.node_list = temp_model.from_map(m['NodeList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTaskInstanceRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskInstanceRelationResponseBody = None,
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
            temp_model = GetTaskInstanceRelationResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        cur_execute_count: int = None,
        cur_result_count: int = None,
        ding_robot: str = None,
        email: str = None,
        last_login_time: str = None,
        max_execute_count: int = None,
        max_result_count: int = None,
        mobile: str = None,
        nick_name: str = None,
        notification_mode: str = None,
        parent_uid: int = None,
        role_id_list: GetUserResponseBodyUserRoleIdList = None,
        role_name_list: GetUserResponseBodyUserRoleNameList = None,
        signature_method: str = None,
        state: str = None,
        uid: str = None,
        user_id: str = None,
        webhook: str = None,
    ):
        self.cur_execute_count = cur_execute_count
        self.cur_result_count = cur_result_count
        self.ding_robot = ding_robot
        self.email = email
        self.last_login_time = last_login_time
        self.max_execute_count = max_execute_count
        self.max_result_count = max_result_count
        self.mobile = mobile
        self.nick_name = nick_name
        self.notification_mode = notification_mode
        self.parent_uid = parent_uid
        self.role_id_list = role_id_list
        self.role_name_list = role_name_list
        self.signature_method = signature_method
        self.state = state
        self.uid = uid
        self.user_id = user_id
        self.webhook = webhook

    def validate(self):
        if self.role_id_list:
            self.role_id_list.validate()
        if self.role_name_list:
            self.role_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_execute_count is not None:
            result['CurExecuteCount'] = self.cur_execute_count
        if self.cur_result_count is not None:
            result['CurResultCount'] = self.cur_result_count
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list.to_map()
        if self.role_name_list is not None:
            result['RoleNameList'] = self.role_name_list.to_map()
        if self.signature_method is not None:
            result['SignatureMethod'] = self.signature_method
        if self.state is not None:
            result['State'] = self.state
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurExecuteCount') is not None:
            self.cur_execute_count = m.get('CurExecuteCount')
        if m.get('CurResultCount') is not None:
            self.cur_result_count = m.get('CurResultCount')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('RoleIdList') is not None:
            temp_model = GetUserResponseBodyUserRoleIdList()
            self.role_id_list = temp_model.from_map(m['RoleIdList'])
        if m.get('RoleNameList') is not None:
            temp_model = GetUserResponseBodyUserRoleNameList()
            self.role_name_list = temp_model.from_map(m['RoleNameList'])
        if m.get('SignatureMethod') is not None:
            self.signature_method = m.get('SignatureMethod')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        user: GetUserResponseBodyUser = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserActiveTenantRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
    ):
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetUserActiveTenantResponseBodyTenant(TeaModel):
    def __init__(
        self,
        status: str = None,
        tenant_name: str = None,
        tid: int = None,
    ):
        self.status = status
        self.tenant_name = tenant_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetUserActiveTenantResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant: GetUserActiveTenantResponseBodyTenant = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.tenant = tenant

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tenant') is not None:
            temp_model = GetUserActiveTenantResponseBodyTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
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
            temp_model = GetUserActiveTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserUploadFileJobRequest(TeaModel):
    def __init__(
        self,
        job_key: str = None,
        tid: int = None,
    ):
        self.job_key = job_key
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        object_name: str = None,
    ):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.object_name = object_name

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
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class GetUserUploadFileJobResponseBodyUploadFileJobDetail(TeaModel):
    def __init__(
        self,
        attachment_key: str = None,
        file_name: str = None,
        file_size: int = None,
        file_source: str = None,
        job_key: str = None,
        job_status: str = None,
        job_status_desc: str = None,
        upload_ossparam: GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam = None,
        upload_type: str = None,
        upload_url: str = None,
        uploaded_size: int = None,
    ):
        self.attachment_key = attachment_key
        self.file_name = file_name
        self.file_size = file_size
        self.file_source = file_source
        self.job_key = job_key
        self.job_status = job_status
        self.job_status_desc = job_status_desc
        self.upload_ossparam = upload_ossparam
        self.upload_type = upload_type
        self.upload_url = upload_url
        self.uploaded_size = uploaded_size

    def validate(self):
        if self.upload_ossparam:
            self.upload_ossparam.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_source is not None:
            result['FileSource'] = self.file_source
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.job_status_desc is not None:
            result['JobStatusDesc'] = self.job_status_desc
        if self.upload_ossparam is not None:
            result['UploadOSSParam'] = self.upload_ossparam.to_map()
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.upload_url is not None:
            result['UploadURL'] = self.upload_url
        if self.uploaded_size is not None:
            result['UploadedSize'] = self.uploaded_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileSource') is not None:
            self.file_source = m.get('FileSource')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('JobStatusDesc') is not None:
            self.job_status_desc = m.get('JobStatusDesc')
        if m.get('UploadOSSParam') is not None:
            temp_model = GetUserUploadFileJobResponseBodyUploadFileJobDetailUploadOSSParam()
            self.upload_ossparam = temp_model.from_map(m['UploadOSSParam'])
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('UploadURL') is not None:
            self.upload_url = m.get('UploadURL')
        if m.get('UploadedSize') is not None:
            self.uploaded_size = m.get('UploadedSize')
        return self


class GetUserUploadFileJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        upload_file_job_detail: GetUserUploadFileJobResponseBodyUploadFileJobDetail = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.upload_file_job_detail = upload_file_job_detail

    def validate(self):
        if self.upload_file_job_detail:
            self.upload_file_job_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.upload_file_job_detail is not None:
            result['UploadFileJobDetail'] = self.upload_file_job_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = GetUserUploadFileJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantUserPermissionRequest(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        ds_type: str = None,
        expire_date: str = None,
        instance_id: int = None,
        logic: bool = None,
        perm_types: str = None,
        table_id: str = None,
        table_name: str = None,
        tid: int = None,
        user_id: str = None,
    ):
        self.db_id = db_id
        self.ds_type = ds_type
        self.expire_date = expire_date
        self.instance_id = instance_id
        self.logic = logic
        self.perm_types = perm_types
        self.table_id = table_id
        self.table_name = table_name
        self.tid = tid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.perm_types is not None:
            result['PermTypes'] = self.perm_types
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PermTypes') is not None:
            self.perm_types = m.get('PermTypes')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GrantUserPermissionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = GrantUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InspectProxyAccessSecretRequest(TeaModel):
    def __init__(
        self,
        proxy_access_id: int = None,
        tid: int = None,
    ):
        self.proxy_access_id = proxy_access_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class InspectProxyAccessSecretResponseBody(TeaModel):
    def __init__(
        self,
        access_secret: str = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_secret = access_secret
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InspectProxyAccessSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InspectProxyAccessSecretResponseBody = None,
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
            temp_model = InspectProxyAccessSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListColumnsRequest(TeaModel):
    def __init__(
        self,
        logic: bool = None,
        table_id: str = None,
        tid: int = None,
    ):
        self.logic = logic
        self.table_id = table_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListColumnsResponseBodyColumnListColumn(TeaModel):
    def __init__(
        self,
        auto_increment: bool = None,
        column_id: str = None,
        column_name: str = None,
        column_type: str = None,
        data_length: int = None,
        data_precision: int = None,
        data_scale: int = None,
        default_value: str = None,
        description: str = None,
        function_type: str = None,
        nullable: bool = None,
        security_level: str = None,
        sensitive: bool = None,
    ):
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.column_name = column_name
        self.column_type = column_type
        self.data_length = data_length
        self.data_precision = data_precision
        self.data_scale = data_scale
        self.default_value = default_value
        self.description = description
        self.function_type = function_type
        self.nullable = nullable
        self.security_level = security_level
        self.sensitive = sensitive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment
        if self.column_id is not None:
            result['ColumnId'] = self.column_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.data_length is not None:
            result['DataLength'] = self.data_length
        if self.data_precision is not None:
            result['DataPrecision'] = self.data_precision
        if self.data_scale is not None:
            result['DataScale'] = self.data_scale
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.nullable is not None:
            result['Nullable'] = self.nullable
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')
        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('DataLength') is not None:
            self.data_length = m.get('DataLength')
        if m.get('DataPrecision') is not None:
            self.data_precision = m.get('DataPrecision')
        if m.get('DataScale') is not None:
            self.data_scale = m.get('DataScale')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        column_list: ListColumnsResponseBodyColumnList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.column_list = column_list
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.column_list:
            self.column_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_list is not None:
            result['ColumnList'] = self.column_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnList') is not None:
            temp_model = ListColumnsResponseBodyColumnList()
            self.column_list = temp_model.from_map(m['ColumnList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ListColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDBTaskSQLJobRequest(TeaModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.dbtask_group_id = dbtask_group_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListDBTaskSQLJobResponseBodyDBTaskSQLJobList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        create_time: str = None,
        db_id: int = None,
        db_search_name: str = None,
        db_task_group_id: int = None,
        job_id: int = None,
        job_type: str = None,
        last_exec_time: str = None,
        logic: bool = None,
        status: str = None,
        transactional: bool = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.db_id = db_id
        self.db_search_name = db_search_name
        self.db_task_group_id = db_task_group_id
        self.job_id = job_id
        self.job_type = job_type
        self.last_exec_time = last_exec_time
        self.logic = logic
        self.status = status
        self.transactional = transactional

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name
        if self.db_task_group_id is not None:
            result['DbTaskGroupId'] = self.db_task_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.last_exec_time is not None:
            result['LastExecTime'] = self.last_exec_time
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.status is not None:
            result['Status'] = self.status
        if self.transactional is not None:
            result['Transactional'] = self.transactional
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')
        if m.get('DbTaskGroupId') is not None:
            self.db_task_group_id = m.get('DbTaskGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('LastExecTime') is not None:
            self.last_exec_time = m.get('LastExecTime')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Transactional') is not None:
            self.transactional = m.get('Transactional')
        return self


class ListDBTaskSQLJobResponseBody(TeaModel):
    def __init__(
        self,
        dbtask_sqljob_list: List[ListDBTaskSQLJobResponseBodyDBTaskSQLJobList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.dbtask_sqljob_list = dbtask_sqljob_list
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_list:
            for k in self.dbtask_sqljob_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBTaskSQLJobList'] = []
        if self.dbtask_sqljob_list is not None:
            for k in self.dbtask_sqljob_list:
                result['DBTaskSQLJobList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbtask_sqljob_list = []
        if m.get('DBTaskSQLJobList') is not None:
            for k in m.get('DBTaskSQLJobList'):
                temp_model = ListDBTaskSQLJobResponseBodyDBTaskSQLJobList()
                self.dbtask_sqljob_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ListDBTaskSQLJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDBTaskSQLJobDetailRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList(TeaModel):
    def __init__(
        self,
        affect_rows: int = None,
        current_sql: str = None,
        db_id: int = None,
        end_time: str = None,
        execute_count: int = None,
        job_detail_id: int = None,
        job_id: int = None,
        log: str = None,
        logic: bool = None,
        skip: bool = None,
        sql_type: str = None,
        start_time: str = None,
        status: str = None,
        time_delay: int = None,
    ):
        self.affect_rows = affect_rows
        self.current_sql = current_sql
        self.db_id = db_id
        self.end_time = end_time
        self.execute_count = execute_count
        self.job_detail_id = job_detail_id
        self.job_id = job_id
        self.log = log
        self.logic = logic
        self.skip = skip
        self.sql_type = sql_type
        self.start_time = start_time
        self.status = status
        self.time_delay = time_delay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.current_sql is not None:
            result['CurrentSql'] = self.current_sql
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count
        if self.job_detail_id is not None:
            result['JobDetailId'] = self.job_detail_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.log is not None:
            result['Log'] = self.log
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.time_delay is not None:
            result['TimeDelay'] = self.time_delay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('CurrentSql') is not None:
            self.current_sql = m.get('CurrentSql')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')
        if m.get('JobDetailId') is not None:
            self.job_detail_id = m.get('JobDetailId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Log') is not None:
            self.log = m.get('Log')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeDelay') is not None:
            self.time_delay = m.get('TimeDelay')
        return self


class ListDBTaskSQLJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        dbtask_sqljob_detail_list: List[ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.dbtask_sqljob_detail_list = dbtask_sqljob_detail_list
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.dbtask_sqljob_detail_list:
            for k in self.dbtask_sqljob_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBTaskSQLJobDetailList'] = []
        if self.dbtask_sqljob_detail_list is not None:
            for k in self.dbtask_sqljob_detail_list:
                result['DBTaskSQLJobDetailList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbtask_sqljob_detail_list = []
        if m.get('DBTaskSQLJobDetailList') is not None:
            for k in m.get('DBTaskSQLJobDetailList'):
                temp_model = ListDBTaskSQLJobDetailResponseBodyDBTaskSQLJobDetailList()
                self.dbtask_sqljob_detail_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = ListDBTaskSQLJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDDLPublishRecordsRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList(TeaModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        execute_count: int = None,
        scripts: str = None,
        status_desc: str = None,
        table_name: str = None,
        task_job_status: str = None,
    ):
        self.dbtask_group_id = dbtask_group_id
        self.execute_count = execute_count
        self.scripts = scripts
        self.status_desc = status_desc
        self.table_name = table_name
        self.task_job_status = task_job_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id
        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count
        if self.scripts is not None:
            result['Scripts'] = self.scripts
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.task_job_status is not None:
            result['TaskJobStatus'] = self.task_job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')
        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')
        if m.get('Scripts') is not None:
            self.scripts = m.get('Scripts')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TaskJobStatus') is not None:
            self.task_job_status = m.get('TaskJobStatus')
        return self


class ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        plan_time: str = None,
        publish_job_list: List[ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList] = None,
        publish_strategy: str = None,
        status_desc: str = None,
        task_job_status: str = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.plan_time = plan_time
        self.publish_job_list = publish_job_list
        self.publish_strategy = publish_strategy
        self.status_desc = status_desc
        self.task_job_status = task_job_status

    def validate(self):
        if self.publish_job_list:
            for k in self.publish_job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time
        result['PublishJobList'] = []
        if self.publish_job_list is not None:
            for k in self.publish_job_list:
                result['PublishJobList'].append(k.to_map() if k else None)
        if self.publish_strategy is not None:
            result['PublishStrategy'] = self.publish_strategy
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.task_job_status is not None:
            result['TaskJobStatus'] = self.task_job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')
        self.publish_job_list = []
        if m.get('PublishJobList') is not None:
            for k in m.get('PublishJobList'):
                temp_model = ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList()
                self.publish_job_list.append(temp_model.from_map(k))
        if m.get('PublishStrategy') is not None:
            self.publish_strategy = m.get('PublishStrategy')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('TaskJobStatus') is not None:
            self.task_job_status = m.get('TaskJobStatus')
        return self


class ListDDLPublishRecordsResponseBodyDDLPublishRecordList(TeaModel):
    def __init__(
        self,
        audit_expire_time: str = None,
        audit_status: str = None,
        creator_id: int = None,
        finality: bool = None,
        finality_reason: str = None,
        publish_status: str = None,
        publish_task_info_list: List[ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList] = None,
        risk_level: str = None,
        status_desc: str = None,
        workflow_instance_id: int = None,
    ):
        self.audit_expire_time = audit_expire_time
        self.audit_status = audit_status
        self.creator_id = creator_id
        self.finality = finality
        self.finality_reason = finality_reason
        self.publish_status = publish_status
        self.publish_task_info_list = publish_task_info_list
        self.risk_level = risk_level
        self.status_desc = status_desc
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        if self.publish_task_info_list:
            for k in self.publish_task_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_expire_time is not None:
            result['AuditExpireTime'] = self.audit_expire_time
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.finality is not None:
            result['Finality'] = self.finality
        if self.finality_reason is not None:
            result['FinalityReason'] = self.finality_reason
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        result['PublishTaskInfoList'] = []
        if self.publish_task_info_list is not None:
            for k in self.publish_task_info_list:
                result['PublishTaskInfoList'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditExpireTime') is not None:
            self.audit_expire_time = m.get('AuditExpireTime')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Finality') is not None:
            self.finality = m.get('Finality')
        if m.get('FinalityReason') is not None:
            self.finality_reason = m.get('FinalityReason')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        self.publish_task_info_list = []
        if m.get('PublishTaskInfoList') is not None:
            for k in m.get('PublishTaskInfoList'):
                temp_model = ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList()
                self.publish_task_info_list.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class ListDDLPublishRecordsResponseBody(TeaModel):
    def __init__(
        self,
        ddlpublish_record_list: List[ListDDLPublishRecordsResponseBodyDDLPublishRecordList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.ddlpublish_record_list = ddlpublish_record_list
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.ddlpublish_record_list:
            for k in self.ddlpublish_record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DDLPublishRecordList'] = []
        if self.ddlpublish_record_list is not None:
            for k in self.ddlpublish_record_list:
                result['DDLPublishRecordList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddlpublish_record_list = []
        if m.get('DDLPublishRecordList') is not None:
            for k in m.get('DDLPublishRecordList'):
                temp_model = ListDDLPublishRecordsResponseBodyDDLPublishRecordList()
                self.ddlpublish_record_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDDLPublishRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDDLPublishRecordsResponseBody = None,
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
            temp_model = ListDDLPublishRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataCorrectPreCheckDBRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListDataCorrectPreCheckDBResponseBodyPreCheckDBList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        search_name: str = None,
        sql_num: int = None,
    ):
        self.db_id = db_id
        self.search_name = search_name
        self.sql_num = sql_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sql_num is not None:
            result['SqlNum'] = self.sql_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('SqlNum') is not None:
            self.sql_num = m.get('SqlNum')
        return self


class ListDataCorrectPreCheckDBResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_dblist: List[ListDataCorrectPreCheckDBResponseBodyPreCheckDBList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.pre_check_dblist = pre_check_dblist
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.pre_check_dblist:
            for k in self.pre_check_dblist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['PreCheckDBList'] = []
        if self.pre_check_dblist is not None:
            for k in self.pre_check_dblist:
                result['PreCheckDBList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.pre_check_dblist = []
        if m.get('PreCheckDBList') is not None:
            for k in m.get('PreCheckDBList'):
                temp_model = ListDataCorrectPreCheckDBResponseBodyPreCheckDBList()
                self.pre_check_dblist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataCorrectPreCheckDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataCorrectPreCheckDBResponseBody = None,
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
            temp_model = ListDataCorrectPreCheckDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataCorrectPreCheckSQLRequest(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        order_id: int = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList(TeaModel):
    def __init__(
        self,
        affect_rows: int = None,
        check_sql: str = None,
        db_id: int = None,
        sqlreview_query_key: str = None,
        sql_review_status: str = None,
        sql_type: str = None,
        table_names: str = None,
    ):
        self.affect_rows = affect_rows
        self.check_sql = check_sql
        self.db_id = db_id
        self.sqlreview_query_key = sqlreview_query_key
        self.sql_review_status = sql_review_status
        self.sql_type = sql_type
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.check_sql is not None:
            result['CheckSQL'] = self.check_sql
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key
        if self.sql_review_status is not None:
            result['SqlReviewStatus'] = self.sql_review_status
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.table_names is not None:
            result['TableNames'] = self.table_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('CheckSQL') is not None:
            self.check_sql = m.get('CheckSQL')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')
        if m.get('SqlReviewStatus') is not None:
            self.sql_review_status = m.get('SqlReviewStatus')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')
        return self


class ListDataCorrectPreCheckSQLResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_sqllist: List[ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.pre_check_sqllist = pre_check_sqllist
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.pre_check_sqllist:
            for k in self.pre_check_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['PreCheckSQLList'] = []
        if self.pre_check_sqllist is not None:
            for k in self.pre_check_sqllist:
                result['PreCheckSQLList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.pre_check_sqllist = []
        if m.get('PreCheckSQLList') is not None:
            for k in m.get('PreCheckSQLList'):
                temp_model = ListDataCorrectPreCheckSQLResponseBodyPreCheckSQLList()
                self.pre_check_sqllist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataCorrectPreCheckSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataCorrectPreCheckSQLResponseBody = None,
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
            temp_model = ListDataCorrectPreCheckSQLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabaseUserPermssionsRequest(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        perm_type: str = None,
        tid: int = None,
        user_name: str = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.page_number = page_number
        self.page_size = page_size
        self.perm_type = perm_type
        self.tid = tid
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        extra_data: str = None,
        origin_from: str = None,
        perm_type: str = None,
        user_access_id: str = None,
    ):
        self.create_date = create_date
        self.expire_date = expire_date
        self.extra_data = extra_data
        self.origin_from = origin_from
        self.perm_type = perm_type
        self.user_access_id = user_access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        alias: str = None,
        column_name: str = None,
        db_id: str = None,
        db_type: str = None,
        ds_type: str = None,
        env_type: str = None,
        instance_id: str = None,
        logic: bool = None,
        perm_details: ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        schema_name: str = None,
        search_name: str = None,
        table_id: str = None,
        table_name: str = None,
        user_id: str = None,
        user_nick_name: str = None,
    ):
        self.alias = alias
        self.column_name = column_name
        self.db_id = db_id
        self.db_type = db_type
        self.ds_type = ds_type
        self.env_type = env_type
        self.instance_id = instance_id
        self.logic = logic
        self.perm_details = perm_details
        self.schema_name = schema_name
        self.search_name = search_name
        self.table_id = table_id
        self.table_name = table_name
        self.user_id = user_id
        self.user_nick_name = user_nick_name

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PermDetails') is not None:
            temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m['PermDetails'])
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_permissions: ListDatabaseUserPermssionsResponseBodyUserPermissions = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.user_permissions = user_permissions

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserPermissions') is not None:
            temp_model = ListDatabaseUserPermssionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m['UserPermissions'])
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
            temp_model = ListDatabaseUserPermssionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabasesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        catalog_name: str = None,
        database_id: str = None,
        db_type: str = None,
        dba_id: str = None,
        dba_name: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        owner_id_list: ListDatabasesResponseBodyDatabaseListDatabaseOwnerIdList = None,
        owner_name_list: ListDatabasesResponseBodyDatabaseListDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
        state: str = None,
    ):
        self.catalog_name = catalog_name
        self.database_id = database_id
        self.db_type = db_type
        self.dba_id = dba_id
        self.dba_name = dba_name
        self.encoding = encoding
        self.env_type = env_type
        self.host = host
        self.instance_id = instance_id
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.schema_name = schema_name
        self.search_name = search_name
        self.sid = sid
        self.state = state

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_name is not None:
            result['DbaName'] = self.dba_name
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerIdList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseListDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseListDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('State') is not None:
            self.state = m.get('State')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        database_list: ListDatabasesResponseBodyDatabaseList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.database_list = database_list
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.database_list:
            self.database_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_list is not None:
            result['DatabaseList'] = self.database_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseList') is not None:
            temp_model = ListDatabasesResponseBodyDatabaseList()
            self.database_list = temp_model.from_map(m['DatabaseList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIndexesRequest(TeaModel):
    def __init__(
        self,
        logic: bool = None,
        table_id: str = None,
        tid: int = None,
    ):
        self.logic = logic
        self.table_id = table_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListIndexesResponseBodyIndexListIndex(TeaModel):
    def __init__(
        self,
        index_comment: str = None,
        index_id: str = None,
        index_name: str = None,
        index_type: str = None,
        table_id: str = None,
    ):
        self.index_comment = index_comment
        self.index_id = index_id
        self.index_name = index_name
        self.index_type = index_type
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index_comment is not None:
            result['IndexComment'] = self.index_comment
        if self.index_id is not None:
            result['IndexId'] = self.index_id
        if self.index_name is not None:
            result['IndexName'] = self.index_name
        if self.index_type is not None:
            result['IndexType'] = self.index_type
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexComment') is not None:
            self.index_comment = m.get('IndexComment')
        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        index_list: ListIndexesResponseBodyIndexList = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.index_list = index_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.index_list:
            self.index_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.index_list is not None:
            result['IndexList'] = self.index_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IndexList') is not None:
            temp_model = ListIndexesResponseBodyIndexList()
            self.index_list = temp_model.from_map(m['IndexList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ListIndexesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceLoginAuditLogRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        self.end_time = end_time
        self.op_user_name = op_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_name = search_name
        self.start_time = start_time
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog(TeaModel):
    def __init__(
        self,
        db_user: str = None,
        instance_id: int = None,
        instance_name: str = None,
        op_time: str = None,
        request_ip: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.db_user = db_user
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.op_time = op_time
        self.request_ip = request_ip
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.op_time is not None:
            result['OpTime'] = self.op_time
        if self.request_ip is not None:
            result['RequestIp'] = self.request_ip
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')
        if m.get('RequestIp') is not None:
            self.request_ip = m.get('RequestIp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList(TeaModel):
    def __init__(
        self,
        instance_login_audit_log: List[ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog] = None,
    ):
        self.instance_login_audit_log = instance_login_audit_log

    def validate(self):
        if self.instance_login_audit_log:
            for k in self.instance_login_audit_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceLoginAuditLog'] = []
        if self.instance_login_audit_log is not None:
            for k in self.instance_login_audit_log:
                result['InstanceLoginAuditLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_login_audit_log = []
        if m.get('InstanceLoginAuditLog') is not None:
            for k in m.get('InstanceLoginAuditLog'):
                temp_model = ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog()
                self.instance_login_audit_log.append(temp_model.from_map(k))
        return self


class ListInstanceLoginAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance_login_audit_log_list: ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.instance_login_audit_log_list = instance_login_audit_log_list
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.instance_login_audit_log_list:
            self.instance_login_audit_log_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_login_audit_log_list is not None:
            result['InstanceLoginAuditLogList'] = self.instance_login_audit_log_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceLoginAuditLogList') is not None:
            temp_model = ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList()
            self.instance_login_audit_log_list = temp_model.from_map(m['InstanceLoginAuditLogList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceLoginAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceLoginAuditLogResponseBody = None,
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
            temp_model = ListInstanceLoginAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceUserPermissionsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        extra_data: str = None,
        origin_from: str = None,
        perm_type: str = None,
        user_access_id: str = None,
    ):
        self.create_date = create_date
        self.expire_date = expire_date
        self.extra_data = extra_data
        self.origin_from = origin_from
        self.perm_type = perm_type
        self.user_access_id = user_access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
        return self


class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails(TeaModel):
    def __init__(
        self,
        perm_detail: List[ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail] = None,
    ):
        self.perm_detail = perm_detail

    def validate(self):
        if self.perm_detail:
            for k in self.perm_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail()
                self.perm_detail.append(temp_model.from_map(k))
        return self


class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        perm_details: ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        user_id: str = None,
        user_nick_name: str = None,
    ):
        self.instance_id = instance_id
        self.perm_details = perm_details
        self.user_id = user_id
        self.user_nick_name = user_nick_name

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PermDetails') is not None:
            temp_model = ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m['PermDetails'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')
        return self


class ListInstanceUserPermissionsResponseBodyUserPermissions(TeaModel):
    def __init__(
        self,
        user_permission: List[ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission] = None,
    ):
        self.user_permission = user_permission

    def validate(self):
        if self.user_permission:
            for k in self.user_permission:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission()
                self.user_permission.append(temp_model.from_map(k))
        return self


class ListInstanceUserPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_permissions: ListInstanceUserPermissionsResponseBodyUserPermissions = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.user_permissions = user_permissions

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserPermissions') is not None:
            temp_model = ListInstanceUserPermissionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m['UserPermissions'])
        return self


class ListInstanceUserPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceUserPermissionsResponseBody = None,
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
            temp_model = ListInstanceUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        instance_source: str = None,
        instance_state: str = None,
        net_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tid: int = None,
    ):
        self.db_type = db_type
        self.env_type = env_type
        self.instance_source = instance_source
        self.instance_state = instance_state
        self.net_type = net_type
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_state is not None:
            result['InstanceState'] = self.instance_state
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceState') is not None:
            self.instance_state = m.get('InstanceState')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')
        return self


class ListInstancesResponseBodyInstanceListInstanceStandardGroup(TeaModel):
    def __init__(
        self,
        group_mode: str = None,
        group_name: str = None,
    ):
        self.group_mode = group_mode
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ListInstancesResponseBodyInstanceListInstance(TeaModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: str = None,
        dba_nick_name: str = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        owner_id_list: ListInstancesResponseBodyInstanceListInstanceOwnerIdList = None,
        owner_name_list: ListInstancesResponseBodyInstanceListInstanceOwnerNameList = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule_id: str = None,
        sid: str = None,
        standard_group: ListInstancesResponseBodyInstanceListInstanceStandardGroup = None,
        state: str = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        self.data_link_name = data_link_name
        self.database_password = database_password
        self.database_user = database_user
        self.dba_id = dba_id
        self.dba_nick_name = dba_nick_name
        self.ddl_online = ddl_online
        self.ecs_instance_id = ecs_instance_id
        self.ecs_region = ecs_region
        self.env_type = env_type
        self.export_timeout = export_timeout
        self.host = host
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.query_timeout = query_timeout
        self.safe_rule_id = safe_rule_id
        self.sid = sid
        self.standard_group = standard_group
        self.state = state
        self.use_dsql = use_dsql
        self.vpc_id = vpc_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()
        if self.standard_group:
            self.standard_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerIdList') is not None:
            temp_model = ListInstancesResponseBodyInstanceListInstanceOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListInstancesResponseBodyInstanceListInstanceOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('StandardGroup') is not None:
            temp_model = ListInstancesResponseBodyInstanceListInstanceStandardGroup()
            self.standard_group = temp_model.from_map(m['StandardGroup'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        instance_list: ListInstancesResponseBodyInstanceList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.instance_list = instance_list
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceList') is not None:
            temp_model = ListInstancesResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m['InstanceList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLhTaskFlowAndScenarioRequest(TeaModel):
    def __init__(
        self,
        space_id: int = None,
        tid: int = None,
        user_id: int = None,
    ):
        self.space_id = space_id
        self.tid = tid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag(TeaModel):
    def __init__(
        self,
        can_edit: bool = None,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        data_flow_id: int = None,
        demo_id: str = None,
        deploy_id: int = None,
        id: int = None,
        is_deleted: bool = None,
        latest_instance_status: int = None,
        latest_instance_time: int = None,
        scenario_id: int = None,
        space_id: int = None,
        status: int = None,
    ):
        self.can_edit = can_edit
        self.creator_id = creator_id
        self.creator_nick_name = creator_nick_name
        self.dag_name = dag_name
        self.dag_owner_id = dag_owner_id
        self.dag_owner_nick_name = dag_owner_nick_name
        self.data_flow_id = data_flow_id
        self.demo_id = demo_id
        self.deploy_id = deploy_id
        self.id = id
        self.is_deleted = is_deleted
        self.latest_instance_status = latest_instance_status
        self.latest_instance_time = latest_instance_time
        self.scenario_id = scenario_id
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_edit is not None:
            result['CanEdit'] = self.can_edit
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name
        if self.dag_name is not None:
            result['DagName'] = self.dag_name
        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id
        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.demo_id is not None:
            result['DemoId'] = self.demo_id
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.id is not None:
            result['Id'] = self.id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status
        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEdit') is not None:
            self.can_edit = m.get('CanEdit')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')
        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')
        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')
        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DemoId') is not None:
            self.demo_id = m.get('DemoId')
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')
        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLhTaskFlowAndScenarioResponseBodyRawDAGList(TeaModel):
    def __init__(
        self,
        dag: List[ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag] = None,
    ):
        self.dag = dag

    def validate(self):
        if self.dag:
            for k in self.dag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dag'] = []
        if self.dag is not None:
            for k in self.dag:
                result['Dag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag = []
        if m.get('Dag') is not None:
            for k in m.get('Dag'):
                temp_model = ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag()
                self.dag.append(temp_model.from_map(k))
        return self


class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag(TeaModel):
    def __init__(
        self,
        can_edit: bool = None,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        data_flow_id: int = None,
        demo_id: str = None,
        deploy_id: int = None,
        id: int = None,
        is_deleted: bool = None,
        latest_instance_status: int = None,
        latest_instance_time: int = None,
        scenario_id: int = None,
        space_id: int = None,
        status: int = None,
    ):
        self.can_edit = can_edit
        self.creator_id = creator_id
        self.creator_nick_name = creator_nick_name
        self.dag_name = dag_name
        self.dag_owner_id = dag_owner_id
        self.dag_owner_nick_name = dag_owner_nick_name
        self.data_flow_id = data_flow_id
        self.demo_id = demo_id
        self.deploy_id = deploy_id
        self.id = id
        self.is_deleted = is_deleted
        self.latest_instance_status = latest_instance_status
        self.latest_instance_time = latest_instance_time
        self.scenario_id = scenario_id
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_edit is not None:
            result['CanEdit'] = self.can_edit
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name
        if self.dag_name is not None:
            result['DagName'] = self.dag_name
        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id
        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name
        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id
        if self.demo_id is not None:
            result['DemoId'] = self.demo_id
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.id is not None:
            result['Id'] = self.id
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status
        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEdit') is not None:
            self.can_edit = m.get('CanEdit')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')
        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')
        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')
        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')
        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')
        if m.get('DemoId') is not None:
            self.demo_id = m.get('DemoId')
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')
        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList(TeaModel):
    def __init__(
        self,
        dag: List[ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag] = None,
    ):
        self.dag = dag

    def validate(self):
        if self.dag:
            for k in self.dag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dag'] = []
        if self.dag is not None:
            for k in self.dag:
                result['Dag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag = []
        if m.get('Dag') is not None:
            for k in m.get('Dag'):
                temp_model = ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag()
                self.dag.append(temp_model.from_map(k))
        return self


class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        description: str = None,
        scenario_name: str = None,
    ):
        self.creator_id = creator_id
        self.description = description
        self.scenario_name = scenario_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.scenario_name is not None:
            result['ScenarioName'] = self.scenario_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScenarioName') is not None:
            self.scenario_name = m.get('ScenarioName')
        return self


class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG(TeaModel):
    def __init__(
        self,
        dag_list: ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList = None,
        scenario: ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario = None,
    ):
        self.dag_list = dag_list
        self.scenario = scenario

    def validate(self):
        if self.dag_list:
            self.dag_list.validate()
        if self.scenario:
            self.scenario.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_list is not None:
            result['DagList'] = self.dag_list.to_map()
        if self.scenario is not None:
            result['Scenario'] = self.scenario.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagList') is not None:
            temp_model = ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList()
            self.dag_list = temp_model.from_map(m['DagList'])
        if m.get('Scenario') is not None:
            temp_model = ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario()
            self.scenario = temp_model.from_map(m['Scenario'])
        return self


class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList(TeaModel):
    def __init__(
        self,
        scenario_dag: List[ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG] = None,
    ):
        self.scenario_dag = scenario_dag

    def validate(self):
        if self.scenario_dag:
            for k in self.scenario_dag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ScenarioDAG'] = []
        if self.scenario_dag is not None:
            for k in self.scenario_dag:
                result['ScenarioDAG'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scenario_dag = []
        if m.get('ScenarioDAG') is not None:
            for k in m.get('ScenarioDAG'):
                temp_model = ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG()
                self.scenario_dag.append(temp_model.from_map(k))
        return self


class ListLhTaskFlowAndScenarioResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        raw_daglist: ListLhTaskFlowAndScenarioResponseBodyRawDAGList = None,
        request_id: str = None,
        scenario_daglist: ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.raw_daglist = raw_daglist
        self.request_id = request_id
        self.scenario_daglist = scenario_daglist
        self.success = success

    def validate(self):
        if self.raw_daglist:
            self.raw_daglist.validate()
        if self.scenario_daglist:
            self.scenario_daglist.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.raw_daglist is not None:
            result['RawDAGList'] = self.raw_daglist.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenario_daglist is not None:
            result['ScenarioDAGList'] = self.scenario_daglist.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RawDAGList') is not None:
            temp_model = ListLhTaskFlowAndScenarioResponseBodyRawDAGList()
            self.raw_daglist = temp_model.from_map(m['RawDAGList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScenarioDAGList') is not None:
            temp_model = ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList()
            self.scenario_daglist = temp_model.from_map(m['ScenarioDAGList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLhTaskFlowAndScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLhTaskFlowAndScenarioResponseBody = None,
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
            temp_model = ListLhTaskFlowAndScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogicDatabasesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        alias: str = None,
        database_id: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList = None,
        owner_name_list: ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        self.alias = alias
        self.database_id = database_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.schema_name = schema_name
        self.search_name = search_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIdList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseListLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        logic_database_list: ListLogicDatabasesResponseBodyLogicDatabaseList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.logic_database_list = logic_database_list
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.logic_database_list:
            self.logic_database_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logic_database_list is not None:
            result['LogicDatabaseList'] = self.logic_database_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogicDatabaseList') is not None:
            temp_model = ListLogicDatabasesResponseBodyLogicDatabaseList()
            self.logic_database_list = temp_model.from_map(m['LogicDatabaseList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListLogicDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogicTableRouteConfigRequest(TeaModel):
    def __init__(
        self,
        table_id: int = None,
        tid: int = None,
    ):
        self.table_id = table_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig(TeaModel):
    def __init__(
        self,
        route_expr: str = None,
        route_key: str = None,
        table_id: int = None,
    ):
        self.route_expr = route_expr
        self.route_key = route_key
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_expr is not None:
            result['RouteExpr'] = self.route_expr
        if self.route_key is not None:
            result['RouteKey'] = self.route_key
        if self.table_id is not None:
            result['TableId'] = self.table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteExpr') is not None:
            self.route_expr = m.get('RouteExpr')
        if m.get('RouteKey') is not None:
            self.route_key = m.get('RouteKey')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        return self


class ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList(TeaModel):
    def __init__(
        self,
        logic_table_route_config: List[ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig] = None,
    ):
        self.logic_table_route_config = logic_table_route_config

    def validate(self):
        if self.logic_table_route_config:
            for k in self.logic_table_route_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogicTableRouteConfig'] = []
        if self.logic_table_route_config is not None:
            for k in self.logic_table_route_config:
                result['LogicTableRouteConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_table_route_config = []
        if m.get('LogicTableRouteConfig') is not None:
            for k in m.get('LogicTableRouteConfig'):
                temp_model = ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig()
                self.logic_table_route_config.append(temp_model.from_map(k))
        return self


class ListLogicTableRouteConfigResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_table_route_config_list: ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.logic_table_route_config_list = logic_table_route_config_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.logic_table_route_config_list:
            self.logic_table_route_config_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logic_table_route_config_list is not None:
            result['LogicTableRouteConfigList'] = self.logic_table_route_config_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogicTableRouteConfigList') is not None:
            temp_model = ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList()
            self.logic_table_route_config_list = temp_model.from_map(m['LogicTableRouteConfigList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLogicTableRouteConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogicTableRouteConfigResponseBody = None,
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
            temp_model = ListLogicTableRouteConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogicTablesRequest(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        page_number: int = None,
        page_size: int = None,
        return_guid: bool = None,
        search_name: str = None,
        tid: int = None,
    ):
        self.database_id = database_id
        self.page_number = page_number
        self.page_size = page_size
        self.return_guid = return_guid
        self.search_name = search_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        logic: bool = None,
        owner_id_list: ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList = None,
        owner_name_list: ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList = None,
        schema_name: str = None,
        table_count: str = None,
        table_expr: str = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
    ):
        self.database_id = database_id
        self.logic = logic
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.schema_name = schema_name
        self.table_count = table_count
        self.table_expr = table_expr
        self.table_guid = table_guid
        self.table_id = table_id
        self.table_name = table_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_count is not None:
            result['TableCount'] = self.table_count
        if self.table_expr is not None:
            result['TableExpr'] = self.table_expr
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIdList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')
        if m.get('TableExpr') is not None:
            self.table_expr = m.get('TableExpr')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        logic_table_list: ListLogicTablesResponseBodyLogicTableList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.logic_table_list = logic_table_list
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.logic_table_list:
            self.logic_table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logic_table_list is not None:
            result['LogicTableList'] = self.logic_table_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogicTableList') is not None:
            temp_model = ListLogicTablesResponseBodyLogicTableList()
            self.logic_table_list = temp_model.from_map(m['LogicTableList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListLogicTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrdersRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        order_result_type: str = None,
        order_status: str = None,
        page_number: int = None,
        page_size: int = None,
        plugin_type: str = None,
        search_content: str = None,
        search_date_type: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        self.end_time = end_time
        self.order_result_type = order_result_type
        self.order_status = order_status
        self.page_number = page_number
        self.page_size = page_size
        self.plugin_type = plugin_type
        self.search_content = search_content
        self.search_date_type = search_date_type
        self.start_time = start_time
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_result_type is not None:
            result['OrderResultType'] = self.order_result_type
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.search_content is not None:
            result['SearchContent'] = self.search_content
        if self.search_date_type is not None:
            result['SearchDateType'] = self.search_date_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderResultType') is not None:
            self.order_result_type = m.get('OrderResultType')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('SearchContent') is not None:
            self.search_content = m.get('SearchContent')
        if m.get('SearchDateType') is not None:
            self.search_date_type = m.get('SearchDateType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListOrdersResponseBodyOrdersOrder(TeaModel):
    def __init__(
        self,
        comment: str = None,
        committer: str = None,
        committer_id: int = None,
        create_time: str = None,
        last_modify_time: str = None,
        order_id: int = None,
        plugin_type: str = None,
        status_code: str = None,
        status_desc: str = None,
    ):
        self.comment = comment
        self.committer = committer
        self.committer_id = committer_id
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.order_id = order_id
        self.plugin_type = plugin_type
        self.status_code = status_code
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.committer is not None:
            result['Committer'] = self.committer
        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Committer') is not None:
            self.committer = m.get('Committer')
        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        orders: ListOrdersResponseBodyOrders = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.orders = orders
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.orders:
            self.orders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.orders is not None:
            result['Orders'] = self.orders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Orders') is not None:
            temp_model = ListOrdersResponseBodyOrders()
            self.orders = temp_model.from_map(m['Orders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProxiesRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
    ):
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListProxiesResponseBodyProxyList(TeaModel):
    def __init__(
        self,
        creator_id: int = None,
        creator_name: str = None,
        https_port: int = None,
        instance_id: int = None,
        mysql_port: int = None,
        private_enable: bool = None,
        private_host: str = None,
        proxy_id: int = None,
        public_enable: bool = None,
        public_host: str = None,
    ):
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.https_port = https_port
        self.instance_id = instance_id
        self.mysql_port = mysql_port
        self.private_enable = private_enable
        self.private_host = private_host
        self.proxy_id = proxy_id
        self.public_enable = public_enable
        self.public_host = public_host

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
        if self.https_port is not None:
            result['HttpsPort'] = self.https_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mysql_port is not None:
            result['MysqlPort'] = self.mysql_port
        if self.private_enable is not None:
            result['PrivateEnable'] = self.private_enable
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.public_enable is not None:
            result['PublicEnable'] = self.public_enable
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('HttpsPort') is not None:
            self.https_port = m.get('HttpsPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MysqlPort') is not None:
            self.mysql_port = m.get('MysqlPort')
        if m.get('PrivateEnable') is not None:
            self.private_enable = m.get('PrivateEnable')
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('PublicEnable') is not None:
            self.public_enable = m.get('PublicEnable')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        return self


class ListProxiesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_list: List[ListProxiesResponseBodyProxyList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.proxy_list = proxy_list
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.proxy_list:
            for k in self.proxy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['ProxyList'] = []
        if self.proxy_list is not None:
            for k in self.proxy_list:
                result['ProxyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.proxy_list = []
        if m.get('ProxyList') is not None:
            for k in m.get('ProxyList'):
                temp_model = ListProxiesResponseBodyProxyList()
                self.proxy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProxiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProxiesResponseBody = None,
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
            temp_model = ListProxiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProxyAccessesRequest(TeaModel):
    def __init__(
        self,
        proxy_id: int = None,
        tid: int = None,
    ):
        self.proxy_id = proxy_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListProxyAccessesResponseBodyProxyAccessList(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        gmt_create: str = None,
        indep_account: str = None,
        instance_id: int = None,
        origin_info: str = None,
        proxy_access_id: int = None,
        proxy_id: int = None,
        user_id: int = None,
        user_name: str = None,
        user_uid: str = None,
    ):
        self.access_id = access_id
        self.gmt_create = gmt_create
        self.indep_account = indep_account
        self.instance_id = instance_id
        self.origin_info = origin_info
        self.proxy_access_id = proxy_access_id
        self.proxy_id = proxy_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_uid = user_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.indep_account is not None:
            result['IndepAccount'] = self.indep_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.origin_info is not None:
            result['OriginInfo'] = self.origin_info
        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('IndepAccount') is not None:
            self.indep_account = m.get('IndepAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OriginInfo') is not None:
            self.origin_info = m.get('OriginInfo')
        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        return self


class ListProxyAccessesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_access_list: List[ListProxyAccessesResponseBodyProxyAccessList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.proxy_access_list = proxy_access_list
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.proxy_access_list:
            for k in self.proxy_access_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['ProxyAccessList'] = []
        if self.proxy_access_list is not None:
            for k in self.proxy_access_list:
                result['ProxyAccessList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.proxy_access_list = []
        if m.get('ProxyAccessList') is not None:
            for k in m.get('ProxyAccessList'):
                temp_model = ListProxyAccessesResponseBodyProxyAccessList()
                self.proxy_access_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProxyAccessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProxyAccessesResponseBody = None,
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
            temp_model = ListProxyAccessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProxySQLExecAuditLogRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        exec_state: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        sqltype: str = None,
        search_name: str = None,
        start_time: int = None,
        tid: int = None,
    ):
        self.end_time = end_time
        self.exec_state = exec_state
        self.op_user_name = op_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.sqltype = sqltype
        self.search_name = search_name
        self.start_time = start_time
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exec_state is not None:
            result['ExecState'] = self.exec_state
        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')
        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog(TeaModel):
    def __init__(
        self,
        affect_rows: int = None,
        elapsed_time: int = None,
        exec_state: str = None,
        instance_id: int = None,
        instance_name: str = None,
        op_time: str = None,
        remark: str = None,
        sql: str = None,
        sqltype: str = None,
        schema_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.affect_rows = affect_rows
        self.elapsed_time = elapsed_time
        self.exec_state = exec_state
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.op_time = op_time
        self.remark = remark
        self.sql = sql
        self.sqltype = sqltype
        self.schema_name = schema_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.exec_state is not None:
            result['ExecState'] = self.exec_state
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.op_time is not None:
            result['OpTime'] = self.op_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList(TeaModel):
    def __init__(
        self,
        proxy_sqlexec_audit_log: List[ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog] = None,
    ):
        self.proxy_sqlexec_audit_log = proxy_sqlexec_audit_log

    def validate(self):
        if self.proxy_sqlexec_audit_log:
            for k in self.proxy_sqlexec_audit_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProxySQLExecAuditLog'] = []
        if self.proxy_sqlexec_audit_log is not None:
            for k in self.proxy_sqlexec_audit_log:
                result['ProxySQLExecAuditLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.proxy_sqlexec_audit_log = []
        if m.get('ProxySQLExecAuditLog') is not None:
            for k in m.get('ProxySQLExecAuditLog'):
                temp_model = ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog()
                self.proxy_sqlexec_audit_log.append(temp_model.from_map(k))
        return self


class ListProxySQLExecAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_sqlexec_audit_log_list: ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.proxy_sqlexec_audit_log_list = proxy_sqlexec_audit_log_list
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.proxy_sqlexec_audit_log_list:
            self.proxy_sqlexec_audit_log_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.proxy_sqlexec_audit_log_list is not None:
            result['ProxySQLExecAuditLogList'] = self.proxy_sqlexec_audit_log_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ProxySQLExecAuditLogList') is not None:
            temp_model = ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList()
            self.proxy_sqlexec_audit_log_list = temp_model.from_map(m['ProxySQLExecAuditLogList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProxySQLExecAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProxySQLExecAuditLogResponseBody = None,
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
            temp_model = ListProxySQLExecAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSQLExecAuditLogRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        exec_state: str = None,
        op_user_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_name: str = None,
        sql_type: str = None,
        start_time: str = None,
        tid: int = None,
    ):
        self.end_time = end_time
        self.exec_state = exec_state
        self.op_user_name = op_user_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_name = search_name
        self.sql_type = sql_type
        self.start_time = start_time
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.exec_state is not None:
            result['ExecState'] = self.exec_state
        if self.op_user_name is not None:
            result['OpUserName'] = self.op_user_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')
        if m.get('OpUserName') is not None:
            self.op_user_name = m.get('OpUserName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog(TeaModel):
    def __init__(
        self,
        affect_rows: int = None,
        db_id: int = None,
        elapsed_time: int = None,
        exec_state: str = None,
        instance_id: int = None,
        instance_name: str = None,
        logic: bool = None,
        op_time: str = None,
        remark: str = None,
        sql: str = None,
        sqltype: str = None,
        schema_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.affect_rows = affect_rows
        self.db_id = db_id
        self.elapsed_time = elapsed_time
        self.exec_state = exec_state
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.logic = logic
        self.op_time = op_time
        self.remark = remark
        self.sql = sql
        self.sqltype = sqltype
        self.schema_name = schema_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.exec_state is not None:
            result['ExecState'] = self.exec_state
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.op_time is not None:
            result['OpTime'] = self.op_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sql is not None:
            result['SQL'] = self.sql
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SQL') is not None:
            self.sql = m.get('SQL')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListSQLExecAuditLogResponseBodySQLExecAuditLogList(TeaModel):
    def __init__(
        self,
        sqlexec_audit_log: List[ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog] = None,
    ):
        self.sqlexec_audit_log = sqlexec_audit_log

    def validate(self):
        if self.sqlexec_audit_log:
            for k in self.sqlexec_audit_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SQLExecAuditLog'] = []
        if self.sqlexec_audit_log is not None:
            for k in self.sqlexec_audit_log:
                result['SQLExecAuditLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlexec_audit_log = []
        if m.get('SQLExecAuditLog') is not None:
            for k in m.get('SQLExecAuditLog'):
                temp_model = ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog()
                self.sqlexec_audit_log.append(temp_model.from_map(k))
        return self


class ListSQLExecAuditLogResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sqlexec_audit_log_list: ListSQLExecAuditLogResponseBodySQLExecAuditLogList = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.sqlexec_audit_log_list = sqlexec_audit_log_list
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.sqlexec_audit_log_list:
            self.sqlexec_audit_log_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlexec_audit_log_list is not None:
            result['SQLExecAuditLogList'] = self.sqlexec_audit_log_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLExecAuditLogList') is not None:
            temp_model = ListSQLExecAuditLogResponseBodySQLExecAuditLogList()
            self.sqlexec_audit_log_list = temp_model.from_map(m['SQLExecAuditLogList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSQLExecAuditLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSQLExecAuditLogResponseBody = None,
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
            temp_model = ListSQLExecAuditLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSQLReviewOriginSQLRequestOrderActionDetailPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSQLReviewOriginSQLRequestOrderActionDetail(TeaModel):
    def __init__(
        self,
        check_status_result: str = None,
        file_id: int = None,
        page: ListSQLReviewOriginSQLRequestOrderActionDetailPage = None,
        sqlreview_result: str = None,
    ):
        self.check_status_result = check_status_result
        self.file_id = file_id
        self.page = page
        self.sqlreview_result = sqlreview_result

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status_result is not None:
            result['CheckStatusResult'] = self.check_status_result
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.sqlreview_result is not None:
            result['SQLReviewResult'] = self.sqlreview_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatusResult') is not None:
            self.check_status_result = m.get('CheckStatusResult')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Page') is not None:
            temp_model = ListSQLReviewOriginSQLRequestOrderActionDetailPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('SQLReviewResult') is not None:
            self.sqlreview_result = m.get('SQLReviewResult')
        return self


class ListSQLReviewOriginSQLRequest(TeaModel):
    def __init__(
        self,
        order_action_detail: ListSQLReviewOriginSQLRequestOrderActionDetail = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_action_detail = order_action_detail
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        if self.order_action_detail:
            self.order_action_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_action_detail is not None:
            result['OrderActionDetail'] = self.order_action_detail.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderActionDetail') is not None:
            temp_model = ListSQLReviewOriginSQLRequestOrderActionDetail()
            self.order_action_detail = temp_model.from_map(m['OrderActionDetail'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListSQLReviewOriginSQLShrinkRequest(TeaModel):
    def __init__(
        self,
        order_action_detail_shrink: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_action_detail_shrink = order_action_detail_shrink
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_action_detail_shrink is not None:
            result['OrderActionDetail'] = self.order_action_detail_shrink
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderActionDetail') is not None:
            self.order_action_detail_shrink = m.get('OrderActionDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListSQLReviewOriginSQLResponseBodyOriginSQLList(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        checked_time: str = None,
        file_id: int = None,
        file_name: str = None,
        review_summary: str = None,
        sqlcontent: str = None,
        sqlid: int = None,
        sqlreview_query_key: str = None,
        sql_hash: str = None,
        status_desc: str = None,
    ):
        self.check_status = check_status
        self.checked_time = checked_time
        self.file_id = file_id
        self.file_name = file_name
        self.review_summary = review_summary
        self.sqlcontent = sqlcontent
        self.sqlid = sqlid
        self.sqlreview_query_key = sqlreview_query_key
        self.sql_hash = sql_hash
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.checked_time is not None:
            result['CheckedTime'] = self.checked_time
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.review_summary is not None:
            result['ReviewSummary'] = self.review_summary
        if self.sqlcontent is not None:
            result['SQLContent'] = self.sqlcontent
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key
        if self.sql_hash is not None:
            result['SqlHash'] = self.sql_hash
        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('CheckedTime') is not None:
            self.checked_time = m.get('CheckedTime')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ReviewSummary') is not None:
            self.review_summary = m.get('ReviewSummary')
        if m.get('SQLContent') is not None:
            self.sqlcontent = m.get('SQLContent')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')
        if m.get('SqlHash') is not None:
            self.sql_hash = m.get('SqlHash')
        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')
        return self


class ListSQLReviewOriginSQLResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        origin_sqllist: List[ListSQLReviewOriginSQLResponseBodyOriginSQLList] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.origin_sqllist = origin_sqllist
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.origin_sqllist:
            for k in self.origin_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['OriginSQLList'] = []
        if self.origin_sqllist is not None:
            for k in self.origin_sqllist:
                result['OriginSQLList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.origin_sqllist = []
        if m.get('OriginSQLList') is not None:
            for k in m.get('OriginSQLList'):
                temp_model = ListSQLReviewOriginSQLResponseBodyOriginSQLList()
                self.origin_sqllist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSQLReviewOriginSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSQLReviewOriginSQLResponseBody = None,
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
            temp_model = ListSQLReviewOriginSQLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveColumnsRequest(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        schema_name: str = None,
        security_level: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        self.column_name = column_name
        self.db_id = db_id
        self.logic = logic
        self.page_number = page_number
        self.page_size = page_size
        self.schema_name = schema_name
        self.security_level = security_level
        self.table_name = table_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListSensitiveColumnsResponseBodySensitiveColumnListSensitiveColumn(TeaModel):
    def __init__(
        self,
        column_count: int = None,
        column_name: str = None,
        function_type: str = None,
        schema_name: str = None,
        security_level: str = None,
        table_name: str = None,
    ):
        self.column_count = column_count
        self.column_name = column_name
        self.function_type = function_type
        self.schema_name = schema_name
        self.security_level = security_level
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_count is not None:
            result['ColumnCount'] = self.column_count
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.function_type is not None:
            result['FunctionType'] = self.function_type
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnCount') is not None:
            self.column_count = m.get('ColumnCount')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_column_list: ListSensitiveColumnsResponseBodySensitiveColumnList = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.sensitive_column_list = sensitive_column_list
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.sensitive_column_list:
            self.sensitive_column_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sensitive_column_list is not None:
            result['SensitiveColumnList'] = self.sensitive_column_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SensitiveColumnList') is not None:
            temp_model = ListSensitiveColumnsResponseBodySensitiveColumnList()
            self.sensitive_column_list = temp_model.from_map(m['SensitiveColumnList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListSensitiveColumnsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSensitiveColumnsDetailRequest(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        logic: bool = None,
        schema_name: str = None,
        table_name: str = None,
        tid: int = None,
    ):
        self.column_name = column_name
        self.db_id = db_id
        self.logic = logic
        self.schema_name = schema_name
        self.table_name = table_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailListSensitiveColumnsDetail(TeaModel):
    def __init__(
        self,
        column_description: str = None,
        column_name: str = None,
        column_type: str = None,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        schema_name: str = None,
        search_name: str = None,
        table_name: str = None,
    ):
        self.column_description = column_description
        self.column_name = column_name
        self.column_type = column_type
        self.db_id = db_id
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.schema_name = schema_name
        self.search_name = search_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_description is not None:
            result['ColumnDescription'] = self.column_description
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnDescription') is not None:
            self.column_description = m.get('ColumnDescription')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_columns_detail_list: ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.sensitive_columns_detail_list = sensitive_columns_detail_list
        self.success = success

    def validate(self):
        if self.sensitive_columns_detail_list:
            self.sensitive_columns_detail_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sensitive_columns_detail_list is not None:
            result['SensitiveColumnsDetailList'] = self.sensitive_columns_detail_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SensitiveColumnsDetailList') is not None:
            temp_model = ListSensitiveColumnsDetailResponseBodySensitiveColumnsDetailList()
            self.sensitive_columns_detail_list = temp_model.from_map(m['SensitiveColumnsDetailList'])
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
            temp_model = ListSensitiveColumnsDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStandardGroupsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
    ):
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListStandardGroupsResponseBodyStandardGroupList(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        group_mode: str = None,
        group_name: str = None,
        last_mender_id: int = None,
    ):
        self.db_type = db_type
        self.description = description
        self.group_mode = group_mode
        self.group_name = group_name
        self.last_mender_id = last_mender_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.last_mender_id is not None:
            result['LastMenderId'] = self.last_mender_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('LastMenderId') is not None:
            self.last_mender_id = m.get('LastMenderId')
        return self


class ListStandardGroupsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        standard_group_list: List[ListStandardGroupsResponseBodyStandardGroupList] = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.standard_group_list = standard_group_list
        self.success = success

    def validate(self):
        if self.standard_group_list:
            for k in self.standard_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StandardGroupList'] = []
        if self.standard_group_list is not None:
            for k in self.standard_group_list:
                result['StandardGroupList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.standard_group_list = []
        if m.get('StandardGroupList') is not None:
            for k in m.get('StandardGroupList'):
                temp_model = ListStandardGroupsResponseBodyStandardGroupList()
                self.standard_group_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListStandardGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListStandardGroupsResponseBody = None,
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
            temp_model = ListStandardGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        page_number: int = None,
        page_size: int = None,
        return_guid: bool = None,
        search_name: str = None,
        tid: int = None,
    ):
        self.database_id = database_id
        self.page_number = page_number
        self.page_size = page_size
        self.return_guid = return_guid
        self.search_name = search_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        description: str = None,
        encoding: str = None,
        engine: str = None,
        num_rows: int = None,
        owner_id_list: ListTablesResponseBodyTableListTableOwnerIdList = None,
        owner_name_list: ListTablesResponseBodyTableListTableOwnerNameList = None,
        store_capacity: int = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
        table_schema_name: str = None,
        table_type: str = None,
    ):
        self.database_id = database_id
        self.description = description
        self.encoding = encoding
        self.engine = engine
        self.num_rows = num_rows
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.store_capacity = store_capacity
        self.table_guid = table_guid
        self.table_id = table_id
        self.table_name = table_name
        self.table_schema_name = table_schema_name
        self.table_type = table_type

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.num_rows is not None:
            result['NumRows'] = self.num_rows
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.store_capacity is not None:
            result['StoreCapacity'] = self.store_capacity
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('NumRows') is not None:
            self.num_rows = m.get('NumRows')
        if m.get('OwnerIdList') is not None:
            temp_model = ListTablesResponseBodyTableListTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = ListTablesResponseBodyTableListTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('StoreCapacity') is not None:
            self.store_capacity = m.get('StoreCapacity')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table_list: ListTablesResponseBodyTableList = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.table_list = table_list
        self.total_count = total_count

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TableList') is not None:
            temp_model = ListTablesResponseBodyTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskFlowRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_instance_id: int = None,
        tid: int = None,
    ):
        self.dag_id = dag_id
        self.dag_instance_id = dag_instance_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_instance_id is not None:
            result['DagInstanceId'] = self.dag_instance_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagInstanceId') is not None:
            self.dag_instance_id = m.get('DagInstanceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListTaskFlowResponseBodyTaskFlowListDAGInstance(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_owner_nick_name: str = None,
        deploy_id: int = None,
        id: int = None,
        latest_instance_status: int = None,
        latest_instance_time: str = None,
        status: int = None,
    ):
        self.creator_id = creator_id
        self.creator_nick_name = creator_nick_name
        self.dag_owner_nick_name = dag_owner_nick_name
        self.deploy_id = deploy_id
        self.id = id
        self.latest_instance_status = latest_instance_status
        self.latest_instance_time = latest_instance_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name
        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.id is not None:
            result['Id'] = self.id
        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status
        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')
        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')
        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListTaskFlowResponseBodyTaskFlowList(TeaModel):
    def __init__(
        self,
        daginstance: List[ListTaskFlowResponseBodyTaskFlowListDAGInstance] = None,
    ):
        self.daginstance = daginstance

    def validate(self):
        if self.daginstance:
            for k in self.daginstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DAGInstance'] = []
        if self.daginstance is not None:
            for k in self.daginstance:
                result['DAGInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daginstance = []
        if m.get('DAGInstance') is not None:
            for k in m.get('DAGInstance'):
                temp_model = ListTaskFlowResponseBodyTaskFlowListDAGInstance()
                self.daginstance.append(temp_model.from_map(k))
        return self


class ListTaskFlowResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_flow_list: ListTaskFlowResponseBodyTaskFlowList = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.task_flow_list = task_flow_list

    def validate(self):
        if self.task_flow_list:
            self.task_flow_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_flow_list is not None:
            result['TaskFlowList'] = self.task_flow_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskFlowList') is not None:
            temp_model = ListTaskFlowResponseBodyTaskFlowList()
            self.task_flow_list = temp_model.from_map(m['TaskFlowList'])
        return self


class ListTaskFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskFlowResponseBody = None,
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
            temp_model = ListTaskFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskFlowInstanceRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        page_index: int = None,
        page_size: int = None,
        start_time_begin: str = None,
        start_time_end: str = None,
        tid: int = None,
        trigger_type: int = None,
    ):
        self.dag_id = dag_id
        self.page_index = page_index
        self.page_size = page_size
        self.start_time_begin = start_time_begin
        self.start_time_end = start_time_end
        self.tid = tid
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time_begin is not None:
            result['StartTimeBegin'] = self.start_time_begin
        if self.start_time_end is not None:
            result['StartTimeEnd'] = self.start_time_end
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTimeBegin') is not None:
            self.start_time_begin = m.get('StartTimeBegin')
        if m.get('StartTimeEnd') is not None:
            self.start_time_end = m.get('StartTimeEnd')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance(TeaModel):
    def __init__(
        self,
        business_time: str = None,
        dag_id: str = None,
        dag_name: str = None,
        end_time: str = None,
        history_dag_id: int = None,
        id: int = None,
        message: str = None,
        owner_name: str = None,
        status: int = None,
        trigger_type: int = None,
    ):
        self.business_time = business_time
        self.dag_id = dag_id
        self.dag_name = dag_name
        self.end_time = end_time
        self.history_dag_id = history_dag_id
        self.id = id
        self.message = message
        self.owner_name = owner_name
        self.status = status
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_name is not None:
            result['DagName'] = self.dag_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.history_dag_id is not None:
            result['HistoryDagId'] = self.history_dag_id
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HistoryDagId') is not None:
            self.history_dag_id = m.get('HistoryDagId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ListTaskFlowInstanceResponseBodyDAGInstanceList(TeaModel):
    def __init__(
        self,
        daginstance: List[ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance] = None,
    ):
        self.daginstance = daginstance

    def validate(self):
        if self.daginstance:
            for k in self.daginstance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DAGInstance'] = []
        if self.daginstance is not None:
            for k in self.daginstance:
                result['DAGInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daginstance = []
        if m.get('DAGInstance') is not None:
            for k in m.get('DAGInstance'):
                temp_model = ListTaskFlowInstanceResponseBodyDAGInstanceListDAGInstance()
                self.daginstance.append(temp_model.from_map(k))
        return self


class ListTaskFlowInstanceResponseBody(TeaModel):
    def __init__(
        self,
        daginstance_list: ListTaskFlowInstanceResponseBodyDAGInstanceList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.daginstance_list = daginstance_list
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.daginstance_list:
            self.daginstance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daginstance_list is not None:
            result['DAGInstanceList'] = self.daginstance_list.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DAGInstanceList') is not None:
            temp_model = ListTaskFlowInstanceResponseBodyDAGInstanceList()
            self.daginstance_list = temp_model.from_map(m['DAGInstanceList'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTaskFlowInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTaskFlowInstanceResponseBody = None,
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
            temp_model = ListTaskFlowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPermissionsRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        page_number: int = None,
        page_size: int = None,
        perm_type: str = None,
        search_key: str = None,
        tid: int = None,
        user_id: str = None,
    ):
        self.database_name = database_name
        self.db_type = db_type
        self.env_type = env_type
        self.logic = logic
        self.page_number = page_number
        self.page_size = page_size
        self.perm_type = perm_type
        self.search_key = search_key
        self.tid = tid
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        extra_data: str = None,
        origin_from: str = None,
        perm_type: str = None,
        user_access_id: str = None,
    ):
        self.create_date = create_date
        self.expire_date = expire_date
        self.extra_data = extra_data
        self.origin_from = origin_from
        self.perm_type = perm_type
        self.user_access_id = user_access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from
        if self.perm_type is not None:
            result['PermType'] = self.perm_type
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')
        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        alias: str = None,
        column_name: str = None,
        db_id: str = None,
        db_type: str = None,
        ds_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        logic: bool = None,
        perm_details: ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        table_id: str = None,
        table_name: str = None,
        user_id: str = None,
        user_nick_name: str = None,
    ):
        self.alias = alias
        self.column_name = column_name
        self.db_id = db_id
        self.db_type = db_type
        self.ds_type = ds_type
        self.env_type = env_type
        self.host = host
        self.instance_id = instance_id
        self.logic = logic
        self.perm_details = perm_details
        self.port = port
        self.schema_name = schema_name
        self.search_name = search_name
        self.table_id = table_id
        self.table_name = table_name
        self.user_id = user_id
        self.user_nick_name = user_nick_name

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PermDetails') is not None:
            temp_model = ListUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m['PermDetails'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_permissions: ListUserPermissionsResponseBodyUserPermissions = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.user_permissions = user_permissions

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserPermissions') is not None:
            temp_model = ListUserPermissionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m['UserPermissions'])
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
            temp_model = ListUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserTenantsRequest(TeaModel):
    def __init__(
        self,
        tid: int = None,
    ):
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListUserTenantsResponseBodyTenantList(TeaModel):
    def __init__(
        self,
        status: str = None,
        tenant_name: str = None,
        tid: int = None,
    ):
        self.status = status
        self.tenant_name = tenant_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListUserTenantsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant_list: List[ListUserTenantsResponseBodyTenantList] = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tenant_list = []
        if m.get('TenantList') is not None:
            for k in m.get('TenantList'):
                temp_model = ListUserTenantsResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k))
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
            temp_model = ListUserTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        role: str = None,
        search_key: str = None,
        tid: int = None,
        user_state: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.role = role
        self.search_key = search_key
        self.tid = tid
        self.user_state = user_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role is not None:
            result['Role'] = self.role
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        cur_execute_count: int = None,
        cur_result_count: int = None,
        ding_robot: str = None,
        email: str = None,
        last_login_time: str = None,
        max_execute_count: int = None,
        max_result_count: int = None,
        mobile: str = None,
        nick_name: str = None,
        notification_mode: str = None,
        parent_uid: str = None,
        role_id_list: ListUsersResponseBodyUserListUserRoleIdList = None,
        role_name_list: ListUsersResponseBodyUserListUserRoleNameList = None,
        signature_method: str = None,
        state: str = None,
        uid: str = None,
        user_id: str = None,
        webhook: str = None,
    ):
        self.cur_execute_count = cur_execute_count
        self.cur_result_count = cur_result_count
        self.ding_robot = ding_robot
        self.email = email
        self.last_login_time = last_login_time
        self.max_execute_count = max_execute_count
        self.max_result_count = max_result_count
        self.mobile = mobile
        self.nick_name = nick_name
        self.notification_mode = notification_mode
        self.parent_uid = parent_uid
        self.role_id_list = role_id_list
        self.role_name_list = role_name_list
        self.signature_method = signature_method
        self.state = state
        self.uid = uid
        self.user_id = user_id
        self.webhook = webhook

    def validate(self):
        if self.role_id_list:
            self.role_id_list.validate()
        if self.role_name_list:
            self.role_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_execute_count is not None:
            result['CurExecuteCount'] = self.cur_execute_count
        if self.cur_result_count is not None:
            result['CurResultCount'] = self.cur_result_count
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.last_login_time is not None:
            result['LastLoginTime'] = self.last_login_time
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.role_id_list is not None:
            result['RoleIdList'] = self.role_id_list.to_map()
        if self.role_name_list is not None:
            result['RoleNameList'] = self.role_name_list.to_map()
        if self.signature_method is not None:
            result['SignatureMethod'] = self.signature_method
        if self.state is not None:
            result['State'] = self.state
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurExecuteCount') is not None:
            self.cur_execute_count = m.get('CurExecuteCount')
        if m.get('CurResultCount') is not None:
            self.cur_result_count = m.get('CurResultCount')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('LastLoginTime') is not None:
            self.last_login_time = m.get('LastLoginTime')
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('RoleIdList') is not None:
            temp_model = ListUsersResponseBodyUserListUserRoleIdList()
            self.role_id_list = temp_model.from_map(m['RoleIdList'])
        if m.get('RoleNameList') is not None:
            temp_model = ListUsersResponseBodyUserListUserRoleNameList()
            self.role_name_list = temp_model.from_map(m['RoleNameList'])
        if m.get('SignatureMethod') is not None:
            self.signature_method = m.get('SignatureMethod')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_list: ListUsersResponseBodyUserList = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            self.user_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_list is not None:
            result['UserList'] = self.user_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserList') is not None:
            temp_model = ListUsersResponseBodyUserList()
            self.user_list = temp_model.from_map(m['UserList'])
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkFlowNodesRequest(TeaModel):
    def __init__(
        self,
        search_name: str = None,
        tid: int = None,
    ):
        self.search_name = search_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        real_name: str = None,
        user_id: int = None,
    ):
        self.nick_name = nick_name
        self.real_name = real_name
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
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        audit_users: ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers = None,
        comment: str = None,
        create_user_id: int = None,
        create_user_nick_name: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: str = None,
    ):
        self.audit_users = audit_users
        self.comment = comment
        self.create_user_id = create_user_id
        self.create_user_nick_name = create_user_nick_name
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type

    def validate(self):
        if self.audit_users:
            self.audit_users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_users is not None:
            result['AuditUsers'] = self.audit_users.to_map()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.create_user_nick_name is not None:
            result['CreateUserNickName'] = self.create_user_nick_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUsers') is not None:
            temp_model = ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers()
            self.audit_users = temp_model.from_map(m['AuditUsers'])
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('CreateUserNickName') is not None:
            self.create_user_nick_name = m.get('CreateUserNickName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        workflow_nodes: ListWorkFlowNodesResponseBodyWorkflowNodes = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WorkflowNodes') is not None:
            temp_model = ListWorkFlowNodesResponseBodyWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
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
            temp_model = ListWorkFlowNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkFlowTemplatesRequest(TeaModel):
    def __init__(
        self,
        search_name: str = None,
        tid: int = None,
    ):
        self.search_name = search_name
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode(TeaModel):
    def __init__(
        self,
        comment: str = None,
        create_user_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_type: str = None,
        position: int = None,
        template_id: int = None,
    ):
        self.comment = comment
        self.create_user_id = create_user_id
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type
        self.position = position
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.position is not None:
            result['Position'] = self.position
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        comment: str = None,
        create_user_id: int = None,
        enabled: str = None,
        is_system: int = None,
        template_id: int = None,
        template_name: str = None,
        workflow_nodes: ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes = None,
    ):
        self.comment = comment
        self.create_user_id = create_user_id
        self.enabled = enabled
        self.is_system = is_system
        self.template_id = template_id
        self.template_name = template_name
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.is_system is not None:
            result['IsSystem'] = self.is_system
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('IsSystem') is not None:
            self.is_system = m.get('IsSystem')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('WorkflowNodes') is not None:
            temp_model = ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m['WorkflowNodes'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        work_flow_templates: ListWorkFlowTemplatesResponseBodyWorkFlowTemplates = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success
        self.work_flow_templates = work_flow_templates

    def validate(self):
        if self.work_flow_templates:
            self.work_flow_templates.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.work_flow_templates is not None:
            result['WorkFlowTemplates'] = self.work_flow_templates.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = ListWorkFlowTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataCorrectExecSQLRequest(TeaModel):
    def __init__(
        self,
        exec_sql: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        self.exec_sql = exec_sql
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_sql is not None:
            result['ExecSQL'] = self.exec_sql
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecSQL') is not None:
            self.exec_sql = m.get('ExecSQL')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ModifyDataCorrectExecSQLResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDataCorrectExecSQLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataCorrectExecSQLResponseBody = None,
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
            temp_model = ModifyDataCorrectExecSQLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseDataCorrectSQLJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        order_id: int = None,
        tid: int = None,
        type: str = None,
    ):
        self.job_id = job_id
        self.order_id = order_id
        self.tid = tid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PauseDataCorrectSQLJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PauseDataCorrectSQLJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PauseDataCorrectSQLJobResponseBody = None,
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
            temp_model = PauseDataCorrectSQLJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReDeployLhDagVersionRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_version: int = None,
        tid: int = None,
    ):
        self.dag_id = dag_id
        self.dag_version = dag_version
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_version is not None:
            result['DagVersion'] = self.dag_version
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagVersion') is not None:
            self.dag_version = m.get('DagVersion')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class ReDeployLhDagVersionResponseBody(TeaModel):
    def __init__(
        self,
        deploy_id: int = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.deploy_id = deploy_id
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReDeployLhDagVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReDeployLhDagVersionResponseBody = None,
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
            temp_model = ReDeployLhDagVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterInstanceRequest(TeaModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_uid: int = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_source: str = None,
        instance_type: str = None,
        network_type: str = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule: str = None,
        sid: str = None,
        skip_test: bool = None,
        tid: int = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        self.data_link_name = data_link_name
        self.database_password = database_password
        self.database_user = database_user
        self.dba_uid = dba_uid
        self.ddl_online = ddl_online
        self.ecs_instance_id = ecs_instance_id
        self.ecs_region = ecs_region
        self.env_type = env_type
        self.export_timeout = export_timeout
        self.host = host
        self.instance_alias = instance_alias
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.network_type = network_type
        self.port = port
        self.query_timeout = query_timeout
        self.safe_rule = safe_rule
        self.sid = sid
        self.skip_test = skip_test
        self.tid = tid
        self.use_dsql = use_dsql
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_uid is not None:
            result['DbaUid'] = self.dba_uid
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.port is not None:
            result['Port'] = self.port
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.safe_rule is not None:
            result['SafeRule'] = self.safe_rule
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.skip_test is not None:
            result['SkipTest'] = self.skip_test
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaUid') is not None:
            self.dba_uid = m.get('DbaUid')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('SafeRule') is not None:
            self.safe_rule = m.get('SafeRule')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('SkipTest') is not None:
            self.skip_test = m.get('SkipTest')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class RegisterInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RegisterInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterUserRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        role_names: str = None,
        tid: int = None,
        uid: str = None,
        user_nick: str = None,
    ):
        self.mobile = mobile
        self.role_names = role_names
        self.tid = tid
        self.uid = uid
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class RegisterUserResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RegisterUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDataCorrectSQLJobRequest(TeaModel):
    def __init__(
        self,
        job_id: int = None,
        order_id: int = None,
        tid: int = None,
        type: str = None,
    ):
        self.job_id = job_id
        self.order_id = order_id
        self.tid = tid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RestartDataCorrectSQLJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartDataCorrectSQLJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartDataCorrectSQLJobResponseBody = None,
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
            temp_model = RestartDataCorrectSQLJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryDataCorrectPreCheckRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class RetryDataCorrectPreCheckResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryDataCorrectPreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryDataCorrectPreCheckResponseBody = None,
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
            temp_model = RetryDataCorrectPreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeUserPermissionRequest(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        ds_type: str = None,
        instance_id: int = None,
        logic: bool = None,
        perm_types: str = None,
        table_id: str = None,
        table_name: str = None,
        tid: int = None,
        user_access_id: str = None,
        user_id: str = None,
    ):
        self.db_id = db_id
        self.ds_type = ds_type
        self.instance_id = instance_id
        self.logic = logic
        self.perm_types = perm_types
        self.table_id = table_id
        self.table_name = table_name
        self.tid = tid
        self.user_access_id = user_access_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.ds_type is not None:
            result['DsType'] = self.ds_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.perm_types is not None:
            result['PermTypes'] = self.perm_types
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('PermTypes') is not None:
            self.perm_types = m.get('PermTypes')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RevokeUserPermissionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = RevokeUserPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDatabaseRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        search_range: str = None,
        search_target: str = None,
        tid: int = None,
    ):
        self.db_type = db_type
        self.env_type = env_type
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.search_range = search_range
        self.search_target = search_target
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.search_range is not None:
            result['SearchRange'] = self.search_range
        if self.search_target is not None:
            result['SearchTarget'] = self.search_target
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')
        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        alias: str = None,
        database_id: str = None,
        datalink_name: str = None,
        db_type: str = None,
        dba_id: str = None,
        encoding: str = None,
        env_type: str = None,
        host: str = None,
        logic: bool = None,
        owner_id_list: SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList = None,
        owner_name_list: SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        sid: str = None,
    ):
        self.alias = alias
        self.database_id = database_id
        self.datalink_name = datalink_name
        self.db_type = db_type
        self.dba_id = dba_id
        self.encoding = encoding
        self.env_type = env_type
        self.host = host
        self.logic = logic
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.port = port
        self.schema_name = schema_name
        self.search_name = search_name
        self.sid = sid

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.datalink_name is not None:
            result['DatalinkName'] = self.datalink_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.host is not None:
            result['Host'] = self.host
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        if self.search_name is not None:
            result['SearchName'] = self.search_name
        if self.sid is not None:
            result['Sid'] = self.sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatalinkName') is not None:
            self.datalink_name = m.get('DatalinkName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIdList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseListSearchDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        search_database_list: SearchDatabaseResponseBodySearchDatabaseList = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.search_database_list = search_database_list
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.search_database_list:
            self.search_database_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_database_list is not None:
            result['SearchDatabaseList'] = self.search_database_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchDatabaseList') is not None:
            temp_model = SearchDatabaseResponseBodySearchDatabaseList()
            self.search_database_list = temp_model.from_map(m['SearchDatabaseList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = SearchDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTableRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        page_number: int = None,
        page_size: int = None,
        return_guid: bool = None,
        search_key: str = None,
        search_range: str = None,
        search_target: str = None,
        tid: int = None,
    ):
        self.db_type = db_type
        self.env_type = env_type
        self.page_number = page_number
        self.page_size = page_size
        self.return_guid = return_guid
        self.search_key = search_key
        self.search_range = search_range
        self.search_target = search_target
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.search_range is not None:
            result['SearchRange'] = self.search_range
        if self.search_target is not None:
            result['SearchTarget'] = self.search_target
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')
        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        dbsearch_name: str = None,
        database_id: str = None,
        db_name: str = None,
        db_type: str = None,
        description: str = None,
        encoding: str = None,
        engine: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: SearchTableResponseBodySearchTableListSearchTableOwnerIdList = None,
        owner_name_list: SearchTableResponseBodySearchTableListSearchTableOwnerNameList = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
        table_schema_name: str = None,
    ):
        self.dbsearch_name = dbsearch_name
        self.database_id = database_id
        self.db_name = db_name
        self.db_type = db_type
        self.description = description
        self.encoding = encoding
        self.engine = engine
        self.env_type = env_type
        self.logic = logic
        self.owner_id_list = owner_id_list
        self.owner_name_list = owner_name_list
        self.table_guid = table_guid
        self.table_id = table_id
        self.table_name = table_name
        self.table_schema_name = table_schema_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbsearch_name is not None:
            result['DBSearchName'] = self.dbsearch_name
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()
        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBSearchName') is not None:
            self.dbsearch_name = m.get('DBSearchName')
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('OwnerIdList') is not None:
            temp_model = SearchTableResponseBodySearchTableListSearchTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m['OwnerIdList'])
        if m.get('OwnerNameList') is not None:
            temp_model = SearchTableResponseBodySearchTableListSearchTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m['OwnerNameList'])
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        search_table_list: SearchTableResponseBodySearchTableList = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.search_table_list = search_table_list
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.search_table_list:
            self.search_table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.search_table_list is not None:
            result['SearchTableList'] = self.search_table_list.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SearchTableList') is not None:
            temp_model = SearchTableResponseBodySearchTableList()
            self.search_table_list = temp_model.from_map(m['SearchTableList'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
            temp_model = SearchTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOwnersRequest(TeaModel):
    def __init__(
        self,
        owner_ids: str = None,
        owner_type: str = None,
        resource_id: str = None,
        tid: int = None,
    ):
        self.owner_ids = owner_ids
        self.owner_type = owner_type
        self.resource_id = resource_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SetOwnersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SetOwnersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitOrderApprovalRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SubmitOrderApprovalResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SubmitOrderApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitStructSyncOrderApprovalRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        tid: int = None,
    ):
        self.order_id = order_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SubmitStructSyncOrderApprovalResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        workflow_instance_id: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
            temp_model = SubmitStructSyncOrderApprovalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncDatabaseMetaRequest(TeaModel):
    def __init__(
        self,
        db_id: str = None,
        logic: bool = None,
        tid: int = None,
    ):
        self.db_id = db_id
        self.logic = logic
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SyncDatabaseMetaResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SyncDatabaseMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncInstanceMetaRequest(TeaModel):
    def __init__(
        self,
        ignore_table: bool = None,
        instance_id: str = None,
        tid: int = None,
    ):
        self.ignore_table = ignore_table
        self.instance_id = instance_id
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_table is not None:
            result['IgnoreTable'] = self.ignore_table
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tid is not None:
            result['Tid'] = self.tid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreTable') is not None:
            self.ignore_table = m.get('IgnoreTable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        return self


class SyncInstanceMetaResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = SyncInstanceMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: str = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule_id: str = None,
        sid: str = None,
        skip_test: bool = None,
        tid: int = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        self.data_link_name = data_link_name
        self.database_password = database_password
        self.database_user = database_user
        self.dba_id = dba_id
        self.ddl_online = ddl_online
        self.ecs_instance_id = ecs_instance_id
        self.ecs_region = ecs_region
        self.env_type = env_type
        self.export_timeout = export_timeout
        self.host = host
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_source = instance_source
        self.instance_type = instance_type
        self.port = port
        self.query_timeout = query_timeout
        self.safe_rule_id = safe_rule_id
        self.sid = sid
        self.skip_test = skip_test
        self.tid = tid
        self.use_dsql = use_dsql
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user
        if self.dba_id is not None:
            result['DbaId'] = self.dba_id
        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout
        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.skip_test is not None:
            result['SkipTest'] = self.skip_test
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')
        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')
        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')
        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('SkipTest') is not None:
            self.skip_test = m.get('SkipTest')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        max_execute_count: int = None,
        max_result_count: int = None,
        mobile: str = None,
        role_names: str = None,
        tid: int = None,
        uid: int = None,
        user_nick: str = None,
    ):
        self.max_execute_count = max_execute_count
        self.max_result_count = max_result_count
        self.mobile = mobile
        self.role_names = role_names
        self.tid = tid
        self.uid = uid
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count
        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.role_names is not None:
            result['RoleNames'] = self.role_names
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')
        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


