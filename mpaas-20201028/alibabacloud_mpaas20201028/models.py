# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddMdsMiniConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mini_config_add_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mini_config_add_json_str = mpaas_mappcenter_mini_config_add_json_str
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
        if self.mpaas_mappcenter_mini_config_add_json_str is not None:
            result['MpaasMappcenterMiniConfigAddJsonStr'] = self.mpaas_mappcenter_mini_config_add_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMiniConfigAddJsonStr') is not None:
            self.mpaas_mappcenter_mini_config_add_json_str = m.get('MpaasMappcenterMiniConfigAddJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class AddMdsMiniConfigResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
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
        if self.content is not None:
            result['Content'] = self.content
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
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddMdsMiniConfigResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: AddMdsMiniConfigResponseBodyResultContentData = None,
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
            temp_model = AddMdsMiniConfigResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddMdsMiniConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: AddMdsMiniConfigResponseBodyResultContent = None,
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
            temp_model = AddMdsMiniConfigResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class AddMdsMiniConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMdsMiniConfigResponseBody = None,
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
            temp_model = AddMdsMiniConfigResponseBody()
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


class ChangeMcubePublicTaskStatusResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
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
        request_id: str = None,
        result_code: str = None,
        result_content: ChangeMcubePublicTaskStatusResponseBodyResultContent = None,
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
            temp_model = ChangeMcubePublicTaskStatusResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
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


class CopyMcdpGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_group_copy_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_group_copy_json_str = mpaas_mappcenter_mcdp_group_copy_json_str
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
        if self.mpaas_mappcenter_mcdp_group_copy_json_str is not None:
            result['MpaasMappcenterMcdpGroupCopyJsonStr'] = self.mpaas_mappcenter_mcdp_group_copy_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpGroupCopyJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_group_copy_json_str = m.get('MpaasMappcenterMcdpGroupCopyJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CopyMcdpGroupResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CopyMcdpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CopyMcdpGroupResponseBodyResultContent = None,
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
            temp_model = CopyMcdpGroupResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CopyMcdpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyMcdpGroupResponseBody = None,
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
            temp_model = CopyMcdpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cors: bool = None,
        domain: str = None,
        dynamicfield: str = None,
        target_url: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.cors = cors
        self.domain = domain
        self.dynamicfield = dynamicfield
        # This parameter is required.
        self.target_url = target_url
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
        if self.cors is not None:
            result['Cors'] = self.cors
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.dynamicfield is not None:
            result['Dynamicfield'] = self.dynamicfield
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cors') is not None:
            self.cors = m.get('Cors')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Dynamicfield') is not None:
            self.dynamicfield = m.get('Dynamicfield')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateLinkResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: str = None,
        target: str = None,
        version: str = None,
    ):
        self.data = data
        self.target = target
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.target is not None:
            result['Target'] = self.target
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateLinkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateLinkResponseBodyResultContent = None,
        result_message: str = None,
    ):
        # Id of the request
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
            temp_model = CreateLinkResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLinkResponseBody = None,
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
            temp_model = CreateLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcdpGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_group_create_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_group_create_json_str = mpaas_mappcenter_mcdp_group_create_json_str
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
        if self.mpaas_mappcenter_mcdp_group_create_json_str is not None:
            result['MpaasMappcenterMcdpGroupCreateJsonStr'] = self.mpaas_mappcenter_mcdp_group_create_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpGroupCreateJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_group_create_json_str = m.get('MpaasMappcenterMcdpGroupCreateJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcdpGroupResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcdpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateMcdpGroupResponseBodyResultContent = None,
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
            temp_model = CreateMcdpGroupResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcdpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcdpGroupResponseBody = None,
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
            temp_model = CreateMcdpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcdpMaterialRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_material_create_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_material_create_json_str = mpaas_mappcenter_mcdp_material_create_json_str
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
        if self.mpaas_mappcenter_mcdp_material_create_json_str is not None:
            result['MpaasMappcenterMcdpMaterialCreateJsonStr'] = self.mpaas_mappcenter_mcdp_material_create_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpMaterialCreateJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_material_create_json_str = m.get('MpaasMappcenterMcdpMaterialCreateJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcdpMaterialResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcdpMaterialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateMcdpMaterialResponseBodyResultContent = None,
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
            temp_model = CreateMcdpMaterialResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcdpMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcdpMaterialResponseBody = None,
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
            temp_model = CreateMcdpMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMcdpZoneRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_zone_create_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_zone_create_json_str = mpaas_mappcenter_mcdp_zone_create_json_str
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
        if self.mpaas_mappcenter_mcdp_zone_create_json_str is not None:
            result['MpaasMappcenterMcdpZoneCreateJsonStr'] = self.mpaas_mappcenter_mcdp_zone_create_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpZoneCreateJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_zone_create_json_str = m.get('MpaasMappcenterMcdpZoneCreateJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMcdpZoneResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcdpZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateMcdpZoneResponseBodyResultContent = None,
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
            temp_model = CreateMcdpZoneResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMcdpZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMcdpZoneResponseBody = None,
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
            temp_model = CreateMcdpZoneResponseBody()
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


class CreateMcubeUpgradePackageResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMcubeUpgradePackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateMcubeUpgradePackageResponseBodyResultContent = None,
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
            temp_model = CreateMcubeUpgradePackageResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
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
            result['upgradeTaskId'] = self.upgrade_task_id
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
        if m.get('upgradeTaskId') is not None:
            self.upgrade_task_id = m.get('upgradeTaskId')
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


class CreateMdsMiniprogramTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: str = None,
        id: int = None,
        memo: str = None,
        package_id: int = None,
        publish_mode: str = None,
        publish_type: int = None,
        sync_mode: str = None,
        tenant_id: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        # This parameter is required.
        self.id = id
        self.memo = memo
        # This parameter is required.
        self.package_id = package_id
        self.publish_mode = publish_mode
        # This parameter is required.
        self.publish_type = publish_type
        self.sync_mode = sync_mode
        self.tenant_id = tenant_id
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
        if self.id is not None:
            result['Id'] = self.id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode
        if self.publish_type is not None:
            result['PublishType'] = self.publish_type
        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode
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
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')
        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')
        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateMdsMiniprogramTaskResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
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
        if self.content is not None:
            result['Content'] = self.content
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
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMdsMiniprogramTaskResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: CreateMdsMiniprogramTaskResponseBodyResultContentData = None,
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
            temp_model = CreateMdsMiniprogramTaskResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMdsMiniprogramTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: CreateMdsMiniprogramTaskResponseBodyResultContent = None,
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
            temp_model = CreateMdsMiniprogramTaskResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class CreateMdsMiniprogramTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMdsMiniprogramTaskResponseBody = None,
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
            temp_model = CreateMdsMiniprogramTaskResponseBody()
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


class DeleteMcdpAimRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_aim_delete_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_aim_delete_json_str = mpaas_mappcenter_mcdp_aim_delete_json_str
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
        if self.mpaas_mappcenter_mcdp_aim_delete_json_str is not None:
            result['MpaasMappcenterMcdpAimDeleteJsonStr'] = self.mpaas_mappcenter_mcdp_aim_delete_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpAimDeleteJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_aim_delete_json_str = m.get('MpaasMappcenterMcdpAimDeleteJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcdpAimResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcdpAimResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: DeleteMcdpAimResponseBodyResultContent = None,
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
            temp_model = DeleteMcdpAimResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcdpAimResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcdpAimResponseBody = None,
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
            temp_model = DeleteMcdpAimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcdpCrowdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_crowd_delete_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_crowd_delete_json_str = mpaas_mappcenter_mcdp_crowd_delete_json_str
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
        if self.mpaas_mappcenter_mcdp_crowd_delete_json_str is not None:
            result['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = self.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpCrowdDeleteJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_crowd_delete_json_str = m.get('MpaasMappcenterMcdpCrowdDeleteJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcdpCrowdResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcdpCrowdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: DeleteMcdpCrowdResponseBodyResultContent = None,
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
            temp_model = DeleteMcdpCrowdResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcdpCrowdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcdpCrowdResponseBody = None,
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
            temp_model = DeleteMcdpCrowdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMcdpZoneRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mcdp_zone_delete_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_mcdp_zone_delete_json_str = mpaas_mappcenter_mcdp_zone_delete_json_str
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
        if self.mpaas_mappcenter_mcdp_zone_delete_json_str is not None:
            result['MpaasMappcenterMcdpZoneDeleteJsonStr'] = self.mpaas_mappcenter_mcdp_zone_delete_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMcdpZoneDeleteJsonStr') is not None:
            self.mpaas_mappcenter_mcdp_zone_delete_json_str = m.get('MpaasMappcenterMcdpZoneDeleteJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DeleteMcdpZoneResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMcdpZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: DeleteMcdpZoneResponseBodyResultContent = None,
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
            temp_model = DeleteMcdpZoneResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class DeleteMcdpZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMcdpZoneResponseBody = None,
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
            temp_model = DeleteMcdpZoneResponseBody()
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


class ExportMappCenterAppConfigRequest(TeaModel):
    def __init__(
        self,
        apk_file_url: str = None,
        app_id: str = None,
        cert_rsa_base_64: str = None,
        identifier: str = None,
        onex_flag: bool = None,
        system_type: str = None,
        workspace_id: str = None,
    ):
        self.apk_file_url = apk_file_url
        self.app_id = app_id
        self.cert_rsa_base_64 = cert_rsa_base_64
        # This parameter is required.
        self.identifier = identifier
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.system_type = system_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apk_file_url is not None:
            result['ApkFileUrl'] = self.apk_file_url
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cert_rsa_base_64 is not None:
            result['CertRsaBase64'] = self.cert_rsa_base_64
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkFileUrl') is not None:
            self.apk_file_url = m.get('ApkFileUrl')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CertRsaBase64') is not None:
            self.cert_rsa_base_64 = m.get('CertRsaBase64')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ExportMappCenterAppConfigResponseBodyExportMappCenterAppConfigResult(TeaModel):
    def __init__(
        self,
        config_download_url: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.config_download_url = config_download_url
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_download_url is not None:
            result['ConfigDownloadUrl'] = self.config_download_url
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDownloadUrl') is not None:
            self.config_download_url = m.get('ConfigDownloadUrl')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportMappCenterAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        export_mapp_center_app_config_result: ExportMappCenterAppConfigResponseBodyExportMappCenterAppConfigResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.export_mapp_center_app_config_result = export_mapp_center_app_config_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.export_mapp_center_app_config_result:
            self.export_mapp_center_app_config_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_mapp_center_app_config_result is not None:
            result['ExportMappCenterAppConfigResult'] = self.export_mapp_center_app_config_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportMappCenterAppConfigResult') is not None:
            temp_model = ExportMappCenterAppConfigResponseBodyExportMappCenterAppConfigResult()
            self.export_mapp_center_app_config_result = temp_model.from_map(m['ExportMappCenterAppConfigResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ExportMappCenterAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportMappCenterAppConfigResponseBody = None,
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
            temp_model = ExportMappCenterAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileTokenForUploadToMsaRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        onex_flag: bool = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
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


class GetFileTokenForUploadToMsaResponseBodyResultContentContent(TeaModel):
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


class GetFileTokenForUploadToMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        content: GetFileTokenForUploadToMsaResponseBodyResultContentContent = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: str = None,
    ):
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

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
        if m.get('Content') is not None:
            temp_model = GetFileTokenForUploadToMsaResponseBodyResultContentContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileTokenForUploadToMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetFileTokenForUploadToMsaResponseBodyResultContent = None,
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
            temp_model = GetFileTokenForUploadToMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetFileTokenForUploadToMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileTokenForUploadToMsaResponseBody = None,
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
            temp_model = GetFileTokenForUploadToMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogUrlInMsaRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
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


class GetLogUrlInMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLogUrlInMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetLogUrlInMsaResponseBodyResultContent = None,
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
            temp_model = GetLogUrlInMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetLogUrlInMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLogUrlInMsaResponseBody = None,
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
            temp_model = GetLogUrlInMsaResponseBody()
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
        back_log: str = None,
        change_log: str = None,
        client_file_size: int = None,
        client_name: str = None,
        cp_id: str = None,
        creator: str = None,
        download_url: str = None,
        global_variables: str = None,
        gmt_create: str = None,
        gmt_create_str: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        id: int = None,
        inner_version: str = None,
        ios_symbol: str = None,
        is_enterprise: int = None,
        is_rc: int = None,
        is_release: int = None,
        max_version: str = None,
        md_5: str = None,
        modifier: str = None,
        need_check: int = None,
        oss_path: str = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version: str = None,
        publish_period: int = None,
        qrcode_url: str = None,
        release_type: str = None,
        release_window: str = None,
        scm_download_url: str = None,
        server_version: int = None,
        verification_code: str = None,
        verify_result: int = None,
        version_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.back_log = back_log
        self.change_log = change_log
        self.client_file_size = client_file_size
        self.client_name = client_name
        self.cp_id = cp_id
        self.creator = creator
        self.download_url = download_url
        self.global_variables = global_variables
        self.gmt_create = gmt_create
        self.gmt_create_str = gmt_create_str
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.id = id
        self.inner_version = inner_version
        self.ios_symbol = ios_symbol
        self.is_enterprise = is_enterprise
        self.is_rc = is_rc
        self.is_release = is_release
        self.max_version = max_version
        self.md_5 = md_5
        self.modifier = modifier
        self.need_check = need_check
        self.oss_path = oss_path
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_name = product_name
        self.product_version = product_version
        self.publish_period = publish_period
        self.qrcode_url = qrcode_url
        self.release_type = release_type
        self.release_window = release_window
        self.scm_download_url = scm_download_url
        self.server_version = server_version
        self.verification_code = verification_code
        self.verify_result = verify_result
        self.version_code = version_code

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
        if self.back_log is not None:
            result['BackLog'] = self.back_log
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log
        if self.client_file_size is not None:
            result['ClientFileSize'] = self.client_file_size
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.cp_id is not None:
            result['CpId'] = self.cp_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.global_variables is not None:
            result['GlobalVariables'] = self.global_variables
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.id is not None:
            result['Id'] = self.id
        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version
        if self.ios_symbol is not None:
            result['IosSymbol'] = self.ios_symbol
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.is_rc is not None:
            result['IsRc'] = self.is_rc
        if self.is_release is not None:
            result['IsRelease'] = self.is_release
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.need_check is not None:
            result['NeedCheck'] = self.need_check
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
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
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.release_type is not None:
            result['ReleaseType'] = self.release_type
        if self.release_window is not None:
            result['ReleaseWindow'] = self.release_window
        if self.scm_download_url is not None:
            result['ScmDownloadUrl'] = self.scm_download_url
        if self.server_version is not None:
            result['ServerVersion'] = self.server_version
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('BackLog') is not None:
            self.back_log = m.get('BackLog')
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')
        if m.get('ClientFileSize') is not None:
            self.client_file_size = m.get('ClientFileSize')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('CpId') is not None:
            self.cp_id = m.get('CpId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('GlobalVariables') is not None:
            self.global_variables = m.get('GlobalVariables')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')
        if m.get('IosSymbol') is not None:
            self.ios_symbol = m.get('IosSymbol')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')
        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
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
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')
        if m.get('ReleaseWindow') is not None:
            self.release_window = m.get('ReleaseWindow')
        if m.get('ScmDownloadUrl') is not None:
            self.scm_download_url = m.get('ScmDownloadUrl')
        if m.get('ServerVersion') is not None:
            self.server_version = m.get('ServerVersion')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
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
        creater: str = None,
        creator: str = None,
        download_url: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        history_force: int = None,
        id: int = None,
        is_enterprise: int = None,
        is_official: int = None,
        is_rc: int = None,
        is_release: int = None,
        memo: str = None,
        modifier: str = None,
        net_type: str = None,
        os_version: str = None,
        package_info_id: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        qrcode_url: str = None,
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
        self.creater = creater
        self.creator = creator
        self.download_url = download_url
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.history_force = history_force
        self.id = id
        self.is_enterprise = is_enterprise
        self.is_official = is_official
        self.is_rc = is_rc
        self.is_release = is_release
        self.memo = memo
        self.modifier = modifier
        self.net_type = net_type
        self.os_version = os_version
        self.package_info_id = package_info_id
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.qrcode_url = qrcode_url
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
        if self.creater is not None:
            result['Creater'] = self.creater
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
        if self.is_official is not None:
            result['IsOfficial'] = self.is_official
        if self.is_rc is not None:
            result['IsRc'] = self.is_rc
        if self.is_release is not None:
            result['IsRelease'] = self.is_release
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
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
        if self.push_content is not None:
            result['PushContent'] = self.push_content
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
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
        if m.get('Creater') is not None:
            self.creater = m.get('Creater')
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
        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')
        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')
        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
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
        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
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


class GetMdsMiniConfigRequest(TeaModel):
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


class GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        config_status: int = None,
        config_type: str = None,
        config_value: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        h_5id: str = None,
        h_5name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.config_status = config_status
        self.config_type = config_type
        self.config_value = config_value
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMdsMiniConfigResponseBodyResultContentDataContent(TeaModel):
    def __init__(
        self,
        api_config_list: List[GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList] = None,
        app_code: str = None,
        enable_server_domain_count: str = None,
        h_5id: str = None,
        h_5name: str = None,
        privilege_switch: GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch = None,
        server_domain_config_list: List[GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList] = None,
        webview_domain_config_list: List[GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList] = None,
    ):
        self.api_config_list = api_config_list
        self.app_code = app_code
        self.enable_server_domain_count = enable_server_domain_count
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.privilege_switch = privilege_switch
        self.server_domain_config_list = server_domain_config_list
        self.webview_domain_config_list = webview_domain_config_list

    def validate(self):
        if self.api_config_list:
            for k in self.api_config_list:
                if k:
                    k.validate()
        if self.privilege_switch:
            self.privilege_switch.validate()
        if self.server_domain_config_list:
            for k in self.server_domain_config_list:
                if k:
                    k.validate()
        if self.webview_domain_config_list:
            for k in self.webview_domain_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiConfigList'] = []
        if self.api_config_list is not None:
            for k in self.api_config_list:
                result['ApiConfigList'].append(k.to_map() if k else None)
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.enable_server_domain_count is not None:
            result['EnableServerDomainCount'] = self.enable_server_domain_count
        if self.h_5id is not None:
            result['H5Id'] = self.h_5id
        if self.h_5name is not None:
            result['H5Name'] = self.h_5name
        if self.privilege_switch is not None:
            result['PrivilegeSwitch'] = self.privilege_switch.to_map()
        result['ServerDomainConfigList'] = []
        if self.server_domain_config_list is not None:
            for k in self.server_domain_config_list:
                result['ServerDomainConfigList'].append(k.to_map() if k else None)
        result['WebviewDomainConfigList'] = []
        if self.webview_domain_config_list is not None:
            for k in self.webview_domain_config_list:
                result['WebviewDomainConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_config_list = []
        if m.get('ApiConfigList') is not None:
            for k in m.get('ApiConfigList'):
                temp_model = GetMdsMiniConfigResponseBodyResultContentDataContentApiConfigList()
                self.api_config_list.append(temp_model.from_map(k))
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('EnableServerDomainCount') is not None:
            self.enable_server_domain_count = m.get('EnableServerDomainCount')
        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')
        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')
        if m.get('PrivilegeSwitch') is not None:
            temp_model = GetMdsMiniConfigResponseBodyResultContentDataContentPrivilegeSwitch()
            self.privilege_switch = temp_model.from_map(m['PrivilegeSwitch'])
        self.server_domain_config_list = []
        if m.get('ServerDomainConfigList') is not None:
            for k in m.get('ServerDomainConfigList'):
                temp_model = GetMdsMiniConfigResponseBodyResultContentDataContentServerDomainConfigList()
                self.server_domain_config_list.append(temp_model.from_map(k))
        self.webview_domain_config_list = []
        if m.get('WebviewDomainConfigList') is not None:
            for k in m.get('WebviewDomainConfigList'):
                temp_model = GetMdsMiniConfigResponseBodyResultContentDataContentWebviewDomainConfigList()
                self.webview_domain_config_list.append(temp_model.from_map(k))
        return self


class GetMdsMiniConfigResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: GetMdsMiniConfigResponseBodyResultContentDataContent = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = GetMdsMiniConfigResponseBodyResultContentDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMdsMiniConfigResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: GetMdsMiniConfigResponseBodyResultContentData = None,
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
            temp_model = GetMdsMiniConfigResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMdsMiniConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetMdsMiniConfigResponseBodyResultContent = None,
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
            temp_model = GetMdsMiniConfigResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetMdsMiniConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMdsMiniConfigResponseBody = None,
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
            temp_model = GetMdsMiniConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAppDonwloadUrlInMsaRequest(TeaModel):
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


class GetUserAppDonwloadUrlInMsaResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        filename: str = None,
        url: str = None,
    ):
        self.filename = filename
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetUserAppDonwloadUrlInMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUserAppDonwloadUrlInMsaResponseBodyResultContentData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetUserAppDonwloadUrlInMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserAppDonwloadUrlInMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetUserAppDonwloadUrlInMsaResponseBodyResultContent = None,
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
            temp_model = GetUserAppDonwloadUrlInMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetUserAppDonwloadUrlInMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserAppDonwloadUrlInMsaResponseBody = None,
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
            temp_model = GetUserAppDonwloadUrlInMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAppEnhanceProcessInMsaRequest(TeaModel):
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


class GetUserAppEnhanceProcessInMsaResponseBodyResultContentDataEnhanceMapping(TeaModel):
    def __init__(
        self,
        info: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.info = info
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserAppEnhanceProcessInMsaResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        after_md_5: str = None,
        after_size: int = None,
        app_code: str = None,
        app_package: str = None,
        assets_file_list: List[str] = None,
        before_md_5: str = None,
        before_size: int = None,
        class_forest: List[str] = None,
        enhance_mapping: List[GetUserAppEnhanceProcessInMsaResponseBodyResultContentDataEnhanceMapping] = None,
        enhance_rules: List[str] = None,
        enhanced_assets_files: List[str] = None,
        enhanced_classes: List[str] = None,
        enhanced_so_files: List[str] = None,
        id: int = None,
        label: str = None,
        progress: int = None,
        so_file_list: List[str] = None,
        status: int = None,
        task_type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.after_md_5 = after_md_5
        self.after_size = after_size
        self.app_code = app_code
        self.app_package = app_package
        self.assets_file_list = assets_file_list
        self.before_md_5 = before_md_5
        self.before_size = before_size
        self.class_forest = class_forest
        self.enhance_mapping = enhance_mapping
        self.enhance_rules = enhance_rules
        self.enhanced_assets_files = enhanced_assets_files
        self.enhanced_classes = enhanced_classes
        self.enhanced_so_files = enhanced_so_files
        self.id = id
        self.label = label
        self.progress = progress
        self.so_file_list = so_file_list
        self.status = status
        self.task_type = task_type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        if self.enhance_mapping:
            for k in self.enhance_mapping:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_md_5 is not None:
            result['AfterMd5'] = self.after_md_5
        if self.after_size is not None:
            result['AfterSize'] = self.after_size
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.assets_file_list is not None:
            result['AssetsFileList'] = self.assets_file_list
        if self.before_md_5 is not None:
            result['BeforeMd5'] = self.before_md_5
        if self.before_size is not None:
            result['BeforeSize'] = self.before_size
        if self.class_forest is not None:
            result['ClassForest'] = self.class_forest
        result['EnhanceMapping'] = []
        if self.enhance_mapping is not None:
            for k in self.enhance_mapping:
                result['EnhanceMapping'].append(k.to_map() if k else None)
        if self.enhance_rules is not None:
            result['EnhanceRules'] = self.enhance_rules
        if self.enhanced_assets_files is not None:
            result['EnhancedAssetsFiles'] = self.enhanced_assets_files
        if self.enhanced_classes is not None:
            result['EnhancedClasses'] = self.enhanced_classes
        if self.enhanced_so_files is not None:
            result['EnhancedSoFiles'] = self.enhanced_so_files
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.so_file_list is not None:
            result['SoFileList'] = self.so_file_list
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterMd5') is not None:
            self.after_md_5 = m.get('AfterMd5')
        if m.get('AfterSize') is not None:
            self.after_size = m.get('AfterSize')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('AssetsFileList') is not None:
            self.assets_file_list = m.get('AssetsFileList')
        if m.get('BeforeMd5') is not None:
            self.before_md_5 = m.get('BeforeMd5')
        if m.get('BeforeSize') is not None:
            self.before_size = m.get('BeforeSize')
        if m.get('ClassForest') is not None:
            self.class_forest = m.get('ClassForest')
        self.enhance_mapping = []
        if m.get('EnhanceMapping') is not None:
            for k in m.get('EnhanceMapping'):
                temp_model = GetUserAppEnhanceProcessInMsaResponseBodyResultContentDataEnhanceMapping()
                self.enhance_mapping.append(temp_model.from_map(k))
        if m.get('EnhanceRules') is not None:
            self.enhance_rules = m.get('EnhanceRules')
        if m.get('EnhancedAssetsFiles') is not None:
            self.enhanced_assets_files = m.get('EnhancedAssetsFiles')
        if m.get('EnhancedClasses') is not None:
            self.enhanced_classes = m.get('EnhancedClasses')
        if m.get('EnhancedSoFiles') is not None:
            self.enhanced_so_files = m.get('EnhancedSoFiles')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SoFileList') is not None:
            self.so_file_list = m.get('SoFileList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetUserAppEnhanceProcessInMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUserAppEnhanceProcessInMsaResponseBodyResultContentData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetUserAppEnhanceProcessInMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserAppEnhanceProcessInMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetUserAppEnhanceProcessInMsaResponseBodyResultContent = None,
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
            temp_model = GetUserAppEnhanceProcessInMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetUserAppEnhanceProcessInMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserAppEnhanceProcessInMsaResponseBody = None,
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
            temp_model = GetUserAppEnhanceProcessInMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAppUploadProcessInMsaRequest(TeaModel):
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


class GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfoEnhanceMapping(TeaModel):
    def __init__(
        self,
        info: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.info = info
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfo(TeaModel):
    def __init__(
        self,
        after_md_5: str = None,
        after_size: int = None,
        app_code: str = None,
        app_package: str = None,
        assets_file_list: List[str] = None,
        before_md_5: str = None,
        before_size: int = None,
        class_forest: str = None,
        enhance_mapping: List[GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfoEnhanceMapping] = None,
        enhance_rules: List[str] = None,
        enhanced_assets_files: List[str] = None,
        enhanced_classes: List[str] = None,
        enhanced_so_files: List[str] = None,
        id: int = None,
        label: str = None,
        progress: int = None,
        so_file_list: List[str] = None,
        status: int = None,
        task_type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.after_md_5 = after_md_5
        self.after_size = after_size
        self.app_code = app_code
        self.app_package = app_package
        self.assets_file_list = assets_file_list
        self.before_md_5 = before_md_5
        self.before_size = before_size
        self.class_forest = class_forest
        self.enhance_mapping = enhance_mapping
        self.enhance_rules = enhance_rules
        self.enhanced_assets_files = enhanced_assets_files
        self.enhanced_classes = enhanced_classes
        self.enhanced_so_files = enhanced_so_files
        self.id = id
        self.label = label
        self.progress = progress
        self.so_file_list = so_file_list
        self.status = status
        self.task_type = task_type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        if self.enhance_mapping:
            for k in self.enhance_mapping:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_md_5 is not None:
            result['AfterMd5'] = self.after_md_5
        if self.after_size is not None:
            result['AfterSize'] = self.after_size
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.assets_file_list is not None:
            result['AssetsFileList'] = self.assets_file_list
        if self.before_md_5 is not None:
            result['BeforeMd5'] = self.before_md_5
        if self.before_size is not None:
            result['BeforeSize'] = self.before_size
        if self.class_forest is not None:
            result['ClassForest'] = self.class_forest
        result['EnhanceMapping'] = []
        if self.enhance_mapping is not None:
            for k in self.enhance_mapping:
                result['EnhanceMapping'].append(k.to_map() if k else None)
        if self.enhance_rules is not None:
            result['EnhanceRules'] = self.enhance_rules
        if self.enhanced_assets_files is not None:
            result['EnhancedAssetsFiles'] = self.enhanced_assets_files
        if self.enhanced_classes is not None:
            result['EnhancedClasses'] = self.enhanced_classes
        if self.enhanced_so_files is not None:
            result['EnhancedSoFiles'] = self.enhanced_so_files
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.so_file_list is not None:
            result['SoFileList'] = self.so_file_list
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterMd5') is not None:
            self.after_md_5 = m.get('AfterMd5')
        if m.get('AfterSize') is not None:
            self.after_size = m.get('AfterSize')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('AssetsFileList') is not None:
            self.assets_file_list = m.get('AssetsFileList')
        if m.get('BeforeMd5') is not None:
            self.before_md_5 = m.get('BeforeMd5')
        if m.get('BeforeSize') is not None:
            self.before_size = m.get('BeforeSize')
        if m.get('ClassForest') is not None:
            self.class_forest = m.get('ClassForest')
        self.enhance_mapping = []
        if m.get('EnhanceMapping') is not None:
            for k in m.get('EnhanceMapping'):
                temp_model = GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfoEnhanceMapping()
                self.enhance_mapping.append(temp_model.from_map(k))
        if m.get('EnhanceRules') is not None:
            self.enhance_rules = m.get('EnhanceRules')
        if m.get('EnhancedAssetsFiles') is not None:
            self.enhanced_assets_files = m.get('EnhancedAssetsFiles')
        if m.get('EnhancedClasses') is not None:
            self.enhanced_classes = m.get('EnhancedClasses')
        if m.get('EnhancedSoFiles') is not None:
            self.enhanced_so_files = m.get('EnhancedSoFiles')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SoFileList') is not None:
            self.so_file_list = m.get('SoFileList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetUserAppUploadProcessInMsaResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        apk_info: GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfo = None,
        enhance_task_id: int = None,
        id: int = None,
        progress: int = None,
        status: int = None,
    ):
        self.apk_info = apk_info
        self.enhance_task_id = enhance_task_id
        self.id = id
        self.progress = progress
        self.status = status

    def validate(self):
        if self.apk_info:
            self.apk_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apk_info is not None:
            result['ApkInfo'] = self.apk_info.to_map()
        if self.enhance_task_id is not None:
            result['EnhanceTaskId'] = self.enhance_task_id
        if self.id is not None:
            result['Id'] = self.id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkInfo') is not None:
            temp_model = GetUserAppUploadProcessInMsaResponseBodyResultContentDataApkInfo()
            self.apk_info = temp_model.from_map(m['ApkInfo'])
        if m.get('EnhanceTaskId') is not None:
            self.enhance_task_id = m.get('EnhanceTaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetUserAppUploadProcessInMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUserAppUploadProcessInMsaResponseBodyResultContentData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetUserAppUploadProcessInMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserAppUploadProcessInMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: GetUserAppUploadProcessInMsaResponseBodyResultContent = None,
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
            temp_model = GetUserAppUploadProcessInMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class GetUserAppUploadProcessInMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserAppUploadProcessInMsaResponseBody = None,
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
            temp_model = GetUserAppUploadProcessInMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListAndroidConfig(TeaModel):
    def __init__(
        self,
        cert_rsa: str = None,
        package_name: str = None,
    ):
        self.cert_rsa = cert_rsa
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_rsa is not None:
            result['CertRSA'] = self.cert_rsa
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertRSA') is not None:
            self.cert_rsa = m.get('CertRSA')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListIosConfig(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
    ):
        self.bundle_id = bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppList(TeaModel):
    def __init__(
        self,
        android_config: ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListAndroidConfig = None,
        app_desc: str = None,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ios_config: ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListIosConfig = None,
        modifier: str = None,
        monitor_json: str = None,
        status: int = None,
        tenant_id: str = None,
        type: int = None,
    ):
        self.android_config = android_config
        self.app_desc = app_desc
        self.app_icon = app_icon
        self.app_id = app_id
        self.app_name = app_name
        self.app_secret = app_secret
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.ios_config = ios_config
        self.modifier = modifier
        self.monitor_json = monitor_json
        self.status = status
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        if self.android_config:
            self.android_config.validate()
        if self.ios_config:
            self.ios_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_config is not None:
            result['AndroidConfig'] = self.android_config.to_map()
        if self.app_desc is not None:
            result['AppDesc'] = self.app_desc
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.ios_config is not None:
            result['IosConfig'] = self.ios_config.to_map()
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.monitor_json is not None:
            result['MonitorJson'] = self.monitor_json
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidConfig') is not None:
            temp_model = ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListAndroidConfig()
            self.android_config = temp_model.from_map(m['AndroidConfig'])
        if m.get('AppDesc') is not None:
            self.app_desc = m.get('AppDesc')
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IosConfig') is not None:
            temp_model = ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppListIosConfig()
            self.ios_config = temp_model.from_map(m['IosConfig'])
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('MonitorJson') is not None:
            self.monitor_json = m.get('MonitorJson')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMappCenterAppsResponseBodyListMappCenterAppResult(TeaModel):
    def __init__(
        self,
        mapp_center_app_list: List[ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppList] = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mapp_center_app_list = mapp_center_app_list
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mapp_center_app_list:
            for k in self.mapp_center_app_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MappCenterAppList'] = []
        if self.mapp_center_app_list is not None:
            for k in self.mapp_center_app_list:
                result['MappCenterAppList'].append(k.to_map() if k else None)
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mapp_center_app_list = []
        if m.get('MappCenterAppList') is not None:
            for k in m.get('MappCenterAppList'):
                temp_model = ListMappCenterAppsResponseBodyListMappCenterAppResultMappCenterAppList()
                self.mapp_center_app_list.append(temp_model.from_map(k))
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMappCenterAppsResponseBody(TeaModel):
    def __init__(
        self,
        list_mapp_center_app_result: ListMappCenterAppsResponseBodyListMappCenterAppResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mapp_center_app_result = list_mapp_center_app_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mapp_center_app_result:
            self.list_mapp_center_app_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mapp_center_app_result is not None:
            result['ListMappCenterAppResult'] = self.list_mapp_center_app_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMappCenterAppResult') is not None:
            temp_model = ListMappCenterAppsResponseBodyListMappCenterAppResult()
            self.list_mapp_center_app_result = temp_model.from_map(m['ListMappCenterAppResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMappCenterAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMappCenterAppsResponseBody = None,
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
            temp_model = ListMappCenterAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList(TeaModel):
    def __init__(
        self,
        compatible_id: str = None,
        create_time: str = None,
        display_name: str = None,
        id: str = None,
        region: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        uid: int = None,
        update_time: str = None,
        workspace_id: str = None,
        zones: str = None,
    ):
        self.compatible_id = compatible_id
        self.create_time = create_time
        self.display_name = display_name
        self.id = id
        self.region = region
        self.status = status
        self.tenant_id = tenant_id
        self.type = type
        self.uid = uid
        self.update_time = update_time
        self.workspace_id = workspace_id
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_id is not None:
            result['CompatibleId'] = self.compatible_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleId') is not None:
            self.compatible_id = m.get('CompatibleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult(TeaModel):
    def __init__(
        self,
        mapp_center_workspace_list: List[ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList] = None,
        result_msg: str = None,
        success: bool = None,
        user_id: str = None,
    ):
        self.mapp_center_workspace_list = mapp_center_workspace_list
        self.result_msg = result_msg
        self.success = success
        self.user_id = user_id

    def validate(self):
        if self.mapp_center_workspace_list:
            for k in self.mapp_center_workspace_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MappCenterWorkspaceList'] = []
        if self.mapp_center_workspace_list is not None:
            for k in self.mapp_center_workspace_list:
                result['MappCenterWorkspaceList'].append(k.to_map() if k else None)
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mapp_center_workspace_list = []
        if m.get('MappCenterWorkspaceList') is not None:
            for k in m.get('MappCenterWorkspaceList'):
                temp_model = ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResultMappCenterWorkspaceList()
                self.mapp_center_workspace_list.append(temp_model.from_map(k))
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListMappCenterWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        list_mapp_center_workspace_result: ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_mapp_center_workspace_result = list_mapp_center_workspace_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_mapp_center_workspace_result:
            self.list_mapp_center_workspace_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_mapp_center_workspace_result is not None:
            result['ListMappCenterWorkspaceResult'] = self.list_mapp_center_workspace_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListMappCenterWorkspaceResult') is not None:
            temp_model = ListMappCenterWorkspacesResponseBodyListMappCenterWorkspaceResult()
            self.list_mapp_center_workspace_result = temp_model.from_map(m['ListMappCenterWorkspaceResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMappCenterWorkspacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMappCenterWorkspacesResponseBody = None,
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
            temp_model = ListMappCenterWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMcdpAimRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        empty_tag: str = None,
        keyword: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        sort: str = None,
        sort_field: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.empty_tag = empty_tag
        self.keyword = keyword
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.sort = sort
        self.sort_field = sort_field
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
        if self.empty_tag is not None:
            result['EmptyTag'] = self.empty_tag
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
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
        if m.get('EmptyTag') is not None:
            self.empty_tag = m.get('EmptyTag')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMcdpAimResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMcdpAimResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: ListMcdpAimResponseBodyResultContent = None,
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
            temp_model = ListMcdpAimResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMcdpAimResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMcdpAimResponseBody = None,
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
            temp_model = ListMcdpAimResponseBody()
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
        back_log: str = None,
        change_log: str = None,
        client_file_size: int = None,
        client_name: str = None,
        cp_id: str = None,
        creator: str = None,
        download_url: str = None,
        global_variables: str = None,
        gmt_create: str = None,
        gmt_create_str: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        id: int = None,
        inner_version: str = None,
        ios_symbol: str = None,
        is_enterprise: int = None,
        is_rc: int = None,
        is_release: int = None,
        max_version: str = None,
        md_5: str = None,
        modifier: str = None,
        need_check: int = None,
        oss_path: str = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version: str = None,
        publish_period: int = None,
        qrcode_url: str = None,
        release_type: str = None,
        release_window: str = None,
        scm_download_url: str = None,
        server_version: int = None,
        verification_code: str = None,
        verify_result: int = None,
        version_code: str = None,
    ):
        self.allow_create_task = allow_create_task
        self.app_code = app_code
        self.appstore_url = appstore_url
        self.back_log = back_log
        self.change_log = change_log
        self.client_file_size = client_file_size
        self.client_name = client_name
        self.cp_id = cp_id
        self.creator = creator
        self.download_url = download_url
        self.global_variables = global_variables
        self.gmt_create = gmt_create
        self.gmt_create_str = gmt_create_str
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.id = id
        self.inner_version = inner_version
        self.ios_symbol = ios_symbol
        self.is_enterprise = is_enterprise
        self.is_rc = is_rc
        self.is_release = is_release
        self.max_version = max_version
        self.md_5 = md_5
        self.modifier = modifier
        self.need_check = need_check
        self.oss_path = oss_path
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_name = product_name
        self.product_version = product_version
        self.publish_period = publish_period
        self.qrcode_url = qrcode_url
        self.release_type = release_type
        self.release_window = release_window
        self.scm_download_url = scm_download_url
        self.server_version = server_version
        self.verification_code = verification_code
        self.verify_result = verify_result
        self.version_code = version_code

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
        if self.back_log is not None:
            result['BackLog'] = self.back_log
        if self.change_log is not None:
            result['ChangeLog'] = self.change_log
        if self.client_file_size is not None:
            result['ClientFileSize'] = self.client_file_size
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.cp_id is not None:
            result['CpId'] = self.cp_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.global_variables is not None:
            result['GlobalVariables'] = self.global_variables
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.id is not None:
            result['Id'] = self.id
        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version
        if self.ios_symbol is not None:
            result['IosSymbol'] = self.ios_symbol
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.is_rc is not None:
            result['IsRc'] = self.is_rc
        if self.is_release is not None:
            result['IsRelease'] = self.is_release
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.need_check is not None:
            result['NeedCheck'] = self.need_check
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
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
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.release_type is not None:
            result['ReleaseType'] = self.release_type
        if self.release_window is not None:
            result['ReleaseWindow'] = self.release_window
        if self.scm_download_url is not None:
            result['ScmDownloadUrl'] = self.scm_download_url
        if self.server_version is not None:
            result['ServerVersion'] = self.server_version
        if self.verification_code is not None:
            result['VerificationCode'] = self.verification_code
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCreateTask') is not None:
            self.allow_create_task = m.get('AllowCreateTask')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')
        if m.get('BackLog') is not None:
            self.back_log = m.get('BackLog')
        if m.get('ChangeLog') is not None:
            self.change_log = m.get('ChangeLog')
        if m.get('ClientFileSize') is not None:
            self.client_file_size = m.get('ClientFileSize')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('CpId') is not None:
            self.cp_id = m.get('CpId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('GlobalVariables') is not None:
            self.global_variables = m.get('GlobalVariables')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')
        if m.get('IosSymbol') is not None:
            self.ios_symbol = m.get('IosSymbol')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')
        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
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
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')
        if m.get('ReleaseWindow') is not None:
            self.release_window = m.get('ReleaseWindow')
        if m.get('ScmDownloadUrl') is not None:
            self.scm_download_url = m.get('ScmDownloadUrl')
        if m.get('ServerVersion') is not None:
            self.server_version = m.get('ServerVersion')
        if m.get('VerificationCode') is not None:
            self.verification_code = m.get('VerificationCode')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        return self


class ListMcubeUpgradePackagesResponseBodyListPackagesResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        error_code: str = None,
        has_more: bool = None,
        packages: List[ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages] = None,
        page_size: int = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.error_code = error_code
        self.has_more = has_more
        self.packages = packages
        self.page_size = page_size
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['Packages'] = []
        if self.packages is not None:
            for k in self.packages:
                result['Packages'].append(k.to_map() if k else None)
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
        self.packages = []
        if m.get('Packages') is not None:
            for k in m.get('Packages'):
                temp_model = ListMcubeUpgradePackagesResponseBodyListPackagesResultPackages()
                self.packages.append(temp_model.from_map(k))
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


class ListMcubeUpgradePackagesResponseBody(TeaModel):
    def __init__(
        self,
        list_packages_result: ListMcubeUpgradePackagesResponseBodyListPackagesResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.list_packages_result = list_packages_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.list_packages_result:
            self.list_packages_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_packages_result is not None:
            result['ListPackagesResult'] = self.list_packages_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListPackagesResult') is not None:
            temp_model = ListMcubeUpgradePackagesResponseBodyListPackagesResult()
            self.list_packages_result = temp_model.from_map(m['ListPackagesResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
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
        device_percent: int = None,
        execution_order: int = None,
        gmt_create: str = None,
        gmt_create_str: str = None,
        gmt_modified: str = None,
        gmt_modified_str: str = None,
        grey_config_info: str = None,
        grey_endtime: str = None,
        grey_notice: int = None,
        grey_num: int = None,
        grey_pause_point: int = None,
        grey_pause_type: int = None,
        grey_uv: int = None,
        history_force: int = None,
        huoban_notice_id: str = None,
        huoban_url: str = None,
        id: int = None,
        inner_version: str = None,
        is_enterprise: int = None,
        is_official: int = None,
        is_push: int = None,
        is_release: int = None,
        max_version: str = None,
        memo: str = None,
        modifier: str = None,
        package_info_id: int = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        real_grey_endtime: str = None,
        real_grey_endtime_str: str = None,
        real_grey_endtype: int = None,
        real_grey_num: int = None,
        real_grey_uv: int = None,
        silent_type: int = None,
        sync_result: str = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        upgrade_valid_time: int = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.creator = creator
        self.device_percent = device_percent
        self.execution_order = execution_order
        self.gmt_create = gmt_create
        self.gmt_create_str = gmt_create_str
        self.gmt_modified = gmt_modified
        self.gmt_modified_str = gmt_modified_str
        self.grey_config_info = grey_config_info
        self.grey_endtime = grey_endtime
        self.grey_notice = grey_notice
        self.grey_num = grey_num
        self.grey_pause_point = grey_pause_point
        self.grey_pause_type = grey_pause_type
        self.grey_uv = grey_uv
        self.history_force = history_force
        self.huoban_notice_id = huoban_notice_id
        self.huoban_url = huoban_url
        self.id = id
        self.inner_version = inner_version
        self.is_enterprise = is_enterprise
        self.is_official = is_official
        self.is_push = is_push
        self.is_release = is_release
        self.max_version = max_version
        self.memo = memo
        self.modifier = modifier
        self.package_info_id = package_info_id
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.real_grey_endtime = real_grey_endtime
        self.real_grey_endtime_str = real_grey_endtime_str
        self.real_grey_endtype = real_grey_endtype
        self.real_grey_num = real_grey_num
        self.real_grey_uv = real_grey_uv
        self.silent_type = silent_type
        self.sync_result = sync_result
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.upgrade_valid_time = upgrade_valid_time
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
        if self.device_percent is not None:
            result['DevicePercent'] = self.device_percent
        if self.execution_order is not None:
            result['ExecutionOrder'] = self.execution_order
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime is not None:
            result['GreyEndtime'] = self.grey_endtime
        if self.grey_notice is not None:
            result['GreyNotice'] = self.grey_notice
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.grey_pause_point is not None:
            result['GreyPausePoint'] = self.grey_pause_point
        if self.grey_pause_type is not None:
            result['GreyPauseType'] = self.grey_pause_type
        if self.grey_uv is not None:
            result['GreyUv'] = self.grey_uv
        if self.history_force is not None:
            result['HistoryForce'] = self.history_force
        if self.huoban_notice_id is not None:
            result['HuobanNoticeId'] = self.huoban_notice_id
        if self.huoban_url is not None:
            result['HuobanUrl'] = self.huoban_url
        if self.id is not None:
            result['Id'] = self.id
        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.is_official is not None:
            result['IsOfficial'] = self.is_official
        if self.is_push is not None:
            result['IsPush'] = self.is_push
        if self.is_release is not None:
            result['IsRelease'] = self.is_release
        if self.max_version is not None:
            result['MaxVersion'] = self.max_version
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
        if self.real_grey_endtime is not None:
            result['RealGreyEndtime'] = self.real_grey_endtime
        if self.real_grey_endtime_str is not None:
            result['RealGreyEndtimeStr'] = self.real_grey_endtime_str
        if self.real_grey_endtype is not None:
            result['RealGreyEndtype'] = self.real_grey_endtype
        if self.real_grey_num is not None:
            result['RealGreyNum'] = self.real_grey_num
        if self.real_grey_uv is not None:
            result['RealGreyUv'] = self.real_grey_uv
        if self.silent_type is not None:
            result['SilentType'] = self.silent_type
        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.upgrade_content is not None:
            result['UpgradeContent'] = self.upgrade_content
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.upgrade_valid_time is not None:
            result['UpgradeValidTime'] = self.upgrade_valid_time
        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DevicePercent') is not None:
            self.device_percent = m.get('DevicePercent')
        if m.get('ExecutionOrder') is not None:
            self.execution_order = m.get('ExecutionOrder')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtime') is not None:
            self.grey_endtime = m.get('GreyEndtime')
        if m.get('GreyNotice') is not None:
            self.grey_notice = m.get('GreyNotice')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('GreyPausePoint') is not None:
            self.grey_pause_point = m.get('GreyPausePoint')
        if m.get('GreyPauseType') is not None:
            self.grey_pause_type = m.get('GreyPauseType')
        if m.get('GreyUv') is not None:
            self.grey_uv = m.get('GreyUv')
        if m.get('HistoryForce') is not None:
            self.history_force = m.get('HistoryForce')
        if m.get('HuobanNoticeId') is not None:
            self.huoban_notice_id = m.get('HuobanNoticeId')
        if m.get('HuobanUrl') is not None:
            self.huoban_url = m.get('HuobanUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')
        if m.get('IsPush') is not None:
            self.is_push = m.get('IsPush')
        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')
        if m.get('MaxVersion') is not None:
            self.max_version = m.get('MaxVersion')
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
        if m.get('RealGreyEndtime') is not None:
            self.real_grey_endtime = m.get('RealGreyEndtime')
        if m.get('RealGreyEndtimeStr') is not None:
            self.real_grey_endtime_str = m.get('RealGreyEndtimeStr')
        if m.get('RealGreyEndtype') is not None:
            self.real_grey_endtype = m.get('RealGreyEndtype')
        if m.get('RealGreyNum') is not None:
            self.real_grey_num = m.get('RealGreyNum')
        if m.get('RealGreyUv') is not None:
            self.real_grey_uv = m.get('RealGreyUv')
        if m.get('SilentType') is not None:
            self.silent_type = m.get('SilentType')
        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UpgradeContent') is not None:
            self.upgrade_content = m.get('UpgradeContent')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('UpgradeValidTime') is not None:
            self.upgrade_valid_time = m.get('UpgradeValidTime')
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


class ListMgsApiRequest(TeaModel):
    def __init__(
        self,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        format: str = None,
        host: str = None,
        need_encrypt: str = None,
        need_etag: str = None,
        need_sign: str = None,
        operation_type: str = None,
        opt_fuzzy: str = None,
        page_index: int = None,
        page_size: int = None,
        sys_id: int = None,
        sys_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.format = format
        self.host = host
        self.need_encrypt = need_encrypt
        self.need_etag = need_etag
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.opt_fuzzy = opt_fuzzy
        self.page_index = page_index
        self.page_size = page_size
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.format is not None:
            result['Format'] = self.format
        if self.host is not None:
            result['Host'] = self.host
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.need_etag is not None:
            result['NeedEtag'] = self.need_etag
        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.opt_fuzzy is not None:
            result['OptFuzzy'] = self.opt_fuzzy
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('NeedEtag') is not None:
            self.need_etag = m.get('NeedEtag')
        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OptFuzzy') is not None:
            self.opt_fuzzy = m.get('OptFuzzy')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMgsApiResponseBodyResultContentValueApiInvokerHttpInvoker(TeaModel):
    def __init__(
        self,
        charset: str = None,
        content_type: str = None,
        host: str = None,
        method: str = None,
        path: str = None,
    ):
        self.charset = charset
        self.content_type = content_type
        self.host = host
        self.method = method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.host is not None:
            result['Host'] = self.host
        if self.method is not None:
            result['Method'] = self.method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ListMgsApiResponseBodyResultContentValueApiInvoker(TeaModel):
    def __init__(
        self,
        http_invoker: ListMgsApiResponseBodyResultContentValueApiInvokerHttpInvoker = None,
        rpc_invoker: str = None,
    ):
        self.http_invoker = http_invoker
        self.rpc_invoker = rpc_invoker

    def validate(self):
        if self.http_invoker:
            self.http_invoker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_invoker is not None:
            result['HttpInvoker'] = self.http_invoker.to_map()
        if self.rpc_invoker is not None:
            result['RpcInvoker'] = self.rpc_invoker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInvoker') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueApiInvokerHttpInvoker()
            self.http_invoker = temp_model.from_map(m['HttpInvoker'])
        if m.get('RpcInvoker') is not None:
            self.rpc_invoker = m.get('RpcInvoker')
        return self


class ListMgsApiResponseBodyResultContentValueCacheRule(TeaModel):
    def __init__(
        self,
        cache_key: str = None,
        need_cache: bool = None,
        ttl: int = None,
    ):
        self.cache_key = cache_key
        self.need_cache = need_cache
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_key is not None:
            result['CacheKey'] = self.cache_key
        if self.need_cache is not None:
            result['NeedCache'] = self.need_cache
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheKey') is not None:
            self.cache_key = m.get('CacheKey')
        if m.get('NeedCache') is not None:
            self.need_cache = m.get('NeedCache')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class ListMgsApiResponseBodyResultContentValueCircuitBreakerRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        default_response: str = None,
        error_threshold: int = None,
        id: int = None,
        model: str = None,
        open_timeout_seconds: int = None,
        slow_ratio_threshold: float = None,
        switch_status: str = None,
        windows_in_seconds: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.default_response = default_response
        self.error_threshold = error_threshold
        self.id = id
        self.model = model
        self.open_timeout_seconds = open_timeout_seconds
        self.slow_ratio_threshold = slow_ratio_threshold
        self.switch_status = switch_status
        self.windows_in_seconds = windows_in_seconds
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
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.error_threshold is not None:
            result['ErrorThreshold'] = self.error_threshold
        if self.id is not None:
            result['Id'] = self.id
        if self.model is not None:
            result['Model'] = self.model
        if self.open_timeout_seconds is not None:
            result['OpenTimeoutSeconds'] = self.open_timeout_seconds
        if self.slow_ratio_threshold is not None:
            result['SlowRatioThreshold'] = self.slow_ratio_threshold
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.windows_in_seconds is not None:
            result['WindowsInSeconds'] = self.windows_in_seconds
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('ErrorThreshold') is not None:
            self.error_threshold = m.get('ErrorThreshold')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OpenTimeoutSeconds') is not None:
            self.open_timeout_seconds = m.get('OpenTimeoutSeconds')
        if m.get('SlowRatioThreshold') is not None:
            self.slow_ratio_threshold = m.get('SlowRatioThreshold')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('WindowsInSeconds') is not None:
            self.windows_in_seconds = m.get('WindowsInSeconds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMgsApiResponseBodyResultContentValueHeaderRule(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListMgsApiResponseBodyResultContentValueHeaderRules(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListMgsApiResponseBodyResultContentValueLimitRule(TeaModel):
    def __init__(
        self,
        default_response: str = None,
        i_18n_response: str = None,
        interval: int = None,
        limit: int = None,
        mode: str = None,
    ):
        self.default_response = default_response
        self.i_18n_response = i_18n_response
        self.interval = interval
        self.limit = limit
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.i_18n_response is not None:
            result['I18nResponse'] = self.i_18n_response
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('I18nResponse') is not None:
            self.i_18n_response = m.get('I18nResponse')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ListMgsApiResponseBodyResultContentValueMigrateRule(TeaModel):
    def __init__(
        self,
        flow_percent: int = None,
        need_migrate: bool = None,
        need_switch_completely: bool = None,
        sys_id: int = None,
        sys_name: str = None,
        upstream_type: str = None,
    ):
        self.flow_percent = flow_percent
        self.need_migrate = need_migrate
        self.need_switch_completely = need_switch_completely
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.upstream_type = upstream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.need_migrate is not None:
            result['NeedMigrate'] = self.need_migrate
        if self.need_switch_completely is not None:
            result['NeedSwitchCompletely'] = self.need_switch_completely
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('NeedMigrate') is not None:
            self.need_migrate = m.get('NeedMigrate')
        if m.get('NeedSwitchCompletely') is not None:
            self.need_switch_completely = m.get('NeedSwitchCompletely')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')
        return self


class ListMgsApiResponseBodyResultContentValueMockRule(TeaModel):
    def __init__(
        self,
        mock_data: str = None,
        need_mock: bool = None,
        percentage: int = None,
        type: str = None,
    ):
        self.mock_data = mock_data
        self.need_mock = need_mock
        self.percentage = percentage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mock_data is not None:
            result['MockData'] = self.mock_data
        if self.need_mock is not None:
            result['NeedMock'] = self.need_mock
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MockData') is not None:
            self.mock_data = m.get('MockData')
        if m.get('NeedMock') is not None:
            self.need_mock = m.get('NeedMock')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMgsApiResponseBodyResultContentValueRequestParams(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_id: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        ref_type: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.api_id = api_id
        self.app_id = app_id
        self.default_value = default_value
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.ref_type = ref_type
        self.type = type
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.ref_type is not None:
            result['RefType'] = self.ref_type
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMgsApiResponseBodyResultContentValue(TeaModel):
    def __init__(
        self,
        api_invoker: ListMgsApiResponseBodyResultContentValueApiInvoker = None,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        auth_rule_name: str = None,
        cache_rule: ListMgsApiResponseBodyResultContentValueCacheRule = None,
        charset: str = None,
        circuit_breaker_rule: ListMgsApiResponseBodyResultContentValueCircuitBreakerRule = None,
        content_type: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        header_rule: List[ListMgsApiResponseBodyResultContentValueHeaderRule] = None,
        header_rules: List[ListMgsApiResponseBodyResultContentValueHeaderRules] = None,
        host: str = None,
        id: int = None,
        interface_type: str = None,
        limit_rule: ListMgsApiResponseBodyResultContentValueLimitRule = None,
        method: str = None,
        method_name: str = None,
        migrate_rule: ListMgsApiResponseBodyResultContentValueMigrateRule = None,
        mock_rule: ListMgsApiResponseBodyResultContentValueMockRule = None,
        need_etag: str = None,
        need_encrypt: str = None,
        need_jsonp: str = None,
        need_sign: str = None,
        operation_type: str = None,
        param_get_method: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params: List[ListMgsApiResponseBodyResultContentValueRequestParams] = None,
        response_body_model: str = None,
        sys_id: int = None,
        sys_name: str = None,
        timeout: str = None,
        workspace_id: str = None,
    ):
        self.api_invoker = api_invoker
        self.api_name = api_name
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.auth_rule_name = auth_rule_name
        self.cache_rule = cache_rule
        self.charset = charset
        self.circuit_breaker_rule = circuit_breaker_rule
        self.content_type = content_type
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.header_rule = header_rule
        self.header_rules = header_rules
        self.host = host
        self.id = id
        self.interface_type = interface_type
        self.limit_rule = limit_rule
        self.method = method
        self.method_name = method_name
        self.migrate_rule = migrate_rule
        self.mock_rule = mock_rule
        self.need_etag = need_etag
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.param_get_method = param_get_method
        self.path = path
        self.request_body_model = request_body_model
        self.request_params = request_params
        self.response_body_model = response_body_model
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.timeout = timeout
        self.workspace_id = workspace_id

    def validate(self):
        if self.api_invoker:
            self.api_invoker.validate()
        if self.cache_rule:
            self.cache_rule.validate()
        if self.circuit_breaker_rule:
            self.circuit_breaker_rule.validate()
        if self.header_rule:
            for k in self.header_rule:
                if k:
                    k.validate()
        if self.header_rules:
            for k in self.header_rules:
                if k:
                    k.validate()
        if self.limit_rule:
            self.limit_rule.validate()
        if self.migrate_rule:
            self.migrate_rule.validate()
        if self.mock_rule:
            self.mock_rule.validate()
        if self.request_params:
            for k in self.request_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoker is not None:
            result['ApiInvoker'] = self.api_invoker.to_map()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_rule_name is not None:
            result['AuthRuleName'] = self.auth_rule_name
        if self.cache_rule is not None:
            result['CacheRule'] = self.cache_rule.to_map()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.circuit_breaker_rule is not None:
            result['CircuitBreakerRule'] = self.circuit_breaker_rule.to_map()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['HeaderRule'] = []
        if self.header_rule is not None:
            for k in self.header_rule:
                result['HeaderRule'].append(k.to_map() if k else None)
        result['HeaderRules'] = []
        if self.header_rules is not None:
            for k in self.header_rules:
                result['HeaderRules'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.id is not None:
            result['Id'] = self.id
        if self.interface_type is not None:
            result['InterfaceType'] = self.interface_type
        if self.limit_rule is not None:
            result['LimitRule'] = self.limit_rule.to_map()
        if self.method is not None:
            result['Method'] = self.method
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.migrate_rule is not None:
            result['MigrateRule'] = self.migrate_rule.to_map()
        if self.mock_rule is not None:
            result['MockRule'] = self.mock_rule.to_map()
        if self.need_etag is not None:
            result['NeedETag'] = self.need_etag
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.need_jsonp is not None:
            result['NeedJsonp'] = self.need_jsonp
        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.param_get_method is not None:
            result['ParamGetMethod'] = self.param_get_method
        if self.path is not None:
            result['Path'] = self.path
        if self.request_body_model is not None:
            result['RequestBodyModel'] = self.request_body_model
        result['RequestParams'] = []
        if self.request_params is not None:
            for k in self.request_params:
                result['RequestParams'].append(k.to_map() if k else None)
        if self.response_body_model is not None:
            result['ResponseBodyModel'] = self.response_body_model
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvoker') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueApiInvoker()
            self.api_invoker = temp_model.from_map(m['ApiInvoker'])
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthRuleName') is not None:
            self.auth_rule_name = m.get('AuthRuleName')
        if m.get('CacheRule') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueCacheRule()
            self.cache_rule = temp_model.from_map(m['CacheRule'])
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('CircuitBreakerRule') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueCircuitBreakerRule()
            self.circuit_breaker_rule = temp_model.from_map(m['CircuitBreakerRule'])
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.header_rule = []
        if m.get('HeaderRule') is not None:
            for k in m.get('HeaderRule'):
                temp_model = ListMgsApiResponseBodyResultContentValueHeaderRule()
                self.header_rule.append(temp_model.from_map(k))
        self.header_rules = []
        if m.get('HeaderRules') is not None:
            for k in m.get('HeaderRules'):
                temp_model = ListMgsApiResponseBodyResultContentValueHeaderRules()
                self.header_rules.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')
        if m.get('LimitRule') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueLimitRule()
            self.limit_rule = temp_model.from_map(m['LimitRule'])
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('MigrateRule') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueMigrateRule()
            self.migrate_rule = temp_model.from_map(m['MigrateRule'])
        if m.get('MockRule') is not None:
            temp_model = ListMgsApiResponseBodyResultContentValueMockRule()
            self.mock_rule = temp_model.from_map(m['MockRule'])
        if m.get('NeedETag') is not None:
            self.need_etag = m.get('NeedETag')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('NeedJsonp') is not None:
            self.need_jsonp = m.get('NeedJsonp')
        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ParamGetMethod') is not None:
            self.param_get_method = m.get('ParamGetMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestBodyModel') is not None:
            self.request_body_model = m.get('RequestBodyModel')
        self.request_params = []
        if m.get('RequestParams') is not None:
            for k in m.get('RequestParams'):
                temp_model = ListMgsApiResponseBodyResultContentValueRequestParams()
                self.request_params.append(temp_model.from_map(k))
        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListMgsApiResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        success: bool = None,
        value: List[ListMgsApiResponseBodyResultContentValue] = None,
    ):
        self.error_message = error_message
        self.success = success
        self.value = value

    def validate(self):
        if self.value:
            for k in self.value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        result['Value'] = []
        if self.value is not None:
            for k in self.value:
                result['Value'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.value = []
        if m.get('Value') is not None:
            for k in m.get('Value'):
                temp_model = ListMgsApiResponseBodyResultContentValue()
                self.value.append(temp_model.from_map(k))
        return self


class ListMgsApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: ListMgsApiResponseBodyResultContent = None,
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
            temp_model = ListMgsApiResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class ListMgsApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMgsApiResponseBody = None,
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
            temp_model = ListMgsApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MTRSOCRServiceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        image_raw: str = None,
        mask: bool = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.image_raw = image_raw
        self.mask = mask
        self.tenant_id = tenant_id
        # This parameter is required.
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
        if self.image_raw is not None:
            result['ImageRaw'] = self.image_raw
        if self.mask is not None:
            result['Mask'] = self.mask
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
        if m.get('ImageRaw') is not None:
            self.image_raw = m.get('ImageRaw')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class MTRSOCRServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        request_id: str = None,
        result: str = None,
        status: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.msg = msg
        self.request_id = request_id
        self.result = result
        self.status = status
        self.trace_id = trace_id

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
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class MTRSOCRServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MTRSOCRServiceResponseBody = None,
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
            temp_model = MTRSOCRServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushBindRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        delivery_token: str = None,
        os_type: int = None,
        phone_number: str = None,
        tenant_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.delivery_token = delivery_token
        # This parameter is required.
        self.os_type = os_type
        self.phone_number = phone_number
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
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
        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushBindResponseBodyPushResult(TeaModel):
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


class PushBindResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushBindResponseBodyPushResult = None,
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
            temp_model = PushBindResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushBindResponseBody = None,
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
            temp_model = PushBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushBroadcastRequest(TeaModel):
    def __init__(
        self,
        android_channel: int = None,
        app_id: str = None,
        bind_period: int = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        msgkey: str = None,
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
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        un_bind_period: int = None,
        workspace_id: str = None,
    ):
        self.android_channel = android_channel
        # This parameter is required.
        self.app_id = app_id
        self.bind_period = bind_period
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
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.un_bind_period = un_bind_period
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
        if self.bind_period is not None:
            result['BindPeriod'] = self.bind_period
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
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.un_bind_period is not None:
            result['UnBindPeriod'] = self.un_bind_period
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidChannel') is not None:
            self.android_channel = m.get('AndroidChannel')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BindPeriod') is not None:
            self.bind_period = m.get('BindPeriod')
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
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('UnBindPeriod') is not None:
            self.un_bind_period = m.get('UnBindPeriod')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushBroadcastShrinkRequest(TeaModel):
    def __init__(
        self,
        android_channel: int = None,
        app_id: str = None,
        bind_period: int = None,
        channel_id: str = None,
        classification: str = None,
        delivery_type: int = None,
        expired_seconds: int = None,
        extended_params: str = None,
        mi_channel_id: str = None,
        msgkey: str = None,
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
        transparent_message_payload: Any = None,
        transparent_message_urgency: str = None,
        un_bind_period: int = None,
        workspace_id: str = None,
    ):
        self.android_channel = android_channel
        # This parameter is required.
        self.app_id = app_id
        self.bind_period = bind_period
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
        self.transparent_message_payload = transparent_message_payload
        self.transparent_message_urgency = transparent_message_urgency
        self.un_bind_period = un_bind_period
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
        if self.bind_period is not None:
            result['BindPeriod'] = self.bind_period
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
        if self.transparent_message_payload is not None:
            result['TransparentMessagePayload'] = self.transparent_message_payload
        if self.transparent_message_urgency is not None:
            result['TransparentMessageUrgency'] = self.transparent_message_urgency
        if self.un_bind_period is not None:
            result['UnBindPeriod'] = self.un_bind_period
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidChannel') is not None:
            self.android_channel = m.get('AndroidChannel')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BindPeriod') is not None:
            self.bind_period = m.get('BindPeriod')
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
        if m.get('TransparentMessagePayload') is not None:
            self.transparent_message_payload = m.get('TransparentMessagePayload')
        if m.get('TransparentMessageUrgency') is not None:
            self.transparent_message_urgency = m.get('TransparentMessageUrgency')
        if m.get('UnBindPeriod') is not None:
            self.un_bind_period = m.get('UnBindPeriod')
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


class PushReportRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        channel: str = None,
        connect_type: str = None,
        delivery_token: str = None,
        imei: str = None,
        imsi: str = None,
        model: str = None,
        os_type: int = None,
        push_version: str = None,
        tenant_id: str = None,
        third_channel: int = None,
        third_channel_device_token: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.channel = channel
        self.connect_type = connect_type
        # This parameter is required.
        self.delivery_token = delivery_token
        self.imei = imei
        self.imsi = imsi
        self.model = model
        # This parameter is required.
        self.os_type = os_type
        self.push_version = push_version
        self.tenant_id = tenant_id
        self.third_channel = third_channel
        self.third_channel_device_token = third_channel_device_token
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
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type
        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.model is not None:
            result['Model'] = self.model
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.push_version is not None:
            result['PushVersion'] = self.push_version
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.third_channel is not None:
            result['ThirdChannel'] = self.third_channel
        if self.third_channel_device_token is not None:
            result['ThirdChannelDeviceToken'] = self.third_channel_device_token
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')
        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PushVersion') is not None:
            self.push_version = m.get('PushVersion')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ThirdChannel') is not None:
            self.third_channel = m.get('ThirdChannel')
        if m.get('ThirdChannelDeviceToken') is not None:
            self.third_channel_device_token = m.get('ThirdChannelDeviceToken')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushReportResponseBodyPushResult(TeaModel):
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


class PushReportResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushReportResponseBodyPushResult = None,
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
            temp_model = PushReportResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushReportResponseBody = None,
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
            temp_model = PushReportResponseBody()
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
        notify_type: str = None,
        push_action: int = None,
        push_style: int = None,
        silent: int = None,
        sms_sign_name: str = None,
        sms_strategy: int = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
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
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_style = push_style
        self.silent = silent
        self.sms_sign_name = sms_sign_name
        self.sms_strategy = sms_strategy
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
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
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_strategy is not None:
            result['SmsStrategy'] = self.sms_strategy
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
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
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsStrategy') is not None:
            self.sms_strategy = m.get('SmsStrategy')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
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
        notify_type: str = None,
        push_action: int = None,
        push_style: int = None,
        silent: int = None,
        sms_sign_name: str = None,
        sms_strategy: int = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
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
        self.notify_type = notify_type
        self.push_action = push_action
        self.push_style = push_style
        self.silent = silent
        self.sms_sign_name = sms_sign_name
        self.sms_strategy = sms_strategy
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
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
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.push_style is not None:
            result['PushStyle'] = self.push_style
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_strategy is not None:
            result['SmsStrategy'] = self.sms_strategy
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
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
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsStrategy') is not None:
            self.sms_strategy = m.get('SmsStrategy')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
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
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        sms_sign_name: str = None,
        sms_strategy: int = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
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
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.sms_sign_name = sms_sign_name
        self.sms_strategy = sms_strategy
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
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
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_strategy is not None:
            result['SmsStrategy'] = self.sms_strategy
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
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
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsStrategy') is not None:
            self.sms_strategy = m.get('SmsStrategy')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
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
        notify_type: str = None,
        push_action: int = None,
        silent: int = None,
        sms_sign_name: str = None,
        sms_strategy: int = None,
        sms_template_code: str = None,
        sms_template_param: str = None,
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
        self.notify_type = notify_type
        self.push_action = push_action
        self.silent = silent
        self.sms_sign_name = sms_sign_name
        self.sms_strategy = sms_strategy
        self.sms_template_code = sms_template_code
        self.sms_template_param = sms_template_param
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
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.push_action is not None:
            result['PushAction'] = self.push_action
        if self.silent is not None:
            result['Silent'] = self.silent
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_strategy is not None:
            result['SmsStrategy'] = self.sms_strategy
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_template_param is not None:
            result['SmsTemplateParam'] = self.sms_template_param
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
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('PushAction') is not None:
            self.push_action = m.get('PushAction')
        if m.get('Silent') is not None:
            self.silent = m.get('Silent')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsStrategy') is not None:
            self.sms_strategy = m.get('SmsStrategy')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsTemplateParam') is not None:
            self.sms_template_param = m.get('SmsTemplateParam')
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


class PushUnBindRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        delivery_token: str = None,
        tenant_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.delivery_token = delivery_token
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
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
        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class PushUnBindResponseBodyPushResult(TeaModel):
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


class PushUnBindResponseBody(TeaModel):
    def __init__(
        self,
        push_result: PushUnBindResponseBodyPushResult = None,
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
            temp_model = PushUnBindResponseBodyPushResult()
            self.push_result = temp_model.from_map(m['PushResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class PushUnBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushUnBindResponseBody = None,
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
            temp_model = PushUnBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInfoFromMdpRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mobile: str = None,
        mobile_md_5: str = None,
        mobile_sha_256: str = None,
        mobile_sm_3: str = None,
        risk_scene: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.mobile = mobile
        self.mobile_md_5 = mobile_md_5
        self.mobile_sha_256 = mobile_sha_256
        self.mobile_sm_3 = mobile_sm_3
        # This parameter is required.
        self.risk_scene = risk_scene
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
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_md_5 is not None:
            result['MobileMd5'] = self.mobile_md_5
        if self.mobile_sha_256 is not None:
            result['MobileSha256'] = self.mobile_sha_256
        if self.mobile_sm_3 is not None:
            result['MobileSm3'] = self.mobile_sm_3
        if self.risk_scene is not None:
            result['RiskScene'] = self.risk_scene
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileMd5') is not None:
            self.mobile_md_5 = m.get('MobileMd5')
        if m.get('MobileSha256') is not None:
            self.mobile_sha_256 = m.get('MobileSha256')
        if m.get('MobileSm3') is not None:
            self.mobile_sm_3 = m.get('MobileSm3')
        if m.get('RiskScene') is not None:
            self.risk_scene = m.get('RiskScene')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryInfoFromMdpResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        result_code: int = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.data = data
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInfoFromMdpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInfoFromMdpResponseBody = None,
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
            temp_model = QueryInfoFromMdpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.url = url
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
        if self.url is not None:
            result['Url'] = self.url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryLinkResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: Any = None,
        target: str = None,
        version: str = None,
    ):
        self.data = data
        self.target = target
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.target is not None:
            result['Target'] = self.target
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryLinkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryLinkResponseBodyResultContent = None,
        result_message: str = None,
    ):
        # Id of the request
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
            temp_model = QueryLinkResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLinkResponseBody = None,
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
            temp_model = QueryLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMappCenterAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
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
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig(TeaModel):
    def __init__(
        self,
        cert_rsa: str = None,
        package_name: str = None,
    ):
        self.cert_rsa = cert_rsa
        self.package_name = package_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_rsa is not None:
            result['CertRSA'] = self.cert_rsa
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertRSA') is not None:
            self.cert_rsa = m.get('CertRSA')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        return self


class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
    ):
        self.bundle_id = bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp(TeaModel):
    def __init__(
        self,
        android_config: QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig = None,
        app_desc: str = None,
        app_icon: str = None,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ios_config: QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig = None,
        modifier: str = None,
        monitor_json: str = None,
        status: int = None,
        tenant_id: str = None,
        type: int = None,
    ):
        self.android_config = android_config
        self.app_desc = app_desc
        self.app_icon = app_icon
        self.app_id = app_id
        self.app_name = app_name
        self.app_secret = app_secret
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.ios_config = ios_config
        self.modifier = modifier
        self.monitor_json = monitor_json
        self.status = status
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        if self.android_config:
            self.android_config.validate()
        if self.ios_config:
            self.ios_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_config is not None:
            result['AndroidConfig'] = self.android_config.to_map()
        if self.app_desc is not None:
            result['AppDesc'] = self.app_desc
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.ios_config is not None:
            result['IosConfig'] = self.ios_config.to_map()
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.monitor_json is not None:
            result['MonitorJson'] = self.monitor_json
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidConfig') is not None:
            temp_model = QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppAndroidConfig()
            self.android_config = temp_model.from_map(m['AndroidConfig'])
        if m.get('AppDesc') is not None:
            self.app_desc = m.get('AppDesc')
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IosConfig') is not None:
            temp_model = QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterAppIosConfig()
            self.ios_config = temp_model.from_map(m['IosConfig'])
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('MonitorJson') is not None:
            self.monitor_json = m.get('MonitorJson')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMappCenterAppResponseBodyQueryMappCenterAppResult(TeaModel):
    def __init__(
        self,
        mapp_center_app: QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mapp_center_app = mapp_center_app
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mapp_center_app:
            self.mapp_center_app.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mapp_center_app is not None:
            result['MappCenterApp'] = self.mapp_center_app.to_map()
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MappCenterApp') is not None:
            temp_model = QueryMappCenterAppResponseBodyQueryMappCenterAppResultMappCenterApp()
            self.mapp_center_app = temp_model.from_map(m['MappCenterApp'])
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMappCenterAppResponseBody(TeaModel):
    def __init__(
        self,
        query_mapp_center_app_result: QueryMappCenterAppResponseBodyQueryMappCenterAppResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.query_mapp_center_app_result = query_mapp_center_app_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.query_mapp_center_app_result:
            self.query_mapp_center_app_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_mapp_center_app_result is not None:
            result['QueryMappCenterAppResult'] = self.query_mapp_center_app_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryMappCenterAppResult') is not None:
            temp_model = QueryMappCenterAppResponseBodyQueryMappCenterAppResult()
            self.query_mapp_center_app_result = temp_model.from_map(m['QueryMappCenterAppResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMappCenterAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMappCenterAppResponseBody = None,
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
            temp_model = QueryMappCenterAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMcdpAimRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
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


class QueryMcdpAimResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMcdpAimResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMcdpAimResponseBodyResultContent = None,
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
            temp_model = QueryMcdpAimResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMcdpAimResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMcdpAimResponseBody = None,
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
            temp_model = QueryMcdpAimResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMcdpZoneRequest(TeaModel):
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


class QueryMcdpZoneResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMcdpZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMcdpZoneResponseBodyResultContent = None,
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
            temp_model = QueryMcdpZoneResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMcdpZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMcdpZoneResponseBody = None,
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
            temp_model = QueryMcdpZoneResponseBody()
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


class QueryMdsUpgradeTaskDetailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        task_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
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


class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList(TeaModel):
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


class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        business: str = None,
        gmt_modified: str = None,
        id: int = None,
        id_type: str = None,
        platform: str = None,
        status: int = None,
        white_list_count: int = None,
        white_list_name: str = None,
    ):
        self.app_code = app_code
        self.business = business
        self.gmt_modified = gmt_modified
        self.id = id
        self.id_type = id_type
        self.platform = platform
        self.status = status
        self.white_list_count = white_list_count
        self.white_list_name = white_list_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.business is not None:
            result['Business'] = self.business
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.status is not None:
            result['Status'] = self.status
        if self.white_list_count is not None:
            result['WhiteListCount'] = self.white_list_count
        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WhiteListCount') is not None:
            self.white_list_count = m.get('WhiteListCount')
        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')
        return self


class QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: str = None,
        appstoreurl: str = None,
        channel_contains: str = None,
        channel_excludes: str = None,
        city_contains: str = None,
        city_excludes: str = None,
        creator: str = None,
        device_grey_num: int = None,
        device_percent: int = None,
        download_url: str = None,
        execution_order: int = None,
        gmt_create_str: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_notice: int = None,
        grey_num: int = None,
        grey_uv: int = None,
        id: int = None,
        inner_version: str = None,
        is_enterprise: int = None,
        is_official: int = None,
        is_push: int = None,
        is_rc: int = None,
        is_release: int = None,
        memo: str = None,
        mobile_model_contains: str = None,
        mobile_model_excludes: str = None,
        modifier: str = None,
        net_type: str = None,
        os_version: str = None,
        package_info_id: int = None,
        package_type: str = None,
        platform: str = None,
        product_id: str = None,
        product_version: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        push_content: str = None,
        qrcode_url: str = None,
        release_type: str = None,
        rule_json_list: List[QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList] = None,
        silent_type: int = None,
        sync_mode: str = None,
        sync_result: str = None,
        task_status: int = None,
        upgrade_content: str = None,
        upgrade_type: int = None,
        upgrade_valid_time: int = None,
        whitelist: List[QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist] = None,
        whitelist_ids: str = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.appstoreurl = appstoreurl
        self.channel_contains = channel_contains
        self.channel_excludes = channel_excludes
        self.city_contains = city_contains
        self.city_excludes = city_excludes
        self.creator = creator
        self.device_grey_num = device_grey_num
        self.device_percent = device_percent
        self.download_url = download_url
        self.execution_order = execution_order
        self.gmt_create_str = gmt_create_str
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_notice = grey_notice
        self.grey_num = grey_num
        self.grey_uv = grey_uv
        self.id = id
        self.inner_version = inner_version
        self.is_enterprise = is_enterprise
        self.is_official = is_official
        self.is_push = is_push
        self.is_rc = is_rc
        self.is_release = is_release
        self.memo = memo
        self.mobile_model_contains = mobile_model_contains
        self.mobile_model_excludes = mobile_model_excludes
        self.modifier = modifier
        self.net_type = net_type
        self.os_version = os_version
        self.package_info_id = package_info_id
        self.package_type = package_type
        self.platform = platform
        self.product_id = product_id
        self.product_version = product_version
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.push_content = push_content
        self.qrcode_url = qrcode_url
        self.release_type = release_type
        self.rule_json_list = rule_json_list
        self.silent_type = silent_type
        self.sync_mode = sync_mode
        self.sync_result = sync_result
        self.task_status = task_status
        self.upgrade_content = upgrade_content
        self.upgrade_type = upgrade_type
        self.upgrade_valid_time = upgrade_valid_time
        self.whitelist = whitelist
        self.whitelist_ids = whitelist_ids

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
        if self.appstoreurl is not None:
            result['Appstoreurl'] = self.appstoreurl
        if self.channel_contains is not None:
            result['ChannelContains'] = self.channel_contains
        if self.channel_excludes is not None:
            result['ChannelExcludes'] = self.channel_excludes
        if self.city_contains is not None:
            result['CityContains'] = self.city_contains
        if self.city_excludes is not None:
            result['CityExcludes'] = self.city_excludes
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.device_grey_num is not None:
            result['DeviceGreyNum'] = self.device_grey_num
        if self.device_percent is not None:
            result['DevicePercent'] = self.device_percent
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.execution_order is not None:
            result['ExecutionOrder'] = self.execution_order
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info
        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data
        if self.grey_notice is not None:
            result['GreyNotice'] = self.grey_notice
        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num
        if self.grey_uv is not None:
            result['GreyUv'] = self.grey_uv
        if self.id is not None:
            result['Id'] = self.id
        if self.inner_version is not None:
            result['InnerVersion'] = self.inner_version
        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise
        if self.is_official is not None:
            result['IsOfficial'] = self.is_official
        if self.is_push is not None:
            result['IsPush'] = self.is_push
        if self.is_rc is not None:
            result['IsRc'] = self.is_rc
        if self.is_release is not None:
            result['IsRelease'] = self.is_release
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.mobile_model_contains is not None:
            result['MobileModelContains'] = self.mobile_model_contains
        if self.mobile_model_excludes is not None:
            result['MobileModelExcludes'] = self.mobile_model_excludes
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.package_info_id is not None:
            result['PackageInfoId'] = self.package_info_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
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
        if self.qrcode_url is not None:
            result['QrcodeUrl'] = self.qrcode_url
        if self.release_type is not None:
            result['ReleaseType'] = self.release_type
        result['RuleJsonList'] = []
        if self.rule_json_list is not None:
            for k in self.rule_json_list:
                result['RuleJsonList'].append(k.to_map() if k else None)
        if self.silent_type is not None:
            result['SilentType'] = self.silent_type
        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode
        if self.sync_result is not None:
            result['SyncResult'] = self.sync_result
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Appstoreurl') is not None:
            self.appstoreurl = m.get('Appstoreurl')
        if m.get('ChannelContains') is not None:
            self.channel_contains = m.get('ChannelContains')
        if m.get('ChannelExcludes') is not None:
            self.channel_excludes = m.get('ChannelExcludes')
        if m.get('CityContains') is not None:
            self.city_contains = m.get('CityContains')
        if m.get('CityExcludes') is not None:
            self.city_excludes = m.get('CityExcludes')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DeviceGreyNum') is not None:
            self.device_grey_num = m.get('DeviceGreyNum')
        if m.get('DevicePercent') is not None:
            self.device_percent = m.get('DevicePercent')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExecutionOrder') is not None:
            self.execution_order = m.get('ExecutionOrder')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')
        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')
        if m.get('GreyNotice') is not None:
            self.grey_notice = m.get('GreyNotice')
        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')
        if m.get('GreyUv') is not None:
            self.grey_uv = m.get('GreyUv')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InnerVersion') is not None:
            self.inner_version = m.get('InnerVersion')
        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')
        if m.get('IsOfficial') is not None:
            self.is_official = m.get('IsOfficial')
        if m.get('IsPush') is not None:
            self.is_push = m.get('IsPush')
        if m.get('IsRc') is not None:
            self.is_rc = m.get('IsRc')
        if m.get('IsRelease') is not None:
            self.is_release = m.get('IsRelease')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MobileModelContains') is not None:
            self.mobile_model_contains = m.get('MobileModelContains')
        if m.get('MobileModelExcludes') is not None:
            self.mobile_model_excludes = m.get('MobileModelExcludes')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('PackageInfoId') is not None:
            self.package_info_id = m.get('PackageInfoId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
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
        if m.get('QrcodeUrl') is not None:
            self.qrcode_url = m.get('QrcodeUrl')
        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')
        self.rule_json_list = []
        if m.get('RuleJsonList') is not None:
            for k in m.get('RuleJsonList'):
                temp_model = QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentRuleJsonList()
                self.rule_json_list.append(temp_model.from_map(k))
        if m.get('SilentType') is not None:
            self.silent_type = m.get('SilentType')
        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')
        if m.get('SyncResult') is not None:
            self.sync_result = m.get('SyncResult')
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
                temp_model = QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContentWhitelist()
                self.whitelist.append(temp_model.from_map(k))
        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')
        return self


class QueryMdsUpgradeTaskDetailResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        content: QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

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
        if m.get('Content') is not None:
            temp_model = QueryMdsUpgradeTaskDetailResponseBodyResultContentDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMdsUpgradeTaskDetailResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: QueryMdsUpgradeTaskDetailResponseBodyResultContentData = None,
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
            temp_model = QueryMdsUpgradeTaskDetailResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMdsUpgradeTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMdsUpgradeTaskDetailResponseBodyResultContent = None,
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
            temp_model = QueryMdsUpgradeTaskDetailResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMdsUpgradeTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMdsUpgradeTaskDetailResponseBody = None,
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
            temp_model = QueryMdsUpgradeTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMgsApipageRequest(TeaModel):
    def __init__(
        self,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        format: str = None,
        host: str = None,
        need_encrypt: str = None,
        need_etag: str = None,
        need_sign: str = None,
        operation_type: str = None,
        opt_fuzzy: str = None,
        page_index: int = None,
        page_size: int = None,
        sys_id: int = None,
        sys_name: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.format = format
        self.host = host
        self.need_encrypt = need_encrypt
        self.need_etag = need_etag
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.opt_fuzzy = opt_fuzzy
        self.page_index = page_index
        self.page_size = page_size
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.format is not None:
            result['Format'] = self.format
        if self.host is not None:
            result['Host'] = self.host
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.need_etag is not None:
            result['NeedEtag'] = self.need_etag
        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.opt_fuzzy is not None:
            result['OptFuzzy'] = self.opt_fuzzy
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('NeedEtag') is not None:
            self.need_etag = m.get('NeedEtag')
        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OptFuzzy') is not None:
            self.opt_fuzzy = m.get('OptFuzzy')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker(TeaModel):
    def __init__(
        self,
        charset: str = None,
        content_type: str = None,
        host: str = None,
        method: str = None,
        path: str = None,
    ):
        self.charset = charset
        self.content_type = content_type
        self.host = host
        self.method = method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.host is not None:
            result['Host'] = self.host
        if self.method is not None:
            result['Method'] = self.method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryMgsApipageResponseBodyResultContentListApiInvoker(TeaModel):
    def __init__(
        self,
        http_invoker: QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker = None,
        rpc_invoker: str = None,
    ):
        self.http_invoker = http_invoker
        self.rpc_invoker = rpc_invoker

    def validate(self):
        if self.http_invoker:
            self.http_invoker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_invoker is not None:
            result['HttpInvoker'] = self.http_invoker.to_map()
        if self.rpc_invoker is not None:
            result['RpcInvoker'] = self.rpc_invoker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInvoker') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListApiInvokerHttpInvoker()
            self.http_invoker = temp_model.from_map(m['HttpInvoker'])
        if m.get('RpcInvoker') is not None:
            self.rpc_invoker = m.get('RpcInvoker')
        return self


class QueryMgsApipageResponseBodyResultContentListCacheRule(TeaModel):
    def __init__(
        self,
        cache_key: str = None,
        need_cache: bool = None,
        ttl: int = None,
    ):
        self.cache_key = cache_key
        self.need_cache = need_cache
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_key is not None:
            result['CacheKey'] = self.cache_key
        if self.need_cache is not None:
            result['NeedCache'] = self.need_cache
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheKey') is not None:
            self.cache_key = m.get('CacheKey')
        if m.get('NeedCache') is not None:
            self.need_cache = m.get('NeedCache')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        default_response: str = None,
        error_threshold: int = None,
        id: int = None,
        model: str = None,
        open_timeout_seconds: int = None,
        slow_ratio_threshold: float = None,
        switch_status: str = None,
        windows_in_seconds: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.default_response = default_response
        self.error_threshold = error_threshold
        self.id = id
        self.model = model
        self.open_timeout_seconds = open_timeout_seconds
        self.slow_ratio_threshold = slow_ratio_threshold
        self.switch_status = switch_status
        self.windows_in_seconds = windows_in_seconds
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
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.error_threshold is not None:
            result['ErrorThreshold'] = self.error_threshold
        if self.id is not None:
            result['Id'] = self.id
        if self.model is not None:
            result['Model'] = self.model
        if self.open_timeout_seconds is not None:
            result['OpenTimeoutSeconds'] = self.open_timeout_seconds
        if self.slow_ratio_threshold is not None:
            result['SlowRatioThreshold'] = self.slow_ratio_threshold
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.windows_in_seconds is not None:
            result['WindowsInSeconds'] = self.windows_in_seconds
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('ErrorThreshold') is not None:
            self.error_threshold = m.get('ErrorThreshold')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OpenTimeoutSeconds') is not None:
            self.open_timeout_seconds = m.get('OpenTimeoutSeconds')
        if m.get('SlowRatioThreshold') is not None:
            self.slow_ratio_threshold = m.get('SlowRatioThreshold')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('WindowsInSeconds') is not None:
            self.windows_in_seconds = m.get('WindowsInSeconds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApipageResponseBodyResultContentListHeaderRule(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMgsApipageResponseBodyResultContentListHeaderRules(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMgsApipageResponseBodyResultContentListLimitRule(TeaModel):
    def __init__(
        self,
        default_response: str = None,
        i_18n_response: str = None,
        interval: int = None,
        limit: int = None,
        mode: str = None,
    ):
        self.default_response = default_response
        self.i_18n_response = i_18n_response
        self.interval = interval
        self.limit = limit
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.i_18n_response is not None:
            result['I18nResponse'] = self.i_18n_response
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('I18nResponse') is not None:
            self.i_18n_response = m.get('I18nResponse')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class QueryMgsApipageResponseBodyResultContentListMigrateRule(TeaModel):
    def __init__(
        self,
        flow_percent: int = None,
        need_migrate: bool = None,
        need_switch_completely: bool = None,
        sys_id: int = None,
        sys_name: str = None,
        upstream_type: str = None,
    ):
        self.flow_percent = flow_percent
        self.need_migrate = need_migrate
        self.need_switch_completely = need_switch_completely
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.upstream_type = upstream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.need_migrate is not None:
            result['NeedMigrate'] = self.need_migrate
        if self.need_switch_completely is not None:
            result['NeedSwitchCompletely'] = self.need_switch_completely
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('NeedMigrate') is not None:
            self.need_migrate = m.get('NeedMigrate')
        if m.get('NeedSwitchCompletely') is not None:
            self.need_switch_completely = m.get('NeedSwitchCompletely')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')
        return self


class QueryMgsApipageResponseBodyResultContentListMockRule(TeaModel):
    def __init__(
        self,
        mock_data: str = None,
        need_mock: bool = None,
        percentage: int = None,
        type: str = None,
    ):
        self.mock_data = mock_data
        self.need_mock = need_mock
        self.percentage = percentage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mock_data is not None:
            result['MockData'] = self.mock_data
        if self.need_mock is not None:
            result['NeedMock'] = self.need_mock
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MockData') is not None:
            self.mock_data = m.get('MockData')
        if m.get('NeedMock') is not None:
            self.need_mock = m.get('NeedMock')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMgsApipageResponseBodyResultContentListRequestParams(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_id: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        ref_type: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.api_id = api_id
        self.app_id = app_id
        self.default_value = default_value
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.ref_type = ref_type
        self.type = type
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.ref_type is not None:
            result['RefType'] = self.ref_type
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApipageResponseBodyResultContentList(TeaModel):
    def __init__(
        self,
        api_invoker: QueryMgsApipageResponseBodyResultContentListApiInvoker = None,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        auth_rule_name: str = None,
        cache_rule: QueryMgsApipageResponseBodyResultContentListCacheRule = None,
        charset: str = None,
        circuit_breaker_rule: QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule = None,
        content_type: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        header_rule: List[QueryMgsApipageResponseBodyResultContentListHeaderRule] = None,
        header_rules: List[QueryMgsApipageResponseBodyResultContentListHeaderRules] = None,
        host: str = None,
        id: int = None,
        interface_type: str = None,
        limit_rule: QueryMgsApipageResponseBodyResultContentListLimitRule = None,
        method: str = None,
        method_name: str = None,
        migrate_rule: QueryMgsApipageResponseBodyResultContentListMigrateRule = None,
        mock_rule: QueryMgsApipageResponseBodyResultContentListMockRule = None,
        need_etag: str = None,
        need_encrypt: str = None,
        need_jsonp: str = None,
        need_sign: str = None,
        operation_type: str = None,
        param_get_method: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params: List[QueryMgsApipageResponseBodyResultContentListRequestParams] = None,
        response_body_model: str = None,
        sys_id: int = None,
        sys_name: str = None,
        timeout: str = None,
        workspace_id: str = None,
    ):
        self.api_invoker = api_invoker
        self.api_name = api_name
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.auth_rule_name = auth_rule_name
        self.cache_rule = cache_rule
        self.charset = charset
        self.circuit_breaker_rule = circuit_breaker_rule
        self.content_type = content_type
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.header_rule = header_rule
        self.header_rules = header_rules
        self.host = host
        self.id = id
        self.interface_type = interface_type
        self.limit_rule = limit_rule
        self.method = method
        self.method_name = method_name
        self.migrate_rule = migrate_rule
        self.mock_rule = mock_rule
        self.need_etag = need_etag
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.param_get_method = param_get_method
        self.path = path
        self.request_body_model = request_body_model
        self.request_params = request_params
        self.response_body_model = response_body_model
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.timeout = timeout
        self.workspace_id = workspace_id

    def validate(self):
        if self.api_invoker:
            self.api_invoker.validate()
        if self.cache_rule:
            self.cache_rule.validate()
        if self.circuit_breaker_rule:
            self.circuit_breaker_rule.validate()
        if self.header_rule:
            for k in self.header_rule:
                if k:
                    k.validate()
        if self.header_rules:
            for k in self.header_rules:
                if k:
                    k.validate()
        if self.limit_rule:
            self.limit_rule.validate()
        if self.migrate_rule:
            self.migrate_rule.validate()
        if self.mock_rule:
            self.mock_rule.validate()
        if self.request_params:
            for k in self.request_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoker is not None:
            result['ApiInvoker'] = self.api_invoker.to_map()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_rule_name is not None:
            result['AuthRuleName'] = self.auth_rule_name
        if self.cache_rule is not None:
            result['CacheRule'] = self.cache_rule.to_map()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.circuit_breaker_rule is not None:
            result['CircuitBreakerRule'] = self.circuit_breaker_rule.to_map()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['HeaderRule'] = []
        if self.header_rule is not None:
            for k in self.header_rule:
                result['HeaderRule'].append(k.to_map() if k else None)
        result['HeaderRules'] = []
        if self.header_rules is not None:
            for k in self.header_rules:
                result['HeaderRules'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.id is not None:
            result['Id'] = self.id
        if self.interface_type is not None:
            result['InterfaceType'] = self.interface_type
        if self.limit_rule is not None:
            result['LimitRule'] = self.limit_rule.to_map()
        if self.method is not None:
            result['Method'] = self.method
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.migrate_rule is not None:
            result['MigrateRule'] = self.migrate_rule.to_map()
        if self.mock_rule is not None:
            result['MockRule'] = self.mock_rule.to_map()
        if self.need_etag is not None:
            result['NeedETag'] = self.need_etag
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.need_jsonp is not None:
            result['NeedJsonp'] = self.need_jsonp
        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.param_get_method is not None:
            result['ParamGetMethod'] = self.param_get_method
        if self.path is not None:
            result['Path'] = self.path
        if self.request_body_model is not None:
            result['RequestBodyModel'] = self.request_body_model
        result['RequestParams'] = []
        if self.request_params is not None:
            for k in self.request_params:
                result['RequestParams'].append(k.to_map() if k else None)
        if self.response_body_model is not None:
            result['ResponseBodyModel'] = self.response_body_model
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvoker') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListApiInvoker()
            self.api_invoker = temp_model.from_map(m['ApiInvoker'])
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthRuleName') is not None:
            self.auth_rule_name = m.get('AuthRuleName')
        if m.get('CacheRule') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListCacheRule()
            self.cache_rule = temp_model.from_map(m['CacheRule'])
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('CircuitBreakerRule') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListCircuitBreakerRule()
            self.circuit_breaker_rule = temp_model.from_map(m['CircuitBreakerRule'])
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.header_rule = []
        if m.get('HeaderRule') is not None:
            for k in m.get('HeaderRule'):
                temp_model = QueryMgsApipageResponseBodyResultContentListHeaderRule()
                self.header_rule.append(temp_model.from_map(k))
        self.header_rules = []
        if m.get('HeaderRules') is not None:
            for k in m.get('HeaderRules'):
                temp_model = QueryMgsApipageResponseBodyResultContentListHeaderRules()
                self.header_rules.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')
        if m.get('LimitRule') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListLimitRule()
            self.limit_rule = temp_model.from_map(m['LimitRule'])
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('MigrateRule') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListMigrateRule()
            self.migrate_rule = temp_model.from_map(m['MigrateRule'])
        if m.get('MockRule') is not None:
            temp_model = QueryMgsApipageResponseBodyResultContentListMockRule()
            self.mock_rule = temp_model.from_map(m['MockRule'])
        if m.get('NeedETag') is not None:
            self.need_etag = m.get('NeedETag')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('NeedJsonp') is not None:
            self.need_jsonp = m.get('NeedJsonp')
        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ParamGetMethod') is not None:
            self.param_get_method = m.get('ParamGetMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestBodyModel') is not None:
            self.request_body_model = m.get('RequestBodyModel')
        self.request_params = []
        if m.get('RequestParams') is not None:
            for k in m.get('RequestParams'):
                temp_model = QueryMgsApipageResponseBodyResultContentListRequestParams()
                self.request_params.append(temp_model.from_map(k))
        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApipageResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        current: int = None,
        list: List[QueryMgsApipageResponseBodyResultContentList] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.list = list
        self.page_size = page_size
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryMgsApipageResponseBodyResultContentList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMgsApipageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMgsApipageResponseBodyResultContent = None,
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
            temp_model = QueryMgsApipageResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMgsApipageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMgsApipageResponseBody = None,
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
            temp_model = QueryMgsApipageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMgsApirestRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        format: str = None,
        id: int = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.format = format
        self.id = id
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
        if self.format is not None:
            result['Format'] = self.format
        if self.id is not None:
            result['Id'] = self.id
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
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApirestResponseBodyResultContentValueApiInvokerHttpInvoker(TeaModel):
    def __init__(
        self,
        charset: str = None,
        content_type: str = None,
        host: str = None,
        method: str = None,
        path: str = None,
    ):
        self.charset = charset
        self.content_type = content_type
        self.host = host
        self.method = method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.host is not None:
            result['Host'] = self.host
        if self.method is not None:
            result['Method'] = self.method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class QueryMgsApirestResponseBodyResultContentValueApiInvoker(TeaModel):
    def __init__(
        self,
        http_invoker: QueryMgsApirestResponseBodyResultContentValueApiInvokerHttpInvoker = None,
        rpc_invoker: str = None,
    ):
        self.http_invoker = http_invoker
        self.rpc_invoker = rpc_invoker

    def validate(self):
        if self.http_invoker:
            self.http_invoker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_invoker is not None:
            result['HttpInvoker'] = self.http_invoker.to_map()
        if self.rpc_invoker is not None:
            result['RpcInvoker'] = self.rpc_invoker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInvoker') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueApiInvokerHttpInvoker()
            self.http_invoker = temp_model.from_map(m['HttpInvoker'])
        if m.get('RpcInvoker') is not None:
            self.rpc_invoker = m.get('RpcInvoker')
        return self


class QueryMgsApirestResponseBodyResultContentValueCacheRule(TeaModel):
    def __init__(
        self,
        cache_key: str = None,
        need_cache: bool = None,
        ttl: int = None,
    ):
        self.cache_key = cache_key
        self.need_cache = need_cache
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_key is not None:
            result['CacheKey'] = self.cache_key
        if self.need_cache is not None:
            result['NeedCache'] = self.need_cache
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheKey') is not None:
            self.cache_key = m.get('CacheKey')
        if m.get('NeedCache') is not None:
            self.need_cache = m.get('NeedCache')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class QueryMgsApirestResponseBodyResultContentValueCircuitBreakerRule(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        default_response: str = None,
        error_threshold: int = None,
        id: int = None,
        model: str = None,
        open_timeout_seconds: int = None,
        slow_ratio_threshold: float = None,
        switch_status: str = None,
        windows_in_seconds: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.default_response = default_response
        self.error_threshold = error_threshold
        self.id = id
        self.model = model
        self.open_timeout_seconds = open_timeout_seconds
        self.slow_ratio_threshold = slow_ratio_threshold
        self.switch_status = switch_status
        self.windows_in_seconds = windows_in_seconds
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
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.error_threshold is not None:
            result['ErrorThreshold'] = self.error_threshold
        if self.id is not None:
            result['Id'] = self.id
        if self.model is not None:
            result['Model'] = self.model
        if self.open_timeout_seconds is not None:
            result['OpenTimeoutSeconds'] = self.open_timeout_seconds
        if self.slow_ratio_threshold is not None:
            result['SlowRatioThreshold'] = self.slow_ratio_threshold
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.windows_in_seconds is not None:
            result['WindowsInSeconds'] = self.windows_in_seconds
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('ErrorThreshold') is not None:
            self.error_threshold = m.get('ErrorThreshold')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OpenTimeoutSeconds') is not None:
            self.open_timeout_seconds = m.get('OpenTimeoutSeconds')
        if m.get('SlowRatioThreshold') is not None:
            self.slow_ratio_threshold = m.get('SlowRatioThreshold')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('WindowsInSeconds') is not None:
            self.windows_in_seconds = m.get('WindowsInSeconds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApirestResponseBodyResultContentValueDefaultLimitRule(TeaModel):
    def __init__(
        self,
        config_id: int = None,
        default_limit: bool = None,
    ):
        self.config_id = config_id
        self.default_limit = default_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.default_limit is not None:
            result['DefaultLimit'] = self.default_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('DefaultLimit') is not None:
            self.default_limit = m.get('DefaultLimit')
        return self


class QueryMgsApirestResponseBodyResultContentValueHeaderRule(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMgsApirestResponseBodyResultContentValueHeaderRules(TeaModel):
    def __init__(
        self,
        header_key: str = None,
        location: str = None,
        type: str = None,
        value: str = None,
    ):
        self.header_key = header_key
        self.location = location
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_key is not None:
            result['HeaderKey'] = self.header_key
        if self.location is not None:
            result['Location'] = self.location
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderKey') is not None:
            self.header_key = m.get('HeaderKey')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryMgsApirestResponseBodyResultContentValueLimitRule(TeaModel):
    def __init__(
        self,
        default_response: str = None,
        i_18n_response: str = None,
        interval: int = None,
        limit: int = None,
        mode: str = None,
    ):
        self.default_response = default_response
        self.i_18n_response = i_18n_response
        self.interval = interval
        self.limit = limit
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_response is not None:
            result['DefaultResponse'] = self.default_response
        if self.i_18n_response is not None:
            result['I18nResponse'] = self.i_18n_response
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResponse') is not None:
            self.default_response = m.get('DefaultResponse')
        if m.get('I18nResponse') is not None:
            self.i_18n_response = m.get('I18nResponse')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class QueryMgsApirestResponseBodyResultContentValueMigrateRule(TeaModel):
    def __init__(
        self,
        flow_percent: int = None,
        need_migrate: bool = None,
        need_switch_completely: bool = None,
        sys_id: int = None,
        sys_name: str = None,
        upstream_type: str = None,
    ):
        self.flow_percent = flow_percent
        self.need_migrate = need_migrate
        self.need_switch_completely = need_switch_completely
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.upstream_type = upstream_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent
        if self.need_migrate is not None:
            result['NeedMigrate'] = self.need_migrate
        if self.need_switch_completely is not None:
            result['NeedSwitchCompletely'] = self.need_switch_completely
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')
        if m.get('NeedMigrate') is not None:
            self.need_migrate = m.get('NeedMigrate')
        if m.get('NeedSwitchCompletely') is not None:
            self.need_switch_completely = m.get('NeedSwitchCompletely')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')
        return self


class QueryMgsApirestResponseBodyResultContentValueMockRule(TeaModel):
    def __init__(
        self,
        mock_data: str = None,
        need_mock: bool = None,
        percentage: int = None,
        type: str = None,
    ):
        self.mock_data = mock_data
        self.need_mock = need_mock
        self.percentage = percentage
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mock_data is not None:
            result['MockData'] = self.mock_data
        if self.need_mock is not None:
            result['NeedMock'] = self.need_mock
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MockData') is not None:
            self.mock_data = m.get('MockData')
        if m.get('NeedMock') is not None:
            self.need_mock = m.get('NeedMock')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryMgsApirestResponseBodyResultContentValueRequestParams(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_id: str = None,
        default_value: str = None,
        description: str = None,
        id: int = None,
        location: str = None,
        name: str = None,
        ref_type: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.api_id = api_id
        self.app_id = app_id
        self.default_value = default_value
        self.description = description
        self.id = id
        self.location = location
        self.name = name
        self.ref_type = ref_type
        self.type = type
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.ref_type is not None:
            result['RefType'] = self.ref_type
        if self.type is not None:
            result['Type'] = self.type
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RefType') is not None:
            self.ref_type = m.get('RefType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApirestResponseBodyResultContentValue(TeaModel):
    def __init__(
        self,
        api_invoker: QueryMgsApirestResponseBodyResultContentValueApiInvoker = None,
        api_name: str = None,
        api_status: str = None,
        api_type: str = None,
        app_id: str = None,
        auth_rule_name: str = None,
        cache_rule: QueryMgsApirestResponseBodyResultContentValueCacheRule = None,
        charset: str = None,
        circuit_breaker_rule: QueryMgsApirestResponseBodyResultContentValueCircuitBreakerRule = None,
        content_type: str = None,
        default_limit_rule: QueryMgsApirestResponseBodyResultContentValueDefaultLimitRule = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        header_rule: List[QueryMgsApirestResponseBodyResultContentValueHeaderRule] = None,
        header_rules: List[QueryMgsApirestResponseBodyResultContentValueHeaderRules] = None,
        host: str = None,
        id: int = None,
        interface_type: str = None,
        limit_rule: QueryMgsApirestResponseBodyResultContentValueLimitRule = None,
        method: str = None,
        method_name: str = None,
        migrate_rule: QueryMgsApirestResponseBodyResultContentValueMigrateRule = None,
        mock_rule: QueryMgsApirestResponseBodyResultContentValueMockRule = None,
        need_etag: str = None,
        need_encrypt: str = None,
        need_jsonp: str = None,
        need_sign: str = None,
        operation_type: str = None,
        param_get_method: str = None,
        path: str = None,
        request_body_model: str = None,
        request_params: List[QueryMgsApirestResponseBodyResultContentValueRequestParams] = None,
        response_body_model: str = None,
        sys_id: int = None,
        sys_name: str = None,
        timeout: str = None,
        workspace_id: str = None,
    ):
        self.api_invoker = api_invoker
        self.api_name = api_name
        self.api_status = api_status
        self.api_type = api_type
        self.app_id = app_id
        self.auth_rule_name = auth_rule_name
        self.cache_rule = cache_rule
        self.charset = charset
        self.circuit_breaker_rule = circuit_breaker_rule
        self.content_type = content_type
        self.default_limit_rule = default_limit_rule
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.header_rule = header_rule
        self.header_rules = header_rules
        self.host = host
        self.id = id
        self.interface_type = interface_type
        self.limit_rule = limit_rule
        self.method = method
        self.method_name = method_name
        self.migrate_rule = migrate_rule
        self.mock_rule = mock_rule
        self.need_etag = need_etag
        self.need_encrypt = need_encrypt
        self.need_jsonp = need_jsonp
        self.need_sign = need_sign
        self.operation_type = operation_type
        self.param_get_method = param_get_method
        self.path = path
        self.request_body_model = request_body_model
        self.request_params = request_params
        self.response_body_model = response_body_model
        self.sys_id = sys_id
        self.sys_name = sys_name
        self.timeout = timeout
        self.workspace_id = workspace_id

    def validate(self):
        if self.api_invoker:
            self.api_invoker.validate()
        if self.cache_rule:
            self.cache_rule.validate()
        if self.circuit_breaker_rule:
            self.circuit_breaker_rule.validate()
        if self.default_limit_rule:
            self.default_limit_rule.validate()
        if self.header_rule:
            for k in self.header_rule:
                if k:
                    k.validate()
        if self.header_rules:
            for k in self.header_rules:
                if k:
                    k.validate()
        if self.limit_rule:
            self.limit_rule.validate()
        if self.migrate_rule:
            self.migrate_rule.validate()
        if self.mock_rule:
            self.mock_rule.validate()
        if self.request_params:
            for k in self.request_params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_invoker is not None:
            result['ApiInvoker'] = self.api_invoker.to_map()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_rule_name is not None:
            result['AuthRuleName'] = self.auth_rule_name
        if self.cache_rule is not None:
            result['CacheRule'] = self.cache_rule.to_map()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.circuit_breaker_rule is not None:
            result['CircuitBreakerRule'] = self.circuit_breaker_rule.to_map()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.default_limit_rule is not None:
            result['DefaultLimitRule'] = self.default_limit_rule.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['HeaderRule'] = []
        if self.header_rule is not None:
            for k in self.header_rule:
                result['HeaderRule'].append(k.to_map() if k else None)
        result['HeaderRules'] = []
        if self.header_rules is not None:
            for k in self.header_rules:
                result['HeaderRules'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.id is not None:
            result['Id'] = self.id
        if self.interface_type is not None:
            result['InterfaceType'] = self.interface_type
        if self.limit_rule is not None:
            result['LimitRule'] = self.limit_rule.to_map()
        if self.method is not None:
            result['Method'] = self.method
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.migrate_rule is not None:
            result['MigrateRule'] = self.migrate_rule.to_map()
        if self.mock_rule is not None:
            result['MockRule'] = self.mock_rule.to_map()
        if self.need_etag is not None:
            result['NeedETag'] = self.need_etag
        if self.need_encrypt is not None:
            result['NeedEncrypt'] = self.need_encrypt
        if self.need_jsonp is not None:
            result['NeedJsonp'] = self.need_jsonp
        if self.need_sign is not None:
            result['NeedSign'] = self.need_sign
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.param_get_method is not None:
            result['ParamGetMethod'] = self.param_get_method
        if self.path is not None:
            result['Path'] = self.path
        if self.request_body_model is not None:
            result['RequestBodyModel'] = self.request_body_model
        result['RequestParams'] = []
        if self.request_params is not None:
            for k in self.request_params:
                result['RequestParams'].append(k.to_map() if k else None)
        if self.response_body_model is not None:
            result['ResponseBodyModel'] = self.response_body_model
        if self.sys_id is not None:
            result['SysId'] = self.sys_id
        if self.sys_name is not None:
            result['SysName'] = self.sys_name
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInvoker') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueApiInvoker()
            self.api_invoker = temp_model.from_map(m['ApiInvoker'])
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthRuleName') is not None:
            self.auth_rule_name = m.get('AuthRuleName')
        if m.get('CacheRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueCacheRule()
            self.cache_rule = temp_model.from_map(m['CacheRule'])
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('CircuitBreakerRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueCircuitBreakerRule()
            self.circuit_breaker_rule = temp_model.from_map(m['CircuitBreakerRule'])
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('DefaultLimitRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueDefaultLimitRule()
            self.default_limit_rule = temp_model.from_map(m['DefaultLimitRule'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.header_rule = []
        if m.get('HeaderRule') is not None:
            for k in m.get('HeaderRule'):
                temp_model = QueryMgsApirestResponseBodyResultContentValueHeaderRule()
                self.header_rule.append(temp_model.from_map(k))
        self.header_rules = []
        if m.get('HeaderRules') is not None:
            for k in m.get('HeaderRules'):
                temp_model = QueryMgsApirestResponseBodyResultContentValueHeaderRules()
                self.header_rules.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InterfaceType') is not None:
            self.interface_type = m.get('InterfaceType')
        if m.get('LimitRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueLimitRule()
            self.limit_rule = temp_model.from_map(m['LimitRule'])
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('MigrateRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueMigrateRule()
            self.migrate_rule = temp_model.from_map(m['MigrateRule'])
        if m.get('MockRule') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValueMockRule()
            self.mock_rule = temp_model.from_map(m['MockRule'])
        if m.get('NeedETag') is not None:
            self.need_etag = m.get('NeedETag')
        if m.get('NeedEncrypt') is not None:
            self.need_encrypt = m.get('NeedEncrypt')
        if m.get('NeedJsonp') is not None:
            self.need_jsonp = m.get('NeedJsonp')
        if m.get('NeedSign') is not None:
            self.need_sign = m.get('NeedSign')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ParamGetMethod') is not None:
            self.param_get_method = m.get('ParamGetMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RequestBodyModel') is not None:
            self.request_body_model = m.get('RequestBodyModel')
        self.request_params = []
        if m.get('RequestParams') is not None:
            for k in m.get('RequestParams'):
                temp_model = QueryMgsApirestResponseBodyResultContentValueRequestParams()
                self.request_params.append(temp_model.from_map(k))
        if m.get('ResponseBodyModel') is not None:
            self.response_body_model = m.get('ResponseBodyModel')
        if m.get('SysId') is not None:
            self.sys_id = m.get('SysId')
        if m.get('SysName') is not None:
            self.sys_name = m.get('SysName')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsApirestResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        success: bool = None,
        value: QueryMgsApirestResponseBodyResultContentValue = None,
    ):
        self.error_message = error_message
        self.success = success
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.value is not None:
            result['Value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Value') is not None:
            temp_model = QueryMgsApirestResponseBodyResultContentValue()
            self.value = temp_model.from_map(m['Value'])
        return self


class QueryMgsApirestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: QueryMgsApirestResponseBodyResultContent = None,
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
            temp_model = QueryMgsApirestResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class QueryMgsApirestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMgsApirestResponseBody = None,
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
            temp_model = QueryMgsApirestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMgsTestreqbodyautogenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        format: str = None,
        mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.format = format
        self.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str = mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
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
        if self.format is not None:
            result['Format'] = self.format
        if self.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str is not None:
            result['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = self.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr') is not None:
            self.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str = m.get('MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class QueryMgsTestreqbodyautogenResponseBody(TeaModel):
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


class QueryMgsTestreqbodyautogenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMgsTestreqbodyautogenResponseBody = None,
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
            temp_model = QueryMgsTestreqbodyautogenResponseBody()
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


class RunMsaDiffRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_msa_diff_run_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.mpaas_mappcenter_msa_diff_run_json_str = mpaas_mappcenter_msa_diff_run_json_str
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
        if self.mpaas_mappcenter_msa_diff_run_json_str is not None:
            result['MpaasMappcenterMsaDiffRunJsonStr'] = self.mpaas_mappcenter_msa_diff_run_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMsaDiffRunJsonStr') is not None:
            self.mpaas_mappcenter_msa_diff_run_json_str = m.get('MpaasMappcenterMsaDiffRunJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunMsaDiffResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunMsaDiffResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: RunMsaDiffResponseBodyResultContent = None,
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
            temp_model = RunMsaDiffResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class RunMsaDiffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunMsaDiffResponseBody = None,
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
            temp_model = RunMsaDiffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveMgsApirestRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        mpaas_mappcenter_mgs_apirest_save_json_str: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.mpaas_mappcenter_mgs_apirest_save_json_str = mpaas_mappcenter_mgs_apirest_save_json_str
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
        if self.mpaas_mappcenter_mgs_apirest_save_json_str is not None:
            result['MpaasMappcenterMgsApirestSaveJsonStr'] = self.mpaas_mappcenter_mgs_apirest_save_json_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MpaasMappcenterMgsApirestSaveJsonStr') is not None:
            self.mpaas_mappcenter_mgs_apirest_save_json_str = m.get('MpaasMappcenterMgsApirestSaveJsonStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class SaveMgsApirestResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        success: bool = None,
        value: bool = None,
    ):
        self.error_message = error_message
        self.success = success
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveMgsApirestResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: SaveMgsApirestResponseBodyResultContent = None,
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
            temp_model = SaveMgsApirestResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class SaveMgsApirestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveMgsApirestResponseBody = None,
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
            temp_model = SaveMgsApirestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartUserAppAsyncEnhanceInMsaRequest(TeaModel):
    def __init__(
        self,
        apk_protector: bool = None,
        app_id: str = None,
        assets_file_list: str = None,
        classes: str = None,
        dalvik_debugger: int = None,
        emulator_environment: int = None,
        id: int = None,
        java_hook: int = None,
        memory_dump: int = None,
        native_debugger: int = None,
        native_hook: int = None,
        package_tampered: int = None,
        root: int = None,
        run_mode: str = None,
        so_file_list: str = None,
        task_type: str = None,
        tenant_id: str = None,
        total_switch: bool = None,
        use_ashield: bool = None,
        workspace_id: str = None,
    ):
        self.apk_protector = apk_protector
        # This parameter is required.
        self.app_id = app_id
        self.assets_file_list = assets_file_list
        self.classes = classes
        self.dalvik_debugger = dalvik_debugger
        self.emulator_environment = emulator_environment
        # This parameter is required.
        self.id = id
        self.java_hook = java_hook
        self.memory_dump = memory_dump
        self.native_debugger = native_debugger
        self.native_hook = native_hook
        self.package_tampered = package_tampered
        self.root = root
        self.run_mode = run_mode
        self.so_file_list = so_file_list
        self.task_type = task_type
        # This parameter is required.
        self.tenant_id = tenant_id
        self.total_switch = total_switch
        self.use_ashield = use_ashield
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apk_protector is not None:
            result['ApkProtector'] = self.apk_protector
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.assets_file_list is not None:
            result['AssetsFileList'] = self.assets_file_list
        if self.classes is not None:
            result['Classes'] = self.classes
        if self.dalvik_debugger is not None:
            result['DalvikDebugger'] = self.dalvik_debugger
        if self.emulator_environment is not None:
            result['EmulatorEnvironment'] = self.emulator_environment
        if self.id is not None:
            result['Id'] = self.id
        if self.java_hook is not None:
            result['JavaHook'] = self.java_hook
        if self.memory_dump is not None:
            result['MemoryDump'] = self.memory_dump
        if self.native_debugger is not None:
            result['NativeDebugger'] = self.native_debugger
        if self.native_hook is not None:
            result['NativeHook'] = self.native_hook
        if self.package_tampered is not None:
            result['PackageTampered'] = self.package_tampered
        if self.root is not None:
            result['Root'] = self.root
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.so_file_list is not None:
            result['SoFileList'] = self.so_file_list
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.total_switch is not None:
            result['TotalSwitch'] = self.total_switch
        if self.use_ashield is not None:
            result['UseAShield'] = self.use_ashield
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkProtector') is not None:
            self.apk_protector = m.get('ApkProtector')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AssetsFileList') is not None:
            self.assets_file_list = m.get('AssetsFileList')
        if m.get('Classes') is not None:
            self.classes = m.get('Classes')
        if m.get('DalvikDebugger') is not None:
            self.dalvik_debugger = m.get('DalvikDebugger')
        if m.get('EmulatorEnvironment') is not None:
            self.emulator_environment = m.get('EmulatorEnvironment')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('JavaHook') is not None:
            self.java_hook = m.get('JavaHook')
        if m.get('MemoryDump') is not None:
            self.memory_dump = m.get('MemoryDump')
        if m.get('NativeDebugger') is not None:
            self.native_debugger = m.get('NativeDebugger')
        if m.get('NativeHook') is not None:
            self.native_hook = m.get('NativeHook')
        if m.get('PackageTampered') is not None:
            self.package_tampered = m.get('PackageTampered')
        if m.get('Root') is not None:
            self.root = m.get('Root')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('SoFileList') is not None:
            self.so_file_list = m.get('SoFileList')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TotalSwitch') is not None:
            self.total_switch = m.get('TotalSwitch')
        if m.get('UseAShield') is not None:
            self.use_ashield = m.get('UseAShield')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class StartUserAppAsyncEnhanceInMsaResponseBodyResultContentDataEnhanceMapping(TeaModel):
    def __init__(
        self,
        info: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.info = info
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StartUserAppAsyncEnhanceInMsaResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        after_md_5: str = None,
        after_size: int = None,
        app_code: str = None,
        app_package: str = None,
        assets_file_list: List[str] = None,
        before_md_5: str = None,
        before_size: int = None,
        class_forest: str = None,
        enhance_mapping: List[StartUserAppAsyncEnhanceInMsaResponseBodyResultContentDataEnhanceMapping] = None,
        enhance_rules: List[str] = None,
        enhanced_assets_files: List[str] = None,
        enhanced_classes: List[str] = None,
        enhanced_so_files: List[str] = None,
        id: int = None,
        label: str = None,
        progress: int = None,
        so_file_list: List[str] = None,
        status: int = None,
        task_type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.after_md_5 = after_md_5
        self.after_size = after_size
        self.app_code = app_code
        self.app_package = app_package
        self.assets_file_list = assets_file_list
        self.before_md_5 = before_md_5
        self.before_size = before_size
        self.class_forest = class_forest
        self.enhance_mapping = enhance_mapping
        self.enhance_rules = enhance_rules
        self.enhanced_assets_files = enhanced_assets_files
        self.enhanced_classes = enhanced_classes
        self.enhanced_so_files = enhanced_so_files
        self.id = id
        self.label = label
        self.progress = progress
        self.so_file_list = so_file_list
        self.status = status
        self.task_type = task_type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        if self.enhance_mapping:
            for k in self.enhance_mapping:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_md_5 is not None:
            result['AfterMd5'] = self.after_md_5
        if self.after_size is not None:
            result['AfterSize'] = self.after_size
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.assets_file_list is not None:
            result['AssetsFileList'] = self.assets_file_list
        if self.before_md_5 is not None:
            result['BeforeMd5'] = self.before_md_5
        if self.before_size is not None:
            result['BeforeSize'] = self.before_size
        if self.class_forest is not None:
            result['ClassForest'] = self.class_forest
        result['EnhanceMapping'] = []
        if self.enhance_mapping is not None:
            for k in self.enhance_mapping:
                result['EnhanceMapping'].append(k.to_map() if k else None)
        if self.enhance_rules is not None:
            result['EnhanceRules'] = self.enhance_rules
        if self.enhanced_assets_files is not None:
            result['EnhancedAssetsFiles'] = self.enhanced_assets_files
        if self.enhanced_classes is not None:
            result['EnhancedClasses'] = self.enhanced_classes
        if self.enhanced_so_files is not None:
            result['EnhancedSoFiles'] = self.enhanced_so_files
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.so_file_list is not None:
            result['SoFileList'] = self.so_file_list
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterMd5') is not None:
            self.after_md_5 = m.get('AfterMd5')
        if m.get('AfterSize') is not None:
            self.after_size = m.get('AfterSize')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('AssetsFileList') is not None:
            self.assets_file_list = m.get('AssetsFileList')
        if m.get('BeforeMd5') is not None:
            self.before_md_5 = m.get('BeforeMd5')
        if m.get('BeforeSize') is not None:
            self.before_size = m.get('BeforeSize')
        if m.get('ClassForest') is not None:
            self.class_forest = m.get('ClassForest')
        self.enhance_mapping = []
        if m.get('EnhanceMapping') is not None:
            for k in m.get('EnhanceMapping'):
                temp_model = StartUserAppAsyncEnhanceInMsaResponseBodyResultContentDataEnhanceMapping()
                self.enhance_mapping.append(temp_model.from_map(k))
        if m.get('EnhanceRules') is not None:
            self.enhance_rules = m.get('EnhanceRules')
        if m.get('EnhancedAssetsFiles') is not None:
            self.enhanced_assets_files = m.get('EnhancedAssetsFiles')
        if m.get('EnhancedClasses') is not None:
            self.enhanced_classes = m.get('EnhancedClasses')
        if m.get('EnhancedSoFiles') is not None:
            self.enhanced_so_files = m.get('EnhancedSoFiles')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('SoFileList') is not None:
            self.so_file_list = m.get('SoFileList')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class StartUserAppAsyncEnhanceInMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartUserAppAsyncEnhanceInMsaResponseBodyResultContentData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartUserAppAsyncEnhanceInMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartUserAppAsyncEnhanceInMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: StartUserAppAsyncEnhanceInMsaResponseBodyResultContent = None,
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
            temp_model = StartUserAppAsyncEnhanceInMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class StartUserAppAsyncEnhanceInMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartUserAppAsyncEnhanceInMsaResponseBody = None,
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
            temp_model = StartUserAppAsyncEnhanceInMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cors: bool = None,
        domain: str = None,
        dynamicfield: str = None,
        target_url: str = None,
        url: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.cors = cors
        self.domain = domain
        self.dynamicfield = dynamicfield
        # This parameter is required.
        self.target_url = target_url
        # This parameter is required.
        self.url = url
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
        if self.cors is not None:
            result['Cors'] = self.cors
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.dynamicfield is not None:
            result['Dynamicfield'] = self.dynamicfield
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.url is not None:
            result['Url'] = self.url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cors') is not None:
            self.cors = m.get('Cors')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Dynamicfield') is not None:
            self.dynamicfield = m.get('Dynamicfield')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateLinkResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: str = None,
        target: str = None,
        version: str = None,
    ):
        self.data = data
        self.target = target
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.target is not None:
            result['Target'] = self.target
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateLinkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: UpdateLinkResponseBodyResultContent = None,
        result_message: str = None,
    ):
        # Id of the request
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
            temp_model = UpdateLinkResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class UpdateLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLinkResponseBody = None,
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
            temp_model = UpdateLinkResponseBody()
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


class UpdateMpaasAppInfoRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        icon_file_url: str = None,
        identifier: str = None,
        onex_flag: bool = None,
        system_type: str = None,
        tenant_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.icon_file_url = icon_file_url
        self.identifier = identifier
        self.onex_flag = onex_flag
        self.system_type = system_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url
        if self.identifier is not None:
            result['Identifier'] = self.identifier
        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag
        if self.system_type is not None:
            result['SystemType'] = self.system_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')
        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')
        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class UpdateMpaasAppInfoResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.app_id = app_id
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMpaasAppInfoResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        data: UpdateMpaasAppInfoResponseBodyResultContentData = None,
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
            temp_model = UpdateMpaasAppInfoResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMpaasAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: UpdateMpaasAppInfoResponseBodyResultContent = None,
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
            temp_model = UpdateMpaasAppInfoResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class UpdateMpaasAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMpaasAppInfoResponseBody = None,
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
            temp_model = UpdateMpaasAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadBitcodeToMsaRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bitcode: str = None,
        code_version: str = None,
        license: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.bitcode = bitcode
        self.code_version = code_version
        self.license = license
        # This parameter is required.
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
        if self.bitcode is not None:
            result['Bitcode'] = self.bitcode
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version
        if self.license is not None:
            result['License'] = self.license
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
        if m.get('Bitcode') is not None:
            self.bitcode = m.get('Bitcode')
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UploadBitcodeToMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadBitcodeToMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: UploadBitcodeToMsaResponseBodyResultContent = None,
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
            temp_model = UploadBitcodeToMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class UploadBitcodeToMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadBitcodeToMsaResponseBody = None,
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
            temp_model = UploadBitcodeToMsaResponseBody()
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
        icon_url: str = None,
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
        self.icon_file_url = icon_file_url
        self.icon_url = icon_url
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
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
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
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
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


class UploadUserAppToMsaRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        file_url: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.file_url = file_url
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping(TeaModel):
    def __init__(
        self,
        info: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.info = info
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info is not None:
            result['Info'] = self.info
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UploadUserAppToMsaResponseBodyResultContentDataApkInfo(TeaModel):
    def __init__(
        self,
        after_md_5: str = None,
        after_size: int = None,
        app_code: str = None,
        app_package: str = None,
        before_md_5: str = None,
        before_size: int = None,
        class_forest: str = None,
        enhance_mapping: UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping = None,
        enhance_rules: List[str] = None,
        enhanced_classes: List[str] = None,
        id: int = None,
        label: str = None,
        progress: int = None,
        status: int = None,
        task_type: str = None,
        version_code: str = None,
        version_name: str = None,
    ):
        self.after_md_5 = after_md_5
        self.after_size = after_size
        self.app_code = app_code
        self.app_package = app_package
        self.before_md_5 = before_md_5
        self.before_size = before_size
        self.class_forest = class_forest
        self.enhance_mapping = enhance_mapping
        self.enhance_rules = enhance_rules
        self.enhanced_classes = enhanced_classes
        self.id = id
        self.label = label
        self.progress = progress
        self.status = status
        self.task_type = task_type
        self.version_code = version_code
        self.version_name = version_name

    def validate(self):
        if self.enhance_mapping:
            self.enhance_mapping.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after_md_5 is not None:
            result['AfterMd5'] = self.after_md_5
        if self.after_size is not None:
            result['AfterSize'] = self.after_size
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_package is not None:
            result['AppPackage'] = self.app_package
        if self.before_md_5 is not None:
            result['BeforeMd5'] = self.before_md_5
        if self.before_size is not None:
            result['BeforeSize'] = self.before_size
        if self.class_forest is not None:
            result['ClassForest'] = self.class_forest
        if self.enhance_mapping is not None:
            result['EnhanceMapping'] = self.enhance_mapping.to_map()
        if self.enhance_rules is not None:
            result['EnhanceRules'] = self.enhance_rules
        if self.enhanced_classes is not None:
            result['EnhancedClasses'] = self.enhanced_classes
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.version_code is not None:
            result['VersionCode'] = self.version_code
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterMd5') is not None:
            self.after_md_5 = m.get('AfterMd5')
        if m.get('AfterSize') is not None:
            self.after_size = m.get('AfterSize')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppPackage') is not None:
            self.app_package = m.get('AppPackage')
        if m.get('BeforeMd5') is not None:
            self.before_md_5 = m.get('BeforeMd5')
        if m.get('BeforeSize') is not None:
            self.before_size = m.get('BeforeSize')
        if m.get('ClassForest') is not None:
            self.class_forest = m.get('ClassForest')
        if m.get('EnhanceMapping') is not None:
            temp_model = UploadUserAppToMsaResponseBodyResultContentDataApkInfoEnhanceMapping()
            self.enhance_mapping = temp_model.from_map(m['EnhanceMapping'])
        if m.get('EnhanceRules') is not None:
            self.enhance_rules = m.get('EnhanceRules')
        if m.get('EnhancedClasses') is not None:
            self.enhanced_classes = m.get('EnhancedClasses')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UploadUserAppToMsaResponseBodyResultContentData(TeaModel):
    def __init__(
        self,
        apk_info: UploadUserAppToMsaResponseBodyResultContentDataApkInfo = None,
        enhance_task_id: int = None,
        id: int = None,
        progress: int = None,
        status: int = None,
    ):
        self.apk_info = apk_info
        self.enhance_task_id = enhance_task_id
        self.id = id
        self.progress = progress
        self.status = status

    def validate(self):
        if self.apk_info:
            self.apk_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apk_info is not None:
            result['ApkInfo'] = self.apk_info.to_map()
        if self.enhance_task_id is not None:
            result['EnhanceTaskId'] = self.enhance_task_id
        if self.id is not None:
            result['Id'] = self.id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkInfo') is not None:
            temp_model = UploadUserAppToMsaResponseBodyResultContentDataApkInfo()
            self.apk_info = temp_model.from_map(m['ApkInfo'])
        if m.get('EnhanceTaskId') is not None:
            self.enhance_task_id = m.get('EnhanceTaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UploadUserAppToMsaResponseBodyResultContent(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UploadUserAppToMsaResponseBodyResultContentData = None,
        extra: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.extra = extra
        self.message = message
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
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UploadUserAppToMsaResponseBodyResultContentData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UploadUserAppToMsaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: UploadUserAppToMsaResponseBodyResultContent = None,
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
            temp_model = UploadUserAppToMsaResponseBodyResultContent()
            self.result_content = temp_model.from_map(m['ResultContent'])
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        return self


class UploadUserAppToMsaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadUserAppToMsaResponseBody = None,
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
            temp_model = UploadUserAppToMsaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


