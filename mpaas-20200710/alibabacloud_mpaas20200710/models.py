# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelMpsSchedulerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        type: int = None,
        unique_ids: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.type = type
        # This parameter is required.
        self.unique_ids = unique_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_ids is not None:
            result['UniqueIds'] = self.unique_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueIds') is not None:
            self.unique_ids = m.get('UniqueIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CancelMpsSchedulerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: str = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CancelMpsSchedulerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelMpsSchedulerResponseBody = None,
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
            temp_model = CancelMpsSchedulerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPushSchedulerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        type: int = None,
        unique_ids: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.tenant_id = tenant_id
        self.type = type
        # This parameter is required.
        self.unique_ids = unique_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_ids is not None:
            result['UniqueIds'] = self.unique_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueIds') is not None:
            self.unique_ids = m.get('UniqueIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CancelPushSchedulerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: str = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CancelPushSchedulerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPushSchedulerResponseBody = None,
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
            temp_model = CancelPushSchedulerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeMcubeMiniTaskStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_type: str = None,
        package_id: int = None,
        task_id: int = None,
        task_status: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.package_id = package_id
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.task_status = task_status
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ChangeMcubeMiniTaskStatusResponseBodyChangeMiniTaskStatusResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeMcubeMiniTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        change_mini_task_status_result: ChangeMcubeMiniTaskStatusResponseBodyChangeMiniTaskStatusResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.change_mini_task_status_result = change_mini_task_status_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.change_mini_task_status_result:
            self.change_mini_task_status_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_mini_task_status_result is not None:
            result['ChangeMiniTaskStatusResult'] = self.change_mini_task_status_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeMiniTaskStatusResult') is not None:
            temp_model = ChangeMcubeMiniTaskStatusResponseBodyChangeMiniTaskStatusResult()
            self.change_mini_task_status_result = temp_model.from_map(m['ChangeMiniTaskStatusResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ChangeMcubeMiniTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeMcubeMiniTaskStatusResponseBody = None,
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
            temp_model = ChangeMcubeMiniTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeMcubeNebulaTaskStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_type: str = None,
        package_id: str = None,
        task_id: str = None,
        task_status: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.biz_type = biz_type
        self.package_id = package_id
        self.task_id = task_id
        self.task_status = task_status
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ChangeMcubeNebulaTaskStatusResponseBodyChangeMcubeNebulaTaskStatusResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeMcubeNebulaTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        change_mcube_nebula_task_status_result: ChangeMcubeNebulaTaskStatusResponseBodyChangeMcubeNebulaTaskStatusResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.change_mcube_nebula_task_status_result = change_mcube_nebula_task_status_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.change_mcube_nebula_task_status_result:
            self.change_mcube_nebula_task_status_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_mcube_nebula_task_status_result is not None:
            result['ChangeMcubeNebulaTaskStatusResult'] = self.change_mcube_nebula_task_status_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeMcubeNebulaTaskStatusResult') is not None:
            temp_model = ChangeMcubeNebulaTaskStatusResponseBodyChangeMcubeNebulaTaskStatusResult()
            self.change_mcube_nebula_task_status_result = temp_model.from_map(m['ChangeMcubeNebulaTaskStatusResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ChangeMcubeNebulaTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeMcubeNebulaTaskStatusResponseBody = None,
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
            temp_model = ChangeMcubeNebulaTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeMcubePublicTaskStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: str = None,
        task_status: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.task_id = task_id
        self.task_status = task_status
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ChangeMcubePublicTaskStatusResponseBodyChangeResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeMcubePublicTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        change_result: ChangeMcubePublicTaskStatusResponseBodyChangeResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.change_result = change_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.change_result:
            self.change_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_result is not None:
            result['ChangeResult'] = self.change_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeResult') is not None:
            temp_model = ChangeMcubePublicTaskStatusResponseBodyChangeResult()
            self.change_result = temp_model.from_map(m['ChangeResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ChangeMcubePublicTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeMcubePublicTaskStatusResponseBody = None,
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
            temp_model = ChangeMcubePublicTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeMiniAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        h_5name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.h_5name = h_5name
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeMiniAppResponseBodyCreateMiniResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeMiniAppResponseBody(TeaModel):
    def __init__(
        self,
        create_mini_result: CreateMcubeMiniAppResponseBodyCreateMiniResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_mini_result = create_mini_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_mini_result:
            self.create_mini_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mini_result is not None:
            result['CreateMiniResult'] = self.create_mini_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMiniResult') is not None:
            temp_model = CreateMcubeMiniAppResponseBodyCreateMiniResult()
            self.create_mini_result = temp_model.from_map(m['CreateMiniResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeMiniAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeMiniAppResponseBody = None,
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
            temp_model = CreateMcubeMiniAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeMiniTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        memo: str = None,
        package_id: int = None,
        publish_mode: int = None,
        publish_type: int = None,
        tenant_id: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        # This parameter is required.
        self.memo = memo
        # This parameter is required.
        self.package_id = package_id
        # This parameter is required.
        self.publish_mode = publish_mode
        # This parameter is required.
        self.publish_type = publish_type
        # This parameter is required.
        self.tenant_id = tenant_id
        self.whitelist_ids = whitelist_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult(TeaModel):
    def __init__(
        self,
        mini_task_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_task_id = mini_task_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_task_id is not None:
            result['MiniTaskId'] = self.mini_task_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniTaskId') is not None:
            self.mini_task_id = m.get('MiniTaskId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeMiniTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_mini_task_result: CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_mini_task_result = create_mini_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_mini_task_result:
            self.create_mini_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mini_task_result is not None:
            result['CreateMiniTaskResult'] = self.create_mini_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMiniTaskResult') is not None:
            temp_model = CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult()
            self.create_mini_task_result = temp_model.from_map(m['CreateMiniTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeMiniTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeMiniTaskResponseBody = None,
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
            temp_model = CreateMcubeMiniTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeNebulaAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        h_5name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeNebulaAppResponseBodyCreateNebulaAppResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeNebulaAppResponseBody(TeaModel):
    def __init__(
        self,
        create_nebula_app_result: CreateMcubeNebulaAppResponseBodyCreateNebulaAppResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_nebula_app_result = create_nebula_app_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_nebula_app_result:
            self.create_nebula_app_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_nebula_app_result is not None:
            result['CreateNebulaAppResult'] = self.create_nebula_app_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateNebulaAppResult') is not None:
            temp_model = CreateMcubeNebulaAppResponseBodyCreateNebulaAppResult()
            self.create_nebula_app_result = temp_model.from_map(m['CreateNebulaAppResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeNebulaAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeNebulaAppResponseBody = None,
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
            temp_model = CreateMcubeNebulaAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeNebulaResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        custom_domain_name: str = None,
        extend_info: str = None,
        file_url: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        install_type: int = None,
        main_url: str = None,
        onex_flag: bool = None,
        platform: str = None,
        repeat_nebula: int = None,
        resource_type: int = None,
        sub_url: str = None,
        tenant_id: str = None,
        vhost: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.custom_domain_name = custom_domain_name
        self.extend_info = extend_info
        self.file_url = file_url
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.install_type = install_type
        self.main_url = main_url
        self.onex_flag = onex_flag
        self.platform = platform
        self.repeat_nebula = repeat_nebula
        self.resource_type = resource_type
        self.sub_url = sub_url
        self.tenant_id = tenant_id
        self.vhost = vhost
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.custom_domain_name is not None:
            result['CustomDomainName'] = self.custom_domain_name
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.repeat_nebula is not None:
            result['RepeatNebula'] = self.repeat_nebula
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sub_url is not None:
            result['SubUrl'] = self.sub_url
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('CustomDomainName') is not None:
            self.custom_domain_name = m.get('CustomDomainName')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RepeatNebula') is not None:
            self.repeat_nebula = m.get('RepeatNebula')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SubUrl') is not None:
            self.sub_url = m.get('SubUrl')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeNebulaResourceResponseBodyCreateMcubeNebulaResourceReslult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_resource_id: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_resource_id = nebula_resource_id
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.nebula_resource_id is not None:
            result['NebulaResourceId'] = self.nebula_resource_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('NebulaResourceId') is not None:
            self.nebula_resource_id = m.get('NebulaResourceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeNebulaResourceResponseBody(TeaModel):
    def __init__(
        self,
        create_mcube_nebula_resource_reslult: CreateMcubeNebulaResourceResponseBodyCreateMcubeNebulaResourceReslult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_mcube_nebula_resource_reslult = create_mcube_nebula_resource_reslult
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_mcube_nebula_resource_reslult:
            self.create_mcube_nebula_resource_reslult.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mcube_nebula_resource_reslult is not None:
            result['CreateMcubeNebulaResourceReslult'] = self.create_mcube_nebula_resource_reslult.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMcubeNebulaResourceReslult') is not None:
            temp_model = CreateMcubeNebulaResourceResponseBodyCreateMcubeNebulaResourceReslult()
            self.create_mcube_nebula_resource_reslult = temp_model.from_map(m['CreateMcubeNebulaResourceReslult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeNebulaResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeNebulaResourceResponseBody = None,
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
            temp_model = CreateMcubeNebulaResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeNebulaTaskRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        biz_type: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_endtime_str: str = None,
        grey_num: int = None,
        grey_url: str = None,
        id: int = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        percent: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        release_version: str = None,
        res_ids: str = None,
        serial_version_uid: int = None,
        status: int = None,
        sync_mode: str = None,
        sync_result: str = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        tenant_id: str = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.biz_type = biz_type
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_endtime_str = grey_endtime_str
        self.grey_num = grey_num
        self.grey_url = grey_url
        self.id = id
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.percent = percent
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.release_version = release_version
        self.res_ids = res_ids
        self.serial_version_uid = serial_version_uid
        self.status = status
        self.sync_mode = sync_mode
        self.sync_result = sync_result
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.tenant_id = tenant_id
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_endtime_str is not None:
            result['GreyEndtimeStr'] = self.grey_endtime_str
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.grey_url is not None:
            result['GreyUrl'] = self.grey_url
        if self.id is not None:
            result['Id'] = self.id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.res_ids is not None:
            result['ResIds'] = self.res_ids
        if self.serial_version_uid is not None:
            result['SerialVersionUID'] = self.serial_version_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode
        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.upgrade_notice_num is not None:
            result['UpgradeNoticeNum'] = self.upgrade_notice_num
        if self.upgrade_progress is not None:
            result['UpgradeProgress'] = self.upgrade_progress
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyEndtimeStr') is not None:
            self.grey_endtime_str = m.get('GreyEndtimeStr')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('GreyUrl') is not None:
            self.grey_url = m.get('GreyUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResIds') is not None:
            self.res_ids = m.get('ResIds')
        if m.get('SerialVersionUID') is not None:
            self.serial_version_uid = m.get('SerialVersionUID')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')
        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UpgradeNoticeNum') is not None:
            self.upgrade_notice_num = m.get('UpgradeNoticeNum')
        if m.get('UpgradeProgress') is not None:
            self.upgrade_progress = m.get('UpgradeProgress')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeNebulaTaskResponseBodyCreateMcubeNebulaTaskResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_task_id: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_task_id = nebula_task_id
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.nebula_task_id is not None:
            result['NebulaTaskId'] = self.nebula_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('NebulaTaskId') is not None:
            self.nebula_task_id = m.get('NebulaTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeNebulaTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_mcube_nebula_task_result: CreateMcubeNebulaTaskResponseBodyCreateMcubeNebulaTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_mcube_nebula_task_result = create_mcube_nebula_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_mcube_nebula_task_result:
            self.create_mcube_nebula_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_mcube_nebula_task_result is not None:
            result['CreateMcubeNebulaTaskResult'] = self.create_mcube_nebula_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMcubeNebulaTaskResult') is not None:
            temp_model = CreateMcubeNebulaTaskResponseBodyCreateMcubeNebulaTaskResult()
            self.create_mcube_nebula_task_result = temp_model.from_map(m['CreateMcubeNebulaTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeNebulaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeNebulaTaskResponseBody = None,
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
            temp_model = CreateMcubeNebulaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeUpgradePackageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        appstore_url: str = None,
        bundle_id: str = None,
        custom_domain_name: str = None,
        desc: str = None,
        download_url: str = None,
        file_url: str = None,
        icon_file_url: str = None,
        install_amount: int = None,
        ios_symbolfile_url: str = None,
        is_enterprise: int = None,
        need_check: int = None,
        onex_flag: bool = None,
        platform: str = None,
        tenant_id: str = None,
        valid_days: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.appstore_url = appstore_url
        self.bundle_id = bundle_id
        self.custom_domain_name = custom_domain_name
        self.desc = desc
        self.download_url = download_url
        self.file_url = file_url
        self.icon_file_url = icon_file_url
        self.install_amount = install_amount
        self.ios_symbolfile_url = ios_symbolfile_url
        self.is_enterprise = is_enterprise
        self.need_check = need_check
        self.onex_flag = onex_flag
        self.platform = platform
        self.tenant_id = tenant_id
        self.valid_days = valid_days
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.custom_domain_name is not None:
            result['CustomDomainName'] = self.custom_domain_name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url
        if self.install_amount is not None:
            result['InstallAmount'] = self.install_amount
        if self.ios_symbolfile_url is not None:
            result['IosSymbolfileUrl'] = self.ios_symbolfile_url
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.need_check is not None:
            result['NeedCheck'] = self.need_check
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.valid_days is not None:
            result['ValidDays'] = self.valid_days
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CustomDomainName') is not None:
            self.custom_domain_name = m.get('CustomDomainName')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')
        if m.get('InstallAmount') is not None:
            self.install_amount = m.get('InstallAmount')
        if m.get('IosSymbolfileUrl') is not None:
            self.ios_symbolfile_url = m.get('IosSymbolfileUrl')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ValidDays') is not None:
            self.valid_days = m.get('ValidDays')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeUpgradePackageResponseBodyCreateUpgradePackageResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        upgrade_package_id: str = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.upgrade_package_id = upgrade_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.upgrade_package_id is not None:
            result['UpgradePackageId'] = self.upgrade_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UpgradePackageId') is not None:
            self.upgrade_package_id = m.get('UpgradePackageId')
        return self


class CreateMcubeUpgradePackageResponseBody(TeaModel):
    def __init__(
        self,
        create_upgrade_package_result: CreateMcubeUpgradePackageResponseBodyCreateUpgradePackageResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_upgrade_package_result = create_upgrade_package_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_upgrade_package_result:
            self.create_upgrade_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_upgrade_package_result is not None:
            result['CreateUpgradePackageResult'] = self.create_upgrade_package_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUpgradePackageResult') is not None:
            temp_model = CreateMcubeUpgradePackageResponseBodyCreateUpgradePackageResult()
            self.create_upgrade_package_result = temp_model.from_map(m['CreateUpgradePackageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeUpgradePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeUpgradePackageResponseBody = None,
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
            temp_model = CreateMcubeUpgradePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeUpgradeTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        history_force: int = None,
        memo: str = None,
        package_info_id: int = None,
        publish_mode: int = None,
        publish_type: int = None,
        tenant_id: str = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.history_force = history_force
        self.memo = memo
        self.package_info_id = package_info_id
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.tenant_id = tenant_id
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.history_force is not None:
            result['HistoryForce'] = self.history_force
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeUpgradeTaskResponseBodyCreateTaskResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        upgrade_task_id: str = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.upgrade_task_id = upgrade_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.upgrade_task_id is not None:
            result['UpgradeTaskId'] = self.upgrade_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UpgradeTaskId') is not None:
            self.upgrade_task_id = m.get('UpgradeTaskId')
        return self


class CreateMcubeUpgradeTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_task_result: CreateMcubeUpgradeTaskResponseBodyCreateTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_task_result = create_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_task_result:
            self.create_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_task_result is not None:
            result['CreateTaskResult'] = self.create_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTaskResult') is not None:
            temp_model = CreateMcubeUpgradeTaskResponseBodyCreateTaskResult()
            self.create_task_result = temp_model.from_map(m['CreateTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeUpgradeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeUpgradeTaskResponseBody = None,
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
            temp_model = CreateMcubeUpgradeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeVhostRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        vhost: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.vhost = vhost
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeVhostResponseBodyCreateVhostResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeVhostResponseBody(TeaModel):
    def __init__(
        self,
        create_vhost_result: CreateMcubeVhostResponseBodyCreateVhostResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_vhost_result = create_vhost_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_vhost_result:
            self.create_vhost_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_vhost_result is not None:
            result['CreateVhostResult'] = self.create_vhost_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateVhostResult') is not None:
            temp_model = CreateMcubeVhostResponseBodyCreateVhostResult()
            self.create_vhost_result = temp_model.from_map(m['CreateVhostResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeVhostResponseBody = None,
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
            temp_model = CreateMcubeVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        white_list_name: str = None,
        whitelist_type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.white_list_name = white_list_name
        # This parameter is required.
        self.whitelist_type = whitelist_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name
        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')
        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeWhitelistResponseBodyCreateWhitelistResult(TeaModel):
    def __init__(
        self,
        result_msg: str = None,
        success: bool = None,
        whitelist_id: str = None,
    ):
        self.result_msg = result_msg
        self.success = success
        self.whitelist_id = whitelist_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')
        return self


class CreateMcubeWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        create_whitelist_result: CreateMcubeWhitelistResponseBodyCreateWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_whitelist_result = create_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_whitelist_result:
            self.create_whitelist_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_whitelist_result is not None:
            result['CreateWhitelistResult'] = self.create_whitelist_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateWhitelistResult') is not None:
            temp_model = CreateMcubeWhitelistResponseBodyCreateWhitelistResult()
            self.create_whitelist_result = temp_model.from_map(m['CreateWhitelistResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeWhitelistResponseBody = None,
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
            temp_model = CreateMcubeWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcubeWhitelistForIdeRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        whitelist_value: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.whitelist_value = whitelist_value
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.whitelist_value is not None:
            result['WhitelistValue'] = self.whitelist_value
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WhitelistValue') is not None:
            self.whitelist_value = m.get('WhitelistValue')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcubeWhitelistForIdeResponseBodyCreateWhitelistForIdeResult(TeaModel):
    def __init__(
        self,
        result_msg: str = None,
        success: bool = None,
        whitelist_id: str = None,
    ):
        self.result_msg = result_msg
        self.success = success
        self.whitelist_id = whitelist_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')
        return self


class CreateMcubeWhitelistForIdeResponseBody(TeaModel):
    def __init__(
        self,
        create_whitelist_for_ide_result: CreateMcubeWhitelistForIdeResponseBodyCreateWhitelistForIdeResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_whitelist_for_ide_result = create_whitelist_for_ide_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_whitelist_for_ide_result:
            self.create_whitelist_for_ide_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_whitelist_for_ide_result is not None:
            result['CreateWhitelistForIdeResult'] = self.create_whitelist_for_ide_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateWhitelistForIdeResult') is not None:
            temp_model = CreateMcubeWhitelistForIdeResponseBodyCreateWhitelistForIdeResult()
            self.create_whitelist_for_ide_result = temp_model.from_map(m['CreateWhitelistForIdeResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcubeWhitelistForIdeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcubeWhitelistForIdeResponseBody = None,
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
            temp_model = CreateMcubeWhitelistForIdeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOpenGlobalDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_max_version: str = None,
        app_min_version: str = None,
        biz_type: str = None,
        ext_attr_str: str = None,
        max_uid: int = None,
        min_uid: int = None,
        os_type: str = None,
        payload: str = None,
        tenant_id: str = None,
        third_msg_id: str = None,
        uids: str = None,
        valid_time_end: int = None,
        valid_time_start: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_max_version = app_max_version
        self.app_min_version = app_min_version
        # This parameter is required.
        self.biz_type = biz_type
        self.ext_attr_str = ext_attr_str
        self.max_uid = max_uid
        self.min_uid = min_uid
        self.os_type = os_type
        # This parameter is required.
        self.payload = payload
        self.tenant_id = tenant_id
        # This parameter is required.
        self.third_msg_id = third_msg_id
        self.uids = uids
        self.valid_time_end = valid_time_end
        self.valid_time_start = valid_time_start
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_max_version is not None:
            result['AppMaxVersion'] = self.app_max_version
        if self.app_min_version is not None:
            result['AppMinVersion'] = self.app_min_version
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.ext_attr_str is not None:
            result['ExtAttrStr'] = self.ext_attr_str
        if self.max_uid is not None:
            result['MaxUid'] = self.max_uid
        if self.min_uid is not None:
            result['MinUid'] = self.min_uid
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_msg_id is not None:
            result['ThirdMsgId'] = self.third_msg_id
        if self.uids is not None:
            result['Uids'] = self.uids
        if self.valid_time_end is not None:
            result['ValidTimeEnd'] = self.valid_time_end
        if self.valid_time_start is not None:
            result['ValidTimeStart'] = self.valid_time_start
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppMaxVersion') is not None:
            self.app_max_version = m.get('AppMaxVersion')
        if m.get('AppMinVersion') is not None:
            self.app_min_version = m.get('AppMinVersion')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtAttrStr') is not None:
            self.ext_attr_str = m.get('ExtAttrStr')
        if m.get('MaxUid') is not None:
            self.max_uid = m.get('MaxUid')
        if m.get('MinUid') is not None:
            self.min_uid = m.get('MinUid')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdMsgId') is not None:
            self.third_msg_id = m.get('ThirdMsgId')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        if m.get('ValidTimeEnd') is not None:
            self.valid_time_end = m.get('ValidTimeEnd')
        if m.get('ValidTimeStart') is not None:
            self.valid_time_start = m.get('ValidTimeStart')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateOpenGlobalDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message

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
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateOpenGlobalDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOpenGlobalDataResponseBody = None,
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
            temp_model = CreateOpenGlobalDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOpenSingleDataRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_max_version: str = None,
        app_min_version: str = None,
        biz_type: str = None,
        check_online: bool = None,
        ext_attr_str: str = None,
        link_token: str = None,
        os_type: str = None,
        payload: str = None,
        tenant_id: str = None,
        third_msg_id: str = None,
        valid_time_end: int = None,
        valid_time_start: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_max_version = app_max_version
        self.app_min_version = app_min_version
        # This parameter is required.
        self.biz_type = biz_type
        self.check_online = check_online
        self.ext_attr_str = ext_attr_str
        # This parameter is required.
        self.link_token = link_token
        self.os_type = os_type
        # This parameter is required.
        self.payload = payload
        self.tenant_id = tenant_id
        # This parameter is required.
        self.third_msg_id = third_msg_id
        self.valid_time_end = valid_time_end
        self.valid_time_start = valid_time_start
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_max_version is not None:
            result['AppMaxVersion'] = self.app_max_version
        if self.app_min_version is not None:
            result['AppMinVersion'] = self.app_min_version
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.check_online is not None:
            result['CheckOnline'] = self.check_online
        if self.ext_attr_str is not None:
            result['ExtAttrStr'] = self.ext_attr_str
        if self.link_token is not None:
            result['LinkToken'] = self.link_token
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_msg_id is not None:
            result['ThirdMsgId'] = self.third_msg_id
        if self.valid_time_end is not None:
            result['ValidTimeEnd'] = self.valid_time_end
        if self.valid_time_start is not None:
            result['ValidTimeStart'] = self.valid_time_start
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppMaxVersion') is not None:
            self.app_max_version = m.get('AppMaxVersion')
        if m.get('AppMinVersion') is not None:
            self.app_min_version = m.get('AppMinVersion')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CheckOnline') is not None:
            self.check_online = m.get('CheckOnline')
        if m.get('ExtAttrStr') is not None:
            self.ext_attr_str = m.get('ExtAttrStr')
        if m.get('LinkToken') is not None:
            self.link_token = m.get('LinkToken')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdMsgId') is not None:
            self.third_msg_id = m.get('ThirdMsgId')
        if m.get('ValidTimeEnd') is not None:
            self.valid_time_end = m.get('ValidTimeEnd')
        if m.get('ValidTimeStart') is not None:
            self.valid_time_start = m.get('ValidTimeStart')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateOpenSingleDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.result_code = result_code
        self.result_message = result_message

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
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateOpenSingleDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOpenSingleDataResponseBody = None,
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
            temp_model = CreateOpenSingleDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        content: str = None,
        desc_info: str = None,
        icon_urls: str = None,
        image_urls: str = None,
        jump_action: int = None,
        push_style: int = None,
        show_style: int = None,
        template_name: str = None,
        tenant_id: str = None,
        title: str = None,
        uri: str = None,
        variables: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.content = content
        self.desc_info = desc_info
        self.icon_urls = icon_urls
        self.image_urls = image_urls
        self.jump_action = jump_action
        self.push_style = push_style
        self.show_style = show_style
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.title = title
        self.uri = uri
        self.variables = variables
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.content is not None:
            result['Content'] = self.content
        if self.desc_info is not None:
            result['DescInfo'] = self.desc_info
        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.jump_action is not None:
            result['JumpAction'] = self.jump_action
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.show_style is not None:
            result['ShowStyle'] = self.show_style
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.variables is not None:
            result['Variables'] = self.variables
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DescInfo') is not None:
            self.desc_info = m.get('DescInfo')
        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('JumpAction') is not None:
            self.jump_action = m.get('JumpAction')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('ShowStyle') is not None:
            self.show_style = m.get('ShowStyle')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCubecardWhitelistContentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        whitelist_id: str = None,
        whitelist_value: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.tenant_id = tenant_id
        self.whitelist_id = whitelist_id
        self.whitelist_value = whitelist_value
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id
        if self.whitelist_value is not None:
            result['WhitelistValue'] = self.whitelist_value
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')
        if m.get('WhitelistValue') is not None:
            self.whitelist_value = m.get('WhitelistValue')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteCubecardWhitelistContentResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCubecardWhitelistContentResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: DeleteCubecardWhitelistContentResponseBodyResultContentData = None,
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
            temp_model = DeleteCubecardWhitelistContentResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCubecardWhitelistContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: DeleteCubecardWhitelistContentResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = DeleteCubecardWhitelistContentResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteCubecardWhitelistContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCubecardWhitelistContentResponseBody = None,
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
            temp_model = DeleteCubecardWhitelistContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcubeMiniAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcubeMiniAppResponseBodyDeleteMiniResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcubeMiniAppResponseBody(TeaModel):
    def __init__(
        self,
        delete_mini_result: DeleteMcubeMiniAppResponseBodyDeleteMiniResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.delete_mini_result = delete_mini_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.delete_mini_result:
            self.delete_mini_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_mini_result is not None:
            result['DeleteMiniResult'] = self.delete_mini_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteMiniResult') is not None:
            temp_model = DeleteMcubeMiniAppResponseBodyDeleteMiniResult()
            self.delete_mini_result = temp_model.from_map(m['DeleteMiniResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcubeMiniAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcubeMiniAppResponseBody = None,
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
            temp_model = DeleteMcubeMiniAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcubeNebulaAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.h_5id = h_5id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcubeNebulaAppResponseBodyDeleteMcubeNebulaAppResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcubeNebulaAppResponseBody(TeaModel):
    def __init__(
        self,
        delete_mcube_nebula_app_result: DeleteMcubeNebulaAppResponseBodyDeleteMcubeNebulaAppResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.delete_mcube_nebula_app_result = delete_mcube_nebula_app_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.delete_mcube_nebula_app_result:
            self.delete_mcube_nebula_app_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_mcube_nebula_app_result is not None:
            result['DeleteMcubeNebulaAppResult'] = self.delete_mcube_nebula_app_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteMcubeNebulaAppResult') is not None:
            temp_model = DeleteMcubeNebulaAppResponseBodyDeleteMcubeNebulaAppResult()
            self.delete_mcube_nebula_app_result = temp_model.from_map(m['DeleteMcubeNebulaAppResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcubeNebulaAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcubeNebulaAppResponseBody = None,
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
            temp_model = DeleteMcubeNebulaAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcubeUpgradeResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: str = None,
        platform: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.id = id
        self.platform = platform
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcubeUpgradeResourceResponseBodyDeleteResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcubeUpgradeResourceResponseBody(TeaModel):
    def __init__(
        self,
        delete_result: DeleteMcubeUpgradeResourceResponseBodyDeleteResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.delete_result = delete_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.delete_result:
            self.delete_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_result is not None:
            result['DeleteResult'] = self.delete_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteResult') is not None:
            temp_model = DeleteMcubeUpgradeResourceResponseBodyDeleteResult()
            self.delete_result = temp_model.from_map(m['DeleteResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcubeUpgradeResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcubeUpgradeResourceResponseBody = None,
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
            temp_model = DeleteMcubeUpgradeResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcubeWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcubeWhitelistResponseBodyDeleteWhitelistResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcubeWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        delete_whitelist_result: DeleteMcubeWhitelistResponseBodyDeleteWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.delete_whitelist_result = delete_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.delete_whitelist_result:
            self.delete_whitelist_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_whitelist_result is not None:
            result['DeleteWhitelistResult'] = self.delete_whitelist_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteWhitelistResult') is not None:
            temp_model = DeleteMcubeWhitelistResponseBodyDeleteWhitelistResult()
            self.delete_whitelist_result = temp_model.from_map(m['DeleteWhitelistResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcubeWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcubeWhitelistResponseBody = None,
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
            temp_model = DeleteMcubeWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMdsWhitelistContentRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        whitelist_id: str = None,
        whitelist_value: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.tenant_id = tenant_id
        self.whitelist_id = whitelist_id
        self.whitelist_value = whitelist_value
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id
        if self.whitelist_value is not None:
            result['WhitelistValue'] = self.whitelist_value
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')
        if m.get('WhitelistValue') is not None:
            self.whitelist_value = m.get('WhitelistValue')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMdsWhitelistContentResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMdsWhitelistContentResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: DeleteMdsWhitelistContentResponseBodyResultContentData = None,
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
            temp_model = DeleteMdsWhitelistContentResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMdsWhitelistContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: DeleteMdsWhitelistContentResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = DeleteMdsWhitelistContentResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMdsWhitelistContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMdsWhitelistContentResponseBody = None,
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
            temp_model = DeleteMdsWhitelistContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.msg = msg
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
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExistMcubeRsaKeyRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ExistMcubeRsaKeyResponseBodyCheckRsaKeyResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExistMcubeRsaKeyResponseBody(TeaModel):
    def __init__(
        self,
        check_rsa_key_result: ExistMcubeRsaKeyResponseBodyCheckRsaKeyResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.check_rsa_key_result = check_rsa_key_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.check_rsa_key_result:
            self.check_rsa_key_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_rsa_key_result is not None:
            result['CheckRsaKeyResult'] = self.check_rsa_key_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRsaKeyResult') is not None:
            temp_model = ExistMcubeRsaKeyResponseBodyCheckRsaKeyResult()
            self.check_rsa_key_result = temp_model.from_map(m['CheckRsaKeyResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ExistMcubeRsaKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExistMcubeRsaKeyResponseBody = None,
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
            temp_model = ExistMcubeRsaKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcubeFileTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        onex_flag: bool = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken(TeaModel):
    def __init__(
        self,
        accessid: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetMcubeFileTokenResponseBodyGetFileTokenResult(TeaModel):
    def __init__(
        self,
        file_token: GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.file_token = file_token
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.file_token:
            self.file_token.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_token is not None:
            result['FileToken'] = self.file_token.to_map()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileToken') is not None:
            temp_model = GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken()
            self.file_token = temp_model.from_map(m['FileToken'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMcubeFileTokenResponseBody(TeaModel):
    def __init__(
        self,
        get_file_token_result: GetMcubeFileTokenResponseBodyGetFileTokenResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_file_token_result = get_file_token_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_file_token_result:
            self.get_file_token_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_file_token_result is not None:
            result['GetFileTokenResult'] = self.get_file_token_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetFileTokenResult') is not None:
            temp_model = GetMcubeFileTokenResponseBodyGetFileTokenResult()
            self.get_file_token_result = temp_model.from_map(m['GetFileTokenResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMcubeFileTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMcubeFileTokenResponseBody = None,
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
            temp_model = GetMcubeFileTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcubeNebulaResourceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.id = id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        creator: str = None,
        download_url: str = None,
        extend_info: str = None,
        extra_data: str = None,
        fallback_base_url: str = None,
        file_size: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        id: int = None,
        install_type: int = None,
        main_url: str = None,
        memo: str = None,
        meta_id: int = None,
        modifier: str = None,
        package_type: int = None,
        platform: str = None,
        publish_period: int = None,
        resource_type: str = None,
        status: int = None,
        vhost: str = None,
    ):
        self.app_code = app_code
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.creator = creator
        self.download_url = download_url
        self.extend_info = extend_info
        self.extra_data = extra_data
        self.fallback_base_url = fallback_base_url
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.id = id
        self.install_type = install_type
        self.main_url = main_url
        self.memo = memo
        self.meta_id = meta_id
        self.modifier = modifier
        self.package_type = package_type
        self.platform = platform
        self.publish_period = publish_period
        self.resource_type = resource_type
        self.status = status
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.fallback_base_url is not None:
            result['FallbackBaseUrl'] = self.fallback_base_url
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.id is not None:
            result['Id'] = self.id
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.meta_id is not None:
            result['MetaId'] = self.meta_id
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FallbackBaseUrl') is not None:
            self.fallback_base_url = m.get('FallbackBaseUrl')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MetaId') is not None:
            self.meta_id = m.get('MetaId')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        return self


class GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_resource_info: GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_resource_info = nebula_resource_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_resource_info:
            self.nebula_resource_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.nebula_resource_info is not None:
            result['NebulaResourceInfo'] = self.nebula_resource_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('NebulaResourceInfo') is not None:
            temp_model = GetMcubeNebulaResourceResponseBodyGetNebulaResourceResultNebulaResourceInfo()
            self.nebula_resource_info = temp_model.from_map(m['NebulaResourceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMcubeNebulaResourceResponseBody(TeaModel):
    def __init__(
        self,
        get_nebula_resource_result: GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_nebula_resource_result = get_nebula_resource_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_nebula_resource_result:
            self.get_nebula_resource_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_nebula_resource_result is not None:
            result['GetNebulaResourceResult'] = self.get_nebula_resource_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetNebulaResourceResult') is not None:
            temp_model = GetMcubeNebulaResourceResponseBodyGetNebulaResourceResult()
            self.get_nebula_resource_result = temp_model.from_map(m['GetNebulaResourceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMcubeNebulaResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMcubeNebulaResourceResponseBody = None,
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
            temp_model = GetMcubeNebulaResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcubeNebulaTaskDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList(TeaModel):
    def __init__(
        self,
        operation: str = None,
        rule_element: str = None,
        rule_type: str = None,
        value: str = None,
    ):
        self.operation = operation
        self.rule_element = rule_element
        self.rule_type = rule_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.rule_element is not None:
            result['RuleElement'] = self.rule_element
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('RuleElement') is not None:
            self.rule_element = m.get('RuleElement')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        atomic: int = None,
        base_info_id: int = None,
        biz_type: str = None,
        creator: str = None,
        cronexpress: int = None,
        download_url: str = None,
        extra_data: str = None,
        file_size: str = None,
        full_repair: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_endtime_str: str = None,
        grey_num: int = None,
        grey_url: str = None,
        id: int = None,
        issue_desc: str = None,
        memo: str = None,
        modifier: str = None,
        oss_path: str = None,
        package_id: int = None,
        percent: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_period: int = None,
        publish_type: int = None,
        quick_rollback: int = None,
        release_version: str = None,
        rule_json_list: List[GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList] = None,
        source_id: str = None,
        source_name: str = None,
        source_type: str = None,
        status: int = None,
        sync_result: str = None,
        sync_type: int = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.atomic = atomic
        self.base_info_id = base_info_id
        self.biz_type = biz_type
        self.creator = creator
        self.cronexpress = cronexpress
        self.download_url = download_url
        self.extra_data = extra_data
        self.file_size = file_size
        self.full_repair = full_repair
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_endtime_str = grey_endtime_str
        self.grey_num = grey_num
        self.grey_url = grey_url
        self.id = id
        self.issue_desc = issue_desc
        self.memo = memo
        self.modifier = modifier
        self.oss_path = oss_path
        self.package_id = package_id
        self.percent = percent
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_period = publish_period
        self.publish_type = publish_type
        self.quick_rollback = quick_rollback
        self.release_version = release_version
        self.rule_json_list = rule_json_list
        self.source_id = source_id
        self.source_name = source_name
        self.source_type = source_type
        self.status = status
        self.sync_result = sync_result
        self.sync_type = sync_type
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        if self.rule_json_list:
            for k in self.rule_json_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.atomic is not None:
            result['Atomic'] = self.atomic
        if self.base_info_id is not None:
            result['BaseInfoId'] = self.base_info_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.cronexpress is not None:
            result['Cronexpress'] = self.cronexpress
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.full_repair is not None:
            result['FullRepair'] = self.full_repair
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_endtime_str is not None:
            result['GreyEndtimeStr'] = self.grey_endtime_str
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.grey_url is not None:
            result['GreyUrl'] = self.grey_url
        if self.id is not None:
            result['Id'] = self.id
        if self.issue_desc is not None:
            result['IssueDesc'] = self.issue_desc
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.quick_rollback is not None:
            result['QuickRollback'] = self.quick_rollback
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k in self.rule_json_list:
                result['RuleJsonList'].append(k.to_map() if k else None)
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.source_name is not None:
            result['SourceName'] = self.source_name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.status is not None:
            result['Status'] = self.status
        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result
        if self.sync_type is not None:
            result['SyncType'] = self.sync_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.upgrade_notice_num is not None:
            result['UpgradeNoticeNum'] = self.upgrade_notice_num
        if self.upgrade_progress is not None:
            result['UpgradeProgress'] = self.upgrade_progress
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Atomic') is not None:
            self.atomic = m.get('Atomic')
        if m.get('BaseInfoId') is not None:
            self.base_info_id = m.get('BaseInfoId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Cronexpress') is not None:
            self.cronexpress = m.get('Cronexpress')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FullRepair') is not None:
            self.full_repair = m.get('FullRepair')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyEndtimeStr') is not None:
            self.grey_endtime_str = m.get('GreyEndtimeStr')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('GreyUrl') is not None:
            self.grey_url = m.get('GreyUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IssueDesc') is not None:
            self.issue_desc = m.get('IssueDesc')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('QuickRollback') is not None:
            self.quick_rollback = m.get('QuickRollback')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k in m.get('RuleJsonList'):
                temp_model = GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetailRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k))
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')
        if m.get('SyncType') is not None:
            self.sync_type = m.get('SyncType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('UpgradeNoticeNum') is not None:
            self.upgrade_notice_num = m.get('UpgradeNoticeNum')
        if m.get('UpgradeProgress') is not None:
            self.upgrade_progress = m.get('UpgradeProgress')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_task_detail: GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_task_detail = nebula_task_detail
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_task_detail:
            self.nebula_task_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.nebula_task_detail is not None:
            result['NebulaTaskDetail'] = self.nebula_task_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('NebulaTaskDetail') is not None:
            temp_model = GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResultNebulaTaskDetail()
            self.nebula_task_detail = temp_model.from_map(m['NebulaTaskDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMcubeNebulaTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        get_mcube_nebula_task_detail_result: GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_mcube_nebula_task_detail_result = get_mcube_nebula_task_detail_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_mcube_nebula_task_detail_result:
            self.get_mcube_nebula_task_detail_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_mcube_nebula_task_detail_result is not None:
            result['GetMcubeNebulaTaskDetailResult'] = self.get_mcube_nebula_task_detail_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetMcubeNebulaTaskDetailResult') is not None:
            temp_model = GetMcubeNebulaTaskDetailResponseBodyGetMcubeNebulaTaskDetailResult()
            self.get_mcube_nebula_task_detail_result = temp_model.from_map(m['GetMcubeNebulaTaskDetailResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMcubeNebulaTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMcubeNebulaTaskDetailResponseBody = None,
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
            temp_model = GetMcubeNebulaTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcubeUpgradePackageInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        package_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.package_id = package_id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoMobileTestFlightConfigDO(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        install_amount: int = None,
        invalid_time: str = None,
        upgrade_id: int = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.install_amount = install_amount
        self.invalid_time = invalid_time
        self.upgrade_id = upgrade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.install_amount is not None:
            result['InstallAmount'] = self.install_amount
        if self.invalid_time is not None:
            result['InvalidTime'] = self.invalid_time
        if self.upgrade_id is not None:
            result['UpgradeId'] = self.upgrade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallAmount') is not None:
            self.install_amount = m.get('InstallAmount')
        if m.get('InvalidTime') is not None:
            self.invalid_time = m.get('InvalidTime')
        if m.get('UpgradeId') is not None:
            self.upgrade_id = m.get('UpgradeId')
        return self


class GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoUpgradeBaseInfoDO(TeaModel):
    def __init__(
        self,
        allow_create_task: bool = None,
        app_code: str = None,
        appstore_url: str = None,
        change_log: str = None,
        creator: str = None,
        download_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_enterprise: int = None,
        modifier: str = None,
        need_check: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version: str = None,
        publish_period: int = None,
        verification_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.change_log = change_log
        self.creator = creator
        self.download_url = download_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_enterprise = is_enterprise
        self.modifier = modifier
        self.need_check = need_check
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_name = product_name
        self.product_version = product_version
        self.publish_period = publish_period
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_create_task is not None:
            result['AllowCreateTask'] = self.allow_create_task
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.need_check is not None:
            result['NeedCheck'] = self.need_check
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfo(TeaModel):
    def __init__(
        self,
        mobile_test_flight_config_do: GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoMobileTestFlightConfigDO = None,
        upgrade_base_info_do: GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoUpgradeBaseInfoDO = None,
    ):
        self.mobile_test_flight_config_do = mobile_test_flight_config_do
        self.upgrade_base_info_do = upgrade_base_info_do

    def validate(self):
        if self.mobile_test_flight_config_do:
            self.mobile_test_flight_config_do.validate()
        if self.upgrade_base_info_do:
            self.upgrade_base_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile_test_flight_config_do is not None:
            result['MobileTestFlightConfigDO'] = self.mobile_test_flight_config_do.to_map()
        if self.upgrade_base_info_do is not None:
            result['UpgradeBaseInfoDO'] = self.upgrade_base_info_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MobileTestFlightConfigDO') is not None:
            temp_model = GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoMobileTestFlightConfigDO()
            self.mobile_test_flight_config_do = temp_model.from_map(m['MobileTestFlightConfigDO'])
        if m.get('UpgradeBaseInfoDO') is not None:
            temp_model = GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfoUpgradeBaseInfoDO()
            self.upgrade_base_info_do = temp_model.from_map(m['UpgradeBaseInfoDO'])
        return self


class GetMcubeUpgradePackageInfoResponseBodyGetPackageResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        package_info: GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfo = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.package_info = package_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('PackageInfo') is not None:
            temp_model = GetMcubeUpgradePackageInfoResponseBodyGetPackageResultPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMcubeUpgradePackageInfoResponseBody(TeaModel):
    def __init__(
        self,
        get_package_result: GetMcubeUpgradePackageInfoResponseBodyGetPackageResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_package_result = get_package_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_package_result:
            self.get_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_package_result is not None:
            result['GetPackageResult'] = self.get_package_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetPackageResult') is not None:
            temp_model = GetMcubeUpgradePackageInfoResponseBodyGetPackageResult()
            self.get_package_result = temp_model.from_map(m['GetPackageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMcubeUpgradePackageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMcubeUpgradePackageInfoResponseBody = None,
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
            temp_model = GetMcubeUpgradePackageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcubeUpgradeTaskInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList(TeaModel):
    def __init__(
        self,
        operation: str = None,
        rule_element: str = None,
        rule_type: str = None,
        value: str = None,
    ):
        self.operation = operation
        self.rule_element = rule_element
        self.rule_type = rule_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.rule_element is not None:
            result['RuleElement'] = self.rule_element
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('RuleElement') is not None:
            self.rule_element = m.get('RuleElement')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        id: int = None,
        id_type: str = None,
        platform: str = None,
        status: int = None,
        user_type: str = None,
        white_list_count: int = None,
        white_list_name: str = None,
        whitelist_type: str = None,
    ):
        self.app_code = app_code
        self.id = id
        self.id_type = id_type
        self.platform = platform
        self.status = status
        self.user_type = user_type
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name
        self.whitelist_type = whitelist_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.status is not None:
            result['Status'] = self.status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count
        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name
        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')
        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')
        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')
        return self


class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        appstore_url: str = None,
        creator: str = None,
        download_url: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        history_force: int = None,
        id: int = None,
        is_enterprise: int = None,
        memo: str = None,
        modifier: str = None,
        package_info_id: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        rule_json_list: List[GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList] = None,
        silent_type: int = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        upgrade_valid_time: int = None,
        whitelist: List[GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist] = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.appstore_url = appstore_url
        self.creator = creator
        self.download_url = download_url
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.history_force = history_force
        self.id = id
        self.is_enterprise = is_enterprise
        self.memo = memo
        self.modifier = modifier
        self.package_info_id = package_info_id
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.rule_json_list = rule_json_list
        self.silent_type = silent_type
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.upgrade_valid_time = upgrade_valid_time
        self.whitelist = whitelist
        self.whitelist_ids = whitelist_ids
        self.workspace_id = workspace_id

    def validate(self):
        if self.rule_json_list:
            for k in self.rule_json_list:
                if k:
                    k.validate()
        if self.whitelist:
            for k in self.whitelist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.history_force is not None:
            result['HistoryForce'] = self.history_force
        if self.id is not None:
            result['Id'] = self.id
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k in self.rule_json_list:
                result['RuleJsonList'].append(k.to_map() if k else None)
        if self.silent_type is not None:
            result['SilentType'] = self.silent_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.upgrade_valid_time is not None:
            result['UpgradeValidTime'] = self.upgrade_valid_time
        result['Whitelist'] = []
        if self.whitelist is not None:
            for k in self.whitelist:
                result['Whitelist'].append(k.to_map() if k else None)
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k in m.get('RuleJsonList'):
                temp_model = GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k))
        if m.get('SilentType') is not None:
            self.silent_type = m.get('SilentType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('UpgradeValidTime') is not None:
            self.upgrade_valid_time = m.get('UpgradeValidTime')
        self.whitelist = []
        if m.get('Whitelist') is not None:
            for k in m.get('Whitelist'):
                temp_model = GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfoWhitelist()
                self.whitelist.append(temp_model.from_map(k))
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        task_info: GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskInfo') is not None:
            temp_model = GetMcubeUpgradeTaskInfoResponseBodyGetTaskResultTaskInfo()
            self.task_info = temp_model.from_map(m['TaskInfo'])
        return self


class GetMcubeUpgradeTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        get_task_result: GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_task_result = get_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_task_result:
            self.get_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_task_result is not None:
            result['GetTaskResult'] = self.get_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetTaskResult') is not None:
            temp_model = GetMcubeUpgradeTaskInfoResponseBodyGetTaskResult()
            self.get_task_result = temp_model.from_map(m['GetTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMcubeUpgradeTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMcubeUpgradeTaskInfoResponseBody = None,
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
            temp_model = GetMcubeUpgradeTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        action: str = None,
        content: str = None,
        desc_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_urls: str = None,
        id: str = None,
        image_urls: str = None,
        name: str = None,
        push_style: str = None,
        show_style: str = None,
        title: str = None,
        uri: str = None,
        variables: str = None,
    ):
        self.action = action
        self.content = content
        self.desc_info = desc_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon_urls = icon_urls
        self.id = id
        self.image_urls = image_urls
        self.name = name
        self.push_style = push_style
        self.show_style = show_style
        self.title = title
        self.uri = uri
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.content is not None:
            result['Content'] = self.content
        if self.desc_info is not None:
            result['DescInfo'] = self.desc_info
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls
        if self.id is not None:
            result['Id'] = self.id
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.name is not None:
            result['Name'] = self.name
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.show_style is not None:
            result['ShowStyle'] = self.show_style
        if self.title is not None:
            result['Title'] = self.title
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DescInfo') is not None:
            self.desc_info = m.get('DescInfo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('ShowStyle') is not None:
            self.show_style = m.get('ShowStyle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTemplateResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        # Id of the request
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAnalysisCoreIndexRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel: str = None,
        end_time: int = None,
        platform: str = None,
        start_time: int = None,
        task_id: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.channel = channel
        self.end_time = end_time
        self.platform = platform
        self.start_time = start_time
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListAnalysisCoreIndexResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        arrival_num: str = None,
        arrival_rate: str = None,
        ignore_num: str = None,
        ignore_rate: str = None,
        open_num: str = None,
        open_rate: str = None,
        push_num: str = None,
        push_total_num: str = None,
    ):
        self.arrival_num = arrival_num
        self.arrival_rate = arrival_rate
        self.ignore_num = ignore_num
        self.ignore_rate = ignore_rate
        self.open_num = open_num
        self.open_rate = open_rate
        self.push_num = push_num
        self.push_total_num = push_total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_num is not None:
            result['ArrivalNum'] = self.arrival_num
        if self.arrival_rate is not None:
            result['ArrivalRate'] = self.arrival_rate
        if self.ignore_num is not None:
            result['IgnoreNum'] = self.ignore_num
        if self.ignore_rate is not None:
            result['IgnoreRate'] = self.ignore_rate
        if self.open_num is not None:
            result['OpenNum'] = self.open_num
        if self.open_rate is not None:
            result['OpenRate'] = self.open_rate
        if self.push_num is not None:
            result['PushNum'] = self.push_num
        if self.push_total_num is not None:
            result['PushTotalNum'] = self.push_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrivalNum') is not None:
            self.arrival_num = m.get('ArrivalNum')
        if m.get('ArrivalRate') is not None:
            self.arrival_rate = m.get('ArrivalRate')
        if m.get('IgnoreNum') is not None:
            self.ignore_num = m.get('IgnoreNum')
        if m.get('IgnoreRate') is not None:
            self.ignore_rate = m.get('IgnoreRate')
        if m.get('OpenNum') is not None:
            self.open_num = m.get('OpenNum')
        if m.get('OpenRate') is not None:
            self.open_rate = m.get('OpenRate')
        if m.get('PushNum') is not None:
            self.push_num = m.get('PushNum')
        if m.get('PushTotalNum') is not None:
            self.push_total_num = m.get('PushTotalNum')
        return self


class ListAnalysisCoreIndexResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: ListAnalysisCoreIndexResponseBodyResultContentData = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListAnalysisCoreIndexResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnalysisCoreIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: ListAnalysisCoreIndexResponseBodyResultContent = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = ListAnalysisCoreIndexResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAnalysisCoreIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAnalysisCoreIndexResponseBody = None,
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
            temp_model = ListAnalysisCoreIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeMiniAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeMiniAppsResponseBodyListMiniResultMiniProgramList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        return self


class ListMcubeMiniAppsResponseBodyListMiniResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        mini_program_list: List[ListMcubeMiniAppsResponseBodyListMiniResultMiniProgramList] = None,
        page_size: int = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.mini_program_list = mini_program_list
        self.page_size = page_size
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.mini_program_list:
            for k in self.mini_program_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['MiniProgramList'] = []
        if self.mini_program_list is not None:
            for k in self.mini_program_list:
                result['MiniProgramList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.mini_program_list = []
        if m.get('MiniProgramList') is not None:
            for k in m.get('MiniProgramList'):
                temp_model = ListMcubeMiniAppsResponseBodyListMiniResultMiniProgramList()
                self.mini_program_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMcubeMiniAppsResponseBody(TeaModel):
    def __init__(
        self,
        list_mini_result: ListMcubeMiniAppsResponseBodyListMiniResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mini_result = list_mini_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mini_result:
            self.list_mini_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mini_result is not None:
            result['ListMiniResult'] = self.list_mini_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMiniResult') is not None:
            temp_model = ListMcubeMiniAppsResponseBodyListMiniResult()
            self.list_mini_result = temp_model.from_map(m['ListMiniResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeMiniAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeMiniAppsResponseBody = None,
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
            temp_model = ListMcubeMiniAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeMiniPackagesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        package_types: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.package_types = package_types
        self.page_num = page_num
        self.page_size = page_size
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.package_types is not None:
            result['PackageTypes'] = self.package_types
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('PackageTypes') is not None:
            self.package_types = m.get('PackageTypes')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeMiniPackagesResponseBodyListMiniPackageResultMiniPackageList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        download_url: str = None,
        extend_info: str = None,
        extra_data: str = None,
        fallback_base_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        id: int = None,
        install_type: int = None,
        main_url: str = None,
        memo: str = None,
        package_type: int = None,
        platform: str = None,
        publish_period: int = None,
        resource_type: int = None,
        status: int = None,
    ):
        self.app_code = app_code
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.download_url = download_url
        self.extend_info = extend_info
        self.extra_data = extra_data
        self.fallback_base_url = fallback_base_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.id = id
        self.install_type = install_type
        self.main_url = main_url
        self.memo = memo
        self.package_type = package_type
        self.platform = platform
        self.publish_period = publish_period
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.fallback_base_url is not None:
            result['FallbackBaseUrl'] = self.fallback_base_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.id is not None:
            result['Id'] = self.id
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FallbackBaseUrl') is not None:
            self.fallback_base_url = m.get('FallbackBaseUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMcubeMiniPackagesResponseBodyListMiniPackageResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        mini_package_list: List[ListMcubeMiniPackagesResponseBodyListMiniPackageResultMiniPackageList] = None,
        page_size: int = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.mini_package_list = mini_package_list
        self.page_size = page_size
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.mini_package_list:
            for k in self.mini_package_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['MiniPackageList'] = []
        if self.mini_package_list is not None:
            for k in self.mini_package_list:
                result['MiniPackageList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.mini_package_list = []
        if m.get('MiniPackageList') is not None:
            for k in m.get('MiniPackageList'):
                temp_model = ListMcubeMiniPackagesResponseBodyListMiniPackageResultMiniPackageList()
                self.mini_package_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMcubeMiniPackagesResponseBody(TeaModel):
    def __init__(
        self,
        list_mini_package_result: ListMcubeMiniPackagesResponseBodyListMiniPackageResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mini_package_result = list_mini_package_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mini_package_result:
            self.list_mini_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mini_package_result is not None:
            result['ListMiniPackageResult'] = self.list_mini_package_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMiniPackageResult') is not None:
            temp_model = ListMcubeMiniPackagesResponseBodyListMiniPackageResult()
            self.list_mini_package_result = temp_model.from_map(m['ListMiniPackageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeMiniPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeMiniPackagesResponseBody = None,
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
            temp_model = ListMcubeMiniPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeMiniTasksRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeMiniTasksResponseBodyListMiniTaskResultMiniTaskList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        memo: str = None,
        package_id: int = None,
        platform: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        status: str = None,
        task_status: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.memo = memo
        self.package_id = package_id
        self.platform = platform
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.status = status
        self.task_status = task_status
        self.whitelist_ids = whitelist_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.id is not None:
            result['Id'] = self.id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        return self


class ListMcubeMiniTasksResponseBodyListMiniTaskResult(TeaModel):
    def __init__(
        self,
        mini_task_list: List[ListMcubeMiniTasksResponseBodyListMiniTaskResultMiniTaskList] = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_task_list = mini_task_list
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mini_task_list:
            for k in self.mini_task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MiniTaskList'] = []
        if self.mini_task_list is not None:
            for k in self.mini_task_list:
                result['MiniTaskList'].append(k.to_map() if k else None)
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mini_task_list = []
        if m.get('MiniTaskList') is not None:
            for k in m.get('MiniTaskList'):
                temp_model = ListMcubeMiniTasksResponseBodyListMiniTaskResultMiniTaskList()
                self.mini_task_list.append(temp_model.from_map(k))
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMcubeMiniTasksResponseBody(TeaModel):
    def __init__(
        self,
        list_mini_task_result: ListMcubeMiniTasksResponseBodyListMiniTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mini_task_result = list_mini_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mini_task_result:
            self.list_mini_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mini_task_result is not None:
            result['ListMiniTaskResult'] = self.list_mini_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMiniTaskResult') is not None:
            temp_model = ListMcubeMiniTasksResponseBodyListMiniTaskResult()
            self.list_mini_task_result = temp_model.from_map(m['ListMiniTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeMiniTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeMiniTasksResponseBody = None,
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
            temp_model = ListMcubeMiniTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeNebulaAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.keyword = keyword
        self.page_num = page_num
        self.page_size = page_size
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos(TeaModel):
    def __init__(
        self,
        h_5id: str = None,
        h_5name: str = None,
    ):
        self.h_5id = h_5id
        self.h_5name = h_5name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        return self


class ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        nebula_app_infos: List[ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.nebula_app_infos = nebula_app_infos
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.nebula_app_infos:
            for k in self.nebula_app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['NebulaAppInfos'] = []
        if self.nebula_app_infos is not None:
            for k in self.nebula_app_infos:
                result['NebulaAppInfos'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.nebula_app_infos = []
        if m.get('NebulaAppInfos') is not None:
            for k in m.get('NebulaAppInfos'):
                temp_model = ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResultNebulaAppInfos()
                self.nebula_app_infos.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMcubeNebulaAppsResponseBody(TeaModel):
    def __init__(
        self,
        list_mcube_nebula_apps_result: ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mcube_nebula_apps_result = list_mcube_nebula_apps_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mcube_nebula_apps_result:
            self.list_mcube_nebula_apps_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mcube_nebula_apps_result is not None:
            result['ListMcubeNebulaAppsResult'] = self.list_mcube_nebula_apps_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMcubeNebulaAppsResult') is not None:
            temp_model = ListMcubeNebulaAppsResponseBodyListMcubeNebulaAppsResult()
            self.list_mcube_nebula_apps_result = temp_model.from_map(m['ListMcubeNebulaAppsResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeNebulaAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeNebulaAppsResponseBody = None,
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
            temp_model = ListMcubeNebulaAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeNebulaResourcesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.h_5id = h_5id
        self.page_num = page_num
        self.page_size = page_size
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResultNebulaResourceInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        creator: str = None,
        debug_url: str = None,
        download_url: str = None,
        extend_info: str = None,
        extra_data: str = None,
        fallback_base_url: str = None,
        file_size: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        id: int = None,
        install_type: int = None,
        lazy_load: int = None,
        main_url: str = None,
        md_5: str = None,
        memo: str = None,
        meta_id: int = None,
        modifier: str = None,
        package_type: int = None,
        platform: str = None,
        publish_period: int = None,
        release_version: str = None,
        resource_type: str = None,
        status: int = None,
        vhost: str = None,
    ):
        self.app_code = app_code
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.creator = creator
        self.debug_url = debug_url
        self.download_url = download_url
        self.extend_info = extend_info
        self.extra_data = extra_data
        self.fallback_base_url = fallback_base_url
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.id = id
        self.install_type = install_type
        self.lazy_load = lazy_load
        self.main_url = main_url
        self.md_5 = md_5
        self.memo = memo
        self.meta_id = meta_id
        self.modifier = modifier
        self.package_type = package_type
        self.platform = platform
        self.publish_period = publish_period
        self.release_version = release_version
        self.resource_type = resource_type
        self.status = status
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.debug_url is not None:
            result['DebugUrl'] = self.debug_url
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.fallback_base_url is not None:
            result['FallbackBaseUrl'] = self.fallback_base_url
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.id is not None:
            result['Id'] = self.id
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.lazy_load is not None:
            result['LazyLoad'] = self.lazy_load
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.meta_id is not None:
            result['MetaId'] = self.meta_id
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DebugUrl') is not None:
            self.debug_url = m.get('DebugUrl')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FallbackBaseUrl') is not None:
            self.fallback_base_url = m.get('FallbackBaseUrl')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('LazyLoad') is not None:
            self.lazy_load = m.get('LazyLoad')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MetaId') is not None:
            self.meta_id = m.get('MetaId')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        return self


class ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        nebula_resource_info: List[ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResultNebulaResourceInfo] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.nebula_resource_info = nebula_resource_info
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.nebula_resource_info:
            for k in self.nebula_resource_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['NebulaResourceInfo'] = []
        if self.nebula_resource_info is not None:
            for k in self.nebula_resource_info:
                result['NebulaResourceInfo'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.nebula_resource_info = []
        if m.get('NebulaResourceInfo') is not None:
            for k in m.get('NebulaResourceInfo'):
                temp_model = ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResultNebulaResourceInfo()
                self.nebula_resource_info.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMcubeNebulaResourcesResponseBody(TeaModel):
    def __init__(
        self,
        list_mcube_nebula_resource_result: ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mcube_nebula_resource_result = list_mcube_nebula_resource_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mcube_nebula_resource_result:
            self.list_mcube_nebula_resource_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mcube_nebula_resource_result is not None:
            result['ListMcubeNebulaResourceResult'] = self.list_mcube_nebula_resource_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMcubeNebulaResourceResult') is not None:
            temp_model = ListMcubeNebulaResourcesResponseBodyListMcubeNebulaResourceResult()
            self.list_mcube_nebula_resource_result = temp_model.from_map(m['ListMcubeNebulaResourceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeNebulaResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeNebulaResourcesResponseBody = None,
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
            temp_model = ListMcubeNebulaResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeNebulaTasksRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.id = id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        biz_type: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_endtime_str: str = None,
        grey_num: int = None,
        grey_url: str = None,
        id: int = None,
        memo: str = None,
        modifier: str = None,
        package_id: int = None,
        percent: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        release_version: str = None,
        status: int = None,
        sync_result: str = None,
        task_name: str = None,
        task_status: int = None,
        task_type: int = None,
        task_version: int = None,
        upgrade_notice_num: int = None,
        upgrade_progress: str = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.biz_type = biz_type
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_endtime_str = grey_endtime_str
        self.grey_num = grey_num
        self.grey_url = grey_url
        self.id = id
        self.memo = memo
        self.modifier = modifier
        self.package_id = package_id
        self.percent = percent
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.release_version = release_version
        self.status = status
        self.sync_result = sync_result
        self.task_name = task_name
        self.task_status = task_status
        self.task_type = task_type
        self.task_version = task_version
        self.upgrade_notice_num = upgrade_notice_num
        self.upgrade_progress = upgrade_progress
        self.whitelist_ids = whitelist_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_endtime_str is not None:
            result['GreyEndtimeStr'] = self.grey_endtime_str
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.grey_url is not None:
            result['GreyUrl'] = self.grey_url
        if self.id is not None:
            result['Id'] = self.id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.release_version is not None:
            result['ReleaseVersion'] = self.release_version
        if self.status is not None:
            result['Status'] = self.status
        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.upgrade_notice_num is not None:
            result['UpgradeNoticeNum'] = self.upgrade_notice_num
        if self.upgrade_progress is not None:
            result['UpgradeProgress'] = self.upgrade_progress
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyEndtimeStr') is not None:
            self.grey_endtime_str = m.get('GreyEndtimeStr')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('GreyUrl') is not None:
            self.grey_url = m.get('GreyUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('ReleaseVersion') is not None:
            self.release_version = m.get('ReleaseVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('UpgradeNoticeNum') is not None:
            self.upgrade_notice_num = m.get('UpgradeNoticeNum')
        if m.get('UpgradeProgress') is not None:
            self.upgrade_progress = m.get('UpgradeProgress')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        return self


class ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        nebula_task_info: List[ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo] = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.nebula_task_info = nebula_task_info
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.nebula_task_info:
            for k in self.nebula_task_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['NebulaTaskInfo'] = []
        if self.nebula_task_info is not None:
            for k in self.nebula_task_info:
                result['NebulaTaskInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.nebula_task_info = []
        if m.get('NebulaTaskInfo') is not None:
            for k in m.get('NebulaTaskInfo'):
                temp_model = ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResultNebulaTaskInfo()
                self.nebula_task_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMcubeNebulaTasksResponseBody(TeaModel):
    def __init__(
        self,
        list_mcube_nebula_task_result: ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mcube_nebula_task_result = list_mcube_nebula_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mcube_nebula_task_result:
            self.list_mcube_nebula_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mcube_nebula_task_result is not None:
            result['ListMcubeNebulaTaskResult'] = self.list_mcube_nebula_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMcubeNebulaTaskResult') is not None:
            temp_model = ListMcubeNebulaTasksResponseBodyListMcubeNebulaTaskResult()
            self.list_mcube_nebula_task_result = temp_model.from_map(m['ListMcubeNebulaTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeNebulaTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeNebulaTasksResponseBody = None,
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
            temp_model = ListMcubeNebulaTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeUpgradePackagesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.page_num = page_num
        self.page_size = page_size
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages(TeaModel):
    def __init__(
        self,
        allow_create_task: bool = None,
        app_code: str = None,
        appstore_url: str = None,
        change_log: str = None,
        creator: str = None,
        download_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_enterprise: int = None,
        md_5: str = None,
        modifier: str = None,
        need_check: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_period: int = None,
        verification_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.change_log = change_log
        self.creator = creator
        self.download_url = download_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.is_enterprise = is_enterprise
        self.md_5 = md_5
        self.modifier = modifier
        self.need_check = need_check
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_period = publish_period
        self.verification_code = verification_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_create_task is not None:
            result['AllowCreateTask'] = self.allow_create_task
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.need_check is not None:
            result['NeedCheck'] = self.need_check
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        return self


class ListMcubeUpgradePackagesResponseBodyListPackagesResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        packages: List[ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages] = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.packages = packages
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.packages:
            for k in self.packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['Packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['Packages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.packages = []
        if m.get('Packages') is not None:
            for k in m.get('Packages'):
                temp_model = ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages()
                self.packages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMcubeUpgradePackagesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        list_packages_result: ListMcubeUpgradePackagesResponseBodyListPackagesResult = None,
        page_size: int = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.list_packages_result = list_packages_result
        self.page_size = page_size
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.total_count = total_count

    def validate(self):
        if self.list_packages_result:
            self.list_packages_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.list_packages_result is not None:
            result['ListPackagesResult'] = self.list_packages_result.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('ListPackagesResult') is not None:
            temp_model = ListMcubeUpgradePackagesResponseBodyListPackagesResult()
            self.list_packages_result = temp_model.from_map(m['ListPackagesResult'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMcubeUpgradePackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeUpgradePackagesResponseBody = None,
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
            temp_model = ListMcubeUpgradePackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeUpgradeTasksRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        package_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.package_id = package_id
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_num: int = None,
        history_force: int = None,
        id: int = None,
        is_enterprise: int = None,
        memo: str = None,
        modifier: str = None,
        package_info_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_num = grey_num
        self.history_force = history_force
        self.id = id
        self.is_enterprise = is_enterprise
        self.memo = memo
        self.modifier = modifier
        self.package_info_id = package_info_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.whitelist_ids = whitelist_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.history_force is not None:
            result['HistoryForce'] = self.history_force
        if self.id is not None:
            result['Id'] = self.id
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.push_content is not None:
            result['PushContent'] = self.push_content
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        return self


class ListMcubeUpgradeTasksResponseBodyListTaskResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        task_info: List[ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo] = None,
    ):
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            for k in self.task_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        result['TaskInfo'] = []
        if self.task_info is not None:
            for k in self.task_info:
                result['TaskInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.task_info = []
        if m.get('TaskInfo') is not None:
            for k in m.get('TaskInfo'):
                temp_model = ListMcubeUpgradeTasksResponseBodyListTaskResultTaskInfo()
                self.task_info.append(temp_model.from_map(k))
        return self


class ListMcubeUpgradeTasksResponseBody(TeaModel):
    def __init__(
        self,
        list_task_result: ListMcubeUpgradeTasksResponseBodyListTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_task_result = list_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_task_result:
            self.list_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_task_result is not None:
            result['ListTaskResult'] = self.list_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListTaskResult') is not None:
            temp_model = ListMcubeUpgradeTasksResponseBodyListTaskResult()
            self.list_task_result = temp_model.from_map(m['ListTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeUpgradeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeUpgradeTasksResponseBody = None,
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
            temp_model = ListMcubeUpgradeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcubeWhitelistsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_num: int = None,
        page_size: int = None,
        tenant_id: str = None,
        whitelist_name: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.page_num = page_num
        self.page_size = page_size
        # This parameter is required.
        self.tenant_id = tenant_id
        self.whitelist_name = whitelist_name
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.whitelist_name is not None:
            result['WhitelistName'] = self.whitelist_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhitelistName') is not None:
            self.whitelist_name = m.get('WhitelistName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        white_list_count: int = None,
        white_list_name: str = None,
        whitelist_type: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name
        self.whitelist_type = whitelist_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count
        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name
        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')
        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')
        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')
        return self


class ListMcubeWhitelistsResponseBodyListWhitelistResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        has_more: bool = None,
        page_size: int = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
        whitelists: List[ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists] = None,
    ):
        self.current_page = current_page
        self.has_more = has_more
        self.page_size = page_size
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count
        self.whitelists = whitelists

    def validate(self):
        if self.whitelists:
            for k in self.whitelists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Whitelists'] = []
        if self.whitelists is not None:
            for k in self.whitelists:
                result['Whitelists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k in m.get('Whitelists'):
                temp_model = ListMcubeWhitelistsResponseBodyListWhitelistResultWhitelists()
                self.whitelists.append(temp_model.from_map(k))
        return self


class ListMcubeWhitelistsResponseBody(TeaModel):
    def __init__(
        self,
        list_whitelist_result: ListMcubeWhitelistsResponseBodyListWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_whitelist_result = list_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_whitelist_result:
            self.list_whitelist_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_whitelist_result is not None:
            result['ListWhitelistResult'] = self.list_whitelist_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListWhitelistResult') is not None:
            temp_model = ListMcubeWhitelistsResponseBodyListWhitelistResult()
            self.list_whitelist_result = temp_model.from_map(m['ListWhitelistResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcubeWhitelistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcubeWhitelistsResponseBody = None,
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
            temp_model = ListMcubeWhitelistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatePageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.current_page = current_page
        self.page_size = page_size
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTemplatePageResponseBodyData(TeaModel):
    def __init__(
        self,
        action: str = None,
        content: str = None,
        desc_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_urls: str = None,
        id: str = None,
        image_urls: str = None,
        name: str = None,
        push_style: str = None,
        show_style: str = None,
        title: str = None,
        uri: str = None,
        variables: str = None,
    ):
        self.action = action
        self.content = content
        self.desc_info = desc_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon_urls = icon_urls
        self.id = id
        self.image_urls = image_urls
        self.name = name
        self.push_style = push_style
        self.show_style = show_style
        self.title = title
        self.uri = uri
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.content is not None:
            result['Content'] = self.content
        if self.desc_info is not None:
            result['DescInfo'] = self.desc_info
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls
        if self.id is not None:
            result['Id'] = self.id
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.name is not None:
            result['Name'] = self.name
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.show_style is not None:
            result['ShowStyle'] = self.show_style
        if self.title is not None:
            result['Title'] = self.title
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DescInfo') is not None:
            self.desc_info = m.get('DescInfo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('ShowStyle') is not None:
            self.show_style = m.get('ShowStyle')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ListTemplatePageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: List[ListTemplatePageResponseBodyData] = None,
        msg: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.msg = msg
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

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
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTemplatePageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListTemplatePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplatePageResponseBody = None,
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
            temp_model = ListTemplatePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushBroadcastRequest(TeaModel):
    def __init__(
        self,
        android_channel: int = None,
        app_id: str = None,
        bind_end_time: int = None,
        bind_start_time: int = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        msgkey: str = None,
        notify_level: Dict[str, Any] = None,
        notify_type: str = None,
        push_action: int = None,
        push_status: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category: Dict[str, Any] = None,
        time_mode: int = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        un_bind_end_time: int = None,
        un_bind_period: int = None,
        un_bind_start_time: int = None,
        workspace_id: str = None,
    ):
        self.android_channel = android_channel
        # This parameter is required.
        self.app_id = app_id
        self.bind_end_time = bind_end_time
        self.bind_start_time = bind_start_time
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        # This parameter is required.
        self.msgkey = msgkey
        self.notify_level = notify_level
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_status = push_status
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category = third_channel_category
        self.time_mode = time_mode
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.un_bind_end_time = un_bind_end_time
        self.un_bind_period = un_bind_period
        self.un_bind_start_time = un_bind_start_time
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_channel is not None:
            result['AndroidChannel'] = self.android_channel
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bind_end_time is not None:
            result['BindEndTime'] = self.bind_end_time
        if self.bind_start_time is not None:
            result['BindStartTime'] = self.bind_start_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.msgkey is not None:
            result['Msgkey'] = self.msgkey
        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category is not None:
            result['ThirdChannelCategory'] = self.third_channel_category
        if self.time_mode is not None:
            result['TimeMode'] = self.time_mode
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.un_bind_end_time is not None:
            result['UnBindEndTime'] = self.un_bind_end_time
        if self.un_bind_period is not None:
            result['UnBindPeriod'] = self.un_bind_period
        if self.un_bind_start_time is not None:
            result['UnBindStartTime'] = self.un_bind_start_time
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidChannel') is not None:
            self.android_channel = m.get('AndroidChannel')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BindEndTime') is not None:
            self.bind_end_time = m.get('BindEndTime')
        if m.get('BindStartTime') is not None:
            self.bind_start_time = m.get('BindStartTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('Msgkey') is not None:
            self.msgkey = m.get('Msgkey')
        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category = m.get('ThirdChannelCategory')
        if m.get('TimeMode') is not None:
            self.time_mode = m.get('TimeMode')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('UnBindEndTime') is not None:
            self.un_bind_end_time = m.get('UnBindEndTime')
        if m.get('UnBindPeriod') is not None:
            self.un_bind_period = m.get('UnBindPeriod')
        if m.get('UnBindStartTime') is not None:
            self.un_bind_start_time = m.get('UnBindStartTime')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushBroadcastShrinkRequest(TeaModel):
    def __init__(
        self,
        android_channel: int = None,
        app_id: str = None,
        bind_end_time: int = None,
        bind_start_time: int = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        msgkey: str = None,
        notify_level_shrink: str = None,
        notify_type: str = None,
        push_action: int = None,
        push_status: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category_shrink: str = None,
        time_mode: int = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        un_bind_end_time: int = None,
        un_bind_period: int = None,
        un_bind_start_time: int = None,
        workspace_id: str = None,
    ):
        self.android_channel = android_channel
        # This parameter is required.
        self.app_id = app_id
        self.bind_end_time = bind_end_time
        self.bind_start_time = bind_start_time
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        # This parameter is required.
        self.msgkey = msgkey
        self.notify_level_shrink = notify_level_shrink
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_status = push_status
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category_shrink = third_channel_category_shrink
        self.time_mode = time_mode
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.un_bind_end_time = un_bind_end_time
        self.un_bind_period = un_bind_period
        self.un_bind_start_time = un_bind_start_time
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_channel is not None:
            result['AndroidChannel'] = self.android_channel
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bind_end_time is not None:
            result['BindEndTime'] = self.bind_end_time
        if self.bind_start_time is not None:
            result['BindStartTime'] = self.bind_start_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.msgkey is not None:
            result['Msgkey'] = self.msgkey
        if self.notify_level_shrink is not None:
            result['NotifyLevel'] = self.notify_level_shrink
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category_shrink is not None:
            result['ThirdChannelCategory'] = self.third_channel_category_shrink
        if self.time_mode is not None:
            result['TimeMode'] = self.time_mode
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.un_bind_end_time is not None:
            result['UnBindEndTime'] = self.un_bind_end_time
        if self.un_bind_period is not None:
            result['UnBindPeriod'] = self.un_bind_period
        if self.un_bind_start_time is not None:
            result['UnBindStartTime'] = self.un_bind_start_time
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidChannel') is not None:
            self.android_channel = m.get('AndroidChannel')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BindEndTime') is not None:
            self.bind_end_time = m.get('BindEndTime')
        if m.get('BindStartTime') is not None:
            self.bind_start_time = m.get('BindStartTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('Msgkey') is not None:
            self.msgkey = m.get('Msgkey')
        if m.get('NotifyLevel') is not None:
            self.notify_level_shrink = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category_shrink = m.get('ThirdChannelCategory')
        if m.get('TimeMode') is not None:
            self.time_mode = m.get('TimeMode')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('UnBindEndTime') is not None:
            self.un_bind_end_time = m.get('UnBindEndTime')
        if m.get('UnBindPeriod') is not None:
            self.un_bind_period = m.get('UnBindPeriod')
        if m.get('UnBindStartTime') is not None:
            self.un_bind_start_time = m.get('UnBindStartTime')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushBroadcastResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushBroadcastResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushBroadcastResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = PushBroadcastResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushBroadcastResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushBroadcastResponseBody = None,
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
            temp_model = PushBroadcastResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMultipleRequestTargetMsg(TeaModel):
    def __init__(
        self,
        extended_params: str = None,
        msg_key: str = None,
        target: str = None,
        template_key_value: str = None,
    ):
        self.extended_params = extended_params
        # This parameter is required.
        self.msg_key = msg_key
        # This parameter is required.
        self.target = target
        self.template_key_value = template_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.target is not None:
            result['Target'] = self.target
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        return self


class PushMultipleRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        notify_level: Dict[str, Any] = None,
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msg: List[PushMultipleRequestTargetMsg] = None,
        task_name: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category: Dict[str, Any] = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        self.notify_level = notify_level
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msg = target_msg
        self.task_name = task_name
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category = third_channel_category
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.target_msg:
            for k in self.target_msg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        result['TargetMsg'] = []
        if self.target_msg is not None:
            for k in self.target_msg:
                result['TargetMsg'].append(k.to_map() if k else None)
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category is not None:
            result['ThirdChannelCategory'] = self.third_channel_category
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        self.target_msg = []
        if m.get('TargetMsg') is not None:
            for k in m.get('TargetMsg'):
                temp_model = PushMultipleRequestTargetMsg()
                self.target_msg.append(temp_model.from_map(k))
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category = m.get('ThirdChannelCategory')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushMultipleShrinkRequestTargetMsg(TeaModel):
    def __init__(
        self,
        extended_params: str = None,
        msg_key: str = None,
        target: str = None,
        template_key_value: str = None,
    ):
        self.extended_params = extended_params
        # This parameter is required.
        self.msg_key = msg_key
        # This parameter is required.
        self.target = target
        self.template_key_value = template_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.target is not None:
            result['Target'] = self.target
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        return self


class PushMultipleShrinkRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        notify_level_shrink: str = None,
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msg: List[PushMultipleShrinkRequestTargetMsg] = None,
        task_name: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category_shrink: str = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        self.notify_level_shrink = notify_level_shrink
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msg = target_msg
        self.task_name = task_name
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category_shrink = third_channel_category_shrink
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.target_msg:
            for k in self.target_msg:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level_shrink is not None:
            result['NotifyLevel'] = self.notify_level_shrink
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        result['TargetMsg'] = []
        if self.target_msg is not None:
            for k in self.target_msg:
                result['TargetMsg'].append(k.to_map() if k else None)
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category_shrink is not None:
            result['ThirdChannelCategory'] = self.third_channel_category_shrink
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level_shrink = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        self.target_msg = []
        if m.get('TargetMsg') is not None:
            for k in m.get('TargetMsg'):
                temp_model = PushMultipleShrinkRequestTargetMsg()
                self.target_msg.append(temp_model.from_map(k))
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category_shrink = m.get('ThirdChannelCategory')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushMultipleResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushMultipleResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushMultipleResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = PushMultipleResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushMultipleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushMultipleResponseBody = None,
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
            temp_model = PushMultipleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushQueryDeviceStateRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        target: str = None,
        target_type: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.target = target
        self.target_type = target_type
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushQueryDeviceStateResponseBodyData(TeaModel):
    def __init__(
        self,
        delivery_token: str = None,
        device_id: str = None,
        manufacturer: str = None,
        platform: str = None,
        statue: str = None,
        third_token: str = None,
        user_id: str = None,
    ):
        self.delivery_token = delivery_token
        self.device_id = device_id
        self.manufacturer = manufacturer
        self.platform = platform
        self.statue = statue
        self.third_token = third_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.statue is not None:
            result['Statue'] = self.statue
        if self.third_token is not None:
            result['ThirdToken'] = self.third_token
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Statue') is not None:
            self.statue = m.get('Statue')
        if m.get('ThirdToken') is not None:
            self.third_token = m.get('ThirdToken')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PushQueryDeviceStateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: PushQueryDeviceStateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = PushQueryDeviceStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushQueryDeviceStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushQueryDeviceStateResponseBody = None,
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
            temp_model = PushQueryDeviceStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushSimpleRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        content: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        icon_urls: str = None,
        image_urls: str = None,
        mi_channel_id: str = None,
        notify_level: Dict[str, Any] = None,
        notify_type: str = None,
        push_action: int = None,
        push_style: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msgkey: str = None,
        task_name: str = None,
        tenant_id: str = None,
        third_channel_category: Dict[str, Any] = None,
        title: str = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.icon_urls = icon_urls
        self.image_urls = image_urls
        self.mi_channel_id = mi_channel_id
        self.notify_level = notify_level
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_style = push_style
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msgkey = target_msgkey
        self.task_name = task_name
        self.tenant_id = tenant_id
        self.third_channel_category = third_channel_category
        # This parameter is required.
        self.title = title
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.uri = uri
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.content is not None:
            result['Content'] = self.content
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.target_msgkey is not None:
            result['TargetMsgkey'] = self.target_msgkey
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category is not None:
            result['ThirdChannelCategory'] = self.third_channel_category
        if self.title is not None:
            result['Title'] = self.title
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TargetMsgkey') is not None:
            self.target_msgkey = m.get('TargetMsgkey')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category = m.get('ThirdChannelCategory')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushSimpleShrinkRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        content: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        icon_urls: str = None,
        image_urls: str = None,
        mi_channel_id: str = None,
        notify_level_shrink: str = None,
        notify_type: str = None,
        push_action: int = None,
        push_style: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msgkey: str = None,
        task_name: str = None,
        tenant_id: str = None,
        third_channel_category_shrink: str = None,
        title: str = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        uri: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.icon_urls = icon_urls
        self.image_urls = image_urls
        self.mi_channel_id = mi_channel_id
        self.notify_level_shrink = notify_level_shrink
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_style = push_style
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msgkey = target_msgkey
        self.task_name = task_name
        self.tenant_id = tenant_id
        self.third_channel_category_shrink = third_channel_category_shrink
        # This parameter is required.
        self.title = title
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.uri = uri
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.content is not None:
            result['Content'] = self.content
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level_shrink is not None:
            result['NotifyLevel'] = self.notify_level_shrink
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.target_msgkey is not None:
            result['TargetMsgkey'] = self.target_msgkey
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category_shrink is not None:
            result['ThirdChannelCategory'] = self.third_channel_category_shrink
        if self.title is not None:
            result['Title'] = self.title
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level_shrink = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TargetMsgkey') is not None:
            self.target_msgkey = m.get('TargetMsgkey')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category_shrink = m.get('ThirdChannelCategory')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushSimpleResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushSimpleResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushSimpleResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = PushSimpleResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushSimpleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushSimpleResponseBody = None,
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
            temp_model = PushSimpleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushTemplateRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        notify_level: Dict[str, Any] = None,
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msgkey: str = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category: Dict[str, Any] = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        self.notify_level = notify_level
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msgkey = target_msgkey
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category = third_channel_category
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level is not None:
            result['NotifyLevel'] = self.notify_level
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.target_msgkey is not None:
            result['TargetMsgkey'] = self.target_msgkey
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category is not None:
            result['ThirdChannelCategory'] = self.third_channel_category
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TargetMsgkey') is not None:
            self.target_msgkey = m.get('TargetMsgkey')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category = m.get('ThirdChannelCategory')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        activity_content_state: Any = None,
        activity_event: str = None,
        app_id: str = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        dismissal_date: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        notify_level_shrink: str = None,
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        strategy_content: str = None,
        strategy_type: int = None,
        target_msgkey: str = None,
        task_name: str = None,
        template_key_value: str = None,
        template_name: str = None,
        tenant_id: str = None,
        third_channel_category_shrink: str = None,
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        workspace_id: str = None,
    ):
        self.activity_content_state = activity_content_state
        self.activity_event = activity_event
        # This parameter is required.
        self.app_id = app_id
        self.channel_id = channel_id
        self.classification = classification
        # This parameter is required.
        self.delivery_type = delivery_type
        self.dismissal_date = dismissal_date
        # This parameter is required.
        self.expired_seconds = expired_seconds
        self.extended_params = extended_params
        self.mi_channel_id = mi_channel_id
        self.notify_level_shrink = notify_level_shrink
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.strategy_content = strategy_content
        self.strategy_type = strategy_type
        # This parameter is required.
        self.target_msgkey = target_msgkey
        self.task_name = task_name
        self.template_key_value = template_key_value
        # This parameter is required.
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.third_channel_category_shrink = third_channel_category_shrink
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_content_state is not None:
            result['ActivityContentState'] = self.activity_content_state
        if self.activity_event is not None:
            result['ActivityEvent'] = self.activity_event
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.dismissal_date is not None:
            result['DismissalDate'] = self.dismissal_date
        if self.expired_seconds is not None:
            result['ExpiredSeconds'] = self.expired_seconds
        if self.extended_params is not None:
            result['ExtendedParams'] = self.extended_params
        if self.mi_channel_id is not None:
            result['MiChannelId'] = self.mi_channel_id
        if self.notify_level_shrink is not None:
            result['NotifyLevel'] = self.notify_level_shrink
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.strategy_content is not None:
            result['StrategyContent'] = self.strategy_content
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.target_msgkey is not None:
            result['TargetMsgkey'] = self.target_msgkey
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_key_value is not None:
            result['TemplateKeyValue'] = self.template_key_value
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel_category_shrink is not None:
            result['ThirdChannelCategory'] = self.third_channel_category_shrink
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityContentState') is not None:
            self.activity_content_state = m.get('ActivityContentState')
        if m.get('ActivityEvent') is not None:
            self.activity_event = m.get('ActivityEvent')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('DismissalDate') is not None:
            self.dismissal_date = m.get('DismissalDate')
        if m.get('ExpiredSeconds') is not None:
            self.expired_seconds = m.get('ExpiredSeconds')
        if m.get('ExtendedParams') is not None:
            self.extended_params = m.get('ExtendedParams')
        if m.get('MiChannelId') is not None:
            self.mi_channel_id = m.get('MiChannelId')
        if m.get('NotifyLevel') is not None:
            self.notify_level_shrink = m.get('NotifyLevel')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('StrategyContent') is not None:
            self.strategy_content = m.get('StrategyContent')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('TargetMsgkey') is not None:
            self.target_msgkey = m.get('TargetMsgkey')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateKeyValue') is not None:
            self.template_key_value = m.get('TemplateKeyValue')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannelCategory') is not None:
            self.third_channel_category_shrink = m.get('ThirdChannelCategory')
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushTemplateResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushTemplateResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushTemplateResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = PushTemplateResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushTemplateResponseBody = None,
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
            temp_model = PushTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMcubeMiniPackageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        h_5id: str = None,
        id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMcubeMiniPackageResponseBodyQueryMiniPackageResultMiniPackageInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        download_url: str = None,
        extend_info: str = None,
        extra_data: str = None,
        fallback_base_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        id: int = None,
        install_type: int = None,
        main_url: str = None,
        memo: str = None,
        package_type: int = None,
        platform: str = None,
        publish_period: int = None,
        resource_type: int = None,
        status: int = None,
    ):
        self.app_code = app_code
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.download_url = download_url
        self.extend_info = extend_info
        self.extra_data = extra_data
        self.fallback_base_url = fallback_base_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.id = id
        self.install_type = install_type
        self.main_url = main_url
        self.memo = memo
        self.package_type = package_type
        self.platform = platform
        self.publish_period = publish_period
        self.resource_type = resource_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.fallback_base_url is not None:
            result['FallbackBaseUrl'] = self.fallback_base_url
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.id is not None:
            result['Id'] = self.id
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.publish_period is not None:
            result['PublishPeriod'] = self.publish_period
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('FallbackBaseUrl') is not None:
            self.fallback_base_url = m.get('FallbackBaseUrl')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PublishPeriod') is not None:
            self.publish_period = m.get('PublishPeriod')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryMcubeMiniPackageResponseBodyQueryMiniPackageResult(TeaModel):
    def __init__(
        self,
        mini_package_info: QueryMcubeMiniPackageResponseBodyQueryMiniPackageResultMiniPackageInfo = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_package_info = mini_package_info
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mini_package_info:
            self.mini_package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_package_info is not None:
            result['MiniPackageInfo'] = self.mini_package_info.to_map()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniPackageInfo') is not None:
            temp_model = QueryMcubeMiniPackageResponseBodyQueryMiniPackageResultMiniPackageInfo()
            self.mini_package_info = temp_model.from_map(m['MiniPackageInfo'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMcubeMiniPackageResponseBody(TeaModel):
    def __init__(
        self,
        query_mini_package_result: QueryMcubeMiniPackageResponseBodyQueryMiniPackageResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_mini_package_result = query_mini_package_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_mini_package_result:
            self.query_mini_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_mini_package_result is not None:
            result['QueryMiniPackageResult'] = self.query_mini_package_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryMiniPackageResult') is not None:
            temp_model = QueryMcubeMiniPackageResponseBodyQueryMiniPackageResult()
            self.query_mini_package_result = temp_model.from_map(m['QueryMiniPackageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMcubeMiniPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMcubeMiniPackageResponseBody = None,
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
            temp_model = QueryMcubeMiniPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMcubeMiniTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        id: int = None,
        memo: str = None,
        package_id: int = None,
        platform: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        status: str = None,
        task_status: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.id = id
        self.memo = memo
        self.package_id = package_id
        self.platform = platform
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.status = status
        self.task_status = task_status
        self.whitelist_ids = whitelist_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.id is not None:
            result['Id'] = self.id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.product_version is not None:
            result['ProductVersion'] = self.product_version
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        return self


class QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult(TeaModel):
    def __init__(
        self,
        mini_task_info: QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_task_info = mini_task_info
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mini_task_info:
            self.mini_task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_task_info is not None:
            result['MiniTaskInfo'] = self.mini_task_info.to_map()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniTaskInfo') is not None:
            temp_model = QueryMcubeMiniTaskResponseBodyQueryMiniTaskResultMiniTaskInfo()
            self.mini_task_info = temp_model.from_map(m['MiniTaskInfo'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMcubeMiniTaskResponseBody(TeaModel):
    def __init__(
        self,
        query_mini_task_result: QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_mini_task_result = query_mini_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_mini_task_result:
            self.query_mini_task_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_mini_task_result is not None:
            result['QueryMiniTaskResult'] = self.query_mini_task_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryMiniTaskResult') is not None:
            temp_model = QueryMcubeMiniTaskResponseBodyQueryMiniTaskResult()
            self.query_mini_task_result = temp_model.from_map(m['QueryMiniTaskResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMcubeMiniTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMcubeMiniTaskResponseBody = None,
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
            temp_model = QueryMcubeMiniTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMcubeVhostRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMcubeVhostResponseBodyQueryVhostResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMcubeVhostResponseBody(TeaModel):
    def __init__(
        self,
        query_vhost_result: QueryMcubeVhostResponseBodyQueryVhostResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_vhost_result = query_vhost_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_vhost_result:
            self.query_vhost_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_vhost_result is not None:
            result['QueryVhostResult'] = self.query_vhost_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryVhostResult') is not None:
            temp_model = QueryMcubeVhostResponseBodyQueryVhostResult()
            self.query_vhost_result = temp_model.from_map(m['QueryVhostResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMcubeVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMcubeVhostResponseBody = None,
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
            temp_model = QueryMcubeVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMpsSchedulerListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        type: int = None,
        unique_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.type = type
        self.unique_id = unique_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMpsSchedulerListResponseBodyResultContentDataList(TeaModel):
    def __init__(
        self,
        create_type: int = None,
        delivery_type: int = None,
        executed_status: str = None,
        gmt_create: int = None,
        parent_id: str = None,
        push_content: str = None,
        push_time: int = None,
        push_title: str = None,
        strategy_type: int = None,
        type: int = None,
        unique_id: str = None,
    ):
        self.create_type = create_type
        self.delivery_type = delivery_type
        self.executed_status = executed_status
        self.gmt_create = gmt_create
        self.parent_id = parent_id
        self.push_content = push_content
        self.push_time = push_time
        self.push_title = push_title
        self.strategy_type = strategy_type
        self.type = type
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.executed_status is not None:
            result['ExecutedStatus'] = self.executed_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.push_content is not None:
            result['PushContent'] = self.push_content
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.push_title is not None:
            result['PushTitle'] = self.push_title
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('ExecutedStatus') is not None:
            self.executed_status = m.get('ExecutedStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('PushTitle') is not None:
            self.push_title = m.get('PushTitle')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class QueryMpsSchedulerListResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        list: List[QueryMpsSchedulerListResponseBodyResultContentDataList] = None,
        total_count: int = None,
    ):
        self.list = list
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryMpsSchedulerListResponseBodyResultContentDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryMpsSchedulerListResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: QueryMpsSchedulerListResponseBodyResultContentData = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryMpsSchedulerListResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryMpsSchedulerListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMpsSchedulerListResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = QueryMpsSchedulerListResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMpsSchedulerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMpsSchedulerListResponseBody = None,
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
            temp_model = QueryMpsSchedulerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushAnalysisCoreIndexRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        channel: str = None,
        end_time: int = None,
        platform: str = None,
        start_time: int = None,
        task_id: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.channel = channel
        # This parameter is required.
        self.end_time = end_time
        self.platform = platform
        # This parameter is required.
        self.start_time = start_time
        self.task_id = task_id
        self.tenant_id = tenant_id
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryPushAnalysisCoreIndexResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        arrival_num: float = None,
        arrival_rate: float = None,
        ignore_num: float = None,
        ignore_rate: float = None,
        open_num: float = None,
        open_rate: float = None,
        push_num: float = None,
        push_total_num: float = None,
    ):
        self.arrival_num = arrival_num
        self.arrival_rate = arrival_rate
        self.ignore_num = ignore_num
        self.ignore_rate = ignore_rate
        self.open_num = open_num
        self.open_rate = open_rate
        self.push_num = push_num
        self.push_total_num = push_total_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arrival_num is not None:
            result['ArrivalNum'] = self.arrival_num
        if self.arrival_rate is not None:
            result['ArrivalRate'] = self.arrival_rate
        if self.ignore_num is not None:
            result['IgnoreNum'] = self.ignore_num
        if self.ignore_rate is not None:
            result['IgnoreRate'] = self.ignore_rate
        if self.open_num is not None:
            result['OpenNum'] = self.open_num
        if self.open_rate is not None:
            result['OpenRate'] = self.open_rate
        if self.push_num is not None:
            result['PushNum'] = self.push_num
        if self.push_total_num is not None:
            result['PushTotalNum'] = self.push_total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrivalNum') is not None:
            self.arrival_num = m.get('ArrivalNum')
        if m.get('ArrivalRate') is not None:
            self.arrival_rate = m.get('ArrivalRate')
        if m.get('IgnoreNum') is not None:
            self.ignore_num = m.get('IgnoreNum')
        if m.get('IgnoreRate') is not None:
            self.ignore_rate = m.get('IgnoreRate')
        if m.get('OpenNum') is not None:
            self.open_num = m.get('OpenNum')
        if m.get('OpenRate') is not None:
            self.open_rate = m.get('OpenRate')
        if m.get('PushNum') is not None:
            self.push_num = m.get('PushNum')
        if m.get('PushTotalNum') is not None:
            self.push_total_num = m.get('PushTotalNum')
        return self


class QueryPushAnalysisCoreIndexResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: QueryPushAnalysisCoreIndexResponseBodyResultContentData = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPushAnalysisCoreIndexResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryPushAnalysisCoreIndexResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryPushAnalysisCoreIndexResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = QueryPushAnalysisCoreIndexResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryPushAnalysisCoreIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushAnalysisCoreIndexResponseBody = None,
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
            temp_model = QueryPushAnalysisCoreIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushAnalysisTaskDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.task_id = task_id
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryPushAnalysisTaskDetailResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        duration: str = None,
        end_time: int = None,
        push_arrival_num: float = None,
        push_num: float = None,
        push_success_num: float = None,
        start_time: int = None,
        task_id: int = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.push_arrival_num = push_arrival_num
        self.push_num = push_num
        self.push_success_num = push_success_num
        self.start_time = start_time
        self.task_id = task_id

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
        if self.push_arrival_num is not None:
            result['PushArrivalNum'] = self.push_arrival_num
        if self.push_num is not None:
            result['PushNum'] = self.push_num
        if self.push_success_num is not None:
            result['PushSuccessNum'] = self.push_success_num
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PushArrivalNum') is not None:
            self.push_arrival_num = m.get('PushArrivalNum')
        if m.get('PushNum') is not None:
            self.push_num = m.get('PushNum')
        if m.get('PushSuccessNum') is not None:
            self.push_success_num = m.get('PushSuccessNum')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryPushAnalysisTaskDetailResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: QueryPushAnalysisTaskDetailResponseBodyResultContentData = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPushAnalysisTaskDetailResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryPushAnalysisTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryPushAnalysisTaskDetailResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = QueryPushAnalysisTaskDetailResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryPushAnalysisTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushAnalysisTaskDetailResponseBody = None,
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
            temp_model = QueryPushAnalysisTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushAnalysisTaskListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        task_id: str = None,
        task_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        self.task_id = task_id
        self.task_name = task_name
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryPushAnalysisTaskListResponseBodyResultContentDataList(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        task_id: str = None,
        task_name: str = None,
        template_id: str = None,
        template_name: str = None,
        type: int = None,
    ):
        self.gmt_create = gmt_create
        self.task_id = task_id
        self.task_name = task_name
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryPushAnalysisTaskListResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        list: List[QueryPushAnalysisTaskListResponseBodyResultContentDataList] = None,
        task_id: str = None,
        task_name: str = None,
        template_id: str = None,
        template_name: str = None,
        type: int = None,
    ):
        self.gmt_create = gmt_create
        self.list = list
        self.task_id = task_id
        self.task_name = task_name
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPushAnalysisTaskListResponseBodyResultContentDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryPushAnalysisTaskListResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: List[QueryPushAnalysisTaskListResponseBodyResultContentData] = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryPushAnalysisTaskListResponseBodyResultContentData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryPushAnalysisTaskListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryPushAnalysisTaskListResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = QueryPushAnalysisTaskListResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryPushAnalysisTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushAnalysisTaskListResponseBody = None,
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
            temp_model = QueryPushAnalysisTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushSchedulerListRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        tenant_id: str = None,
        type: int = None,
        unique_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time
        self.tenant_id = tenant_id
        self.type = type
        self.unique_id = unique_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryPushSchedulerListResponseBodyResultContentDataList(TeaModel):
    def __init__(
        self,
        create_type: int = None,
        delivery_type: int = None,
        executed_status: str = None,
        gmt_create: int = None,
        parent_id: str = None,
        push_content: str = None,
        push_time: int = None,
        push_title: str = None,
        strategy_type: int = None,
        type: int = None,
        unique_id: str = None,
    ):
        self.create_type = create_type
        self.delivery_type = delivery_type
        self.executed_status = executed_status
        self.gmt_create = gmt_create
        self.parent_id = parent_id
        self.push_content = push_content
        self.push_time = push_time
        self.push_title = push_title
        self.strategy_type = strategy_type
        self.type = type
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_type is not None:
            result['CreateType'] = self.create_type
        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type
        if self.executed_status is not None:
            result['ExecutedStatus'] = self.executed_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.push_content is not None:
            result['PushContent'] = self.push_content
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.push_title is not None:
            result['PushTitle'] = self.push_title
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.type is not None:
            result['Type'] = self.type
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')
        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')
        if m.get('ExecutedStatus') is not None:
            self.executed_status = m.get('ExecutedStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('PushTitle') is not None:
            self.push_title = m.get('PushTitle')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class QueryPushSchedulerListResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        list: List[QueryPushSchedulerListResponseBodyResultContentDataList] = None,
        total_count: int = None,
    ):
        self.list = list
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPushSchedulerListResponseBodyResultContentDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryPushSchedulerListResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: QueryPushSchedulerListResponseBodyResultContentData = None,
    ):
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryPushSchedulerListResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryPushSchedulerListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryPushSchedulerListResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultContent') is not None:
            temp_model = QueryPushSchedulerListResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryPushSchedulerListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushSchedulerListResponseBody = None,
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
            temp_model = QueryPushSchedulerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePushMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        message_id: str = None,
        target_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.message_id = message_id
        # This parameter is required.
        self.target_id = target_id
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RevokePushMessageResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokePushMessageResponseBody(TeaModel):
    def __init__(
        self,
        push_result: RevokePushMessageResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = RevokePushMessageResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class RevokePushMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokePushMessageResponseBody = None,
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
            temp_model = RevokePushMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePushTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.task_id = task_id
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RevokePushTaskResponseBodyPushResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokePushTaskResponseBody(TeaModel):
    def __init__(
        self,
        push_result: RevokePushTaskResponseBodyPushResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.push_result = push_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.push_result:
            self.push_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_result is not None:
            result['PushResult'] = self.push_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushResult') is not None:
            temp_model = RevokePushTaskResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class RevokePushTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokePushTaskResponseBody = None,
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
            temp_model = RevokePushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMcubeWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: str = None,
        key_ids: str = None,
        onex_flag: bool = None,
        oss_url: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.id = id
        self.key_ids = key_ids
        # This parameter is required.
        self.onex_flag = onex_flag
        self.oss_url = oss_url
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.id is not None:
            result['Id'] = self.id
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo(TeaModel):
    def __init__(
        self,
        fail_num: int = None,
        fail_user_ids: str = None,
        success_num: int = None,
    ):
        self.fail_num = fail_num
        self.fail_user_ids = fail_user_ids
        self.success_num = success_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_num is not None:
            result['FailNum'] = self.fail_num
        if self.fail_user_ids is not None:
            result['FailUserIds'] = self.fail_user_ids
        if self.success_num is not None:
            result['SuccessNum'] = self.success_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')
        if m.get('FailUserIds') is not None:
            self.fail_user_ids = m.get('FailUserIds')
        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')
        return self


class UpdateMcubeWhitelistResponseBodyAddWhitelistResult(TeaModel):
    def __init__(
        self,
        add_whitelist_info: UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.add_whitelist_info = add_whitelist_info
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.add_whitelist_info:
            self.add_whitelist_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_whitelist_info is not None:
            result['AddWhitelistInfo'] = self.add_whitelist_info.to_map()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWhitelistInfo') is not None:
            temp_model = UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo()
            self.add_whitelist_info = temp_model.from_map(m['AddWhitelistInfo'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMcubeWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        add_whitelist_result: UpdateMcubeWhitelistResponseBodyAddWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.add_whitelist_result = add_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.add_whitelist_result:
            self.add_whitelist_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_whitelist_result is not None:
            result['AddWhitelistResult'] = self.add_whitelist_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWhitelistResult') is not None:
            temp_model = UpdateMcubeWhitelistResponseBodyAddWhitelistResult()
            self.add_whitelist_result = temp_model.from_map(m['AddWhitelistResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class UpdateMcubeWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMcubeWhitelistResponseBody = None,
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
            temp_model = UpdateMcubeWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMcubeMiniPackageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        enable_keep_alive: str = None,
        enable_option_menu: str = None,
        enable_tab_bar: int = None,
        extend_info: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        icon_file_url: str = None,
        install_type: int = None,
        main_url: str = None,
        onex_flag: bool = None,
        package_type: int = None,
        platform: str = None,
        resource_file_url: str = None,
        resource_type: int = None,
        tenant_id: str = None,
        user_id: str = None,
        uuid: str = None,
        vhost: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        # This parameter is required.
        self.client_version_min = client_version_min
        # This parameter is required.
        self.enable_keep_alive = enable_keep_alive
        # This parameter is required.
        self.enable_option_menu = enable_option_menu
        # This parameter is required.
        self.enable_tab_bar = enable_tab_bar
        self.extend_info = extend_info
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.h_5name = h_5name
        # This parameter is required.
        self.h_5version = h_5version
        # This parameter is required.
        self.icon_file_url = icon_file_url
        # This parameter is required.
        self.install_type = install_type
        # This parameter is required.
        self.main_url = main_url
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.package_type = package_type
        # This parameter is required.
        self.platform = platform
        # This parameter is required.
        self.resource_file_url = resource_file_url
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
        self.uuid = uuid
        # This parameter is required.
        self.vhost = vhost
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max
        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min
        if self.enable_keep_alive is not None:
            result['EnableKeepAlive'] = self.enable_keep_alive
        if self.enable_option_menu is not None:
            result['EnableOptionMenu'] = self.enable_option_menu
        if self.enable_tab_bar is not None:
            result['EnableTabBar'] = self.enable_tab_bar
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.h_5version is not None:
            result['H5Version'] = self.h_5version
        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.main_url is not None:
            result['MainUrl'] = self.main_url
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.resource_file_url is not None:
            result['ResourceFileUrl'] = self.resource_file_url
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')
        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')
        if m.get('EnableKeepAlive') is not None:
            self.enable_keep_alive = m.get('EnableKeepAlive')
        if m.get('EnableOptionMenu') is not None:
            self.enable_option_menu = m.get('EnableOptionMenu')
        if m.get('EnableTabBar') is not None:
            self.enable_tab_bar = m.get('EnableTabBar')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')
        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ResourceFileUrl') is not None:
            self.resource_file_url = m.get('ResourceFileUrl')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult(TeaModel):
    def __init__(
        self,
        debug_url: str = None,
        package_id: str = None,
        user_id: str = None,
    ):
        self.debug_url = debug_url
        self.package_id = package_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_url is not None:
            result['DebugUrl'] = self.debug_url
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugUrl') is not None:
            self.debug_url = m.get('DebugUrl')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult(TeaModel):
    def __init__(
        self,
        result_msg: str = None,
        return_package_result: UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult = None,
        success: bool = None,
    ):
        self.result_msg = result_msg
        self.return_package_result = return_package_result
        self.success = success

    def validate(self):
        if self.return_package_result:
            self.return_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.return_package_result is not None:
            result['ReturnPackageResult'] = self.return_package_result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('ReturnPackageResult') is not None:
            temp_model = UploadMcubeMiniPackageResponseBodyUploadMiniPackageResultReturnPackageResult()
            self.return_package_result = temp_model.from_map(m['ReturnPackageResult'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadMcubeMiniPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        upload_mini_package_result: UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.upload_mini_package_result = upload_mini_package_result

    def validate(self):
        if self.upload_mini_package_result:
            self.upload_mini_package_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.upload_mini_package_result is not None:
            result['UploadMiniPackageResult'] = self.upload_mini_package_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('UploadMiniPackageResult') is not None:
            temp_model = UploadMcubeMiniPackageResponseBodyUploadMiniPackageResult()
            self.upload_mini_package_result = temp_model.from_map(m['UploadMiniPackageResult'])
        return self


class UploadMcubeMiniPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMcubeMiniPackageResponseBody = None,
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
            temp_model = UploadMcubeMiniPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadMcubeRsaKeyRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        file_url: str = None,
        onex_flag: bool = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UploadMcubeRsaKeyResponseBodyUploadRsaResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
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
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadMcubeRsaKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        upload_rsa_result: UploadMcubeRsaKeyResponseBodyUploadRsaResult = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.upload_rsa_result = upload_rsa_result

    def validate(self):
        if self.upload_rsa_result:
            self.upload_rsa_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.upload_rsa_result is not None:
            result['UploadRsaResult'] = self.upload_rsa_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('UploadRsaResult') is not None:
            temp_model = UploadMcubeRsaKeyResponseBodyUploadRsaResult()
            self.upload_rsa_result = temp_model.from_map(m['UploadRsaResult'])
        return self


class UploadMcubeRsaKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadMcubeRsaKeyResponseBody = None,
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
            temp_model = UploadMcubeRsaKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


